# Inferno

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Boot2Root / Linux | inferno | https://tryhackme.com/room/inferno | 02 Level Medium | TryHackMe | Apache, CMS, Hydra, sudo/tee (GTFOBins) | Escalada a root |

---

**Contexto:** **Inferno** es una máquina Linux *boot2root* con dos claves (hash): `local.txt` (usuario) y `proof.txt` (root). La ruta de ataque comienza con un reconocimiento web que descubre un CMS en `/inferno/`; un brute force contra su panel de login obtiene credenciales válidas, y un registro **DNS TXT** de un subdominio revela una contraseña usada para acceder por SSH. Dentro de la máquina, un archivo en el directorio `Downloads` del usuario `dante` contiene las credenciales de este, permitiendo el movimiento lateral (`www-data` → `dante`). Finalmente, un permiso `sudo` sobre `tee` (abuso de **GTFOBins**) permite escribir en `/etc/passwd`, crear un usuario privilegiado y obtener `proof.txt`. La versión 1.1 incluye *trolls*: la shell ejecuta `exit` tras un minuto en PTY y `logout` tras 5 segundos en SSH.

## Solucionario

### Task 1: local.txt (flag de usuario)
**Explicación:**

1. **Reconocimiento:** `nmap` muestra ambos servicios HTTP y un CMS accesible en `http://<IP>/inferno/`.
2. **Fuerza bruta del login:** con `hydra`/ffuf contra el panel se obtiene la combinación válida `admin:dante1`.
3. **Pistas en el CMS:** dentro del panel se encuentra una pista de un subdominio; su registro **DNS TXT** contiene una contraseña (p. ej. consultando con `dig`/`host -t txt`).
4. **Acceso inicial:** SSH con las credenciales obtenidas entra como `www-data`.
5. **Movimiento lateral:** en `/home/dante/Downloads/download.dat` aparecen, al final del archivo, las credenciales de `dante`. Se accede por SSH como `dante`.
6. **Flag de usuario:** se lee `/home/dante/local.txt`.

Respuesta: `77f6f3c544ec0811e2d1243e2e0d1835`

### Task 2: proof.txt (flag de root)
**Explicación:**

1. **Enumeración de privilegios:** `sudo -l` revela que `dante` puede ejecutar `/usr/bin/tee` como root sin contraseña.
2. **Abuso de tee (GTFOBins):** se genera un hash de contraseña y se añade un usuario privilegiado a `/etc/passwd`:
   ```
   dante@Inferno:~$ openssl passwd -1 -salt "inferno" "dante"
   $1$inferno$vA66L6zp5Qks4kxIc3tvn/
   dante@Inferno:~$ printf 'inferno:$1$inferno$vA66L6zp5Qks4kxIc3tvn/:0:0:root:/root:/bin/bash\n' | sudo tee -a /etc/passwd
   ```
3. **Escalada:** `su - inferno` con la contraseña `dante` concede root; se lee `/root/proof.txt`.

Respuesta: `f332678ed0d0767d7434b8516a7c6144`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de usuario (local.txt) | `77f6f3c544ec0811e2d1243e2e0d1835` |
| 2 | Flag de root (proof.txt) | `f332678ed0d0767d7434b8516a7c6144` |

---

**Metodología:** Enumeración web (CMS en `/inferno/`), brute force de credenciales (`hydra`), reconocimiento DNS (registro TXT de un subdominio), acceso SSH como `www-data`, movimiento lateral mediante credenciales en `Downloads/download.dat`, y escalada de privilegios abusando de `sudo tee` (GTFOBins) para inyectar un usuario root en `/etc/passwd`.

**Learning chain:** Nmap → CMS en `/inferno/` → brute force → credenciales → DNS TXT → SSH (www-data) → lateral a dante → local.txt → `sudo -l` (tee) → /etc/passwd → su → proof.txt.

**Lección:** *Un binario aparentemente inocuo como `tee` con `sudo` NOPASSWD equivale a root: cualquier utilidad que escriba archivos arbitrarios permite manipular `/etc/passwd` o `/etc/sudoers`.*

**MITRE ATT&CK:** T1595 Active Scanning · T1110.001 Brute Force: Password Guessing · T1590.002 Gather Victim Network Information: DNS · T1078.003 Valid Accounts: Local Accounts · T1548.003 Abuse Elevation Control Mechanism: Sudo and Sudo Caching · T1552.001 Unsecured Credentials: Credentials In Files.

**Fuente:** [TryHackMe - Inferno](https://tryhackme.com/room/inferno)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.