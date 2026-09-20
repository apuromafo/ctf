# Passwords - A Cracking Christmas

| **Dificultad** | Easy | **Tipo** | walkthrough | **Slug** | `day09passwordsacrackingchristmas` |
| **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber25) |
| **Sección** | Advent of Cyber Tryhackme |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | password cracking / dictionary attacks / mask attacks / brute-force attacks / rockyou.txt / common-passwords.txt / pdfcrack / fcrackzip / john / hashcat / zip2john / pdf2john / GPU-accelerated cracking |
| **Impacto** | Detectar y responder ante intentos de cracking de contraseñas sobre archivos protegidos (PDF/ZIP) |

---

**Contexto:** Día 09 del Advent of Cyber 2025. Se presentan las formas de adivinar la contraseña que protege un archivo (ataques de diccionario, mask attacks y fuerza bruta), las wordlists más comunes (rockyou.txt y common-passwords.txt), las herramientas según el tipo de archivo (pdfcrack/john para PDF, fcrackzip/john para ZIP) y los indicadores para detectar password cracking en una máquina comprometida, cerrando con los flags del PDF y del ZIP cifrados.

## Solucionario

### Día 09: Passwords - A Cracking Christmas

**Explicación:**

- Ways of guessing the password that protects a file
     1. Dictionary Attacks: Use a predefined list of potential passwords (AKA wordlist); useful in case of weak or common passwords
     2. Mask Attacks: Basically, a Brute-force attack, but limits gueasses to a specific format to make it faster
     3. Brute-force Attacks: systematically tries every possible combination of characters until the right one is found

- Common wordlists
     1. rockyou.txt
     2. common-passwords.txt

- You can use GPU-accelerated cracking when possible (in cases such as MD5, SHA-1, SHA-256, NTLM)
- Tools to Use (pick one based on file type)
  1. PDF: pdfcrack, john (via pdf2john)
  2. ZIP: fcrackzip, john (via zip2john)
  3. General: john (very flexible) and hashcat (GPU acceleration, more advanced)

- Tools and indicators for password cracking:
    1. Binaries and aliases: john, hashcat, fcrackzip, pdfcrack, zip2john, pdf2john.pl, 7z, qpdf, unzip, 7za, perl invoking pdf2john.pl.
    2. Command‑line traits: --wordlist, -w, --rules, --mask, -a 3, -m in Hashcat, references to rockyou.txt, SecLists, zip2john, pdf2john.
    3. Potfiles and state: ~/.john/john.pot, .hashcat/hashcat.potfile, john.rec.

- Steps to take when suspicious activity or a possible password-cracking on a machine is detected:
    1. Isolate the system if real malicious activity is suspected; ignore or suppress alerts if it’s just a lab or training machine.
    2. Collect evidence early (running processes, memory, GPU usage, open files, and the protected file involved).
    3. Preserve cracking artefacts like the working folder, wordlists, hash files, and command history.
    4. Check impact by seeing which files or passwords were successfully cracked and whether there was further access or data theft.
    5. Decide intent by identifying who ran the activity and whether it was authorised; escalate if it wasn’t.
    6. Fix and prevent by changing compromised passwords/keys, enforcing MFA, and educating users to keep such tools only in approved lab environments.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag inside the encrypted PDF? | `THM{Cr4ck1ng_PDFs_1s_34$y}` |
| 2 | What is the flag inside the encrypted zip file? | `THM{Cr4ck1n6_z1p$_1s_34$yyyy}` |

---

**Metodología:** Se identificó el tipo de archivo protegido (PDF y ZIP) y se seleccionó la herramienta de cracking adecuada: para el PDF se extrajo el hash con pdf2john y se crackeó con john/hashcat, mientras que para el ZIP se usó zip2john o fcrackzip. Con las contraseñas recuperadas se abrieron ambos archivos y se obtuvieron los flags.
**Learning chain:** Dictionary Attacks -> Mask Attacks -> Brute-force Attacks -> Wordlists (rockyou.txt / common-passwords.txt) -> pdf2john/zip2john (extracción de hash) -> john/hashcat/fcrackzip/pdfcrack -> descifrado de PDF y ZIP -> Flags

Cadena de ataque / Attack Chain:
```
pdf2john.pl archivo.pdf -> hash -> john --wordlist=rockyou.txt -> contraseña PDF -> flag THM{Cr4ck1ng_PDFs_1s_34$y}
zip2john archivo.zip -> hash -> john/hashcat (--mask o --wordlist) -> contraseña ZIP -> flag THM{Cr4ck1n6_z1p$_1s_34$yyyy}
```

**Lección:** *El cracking de contraseñas no es solo fuerza bruta: elegir el ataque correcto (diccionario, mask o fuerza bruta) y la herramienta adecuada al tipo de archivo (pdfcrack vs fcrackzip vs john/hashcat) es clave; además, cualquier máquina con john/hashcat, wordlists y potfiles debe considerarse sospechosa.*

**MITRE ATT&CK:** T1110.002 - Password Cracking

**Fuente:** [TryHackMe - Passwords - A Cracking Christmas](https://tryhackme.com/room/adventofcyber25)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.