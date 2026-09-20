# Easy Peasy

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | challenge | `easypeasy` | [TryHackMe](https://tryhackme.com/room/easypeasy) | 01 Level Easy | TryHackMe | nmap / nginx / Apache / directory brute-fource / GoBuster / Steghide / hashes / privilegios | Enumerar un servicio web, encontrar directorios ocultos, extraer flags y credenciales y escalar privilegios. |

> **Objeto:** Comprometer la máquina Easy Peasy: escanear los servicios abiertos, enumerar dos servidores web (nginx en el 80 y Apache en el puerto alto), localizar directorios ocultos con GoBuster, extraer un mensaje oculto de una imagen con Steghide y escalar privilegios para leer la flag final.

---

**Contexto:** La máquina expone 3 puertos. El servidor nginx del puerto 80 oculta un directorio con la primera flag y pistas hacia el Apache del puerto alto, donde se esconden más flags. Una imagen permite extraer con Steghide la contraseña del usuario, y una tarea crontab mal configurada permite hacer lectura de flags del sistema (todas las flags tienen formato flag{...}).

> **ES:** Reto de nivel Easy de enumeración web y escalada. Se detectan 3 puertos abiertos; el servicio Apache del puerto alto (65524) y el nginx del 80. Con GoBuster se encuentra /n0th1ng3ls3m4tt3r (flag 1), en el otro servidor una página oculta da la flag 2 y la flag 3 aparece en un documento del sistema; con Steghide se extrae de una imagen la contraseña para entrar por SSH y una tarea programada (crontab) permite leer la flag 4 y la flag final.
> **EN:** Easy web-enumeration and privilege-escalation challenge. 3 open ports are found; Apache on the high port (65524) and nginx on 80. GoBuster finds /n0th1ng3ls3m4tt3r (flag 1), a hidden page on the other server gives flag 2, flag 3 is in a system doc, Steghide extracts the SSH password from an image, and a crontab job allows reading flag 4 and the final flag.

## Solucionario

### Task 1: Reconocimiento inicial / Introduction & Scanning
**Explicación:** Escaneo de puertos de la máquina para descubrir los servicios expuestos: la respuesta cuenta los puertos abiertos vía nmap.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many ports are open? / ¿Cuántos puertos están abiertos? | `3` |

### Task 2: Enumeración web / Web Enumeration
**Explicación:** Sobre el puerto 80 corre nginx (versión 1.16.1). El tercer puerto (el más alto) sirve un sitio Apache. Un directorio oculto, /n0th1ng3ls3m4tt3r, contiene la primera flag y pistas hacia el resto del reto.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the version of nginx? / ¿Cuál es la versión de nginx? | `1.16.1` |
| 2 | What is running on the highest port? / ¿Qué se está ejecutando en el puerto más alto? | `Apache` |
| 3 | What flag does the hidden directory give you? / ¿Qué flag te da el directorio oculto? | `flag{f1rs7_fl4g}` |

### Task 3: Comprometiendo la máquina / Compromising the machine
**Explicación:** En el Apache del puerto alto se encuentra la flag 2 y una imagen que, analizada con Steghide, revela la contraseña y el binario (iconvertedmypasswordtobinary) para acceder por SSH. La flag 3 está en un documento del sistema con duplicados (desencriptando el hash). Una tarea crontab permite leer la flag 4 y la flag final como el usuario objetivo. División de tareas al hacer login: usar el nombre de usuario del directorio home y la contraseña extraída.

```bash
gobuster dir -u http://MACHINE_IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
steghide extract -sf image.jpg        # extraer el mensaje oculto
unshadow /etc/passwd /etc/shadow > unshadow.txt && john unshadow.txt   # cracking opcional
cat /var/www/path-to-doc               # flag 3 en el documento del sistema
ls /etc/crontab                        # tarea programada para la escalada
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag 1? / ¿Cuál es la flag 1? | `flag{f1rs7_fl4g}` |
| 2 | What is the flag 2? / ¿Cuál es la flag 2? | `flag{1m_s3c0nd_fl4g}` |
| 3 | What is the flag 3? / ¿Cuál es la flag 3? | `flag{9fdafbd64c47471a8f54cd3fc64cd312}` |
| 4 | What is the password? / ¿Cuál es la contraseña? | `mypasswordforthatjob` |
| 5 | What is the binary? / ¿Cuál es el binario? | `iconvertedmypasswordtobinary` |
| 6 | What is the flag 4? / ¿Cuál es la flag 4? | `flag{n0wits33msn0rm4l}` |
| 7 | What is the flag 5 (final flag)? / ¿Cuál es la flag 5 (flag final)? | `flag{63a9f0ea7bb98050796b649e85481845}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many ports are open? | `3` |
| 2 | What is the version of nginx? | `1.16.1` |
| 3 | What is running on the highest port? | `Apache` |
| 4 | What flag does the hidden directory give you? | `flag{f1rs7_fl4g}` |
| 5 | What is the flag 1? | `flag{f1rs7_fl4g}` |
| 6 | What is the flag 2? | `flag{1m_s3c0nd_fl4g}` |
| 7 | What is the flag 3? | `flag{9fdafbd64c47471a8f54cd3fc64cd312}` |
| 8 | What is the password? | `mypasswordforthatjob` |
| 9 | What is the binary? | `iconvertedmypasswordtobinary` |
| 10 | What is the flag 4? | `flag{n0wits33msn0rm4l}` |
| 11 | What is the flag 5 (final flag)? | `flag{63a9f0ea7bb98050796b649e85481845}` |

---

**Metodología:** Escaneo con nmap para descubrir los 3 puertos y sus servicios. Con GoBuster se fuzzan los directorios del servidor, encontrando /n0th1ng3ls3m4tt3r. Se enumeran las páginas del Apache del puerto alto, se extrae el mensaje oculto de una imagen con Steghide (contraseña y binario) y se desencripta la contraseña para conectar por SSH. Dentro del sistema se localizan las flags 3 y 4 y, abusando de la tarea crontab, se alcanza la flag final.

### Cadena de ataque / Attack Chain

```text
nmap (3 puertos) -> nginx 1.16.1 (80) + Apache (65524) -> GoBuster /n0th1ng3ls3m4tt3r -> flag 1 -> flag 2 (Apache) -> Steghide (imagen) -> contraseña + binario -> SSH -> flag 3 (documento sistema) -> crontab -> flag 4 -> flag final
```

**Learning chain:** port scanning → web enumeration (GoBuster) → hidden directory → flags discovery → Steghide (steganography) → SSH access → flag hunting → crontab abuse → final flag.

**Lección:** *La enumeración web exhaustiva (directorios ocultos, puertos alternativos y archivos embebidos con esteganografía) da acceso a flags y credenciales; una tarea crontab que se ejecuta con privilegios suele ser la llave a la escalada y al control total del sistema.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1190 (Exploit Public-Facing Application), T1552 (Unsecured Credentials), T1053 (Scheduled Task/Job), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Easy Peasy](https://tryhackme.com/room/easypeasy)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.