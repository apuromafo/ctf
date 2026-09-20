# Passwords - A Cracking Christmas

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `attacks-on-ecrypted-files-aoc2025-asdfghj123` | https://tryhackme.com/room/attacks-on-ecrypted-files-aoc2025-asdfghj123 | Advent of Cyber 2025 | TryHackMe | John the Ripper, PDF cracking, ZIP cracking | Cracking encrypted files using offline tools for credential/flag extraction |

---

**Contexto:** SOC-mas necesita recuperar archivos cifrados que contienen banderas de seguridad. Los archivos protegidos — un PDF y un ZIP — usan contraseñas débiles crackeables con John the Ripper. Un desafío clásico de cracked passwords en Navidad.

> **ES:** SOC-mas necesita recuperar los archivos cifrados (PDF y ZIP) que contienen flags: se extraen sus hashes con `pdf2john`/`zip2john` y se rompen con John the Ripper y `rockyou.txt` para descifrar su contenido y obtener las banderas.
> **EN:** SOC-mas needs to recover encrypted files (a PDF and a ZIP) that contain flags: extract their hashes with `pdf2john`/`zip2john`, crack them with John the Ripper and `rockyou.txt`, and decrypt the content to retrieve the flags.

## Solucionario

### Task 1: Cracking de Archivos Cifrados / Cracking Encrypted Files

**Explicación:** El room entrega un PDF y un ZIP protegidos con contraseña. Para el PDF se usa `pdf2john` (convertidor del formato PDF al hash que entiende John the Ripper) y para el ZIP `zip2john`. Ambos generan un hash que se pasa a `john -w rockyou.txt` para un ataque de diccionario. Las contraseñas débiles ceden rápidamente y, una vez abiertos los archivos, se extraen las flags: la del PDF (`THM{Cr4ck1ng_PDFs_1s_34$y}`) y la del ZIP (`THM{Cr4ck1n6_z1p$_1s_34$yyyy}`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag inside the encrypted PDF? | `THM{Cr4ck1ng_PDFs_1s_34$y}` |
| 2 | What is the flag inside the encrypted zip file? | `THM{Cr4ck1n6_z1p$_1s_34$yyyy}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag inside the encrypted PDF? | `THM{Cr4ck1ng_PDFs_1s_34$y}` |
| 2 | What is the flag inside the encrypted zip file? | `THM{Cr4ck1n6_z1p$_1s_34$yyyy}` |

---

**Metodología:** Se utilizó `john` con wordlist `rockyou.txt` y la herramienta `pdf2john` / `zip2john` para generar hashes a partir de los archivos cifrados, luego se crackearon las contraseñas débiles para extraer los flags internos.

### Cadena de ataque / Attack Chain

```text
PDF/ZIP cifrados -> pdf2john/zip2john (extracción de hash) -> john + rockyou.txt (ataque de diccionario) -> contraseña débil -> descifrado/extracción -> flags
```

**Learning chain:** PDF/ZIP encryption → hash extraction (`pdf2john`, `zip2john`) → dictionary attack (John the Ripper + rockyou.txt) → flag retrieval from decrypted content

**Lección:** *El cifrado en reposo solo protege si la contraseña es fuerte: cualquier PDF o ZIP cifrado con una contraseña presente en `rockyou.txt` caerá en segundos ante un ataque de diccionario con John the Ripper.*

**MITRE ATT&CK:** N/A (defensive walkthrough)

**Fuente:** [TryHackMe - Passwords - A Cracking Christmas](https://tryhackme.com/r/room/attacks-on-ecrypted-files-aoc2025-asdfghj123)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.