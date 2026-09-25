# oBfsC4t10n [HARD]

> **ES:** Challenge Forensics Hard: un documento adjunto de phishing que no llegó a ejecutarse (el SOC sospecha errores en la muestra); hay que analizar sus macros ofuscadas, reconstruir el shellcode y deducir cuál habría sido su mecanismo de command & control para extraer la flag (`HTB{...}`).
> **EN:** Hard Forensics challenge: a phishing attachment that never executed correctly (the SOC suspects errors in the sample); analyze its obfuscated macros, rebuild the shellcode and work out what its command & control mechanism would have been to extract the flag (`HTB{...}`).

| Campo | Valor |
|-------|-------|
| **Categoría** | Forensics |
| **Dificultad** | Hard |
| **Estado** | Retired |
| **URL** | https://app.hackthebox.com/challenges/oBfsC4t10n |
| **Archivos** | Zip descargable con el documento adjunto (`invoice-*.html`/documento Office con macros, según fuente citada) [verificar nombre exacto del zip] |
| **Fecha de resolución** | 2026-09-25 (documentación; resuelto previamente según stub local) |
| **Puntos** | 60 (índice público actual; la nota previa local indicaba 6pts — se corrige aquí) |

---

## 🎯 Objetivo / Goal

> **ES:** Extraer el documento, analizar sus macros (Excel 4.0/XLM + VBA ofuscado con `Chr`/`Hex`/`Base64`), reconstruir el array de bytes en un shellcode válido y emularlo para identificar el C2 previsto (dominio `evil-domain` + puerto 443/TCP) y la flag (`HTB{...}`).
> **EN:** Extract the document, analyze its macros (Excel 4.0/XLM + VBA obfuscated with `Chr`/hex/base64), rebuild the byte array into a valid shellcode and emulate it to identify the intended C2 (an `evil-domain` host + port 443/TCP) and the flag (`HTB{...}`).

---

## 🛠️ Herramientas usadas / Tools used

- [ ] `unzip` + `file` (triage del adjunto)
- [ ] `olevba` (oletools) para listar macros auto-ejecutables, palabras sospechosas e IOCs
- [ ] Visor de Office / editor para leer el cuerpo de la macro (macros siempre desactivadas)
- [ ] CyberChef (normalizar el ofuscado: comillas `""""`→`""`, `&`→espacio, `Chr(x)`→carácter)
- [ ] `python3` (reconstruir `myArray` con `& 0xFF` → `shellcode.bin`)
- [ ] `scdbg` (emulación del shellcode y traza de llamadas Winsock)

---

## 📋 Pasos / Steps

### Paso 1 — Triage + `olevba` / Triage + `olevba`

> **ES:** Se descomprime el zip y se identifica el adjunto; `olevba` revela ejecución automática al abrir (`Auto_Open`, `Label1_Click`), primitivas sospechosas (`Environ`, `Open`/`Write`/`Output`, `Shell`, `Call`, `Chr`), cadenas hex/base64 y un IOC con nombre de ejecutable (`.hta`).
> **EN:** Unzip the archive and identify the attachment; `olevba` reveals auto-execution on open (`Auto_Open`, `Label1_Click`), suspicious primitives (`Environ`, `Open`/`Write`/`Output`, `Shell`, `Call`, `Chr`), hex/base64 strings and an IOC executable name (`.hta`).

```bash
unzip <archivo>.zip && file *
olevba <documento>
# esperado: AutoExec Auto_Open/Label1_Click + Suspicious (Environ/Open/Write/Shell/Call/Chr/Hex/Base64) + IOC *.hta
```

**Resultado / Result:** Confirmado maldoc de phishing con macros: el informe apunta a un dropper que escribe/ejecuta un `.hta` y a ofuscación por concatenación de cadenas.

### Paso 2 — Desofuscado de la macro / Macro deobfuscation

> **ES:** Se lee la macro ofuscada (cadenas partidas con `&`, comillas cuadruplicadas y `Chr(n)`); normalizando con CyberChef (o sustitución asistida) aparece un bloque que rellena `myArray` con enteros con signo: es el shellcode del payload.
> **EN:** Read the obfuscated macro (strings split with `&`, quadrupled quotes and `Chr(n)`); normalizing with CyberChef (or assisted substitution) reveals a block filling `myArray` with signed integers: the payload shellcode.

```bash
# Normalización conceptual (paráfrasis de la fuente citada):
# """" → "" ; & → espacio ; Chr(10) → \n ; Chr(34) → " ; Chr(92) → \
python3 -c "
myArray = [ ... ]  # enteros con signo extraídos de la macro
open('shellcode.bin','wb').write(bytes([(b & 0xFF) for b in myArray]))
print('shellcode.bin escrito')
"
file shellcode.bin
```

**Resultado / Result:** `shellcode.bin` reconstruido a partir de `myArray` (conversión `& 0xFF` de cada valor con signo a byte); listo para emulación estática.

### Paso 3 — Emulación con `scdbg` e identificación del C2 / Emulation with `scdbg` and C2 identification

> **ES:** Se emula el shellcode: carga `ws2_32.dll` (Winsock), inicializa sockets (`WSAStartup`/`WSASocket`), resuelve el dominio C2 y abre una conexión TCP al puerto 443; el hostname resuelto contiene la flag (`HTB{...}`), que es el mecanismo de C2 que habría usado de haber funcionado.
> **EN:** Emulate the shellcode: it loads `ws2_32.dll` (Winsock), initializes sockets (`WSAStartup`/`WSASocket`), resolves the C2 domain and opens a TCP connection to port 443; the resolved hostname carries the flag (`HTB{...}`) — the C2 mechanism it would have used had it worked.

```bash
scdbg /f shellcode.bin
# traza esperada: LoadLibraryA(ws2_32) → WSAStartup → WSASocket → gethostbyname(evil-domain…/HTB{…}) → connect(…:443) → recv → closesocket
```

**Resultado / Result:** C2 identificado: reverse-shell TCP contra el dominio señuelo en el puerto 443; la flag en formato `HTB{...}` viaja incrustada en el hostname resuelto (no se reproduce aquí por integridad del contenido; challenge retirado, ver capturas de las fuentes citadas). [verificar] reproducción propia con captura en `img/`.

---

## 🧠 Lo aprendido / Learned

- [ ] `olevba` como primer triage de maldocs: auto-exec, primitivas sospechosas e IOCs sin ejecutar nada.
- [ ] Macros Excel 4.0/XLM + VBA ofuscado con `&`, `""""` y `Chr(n)`: normalizar cadenas antes de razonar.
- [ ] Arrays de enteros con signo en la macro = shellcode embebido; reconstrucción con `byte = valor & 0xFF`.
- [ ] Emulación con `scdbg`: `ws2_32` + `WSASocket`/`connect` delata el C2 aunque la muestra original estuviera rota.
- [ ] El "error" del SOC es la pista: analizar lo que el payload *habría hecho*, no lo que hizo.

---

## 📚 Fuentes y Referencias / Sources

- **Walkthrough de referencia:** [oBfsC4t10n — vanniichan/HackTheBox](https://github.com/vanniichan/HackTheBox/blob/main/oBfsC4t10n/WriteUp.md) — vanniichan (descripción del challenge, `olevba` con `Auto_Open`/`Label1_Click`/`Shell`/`Chr`/IOC `.hta`, normalización en CyberChef, reconstrucción de `myArray` con `& 0xFF`, traza `scdbg` con `ws2_32`/`gethostbyname`/`connect :443`)
- **Writeup de referencia:** [oBfsC4t10n HTB Challenge – Esther7171](https://github.com/Esther7171/HackTheBox-Writeups-Walkthroughs/tree/main/Write-ups/Challanges/oBfsC4t10n) — Esther7171 ("Category: Forensics, Difficulty: Hard (60 Points)"; objetivo: documento adjunto con errores, deducir el C2)
- **Índice público de challenges:** [foobarto.me/htb/challenges](https://foobarto.me/htb/challenges/) — Bartosz Ptaszyński (`obfsc4t10n · Forensics · Hard · 60 pts`, 2019-11-01)
- **Hilo oficial:** [oBfsC4t10n – HTB Forums](https://forum.hackthebox.com/t/obfsc4t10n/2011) — Hack The Box :: Forums
- **Nota local previa:** stub raíz `Soluciones/Challenges/obfsc4t10n.md` ("Points: 6pts") migrado a esta plantilla; el valor oficial documentado es 60 pts
- **Fecha de acceso:** 2026-09-25
- **Autor de este walkthrough:** Apuromafo (síntesis propia parafraseada a partir de las fuentes citadas)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. Challenge retirado; no se publican flags literales.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Retired challenge; no literal flags published.

_Fecha de edición: 2026-09-25_
