# Chill Hack

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | ctf | `chillhack` | [TryHackMe](https://tryhackme.com/room/chillhack) | 01 Level Easy | THM | FTP anónimo, RCE con filtro, backup.zip, command injection, docker group | Medio |

---

**Contexto:** Máquina boot2root de nivel Easy. El box expone FTP anónimo (nota con los usuarios y una pista sobre la protección del campo de comandos), un servidor web con un portal que ejecuta comandos bajo un filtro evasible (suplencias con xxd, `echo *`, python con un carácter escapado), y una app PHP en /var/www/files cuya imagen contiene un backup.zip protegido con contraseña crackeable. Tras obtener la primera shell como www-data se descubre que .helpline.sh es ejecutable con sudo como apaar y es vulnerable a command injection, permitiendo leer el user flag. La escalada pasa por las credenciales de la base de datos webportal (hashes crackeados) que dan acceso SSH a anurodh, miembro del grupo docker; usando `docker run -v /:/mnt alpine chroot /mnt sh` se lee el root flag.

> **ES:** Box CTF: FTP anónimo → portal web con RCE filtrado (bypass del filtro) → reverse shell → extracción del backup.zip oculto en una imagen → credenciales de la BD webportal → command injection en .helpline.sh → user flag → acceso SSH como anurodh → abuso del grupo docker (GTFOBins) → root flag.

> **EN:** CTF box: anonymous FTP → web portal with filtered RCE (filter bypass) → reverse shell → extraction of the backup.zip hidden in an image → webportal DB credentials → command injection in .helpline.sh → user flag → SSH access as anurodh → docker group abuse (GTFOBins) → root flag.

## Solucionario

### Task 1: Flags / Flags

**Explicación:** Se enumeran 3 servicios (FTP anónimo, web y puerto con servicio adicional). En el FTP anónimo una nota revela los usuarios (anurodh y apaar) y avisa de que habrá que esquivar una protección al introducir comandos. En el portal web algunos comandos funcionan (id) pero otros están filtrados (ls, cat, more, less...); se evitan con alternativas: `xxd` para leer, `echo *` para listar. Se obtiene una reverse shell (python con un carácter escapado) como www-data. En /var/www/files se localiza el portal PHP y una imagen (hacker-with-laptop) con un backup.zip oculto extraíble cuyo password se crackea; el código PHP revela un usuario y una contraseña base64, permitiendo SSH como anurodh. Con sudo se ejecuta /home/apaar/.helpline.sh como apaar, cuyo campo msg inyecta el comando (/bin/bash o reverse shell) → user flag en local.txt. Finalmente, anurodh pertenece al grupo docker y con `docker run -v /:/mnt --rm -it alpine chroot /mnt sh` (GTFOBins) se obtiene root y se lee proof.txt.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | What is the user flag? | `{USER-FLAG: e8vpd3323cfvlp0qpxxx9qtr5iq37oww}` |
| 2 | What is the root flag? | `{ROOT-FLAG: w18gfpn9xehsgd3tovhk0hby4gdp89bg}` |

---

**Metodología:** nmap → FTP anónimo → notas y usuarios → portal web con RCE filtrado → bypass del filtro (xxd, `echo *`, python escapado) → reverse shell → enumeración → /var/www/files → extracción del backup.zip de la imagen → crackeo del password → credenciales de la BD webportal → SSH anurodh → command injection en .helpline.sh (sudo como apaar) → user flag → abuso del grupo docker (GTFOBins) → root flag.

### Cadena de ataque / Attack Chain

FTP anónimo → pistas de usuarios → RCE filtrado en el portal → bypass del filtro → reverse shell (www-data) → backup.zip oculto en imagen → credenciales webportal → SSH anurodh → command injection .helpline.sh → local.txt (user flag) → grupo docker → `docker run ... chroot /mnt sh` → proof.txt (root flag).

**Learning chain:** Enumeración de servicios → FTP anónimo → command execution bypass → reverse shells → steganografía/backup oculto → hash cracking → SQL/DB recon → credential reuse → sudo command injection → Docker misconfiguration → root.

**Lección:** *Un filtro de comandos se esquiva con suplencias del mismo binario, un script con permisos sudo y un campo de mensaje es una inyección de comandos, y un usuario en el grupo docker equivale a root; la enumeración meticulosa encadena todos los eslabones.*

**MITRE ATT&CK:** T1048 (Exfiltration Over Alternative Protocol), T1059 (Command and Scripting Interpreter), T1068 (Exploitation for Privilege Escalation), T1611 (Escape to Host / container), T1083 (File and Directory Discovery).

**Fuente:** [TryHackMe - Chill Hack](https://tryhackme.com/room/chillhack)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.