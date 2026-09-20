# Container Hardening

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough (hardening de contenedores) | `containerhardening` | https://tryhackme.com/room/containerhardening | 01 Level Easy | TryHackMe | Docker / cgroups / capabilities / Seccomp / AppArmor / escaneo de imágenes / Docker Scout / NIST SP 800-190 / Docker Bench | Endurecer contenedores Docker frente a amenazas: daemon, cgroups, capacidades, AppArmor/Seccomp y benchmarking. |

---

**Contexto:** Room de hardening de contenedores Docker. Repasa las principales amenazas para contenedores y las contramedidas: proteger el socket del daemon, limitar recursos con cgroups, restar privilegios con capabilities, filtrar syscalls con Seccomp, etiquetar perfiles con AppArmor, revisar las imágenes y aplicar benchmarks y herramientas de escaneo (Docker Bench, Docker Scout, NIST SP 800-190). Termina con una práctica de escaneo de imágenes vulnerables con Docker Scout.

> **ES:** Aprende las amenazas a los contenedores y cómo endurecer Docker: daemon seguro, cgroups, capabilities, AppArmor, Seccomp, imágenes y benchmarking.
> **EN:** Learn about container threats and how to harden Docker: secure daemon, cgroups, capabilities, AppArmor, Seccomp, images and benchmarking.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Se presentan las amenazas típicas de los contenedores (daemon expuesto, contenedores muy privilegiados, imágenes hostiles, fugas de red y errores de configuración) y el objetivo de la room: aplicar buenas prácticas de hardening. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la introducción de la room. / Read the room's introduction. | `No answer needed` |

### Task 2: Protegiendo el daemon de Docker / Protecting the Docker Daemon

**Explicación:** El daemon de Docker corre como root y controla todos los contenedores; exponer su socket equivale a dar acceso root. La configuración segura crea un contexto personalizado que usa un socket remoto seguro, y las operaciones se ejecutan con ese contexto de Docker (sin variar la variable de entorno por defecto).

```bash
docker context create --docker host=ssh://user@REMOTE_HOST myremotecontext
docker context use myremotecontext
docker context ls
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando crea un contexto de Docker para conectarse a un servicio Docker remoto vía SSH? / What command creates a Docker context to connect to a remote Docker service over SSH? | `docker context create` |
| 2 | ¿Qué comando activa el contexto que acabamos de crear (lo usa como contexto activo)? / What command makes the context we just created the active context? | `docker context use` |

### Task 3: Implementando grupos de control (cgroups) / Implementing Control Groups

**Explicación:** Los cgroups limitan los recursos (CPU, memoria, I/O) que usa un contenedor, evitando ataques de agotamiento de recursos (DoS sobre el host). En el ejemplo se limita el contenedor apache a un núcleo (`--cpus=1`) y se comprueba con `docker inspect apache`.

```bash
docker run -d --name apache --cpus=1 httpd:latest
docker inspect apache --format '{{.HostConfig.NanoCpus}}'
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué flag se usa junto a `docker run` para limitar el número de CPUs de un contenedor? / What flag is used with `docker run` to limit the container's number of CPUs? | `--cpus` |
| 2 | ¿Qué comando se usa para confirmar los recursos limitados del contenedor apache? / What command is used to confirm the container's restricted resources? | `docker inspect apache` |

### Task 4: Previniendo contenedores "over-privileged" (sudo dentro de contenedores) / Preventing Over-Privileged Containers

**Explicación:** Por defecto Docker añade capabilities de Linux a los contenedores, muchas innecesarias. La amenaza es un contenedor con capabilities excesivas; la mitigación es ejecutarlo eliminando todas las capabilities (`--cap-drop ALL`) y añadiendo solo las necesarias (`--cap-add CAP_NET_BIND_SERVICE`), verificando la lista en el momento de ejecución con `capsh --print`.

```bash
docker run --cap-drop ALL --cap-add CAP_NET_BIND_SERVICE -d -p 80:80 httpd:latest
capsh --print   # dentro del contenedor, para ver las capabilities efectivas
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama la capability que permite a un proceso enlazar sockets por debajo del puerto 1024? / What is the name of the capability that allows a process to bind to sockets under port 1024? | `CAP_NET_BIND_SERVICE` |
| 2 | ¿Qué flag de `docker run` se usa para añadir capabilities adicionales a un contenedor? / What `docker run` flag is used to add additional capabilities to a container? | `--cap-add` |
| 3 | ¿Qué comando se usa para mostrar las capabilities efectivas del contenedor? / What command is used to show the container's effective capabilities? | `capsh --print` |

### Task 5: Seccomp y AppArmor 101 / Seccomp and AppArmor 101

**Explicación:** Se explican los dos mecanismos de seguridad del kernel para restringir syscalls y procesos: AppArmor (perfiles por aplicación etiquetada, como `aa-status` para listarlos) y Seccomp (filtro de syscalls). Un contenedor endurecido usa un perfil de AppArmor personalizado y un filtro seccomp limitado (en vez de `--privileged`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el mecanismo que aplica un perfil de seguridad sobre un programa etiquetado (usado por los contenedores Docker)? / Which mechanism enforces a security profile on a labeled program (used by Docker containers)? | `AppArmor` |
| 2 | ¿Cuál es el mecanismo que filtra las llamadas al sistema (syscalls) del contenedor? / Which mechanism filters the container's system calls? | `Seccomp` |
| 3 | ¿Qué comando se usa para listar los perfiles de AppArmor disponibles? / What command lists the available AppArmor profiles? | `aa-status` |

### Task 6: Revisando imágenes de Docker / Reviewing Docker Images

**Explicación:** Una imagen Docker es una plantilla inmutable; las imágenes hostiles o desactualizadas pueden contener malware o vulnerabilidades. Se recomienda obtenerlas solo de fuentes de confianza oficiales, verificarlas y mantenerlas al día. Esta tarea es de teoría y no tiene flag ni respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la teoría sobre la revisión y verificación de imágenes de Docker. / Read about reviewing and verifying Docker images. | `No answer needed` |

### Task 7: Cumplimiento y benchmarking / Compliance and Benchmarking

**Explicación:** Se presentan el marco de referencia de la NSA (NIST SP 800-190) sobre contenedores y la herramienta Docker Bench que audita la configuración contra esos benchmarks. Además, Docker Scout analiza las imágenes en busca de vulnerabilidades CVE. La detección temprana de vulnerabilidades se hace antes de ejecutar el contenedor (en la fase de build).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué marco de referencia de seguridad aporta directrices para contenedores? / What reference security framework provides guidelines for containerization? | `NIST SP 800-190` |
| 2 | ¿Qué herramienta de Docker identifica vulnerabilidades conocidas en tus imágenes? / What Docker tool identifies known vulnerabilities in your images? | `Docker Scout` |

### Task 8: Ejercicio práctico / Practical

**Explicación:** Se practica el escaneo de imágenes. Se configura el Dockerfile, se construye la imagen (apache desde `httpd:latest` con un índice de prueba) y se corre Docker Scout para obtener la lista de vulnerabilidades. La imagen de prueba `tryhackme/couchdb:0.1.0` muestra el paquete y la versión vulnerables tras ejecutar `docker scout cves`. Respuestas: el paquete vulnerable es `couchdb`, la versión es `struts2-core` (librería Apache Struts de la imagen de ejemplo) y la severidad de las vulnerabilidades es `Critical`.

```dockerfile
FROM httpd:latest
COPY ./index.html /usr/local/apache2/htdocs/
```
```bash
docker scout cves tryhackme/couchdb:0.1.0
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el paquete vulnerable? / What is the vulnerable package? | `couchdb` |
| 2 | ¿Cuál es la versión del paquete vulnerable? / What is the vulnerable package's version? | `struts2-core` |
| 3 | ¿Cuál es la severidad de las vulnerabilidades? / What is the severity of the vulnerabilities? | `Critical` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando crea un contexto de Docker para conectar con un daemon remoto vía SSH? | `docker context create` |
| 2 | ¿Qué comando activa el contexto recién creado como activo? | `docker context use` |
| 3 | ¿Qué flag de `docker run` limita el número de CPUs? | `--cpus` |
| 4 | ¿Qué comando confirma los recursos limitados del contenedor apache? | `docker inspect apache` |
| 5 | ¿Qué capability permite enlazar sockets bajo el puerto 1024? | `CAP_NET_BIND_SERVICE` |
| 6 | ¿Qué flag de `docker run` añade capabilities adicionales? | `--cap-add` |
| 7 | ¿Qué comando muestra las capabilities efectivas del contenedor? | `capsh --print` |
| 8 | ¿Qué mecanismo aplica un perfil de seguridad sobre un programa etiquetado? | `AppArmor` |
| 9 | ¿Qué mecanismo filtra las syscalls del contenedor? | `Seccomp` |
| 10 | ¿Qué comando lista los perfiles de AppArmor? | `aa-status` |
| 11 | ¿Qué marco de referencia aporta directrices para contenedores? | `NIST SP 800-190` |
| 12 | ¿Qué herramienta de Docker identifica vulnerabilidades conocidas en las imágenes? | `Docker Scout` |
| 13 | ¿Cuál es el paquete vulnerable? | `couchdb` |
| 14 | ¿Cuál es la versión del paquete vulnerable? | `struts2-core` |
| 15 | ¿Cuál es la severidad de las vulnerabilidades? | `Critical` |

---

**Metodología:** Se identifica cada amenaza de los contenedores y se aplica la contramedida correspondiente en capas: contexto/demonio seguro, cgroups para recursos, capabilities mínimas (`--cap-drop ALL` + `--cap-add`), AppArmor/Seccomp para syscalls, revisión de imágenes, y cumplimiento con NIST SP 800-190, Docker Bench y Docker Scout (escaneo de CVEs).

### Cadena de ataque / Attack Chain

```text
Daemon expuesto (contexto SSH) -> cgroups (--cpus, docker inspect) -> capabilities (--cap-drop/--cap-add, capsh) -> AppArmor/Seccomp (aa-status) -> imágenes (Docker Scout/NIST 800-190) -> práctica de escaneo
```

**Learning chain:** Amenazas de contenedores -> daemon/contextos -> cgroups -> capabilities -> AppArmor/Seccomp -> revisión de imágenes -> compliance/benchmarking -> escaneo con Docker Scout.

**Lección:** *Un contenedor endurecido se consigue por capas: mínimas capabilities, recursos limitados con cgroups, perfiles AppArmor y seccomp, imágenes verificadas y escaneo continuo; confiar en el aislamiento por defecto de Docker es lo que permite los escapes.*

**MITRE ATT&CK:** T1610 - Deploy Container

**Fuente:** [TryHackMe - Container Hardening](https://tryhackme.com/room/containerhardening)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.