# Window's Infinity Edge [HARD]

> **ES:** Challenge Forensics Hard: un APT vulneró la empresa con tooling propio; los implantes se limpiaron con antivirus, pero un servidor "limpio" sigue generando tráfico sospechoso. Se entrega un PCAP (`2019-11-12_21:00:30-EXT07.pcap`) y restos de una web shell (`shell.aspx`): hay que descubrir lo que la limpieza pasó por alto (un SharPyShell con C2 cifrado + shellcode) y extraer la flag (`HTB{...}`).
> **EN:** Hard Forensics challenge: an APT breached the company with custom tooling; implants were cleaned with antivirus, but one "clean" server still produces suspicious traffic. A PCAP (`2019-11-12_21:00:30-EXT07.pcap`) and web shell remnants (`shell.aspx`) are provided: find what the cleanup missed (a SharPyShell with encrypted C2 + shellcode) and extract the flag (`HTB{...}`).

| Campo | Valor |
|-------|-------|
| **Categoría** | Forensics |
| **Dificultad** | Hard |
| **Estado** | Retired |
| **URL** | https://app.hackthebox.com/challenges/Window's%20Infinity%20Edge |
| **Archivos** | Zip con PCAP `2019-11-12_21:00:30-EXT07.pcap` + `shell.aspx` (web shell remanente) [verificar nombre exacto del zip] |
| **Fecha de resolución** | 2026-09-25 (documentación; resuelto previamente según stub local) |
| **Puntos** | 70 (índice público actual; la nota previa local indicaba 7pts — se corrige aquí) |

---

## 🎯 Objetivo / Goal

> **ES:** Identificar la web shell como SharPyShell (repo público de Antonio Coco), recuperar clave AES + IV, descifrar el tráfico C2 del PCAP con `tshark` + script propio, aislar el shellcode de las peticiones y emularlo (XOR + `speakeasy` x64) para leer la flag (`HTB{...}`).
> **EN:** Identify the web shell as SharPyShell (Antonio Coco's public repo), recover the AES key + IV, decrypt the PCAP's C2 traffic with `tshark` + a custom script, isolate the request shellcode and emulate it (XOR + `speakeasy` x64) to read the flag (`HTB{...}`).

---

## 🛠️ Herramientas usadas / Tools used

- [ ] Wireshark / `tshark` (inspección y exportación del tráfico HTTP del PCAP)
- [ ] CyberChef (decodificados y pruebas AES rápidas)
- [ ] `python3` + `pycryptodome` (script de descifrado del C2, estilo `dcrypt.py` de la fuente)
- [ ] Descompilador .NET / editor (revisar `shell.aspx` y el `runtime_compiler_aes.cs` de referencia)
- [ ] `speakeasy` (emulación del shellcode x64; mejor que `scdbg` en este caso según la fuente)

---

## 📋 Pasos / Steps

### Paso 1 — La web shell pasada por alto / The overlooked web shell

> **ES:** El servidor parecía limpio, pero `shell.aspx` sigue presente: su código corresponde a SharPyShell (compilador en tiempo de ejecución con AES). Reconstruyendo el fichero se obtienen la clave y el IV que cifran el C2.
> **EN:** The server looked clean, but `shell.aspx` is still there: its code matches SharPyShell (AES runtime compiler). Rebuilding the file yields the key and IV encrypting the C2.

```bash
unzip <archivo>.zip && file *
# comparar shell.aspx con el runtime de referencia:
# https://github.com/antonioCoco/SharPyShell/blob/master/agent/runtime_compiler/runtime_compiler_aes.cs
grep -inE "key|iv|aes|encrypt|decrypt" shell.aspx | head -20
```

**Resultado / Result:** Web shell identificada como SharPyShell; clave AES + IV recuperados del código reconstruido (base del descifrado del paso 2).

### Paso 2 — Descifrar el C2 del PCAP / Decrypt the PCAP's C2

> **ES:** Se exporta el tráfico HTTP del PCAP con `tshark` y se descifra cada mensaje con clave+IV (script propio): aparecen request/response en claro del canal C2, donde dos peticiones transportan shellcode.
> **EN:** Export the PCAP's HTTP traffic with `tshark` and decrypt each message with key+IV (custom script): the C2 channel's plaintext request/response appear, with two requests carrying shellcode.

```bash
tshark -r 2019-11-12_21:00:30-EXT07.pcap -Y http -T fields -e http.file_data > c2_blobs.txt
python3 dcrypt.py   # AES con key+IV del paso 1 → request.raw / response.raw
file request.raw response.raw && wc -l request.raw response.raw
```

**Resultado / Result:** Canal C2 en claro reconstruido (`request.raw`/`response.raw`); las líneas de interés transportan shellcode generado por el operador.

### Paso 3 — Shellcode: XOR + emulación / Shellcode: XOR + emulation

> **ES:** El shellcode de una de las peticiones está truncado por un byte `x00` que lo corta: se toma desde el desplazamiento válido, se aplica XOR con la clave corta hallada y se emula el resultado con `speakeasy` en modo x64 para obtener la flag (`HTB{...}`).
> **EN:** One request's shellcode is cut short by an `x00` byte that terminates it: take it from the valid offset, XOR with the short key found, and emulate the result with `speakeasy` in x64 mode to obtain the flag (`HTB{...}`).

```bash
python3 -c "
xor_key = b'<clave_corta>'   # clave XOR hallada en el análisis (paráfrasis de la fuente)
enc = shellcode[380:]        # desde el desplazamiento válido tras el x00
open('shellcode.sc','wb').write(bytes(b ^ xor_key[i % len(xor_key)] for i, b in enumerate(enc)))
"
speakeasy -t shellcode.sc -a x64 -r -m
```

**Resultado / Result:** Shellcode emulado correctamente en x64; la flag en formato `HTB{...}` queda visible en la salida de la emulación (no se reproduce aquí por integridad del contenido; challenge retirado, ver capturas de las fuentes citadas). [verificar] reproducción propia con captura en `img/`.

---

## 🧠 Lo aprendido / Learned

- [ ] Un servidor "limpio" puede conservar una web shell: el PCAP manda cuando el AV calla.
- [ ] Fingerprinting de tooling público (SharPyShell de Antonio Coco) acelera el análisis: el repo explica el cifrado.
- [ ] Patrón C2 .NET ofuscado: `shell.aspx` + AES (clave en código, IV en tráfico) + compilación en tiempo de ejecución.
- [ ] Shellcode cortado por `x00`: buscar el desplazamiento válido y la capa XOR antes de emular.
- [ ] `speakeasy` supera a `scdbg` emulando shellcode x64 moderno.

---

## 📚 Fuentes y Referencias / Sources

- **Walkthrough de referencia:** [Window's Infinity Edge — TwentySeV (HackMD)](https://hackmd.io/@TwentySeV/Sy_SvoTNgg) — TwentySeV (descripción del challenge, `shell.aspx` reconstruido con clave, IV, repo SharPyShell, `tshark`, script de descifrado, request/response, shellcode con `x00`, XOR desde el byte 380 con clave corta, `speakeasy -t … -a x64 -r -m`)
- **Writeups de referencia:** [Window's Infinity Edge — vanniichan/HackTheBox](https://github.com/vanniichan/HackTheBox/tree/main/Window's%20Infinity%20Edge) — vanniichan (`shell.aspx`, `dcrypt.py`, `request.raw`, `response.raw`)
- **Código de referencia del operador:** [SharPyShell — antonioCoco](https://github.com/antonioCoco/SharPyShell/blob/master/agent/runtime_compiler/runtime_compiler_aes.cs) — Antonio Coco (agente `runtime_compiler_aes.cs` reutilizado por el APT del reto)
- **Writeup de referencia:** [HackTheBox: Window's Infinity Edge — forensicskween](https://forensicskween.com/ctf/) — forensicskween (entrada protegida del índice CTF)
- **Hilo oficial:** [Official Window's Infinity Edge Discussion — HTB Forums](https://forum.hackthebox.com/t/official-windows-infinity-edge-discussion/3253) — Hack The Box :: Forums
- **Índice público de challenges:** [foobarto.me/htb/challenges](https://foobarto.me/htb/challenges/) — Bartosz Ptaszyński (`windows_infinity_edge · Forensics · Hard · 70 pts`, 2020-09-11)
- **Nota local previa:** stub raíz `Soluciones/Challenges/window_s_infinity_edge.md` ("Points: 7pts") migrado a esta plantilla; el valor oficial documentado es 70 pts
- **Fecha de acceso:** 2026-09-25
- **Autor de este walkthrough:** Apuromafo (síntesis propia parafraseada a partir de las fuentes citadas)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. Challenge retirado; no se publican flags literales.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Retired challenge; no literal flags published.

_Fecha de edición: 2026-09-25_
