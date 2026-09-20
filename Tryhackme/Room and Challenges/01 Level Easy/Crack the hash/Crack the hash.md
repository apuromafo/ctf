# Crack the hash

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | Password cracking / Hashing | `crackthehash` | https://tryhackme.com/room/crackthehash | 01 Level Easy | TryHackMe | hash identificación / hashcat / John the Ripper / crackstation / rockyou.txt / MD5 / SHA1 / SHA256 / MD4 / NTLM / bcrypt / sha512crypt / HMAC-SHA1 | Aprender a identificar el tipo de hash y crackearlos con wordlists (rockyou.txt) usando hashcat, John the Ripper y herramientas online. |

---

**Contexto:** Sala centrada en el crackeo de hashes. Se presentan dos niveles de dificultad (Level 1 y Level 2) con hashes de distintos algoritmos y, en el nivel 2, hashes salados y modos avanzados de hashcat (NTLM, sha512crypt, HMAC-SHA1). El objetivo es identificar correctamente el algoritmo con herramientas como `hash-identifier`/haiti y descifrar cada hash con la wordlist `rockyou.txt`.

> **ES:** "Identifica el tipo de hash y crackéalo. En el nivel 2 los hashes son más difíciles: todos los passwords están en rockyou.txt y tendrás que consultar los ejemplos de hashcat."
> **EN:** "Identify the hash type and crack it. In level 2 the hashes are harder: all passwords are in rockyou.txt and you may have to check the hashcat example hashes."

## Solucionario

### Task 1: Nivel 1 / Level 1

**Explicación:** Se entregan cinco hashes de algoritmos comunes. Para cada uno se identifica el formato (MD5, SHA1, SHA256, bcrypt, MD4) y se crackea contra `rockyou.txt` con hashcat o John the Ripper. El quinto hash (MD4) no aparece en hashcat con `rockyou.txt` tal cual, así que se resuelve con una herramienta online tipo CrackStation.

```bash
hash-identifier <hash>                       # o haiti <hash>
hashcat -m 0     <hash> rockyou.txt          # MD5    -> easy
hashcat -m 100   <hash> rockyou.txt          # SHA1   -> password123
hashcat -m 1400  <hash> rockyou.txt          # SHA256 -> letmein
hashcat -m 3200  <hash> rockyou.txt          # bcrypt -> bleh
hashcat -m 900   <hash> rockyou.txt          # MD4    -> Eternity22 (se resuelve online)
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Crackea `48bb6e862e54f2a795ffc4e541caed4d` (MD5). / Crack the hash `48bb6e862e54f2a795ffc4e541caed4d` (MD5). | `easy` |
| 2 | Crackea `CBFDAC6008F9CAB4083784CBD1874F76618D2A97` (SHA1). / Crack the hash `CBFDAC6008F9CAB4083784CBD1874F76618D2A97` (SHA1). | `password123` |
| 3 | Crackea `1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032` (SHA256). / Crack the hash `1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032` (SHA256). | `letmein` |
| 4 | Crackea `$2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom` (bcrypt). / Crack the hash `$2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom` (bcrypt). | `bleh` |
| 5 | Crackea `279412f945939ba78ce0758d3fd83daa` (MD4). / Crack the hash `279412f945939ba78ce0758d3fd83daa` (MD4). | `Eternity22` |

---

### Task 2: Nivel 2 / Level 2

**Explicación:** En este nivel los hashes requieren modos específicos de hashcat y, en dos casos, del uso de sal. El primero es SHA256, el segundo un hash NTLM, el tercero sha512crypt (`$6$...`) y el último un HMAC-SHA1 con sal `tryhackme` (modo 160).

```bash
hashcat -m 1400  <hash> rockyou.txt          # SHA256    -> paule
hashcat -m 1000  <hash> rockyou.txt          # NTLM      -> n63umy8lkf4i
hashcat -m 1800  <hash> rockyou.txt          # sha512crypt -> waka99
hashcat -m 160   e5d8870e5bdd26602cab8dbe07a942c8669e56d6:tryhackme rockyou.txt   # HMAC-SHA1 -> 481616481616
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Crackea `F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85` (SHA256). / Crack the hash `F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85` (SHA256). | `paule` |
| 2 | Crackea `1DFECA0C002AE40B8619ECF94819CC1B` (NTLM). / Crack the hash `1DFECA0C002AE40B8619ECF94819CC1B` (NTLM). | `n63umy8lkf4i` |
| 3 | Crackea `$6$aReallyHardSalt$6WKUTqzq.UQQmrm0p/T7MPpMbGNnzXPMAXi4bJMl9be.cfi3/qxIf.hsGpS41BqMhSrHVXgMpdjS6xeKZAs02` (sha512crypt). / Crack the hash `$6$aReallyHardSalt$6WKUTqzq.UQQmrm0p/T7MPpMbGNnzXPMAXi4bJMl9be.cfi3/qxIf.hsGpS41BqMhSrHVXgMpdjS6xeKZAs02` (sha512crypt). | `waka99` |
| 4 | Crackea `e5d8870e5bdd26602cab8dbe07a942c8669e56d6` con sal `tryhackme` (HMAC-SHA1). / Crack the hash `e5d8870e5bdd26602cab8dbe07a942c8669e56d6` with salt `tryhackme` (HMAC-SHA1). | `481616481616` |

---

| # | Task | Pregunta | Respuesta |
|---|------|----------|-----------|
| 1 | Level 1 | Hash MD5 `48bb6e862e54f2a795ffc4e541caed4d` | `easy` |
| 2 | Level 1 | Hash SHA1 `CBFDAC6008F9CAB4083784CBD1874F76618D2A97` | `password123` |
| 3 | Level 1 | Hash SHA256 `1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032` | `letmein` |
| 4 | Level 1 | Hash bcrypt `$2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom` | `bleh` |
| 5 | Level 1 | Hash MD4 `279412f945939ba78ce0758d3fd83daa` | `Eternity22` |
| 6 | Level 2 | Hash SHA256 `F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85` | `paule` |
| 7 | Level 2 | Hash NTLM `1DFECA0C002AE40B8619ECF94819CC1B` | `n63umy8lkf4i` |
| 8 | Level 2 | Hash sha512crypt `$6$aReallyHardSalt$6WKUTqzq.UQQmrm0p/T7MPpMbGNnzXPMAXi4bJMl9be.cfi3/qxIf.hsGpS41BqMhSrHVXgMpdjS6xeKZAs02` | `waka99` |
| 9 | Level 2 | Hash HMAC-SHA1 `e5d8870e5bdd26602cab8dbe07a942c8669e56d6` (salt `tryhackme`) | `481616481616` |

---

**Metodología:** Para cada hash: 1) identificar el formato con `hash-identifier`/`haiti` o la web de ejemplos de hashcat; 2) elegir el modo correspondiente (`-m`); 3) lanzar el ataque de diccionario con `rockyou.txt`; 4) en los casos especiales usar herramienta online (CrackStation) o los parámetros con sal indicados en el reto.

### Cadena de ataque / Attack Chain

```text
hash-identifier/haiti -> identificar algoritmo -> elegir modo hashcat -> ataque con rockyou.txt -> recuperar el plaintext (y->contraseña)
```

**Learning chain:** identificación de hash -> hashcat -m 0/100/1400/3200/900/1000/1800/160 -> rockyou.txt -> CrackStation -> password recovery.

**Lección:** *Identificar el algoritmo correcto del hash es el paso decisivo; un solo modo equivocado en hashcat hace que nunca encuentres el plaintext aunque esté en la wordlist.*

**MITRE ATT&CK:** N/A (ejercicio de cracking local; relacionado con T1003 - OS Credential Dumping)

**Fuente:** [TryHackMe - Crack the hash](https://tryhackme.com/room/crackthehash)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.