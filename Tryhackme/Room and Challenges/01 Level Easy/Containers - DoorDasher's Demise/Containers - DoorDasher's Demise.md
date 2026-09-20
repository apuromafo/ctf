# Containers - DoorDasher's Demise

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Medium | walkthrough | `container-security-aoc2025-z0x3v6n9m2` | [TryHackMe](https://tryhackme.com/r/room/container-security-aoc2025-z0x3v6n9m2) | Advent of Cyber 2025 | TryHackMe | Docker, container escape, images, Dockerfile | Escapar de un contenedor comprometido hacia el host |

---

**Contexto:** Docker permite empaquetar aplicaciones en containers aislados, pero una mala configuración puede permitir la escalada de privilegios y escape al host. En esta práctica se explora la enumeración de contenedores, construcción de imágenes personalizadas y obtención de acceso al sistema subyacente mediante técnicas de container escape.

> **ES:** Enumera los contenedores Docker activos, construye una imagen personalizada para escapar del contenedor, consigue acceso al host y extrae la bandera y las credenciales del usuario `deployer`.
> **EN:** Enumerate the running Docker containers, craft a custom image to escape the container, gain host access and extract the flag and the `deployer` user's credentials.

## Solucionario

### Task 1: Enumeración de Docker / Docker Enumeration

**Explicación:** Se enumeran los contenedores activos. El comando que lista los contenedores en ejecución es `docker ps`, y el fichero que define las instrucciones para construir una imagen Docker es el `Dockerfile`. Con esta información base se prepara el terreno para el escape.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando exacto lista los contenedores Docker en ejecución? / What exact command lists running Docker containers? | `docker ps` |
| 2 | ¿Qué fichero se usa para definir las instrucciones de construcción de una imagen Docker? / What file is used to define the instructions for building a Docker image? | `Dockerfile` |

### Task 2: Escape de contenedor / Container Escape

**Explicación:** Aprovechando la configuración del entorno (por ejemplo, montajes del host o privilegios), se construye una imagen personalizada con un `Dockerfile` que permite escribir fuera del contenedor y escalar al host. Una vez fuera, se extrae la bandera `THM{DOCKER_ESCAPE_SUCCESS}` y, como bonus, la contraseña secreta del usuario `deployer` (`DeployMaster2025!`), contenida en la web de noticias del puerto 5002.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 3 | ¿Cuál es la bandera? / What's the flag? | `THM{DOCKER_ESCAPE_SUCCESS}` |
| 4 | Bonus: ¿Cuál es el código secreto de la web de noticias del puerto 5002 (la contraseña del usuario deployer)? / Bonus: What is the secret code contained within the news site running on port 5002 (the deployer user's password)? | `DeployMaster2025!` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando exacto lista los contenedores Docker en ejecución? / What exact command lists running Docker containers? | `docker ps` |
| 2 | ¿Qué fichero se usa para definir las instrucciones de construcción de una imagen Docker? / What file is used to define the instructions for building a Docker image? | `Dockerfile` |
| 3 | ¿Cuál es la bandera? / What's the flag? | `THM{DOCKER_ESCAPE_SUCCESS}` |
| 4 | Bonus: ¿Cuál es el código secreto de la web de noticias del puerto 5002? / Bonus: What is the secret code contained within the news site running on port 5002? | `DeployMaster2025!` |

---

**Metodología:** Se inició con enumeración de contenedores activos usando `docker ps`. Se identificaron imágenes y se construyó una imagen personalizada mediante `Dockerfile` para lograr el escape del contenedor. Posteriormente se accedió al host y se extrajo la bandera y las credenciales del usuario deployer.
**Learning chain:** Docker enumeration → image analysis → Dockerfile crafting → container escape → host access → credential extraction

### Cadena de ataque / Attack Chain

```text
docker ps (enumeración) -> análisis de imágenes -> Dockerfile malicioso -> container escape -> acceso al host -> flag + credenciales deployer
```

**Learning chain:** Docker enumeration → image analysis → Dockerfile crafting → container escape → host access → credential extraction

**Lección:** *Un contenedor que permite la construcción de imágenes propias con acceso a recursos del host (montajes/privilegios) es una puerta abierta al host: la enumeración correcta de contenedores e imágenes es el primer paso, y el hardening preventivo la única defensa real.*

**MITRE ATT&CK:** T1611 - Escape to Host

**Fuente:** [TryHackMe - Containers - DoorDasher's Demise](https://tryhackme.com/r/room/container-security-aoc2025-z0x3v6n9m2)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.