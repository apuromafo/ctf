# Intro to Docker

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `introtodocker` | https://tryhackme.com/room/introtodocker | 01 Level Easy | TryHackMe | docker pull / docker image ls / docker run -it/-d/-p / docker ps / docker ps -a / Dockerfile (FROM, RUN, EXPOSE) / docker build -t / docker-compose (up/down) / docker socket / IPC / webserver container | Dominar la sintaxis básica de Docker, crear y ejecutar contenedores, escribir Dockerfiles, usar docker-compose y comprender el socket Docker, hasta desplegar un webserver y obtener la flag. |

---

**Contexto:** La room introduce Docker paso a paso: sintaxis básica (pull, image ls, run con flags -it/-d/-p, ps y ps -a), la creación de contenedores desde imágenes, los Dockerfiles (instrucciones FROM, RUN, EXPOSE), docker-compose (archivos YAML para orquestación), el socket Docker (IPC, API) y un laboratorio final donde se identifica un contenedor ya en ejecución (CloudIsland) y se arranca un webserver con el puerto 80 mapeado para obtener la flag.

> **ES:** Docker desde cero: pull, image ls, run, ps; creación de imágenes con Dockerfile (FROM/RUN/EXPOSE); docker-compose (up/down); socket Docker (IPC/API); prácticas de identificar y arrancar un webserver en contenedor.
> **EN:** Docker from scratch: pull, image ls, run, ps; creating images with Dockerfile (FROM/RUN/EXPOSE); docker-compose (up/down); Docker socket (IPC/API); practices identifying and launching a webserver container.

## Solucionario

### Task 1: Introduction / Introducción

**Explicación:** Introducción a la room de Docker: se presentan los objetivos y los conceptos que se van a cubrir. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Deploy the machine and read the introduction. / Despliega la máquina y lee la introducción. | `No answer needed` |

### Task 2: Basic Docker Syntax / Sintaxis básica de Docker

**Explicación:** Los comandos fundamentales de Docker: `docker pull` descarga una imagen de Docker Hub; `docker image ls` lista las imágenes disponibles en el equipo; con pull se puede especificar un tag para elegir versión (`:1337`). Sin tag, Docker descarga la versión **latest** por defecto.

```bash
docker pull tryhackme
docker pull tryhackme:1337
docker image ls
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | If we wanted to pull a docker image, what would our command look like? / ¿Cómo sería el comando para descargar una imagen docker? | `docker pull` |
| 2 | If we wanted to list all images on a device running Docker, what would our command look like? / ¿Cómo sería el comando para listar todas las imágenes de un equipo con Docker? | `docker image ls` |
| 3 | Let's say we wanted to pull the image "tryhackme" (no quotations); what would our command look like? / ¿Cómo sería el comando para descargar la imagen "tryhackme"? | `docker pull tryhackme` |
| 4 | Let's say we wanted to pull the image "tryhackme" with the tag "1337" (no quotations). What would our command look like? / ¿Cómo sería el comando para descargar "tryhackme" con el tag "1337"? | `docker pull tryhackme:1337` |

### Task 3: Running Your First Container / Ejecutando tu primer contenedor

**Explicación:** Para ejecutar un contenedor se usa `docker run` con distintos flags: `-it` ejecuta en modo interactivo (interactúa con el shell del contenedor), `-d` lo lanza en modo detached (segundo plano), y `-p 80:80` mapea el puerto del host al contenedor. Para ver qué contenedores están corriendo: `docker ps`, y para ver todos (incluyendo los detenidos): `docker ps -a`.

```bash
docker run -it <image> /bin/bash   # interactivo
docker run -d <image>               # detached
docker run -p 80:80 <image>         # mapeo de puertos
docker ps                           # contenedores en ejecución
docker ps -a                        # todos los contenedores
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What would our command look like if we wanted to run a container interactively? / ¿Cómo sería el comando para ejecutar un contenedor en modo interactivo? (Asumir que no se especifica imagen) | `docker run -it` |
| 2 | What would our command look like if we wanted to run a container in "detached" mode? / ¿Cómo sería el comando para ejecutar un contenedor en modo "detached"? | `docker run -d` |
| 3 | Let's say we want to run a container that will run and bind a webserver on port 80. What would our command look like? / ¿Cómo sería el comando para ejecutar un contenedor que sirva un webserver en el puerto 80? | `docker run -p 80:80` |
| 4 | What command would we use to see running containers? / ¿Qué comando usamos para ver los contenedores en ejecución? | `docker ps` |
| 5 | What command would we use to see all containers (running and stopped)? / ¿Qué comando usamos para ver todos los contenedores (ejecutándose y detenidos)? | `docker ps -a` |

### Task 4: Intro to Dockerfiles / Introducción a Dockerfiles

**Explicación:** Un Dockerfile es un script de instrucciones para construir una imagen Docker. La instrucción **FROM** define la imagen base (por ejemplo, `ubuntu:22.04`); la instrucción **RUN** ejecuta comandos durante la construcción (instalación de paquetes); **EXPOSE** documenta el puerto expuesto. Se construye la imagen con `docker build` y se nombra con el flag **-t** (tag).

```dockerfile
FROM ubuntu:22.04
RUN apt-get update -y
RUN apt-get install apache2 -y
EXPOSE 80
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What instruction would we use to specify what base image the container should be using (e.g. ubuntu:22.04)? / ¿Qué instrucción usaríamos para especificar la imagen base del contenedor (por ejemplo, ubuntu:22.04)? | `FROM` |
| 2 | What instruction would we use to tell the container to run a command? / ¿Qué instrucción usaríamos para decirle al contenedor que ejecute un comando? | `RUN` |
| 3 | What docker command would we use to build an image using a Dockerfile? / ¿Qué comando de docker usaríamos para construir una imagen a partir de un Dockerfile? | `build` |
| 4 | If we wanted to tag an image when building it, what flag would we use? / Si quisiéramos etiquetar una imagen al construirla, ¿qué flag usaríamos? | `-t` |

### Task 5: Intro to Docker Compose / Introducción a Docker Compose

**Explicación:** Docker Compose permite definir y ejecutar múltiples contenedores con un solo archivo YAML (`docker-compose.yml`). Para arrancar todos los servicios definidos: `docker-compose up`; para detenerlos y eliminarlos: `docker-compose down`. El archivo por defecto se llama **docker-compose.yml** y usa la sintaxis de Dockerfile combinada con define servicios, redes y volúmenes.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What command would we use to bring up a docker compose environment? / ¿Qué comando usaríamos para arrancar un entorno docker-compose? | `up` |
| 2 | What command would we use to tear down the environment? / ¿Qué comando usaríamos para detener el entorno? | `down` |
| 3 | What is the name of the file docker-compose uses by default? / ¿Cómo se llama el archivo que usa docker-compose por defecto? | `docker-compose.yml` |

### Task 6: Intro to the Docker Socket / Introducción al socket de Docker

**Explicación:** El socket Docker (`/var/run/docker.sock`) es la interfaz de comunicación entre el motor Docker y el host. IPC significa **Interprocess Communication** (comunicación entre procesos) y el socket Docker funciona como una **API**: el motor Docker actúa como servidor que expone una interfaz REST a la que se le envían comandos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What does the term "IPC" stand for? / ¿Qué significa el término "IPC"? | `Interprocess Communication` |
| 2 | What technology can the Docker Server be equalled to? / ¿A qué tecnología se puede equiparar el servidor Docker? | `API` |

### Task 7: Practical / Práctica

**Explicación:** Laboratorio final: se conecta a la VM en ejecución y se inspeccionan los contenedores con `docker ps`. Ya hay un contenedor en ejecución llamado **CloudIsland**. Con la imagen **webserver** se arranca un nuevo contenedor mapeando el puerto 80 y se accede al sitio para obtener la flag.

```bash
docker ps
docker run -d --name webserver -p 80:80 webserver
curl http://YOURIP.p.thmlabs.com/
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Connect to the machine. What is the name of the container that is currently running? / Conéctate a la máquina. ¿Cuál es el nombre del contenedor que está en ejecución? | `CloudIsland` |
| 2 | Use Docker to start a web server with the "webserver" image (no quotations). You will need to run the container with port 80. After starting the container, try to connect to https://YOURIP.p.thmlabs.com/ in your browser. What is the flag? / Inicia un webserver con la imagen "webserver" usando el puerto 80. Después accede a tu sitio. ¿Cuál es la flag? | `THM{WEBSERVER_CONTAINER}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | If we wanted to pull a docker image, what would our command look like? | `docker pull` |
| 2 | If we wanted to list all images on a device running Docker, what would our command look like? | `docker image ls` |
| 3 | Let's say we wanted to pull the image "tryhackme" (no quotations); what would our command look like? | `docker pull tryhackme` |
| 4 | Let's say we wanted to pull the image "tryhackme" with the tag "1337" (no quotations). What would our command look like? | `docker pull tryhackme:1337` |
| 5 | What would our command look like if we wanted to run a container interactively? | `docker run -it` |
| 6 | What would our command look like if we wanted to run a container in "detached" mode? | `docker run -d` |
| 7 | Let's say we want to run a container that will run and bind a webserver on port 80. What would our command look like? | `docker run -p 80:80` |
| 8 | What command would we use to see running containers? | `docker ps` |
| 9 | What command would we use to see all containers (running and stopped)? | `docker ps -a` |
| 10 | What instruction would we use to specify what base image the container should be using? | `FROM` |
| 11 | What instruction would we use to tell the container to run a command? | `RUN` |
| 12 | What docker command would we use to build an image using a Dockerfile? | `build` |
| 13 | If we wanted to tag an image when building it, what flag would we use? | `-t` |
| 14 | What command would we use to bring up a docker compose environment? | `up` |
| 15 | What command would we use to tear down the environment? | `down` |
| 16 | What is the name of the file docker-compose uses by default? | `docker-compose.yml` |
| 17 | What does the term "IPC" stand for? | `Interprocess Communication` |
| 18 | What technology can the Docker Server be equalled to? | `API` |
| 19 | Connect to the machine. What is the name of the container that is currently running? | `CloudIsland` |
| 20 | Use Docker to start a web server with the "webserver" image. What is the flag? | `THM{WEBSERVER_CONTAINER}` |

---

**Metodología:** De la sintaxis a la orquestación completa: (1) pull y listado de imágenes; (2) ejecución con flags `-it`, `-d`, `-p` y visibilidad con `docker ps`; (3) construcción de imágenes con Dockerfile (FROM, RUN, EXPOSE, build -t); (4) orquestación con docker-compose (up, down, YAML); (5) comprensión del socket Docker (IPC, API); (6) laboratorio práctico: identificar contenedores existentes y desplegar un webserver.

### Cadena de ataque / Attack Chain

```text
docker pull -> docker image ls -> docker run (-it/-d/-p) -> docker ps -> Dockerfile (FROM/RUN/EXPOSE) -> docker build -t -> docker-compose (up/down) -> Docker socket (IPC/API) -> CloudIsland + webserver -> flag
```

**Learning chain:** Pull/ls -> run flags -> ps -> Dockerfiles -> docker-compose -> socket IPC/API -> práctica webserver.

**Lección:** *Docker no es magia: es una API que expone el kernel del host a contenedores; el socket, los Dockerfiles y docker-compose son las piezas que convierten "funciona en mi máquina" en "funciona en cualquier sitio".*

**MITRE ATT&CK:** T1610 (Deploy Container), T1609 (Container Administration Command), T1525 (Implant Container Image)

**Fuente:** [TryHackMe - Intro to Docker](https://tryhackme.com/room/introtodocker)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.