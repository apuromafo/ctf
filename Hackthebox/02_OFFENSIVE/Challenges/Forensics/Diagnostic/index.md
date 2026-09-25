# Diagnostic [EASY — verificar en plataforma]

> **ES:** Challenge Forensics: el SOC detecta phishing con un supuesto documento de despidos (`layoffs.doc`) servido por una instancia Docker (`diagnostic.htb`); el `.doc` es en realidad un contenedor OOXML con una referencia externa a un tema HTML (`..._index_style_fancy.html!`) que explota Follina (CVE-2022-30190, `msdt.exe`) y esconde un PowerShell ofuscado con `-f` donde la flag (`HTB{...}`) está fragmentada y reordenada.
> **EN:** Forensics challenge: the SOC spots phishing with a supposed layoffs document (`layoffs.doc`) served by a Docker instance (`diagnostic.htb`); the `.doc` is actually an OOXML container with an external theme reference (`..._index_style_fancy.html!`) exploiting Follina (CVE-2022-30190, `msdt.exe`) and hiding a `-f`-obfuscated PowerShell where the flag (`HTB{...}`) is split and reordered.

| Campo | Valor |
|-------|-------|
| **Categoría** | Forensics |
| **Dificultad** | Easy [verificar en plataforma; las fuentes externas consultadas no indican dificultad oficial] |
| **Estado** | Retired (hilo oficial de 2022; sin flag literal aquí por criterio de la colección) |
| **URL** | https://app.hackthebox.com/challenges/Diagnostic [verificar slug exacto] |
| **Archivos** | `layoffs.doc` (vía instancia Docker `diagnostic.htb:<puerto>/layoffs.doc`) + referencia externa `223_index_style_fancy.html` [verificar nombre exacto del zip] |
| **Fecha de resolución** | 2026-09-25 (documentación; resuelto previamente según stub local) |
| **Puntos** | [verificar] (nota previa local: 2pts, sistema de puntuación antiguo) |

---

## 🎯 Objetivo / Goal

> **ES:** Descargar el `.doc` sin abrirlo, demostrar que es un OOXML (zip) con referencia externa maliciosa, recuperar el payload HTML/Base64 del tema, decodificar el PowerShell ofuscado y recomponer la flag ordenando los fragmentos del operador `-f`.
> **EN:** Download the `.doc` without opening it, prove it is an OOXML (zip) with a malicious external reference, recover the HTML/Base64 theme payload, decode the obfuscated PowerShell, and rebuild the flag by ordering the `-f` fragments.

---

## 🛠️ Herramientas usadas / Tools used

- [ ] Instancia Docker del challenge + `curl` (descarga del `.doc` y del HTML del tema)
- [ ] `file`, `cp`, `unzip`, `find`/`grep` (triage del contenedor OOXML)
- [ ] CyberChef (`From Base64`) o `base64 -d` (decodificación del payload)
- [ ] `oleid` / `oleobj` / `olevba` (oletools; análisis estático alternativo del documento) [verificar reproducción propia]
- [ ] Python3 o PowerShell local (reordenar los fragmentos `{n}` del operador `-f`; sin ejecutar el payload)

---

## 📋 Pasos / Steps

### Paso 1 — Descargar el documento sin abrirlo / Download without opening

> **ES:** La descripción apunta a phishing con enlace a `diagnostic.htb/layoffs.doc`. Se resuelve el dominio contra la IP de la instancia y se descarga el archivo. No abrirlo en una máquina sin sandbox: es la muestra maliciosa.
> **EN:** The description points to phishing linking `diagnostic.htb/layoffs.doc`. Resolve the domain to the instance IP and download the file. Do not open it outside a sandbox: it is the malicious sample.

```bash
echo "<IP-instancia> diagnostic.htb" | sudo tee -a /etc/hosts
curl -s -o layoffs.doc http://diagnostic.htb:<puerto>/layoffs.doc
file layoffs.doc
# esperado: .../Zip archive data ... (contenedor OOXML, no .doc binario clásico)
```

**Resultado / Result:** `layoffs.doc` descargado y detectado como datos zip/OOXML [verificar captura propia en `img/`].

### Paso 2 — Tratar el .doc como zip y localizar la referencia externa / Unzip and find the external reference

> **ES:** Se copia a `.zip`, se descomprime y se rastrea la URL del tema con `!` final (marca típica de Follina/CVE-2022-30190: el URI largo terminado en `!` fuerza a `msdt.exe` a procesar el HTML remoto al abrir el documento).
> **EN:** Copy to `.zip`, extract, and hunt for the theme URL with a trailing `!` (typical Follina/CVE-2022-30190 marker: the long URI ending in `!` makes `msdt.exe` process the remote HTML when the document opens).

```bash
mkdir -p triage && cp layoffs.doc triage/layoffs.zip
cd triage && unzip -o -q layoffs.zip -d ooxml
grep -rhoE 'http://diagnostic\.htb:[0-9]+/[^"<> ]+!' ooxml/ | sort -u
# esperado: http://diagnostic.htb:<puerto>/223_index_style_fancy.html!
```

**Resultado / Result:** Referencia externa al HTML del tema con `!` final localizada en los XML del documento (paráfrasis de Carrick Blake y Fataal Muthoni).

### Paso 3 — Descargar el HTML y extraer el Base64 / Fetch the HTML and extract Base64

> **ES:** Se descarga el HTML del tema y se aísla el bloque Base64 (el resto es relleno —letras de canciones universitarias— para superar los ~4096 bytes que exige el exploit).
> **EN:** Download the theme HTML and isolate the Base64 blob (the rest is filler — college fight-song lyrics — to exceed the ~4096 bytes the exploit requires).

```bash
curl -s 'http://diagnostic.htb:<puerto>/223_index_style_fancy.html' -o theme.html
grep -oE '[A-Za-z0-9+/=]{200,}' theme.html | head -5
# esperado: un bloque Base64 largo (el payload) entre el relleno
```

**Resultado / Result:** Bloque Base64 del payload aislado [verificar reproducción propia].

### Paso 4 — Decodificar y recomponer la flag / Decode and rebuild the flag

> **ES:** El Base64 decodificado muestra un PowerShell con formato `"...{7}{1}..." -f '...','B{msDt_4s_A_pr0',...` más un `Invoke-WebRequest` de segunda etapa (`.../mation.di.../n.exe` → `C:\Windows\Tasks\...`) y relleno. La flag no está en claro: hay que ordenar los fragmentos según los índices `{7}{1}{6}{8}{5}{3}{2}{4}{0}`.
> **EN:** The decoded Base64 shows PowerShell shaped as `"...{7}{1}..." -f '...','B{msDt_4s_A_pr0',...` plus a second-stage `Invoke-WebRequest` (`.../mation.di.../n.exe` → `C:\Windows\Tasks\...`) and filler. The flag is not in plaintext: order the fragments per the `{7}{1}{6}{8}{5}{3}{2}{4}{0}` indexes.

```bash
# Decodificar (CyberChef "From Base64" o):
base64 -d payload.b64 > payload.txt
grep -o '\${f`ile}.*' payload.txt | head -c 600

# Recomponer la flag (paráfrasis; sin ejecutar el payload):
python3 - <<'EOF'
frags = ['}.exe','B{msDt_4s_A_pr0','E','r...s','3Ms_b4D','l3','toC','HT','0l_h4nD']
order = [7,1,6,8,5,3,2,4,0]
print(''.join(frags[i] for i in order))
# esperado: flag con formato HTB{...} (no se reproduce literal aquí)
EOF
```

**Resultado / Result:** Flag con formato `HTB{...}` recompuesta a partir de los fragmentos ordenados (criterio de la colección: no se pegan flags literales aunque el challenge esté retirado). [verificar] reproducción propia con captura en `img/`.

---

## 🧠 Lo aprendido / Learned

- [ ] Un `.doc` moderno es un contenedor OOXML (zip): `file` + `unzip` + `grep` bastan para el triage inicial sin abrir la muestra.
- [ ] Follina (CVE-2022-30190): un URI largo terminado en `!` en una referencia externa (tema HTML) hace que `msdt.exe` procese contenido remoto al abrir el documento; el relleno (~4096 bytes) es parte del exploit, no ruido.
- [ ] Ofuscación PowerShell con `-f`: `"...{n}..." -f a,b,c` reordena fragmentos; leer los índices revela la cadena real (aquí, la flag) sin ejecutar nada.
- [ ] El payload incluía segunda etapa (`Invoke-WebRequest` → binario en `C:\Windows\Tasks\`): en forense basta con describirla, nunca ejecutarla.
- [ ] `oleid`/`oleobj`/`olevba` son la vía alternativa estándar para el mismo triage (paráfrasis de Fataal Muthoni) [verificar reproducción propia].

---

## 📚 Fuentes y Referencias / Sources

- **Writeup de referencia:** [Analyzing Malicious Word Documents (HTB Challenge - Diagnostic) — Carrick Blake](https://loqt-cb.github.io/posts/HackTheBox-Diagnostic/) — Carrick Blake, 2025-12-03 (escenario SOC/phishing, `/etc/hosts` + `curl` del `.doc`, `file`→zip, `grep htb`→URL del tema con `!`, CyberChef `From Base64`, orden de fragmentos `-f`, Follina CVE-2022-30190 y relleno de 4096 bytes)
- **Writeup de referencia:** [Diagnostic HTB CTF Write-up — Fataal Muthoni](https://f4taal.github.io/posts/HTB-Diagnostic-CTF-Challenge-Writeup/) — Fataal Muthoni, 2024-01-24 (`diagnostic.doc` vía IP de instancia, `oleid`/`oleobj`, script en la página del tema, ASCII→Base64 en CyberChef, concatenación del PowerShell con `-f`)
- **Análisis complementario:** [Microsoft Office Word Document Malware Analysis (HackTheBox Diagnostic) — Motasem Hamdan](https://motasemhamdan.medium.com/microsoft-office-word-document-malware-analysis-hackthebox-diagnostic-f91e68a56732) — Motasem Hamdan (análisis del `.doc` malicioso; acceso 2026-09-25, cita parcial por 403 en la descarga)
- **Hilo oficial:** [Official Diagnostic Discussion](https://forum.hackthebox.com/t/official-diagnostic-discussion/259013) — Hack The Box :: Forums (hilo oficial, sin spoilers)
- **Nota local previa:** stub raíz `Soluciones/Challenges/diagnostic.md` ("Points: 2pts / Status: Solved") migrado a esta plantilla
- **Fecha de acceso:** 2026-09-25
- **Autor de este walkthrough:** Apuromafo (síntesis propia parafraseada a partir de las fuentes citadas)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. Challenge retirado; no se publican flags literales. No abrir muestras maliciosas fuera de un entorno aislado.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Retired challenge; no literal flags published. Do not open malicious samples outside an isolated environment.

_Fecha de edición: 2026-09-25_
