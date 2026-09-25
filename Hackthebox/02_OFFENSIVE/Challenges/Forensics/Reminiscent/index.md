# Reminiscent [EASY]

> **ES:** Challenge Forensics Easy: tráfico sospechoso desde el PC virtual de un reclutador; se entrega un memory dump (`flounder-pc.memdump.elf`) más `imageinfo.txt` y una copia del email (`Resume.eml`) con el supuesto currículum. Hay que encontrar y decodificar el origen del malware para obtener la flag (`HTB{...}`).
> **EN:** Easy Forensics challenge: suspicious traffic from a recruiter's virtual PC; a memory dump (`flounder-pc.memdump.elf`) is provided plus `imageinfo.txt` and a copy of the email (`Resume.eml`) with the alleged resume. Find and decode the malware source to get the flag (`HTB{...}`).

| Campo | Valor |
|-------|-------|
| **Categoría** | Forensics |
| **Dificultad** | Easy |
| **Estado** | Retired |
| **URL** | https://app.hackthebox.com/challenges/Reminiscent |
| **Archivos** | Zip con `flounder-pc.memdump.elf` + `imageinfo.txt` + `Resume.eml` [verificar nombre exacto del zip] |
| **Fecha de resolución** | 2026-09-25 (documentación; resuelto previamente según stub local) |
| **Puntos** | 30 (índice público actual; índices antiguos listaban Medium/40pts y la nota previa local 3pts — ver Fuentes) |

---

## 🎯 Objetivo / Goal

> **ES:** Analizar el dump con Volatility (perfil `Win7SP1x64`): listar procesos, detectar el `powershell.exe` con conexiones externas, extraer su línea de comando en base64, decodificar el stager (anti-logging/AMSI + RC4 + descarga HTTP) y leer la flag embebida (`HTB{...}`).
> **EN:** Analyze the dump with Volatility (`Win7SP1x64` profile): list processes, spot the `powershell.exe` with external connections, extract its base64 command line, decode the stager (anti-logging/AMSI + RC4 + HTTP download) and read the embedded flag (`HTB{...}`).

---

## 🛠️ Herramientas usadas / Tools used

- [ ] `unzip` + `file` (extracción del paquete)
- [ ] Volatility 2 (`--profile=Win7SP1x64`) o Volatility 3 (`windows.*`)
- [ ] Thunderbird / lector `.eml` (revisar el correo del "currículum")
- [ ] `base64` + CyberChef (decodificar el `-enc` de PowerShell y capas siguientes)

---

## 📋 Pasos / Steps

### Paso 1 — Triage: email + perfil del dump / Triage: email + dump profile

> **ES:** El `.eml` muestra que el usuario descargó un `resume.zip`: probable vector de entrada. `imageinfo.txt` sugiere el perfil `Win7SP1x64` para Volatility.
> **EN:** The `.eml` shows the user downloaded a `resume.zip`: likely entry vector. `imageinfo.txt` suggests the `Win7SP1x64` Volatility profile.

```bash
unzip <archivo>.zip && file *
cat imageinfo.txt          # Suggested Profile(s): Win7SP1x64, …
# leer Resume.eml: remitente/asunto/adjunto resume.zip
volatility -f flounder-pc.memdump.elf --profile=Win7SP1x64 pslist
# o en Volatility 3: vol.py -f flounder-pc.memdump.elf windows.pslist
```

**Resultado / Result:** Pista del vector (currículum por email) y perfil válido; `pslist` lista procesos normales más dos `powershell.exe`, uno de ellos tardío (PID 2752) que se convierte en sospechoso principal.

### Paso 2 — Conexiones del sospechoso / Suspect connections

> **ES:** Con `netscan`/`connections` se buscan sockets del `powershell.exe` sospechoso: aparecen conexiones cerradas contra `10.10.99.55:80` (HTTP), impropias de un uso legítimo de PowerShell por un reclutador.
> **EN:** With `netscan`/`connections` look for sockets of the suspect `powershell.exe`: closed connections to `10.10.99.55:80` (HTTP) show up — unusual for a recruiter's legitimate PowerShell use.

```bash
volatility -f flounder-pc.memdump.elf --profile=Win7SP1x64 netscan | grep -i powershell
# o en Volatility 3: vol.py -f flounder-pc.memdump.elf windows.netscan
# esperado: PID 2752 powershell.exe ↔ 10.10.99.55:80 (CLOSED)
```

**Resultado / Result:** El PID 2752 habló por HTTP con `10.10.99.55:80`: candidato a canal C2; el siguiente paso es ver qué comando lanzó ese proceso.

### Paso 3 — Línea de comando, base64 y flag / Command line, base64 and flag

> **ES:** `cmdline --pid 2752` devuelve un `powershell.exe -enc …` en base64 (UTF-16LE). Al decodificarlo se lee el stager: desactiva `ScriptBlockLogging`/trazas y AMSI, monta un RC4 casero (bucle KSA/PRGA sobre tabla 0..255), descarga `/login/process.php` con cookie de sesión y descifra la respuesta (IV = primeros 4 bytes + clave ASCII); la variable del script porta la flag (`HTB{...}`). Vía alternativa documentada: `filescan | grep -i resume` + `dumpfiles` del fichero del currículum y decodificados base64 encadenados.
> **EN:** `cmdline --pid 2752` returns a base64 `-enc` PowerShell (UTF-16LE). Decoding it reveals the stager: it disables `ScriptBlockLogging`/tracing and AMSI, builds a home-grown RC4 (KSA/PRGA loop over a 0..255 table), downloads `/login/process.php` with a session cookie and decrypts the response (IV = first 4 bytes + ASCII key); a script variable carries the flag (`HTB{...}`). Documented alternate route: `filescan | grep -i resume` + `dumpfiles` of the resume file and chained base64 decodings.

```bash
volatility -f flounder-pc.memdump.elf --profile=Win7SP1x64 cmdline --pid 2752
# o en Volatility 3: vol.py -f flounder-pc.memdump.elf windows.cmdline --pid 2752
echo '<bloque_-enc>' | base64 -d | iconv -f UTF-16LE -t UTF-8 | head -c 600
# leer: GroupPolicy ScriptBlockLogging=0, AMSI amsiInitFailed=True,
#      WebClient + User-Agent, RC4 $R, cookie session=…, $ser=http://10.10.99.55:80, $t=/login/process.php
```

**Resultado / Result:** Stager completamente legible: evasión de logging/AMSI + exfiltración/descarga HTTP con RC4; la flag en formato `HTB{...}` aparece en el propio comando decodificado (no se reproduce aquí por integridad del contenido; challenge retirado, ver capturas de las fuentes citadas). [verificar] reproducción propia con captura en `img/`.

---

## 🧠 Lo aprendido / Learned

- [ ] Flujo clásico de memory forensics: `imageinfo` → `pslist` → `netscan` → `cmdline --pid`.
- [ ] `powershell.exe -enc` = base64 de UTF-16LE: decodificar con `iconv -f UTF-16LE` tras `base64 -d`.
- [ ] Marcas de stager malicioso: desactivar `ScriptBlockLogging`/trazas, neutralizar AMSI, `Net.WebClient` con `User-Agent` falso y cookie de sesión.
- [ ] RC4 casero en PowerShell: bucles KSA/PRGA sobre `0..255` + XOR; IV prefijado (primeros bytes) + clave ASCII.
- [ ] El `.eml` no es decorado: confirma el vector (currículum) y orienta `filescan | grep resume` como ruta alternativa.

---

## 📚 Fuentes y Referencias / Sources

- **Walkthrough de referencia:** [HTB Reminiscent – harshitm98](https://harshitm98.github.io/posts/htb-challenge-reminiscent/) — Harshit Maheshwari (setup Volatility 3, `windows.pslist`/`windows.netscan`/`windows.cmdline --pid 2752`, conexiones del PID 2752 a `10.10.99.55:80`, decodificado del `-enc` con ScriptBlockLogging/AMSI/RC4/cookie/`/login/process.php`)
- **Walkthrough de referencia:** [Reminiscent — jon-brandy/hackthebox](https://github.com/jon-brandy/hackthebox/blob/main/Categories/Forensics/Reminiscent/README.md) — jon-brandy (descripción oficial, perfil `Win7SP1x64`, ruta alternativa `filescan | grep resume` + `dumpfiles --physoffset …` y decodificados base64)
- **Writeup de referencia:** [Reminiscent — Isaac Potts](https://medium.com/@isaac.potts03/reminiscent-hack-the-box-forensics-e67b365071e0) — Isaac Potts (primer CTF forense del autor con `readelf`/Volatility)
- **Índice público de challenges:** [foobarto.me/htb/challenges](https://foobarto.me/htb/challenges/) — Bartosz Ptaszyński (`reminiscent · Forensics · Easy · 30 pts`, 2017-10-26)
- **Índice histórico:** [HTB Retired Challenges — jebidiah-anthony](https://jebidiah-anthony.github.io/chals/htb/challenges.html) — Jebidiah Anthony (listaba `Reminiscent · Forensics · 40 pts · Medium`; HTB reequilibró puntos/dificultad con el tiempo — se adopta el valor actual Easy/30)
- **Hilo oficial:** [Reminiscent aka Mem Forensics — HTB Forums](https://forum.hackthebox.com/t/reminiscent-aka-mem-forensics/525) — Hack The Box :: Forums
- **Nota local previa:** stub raíz `Soluciones/Challenges/reminiscent.md` ("Points: 3pts") migrado a esta plantilla; el valor oficial documentado es 30 pts
- **Fecha de acceso:** 2026-09-25
- **Autor de este walkthrough:** Apuromafo (síntesis propia parafraseada a partir de las fuentes citadas)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. Challenge retirado; no se publican flags literales.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Retired challenge; no literal flags published.

_Fecha de edición: 2026-09-25_
