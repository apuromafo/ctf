# Containers - DoorDasher's Demise

| **Dificultad** | Medium |
| **Tipo** | walkthrough |
| **Slug** | `container-security-aoc2025-z0x3v6n9m2` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/container-security-aoc2025-z0x3v6n9m2) |
| **Sección** | Advent of Cyber 2025 |
| **Componentes** | Docker, container escape, images, Dockerfile |
| **Impacto** | Escapar de un contenedor comprometido hacia el host |

---

**Contexto:** Docker permite empaquetar aplicaciones en containers aislados, pero una mala configuración puede permitir la escalada de privilegios y escape al host. En esta práctica se explora la enumeración de contenedores, construcción de imágenes personalizadas y obtención de acceso al sistema subyacente mediante técnicas de container escape.

## Solucionario

### Task 1: Docker Enumeration

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What exact command lists running Docker containers? | `docker ps` |
| 2 | What file is used to define the instructions for building a Docker image? | `Dockerfile` |

### Task 2: Container Escape

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 3 | What's the flag? | `THM{DOCKER_ESCAPE_SUCCESS}` |
| 4 | Bonus: What is the secret code contained within the news site running on port 5002 (the deployer user's password)? | `DeployMaster2025!` |

---

**Metodología:** Se inició con enumeración de contenedores activos usando `docker ps`. Se identificaron imágenes y se construyó una imagen personalizada mediante `Dockerfile` para lograr el escape del contenedor. Posteriormente se accedió al host y se extrajo la bandera y las credenciales del usuario deployer.
**Learning chain:** Docker enumeration → image analysis → Dockerfile crafting → container escape → host access → credential extraction
**MITRE ATT&CK:** T1611 - Escape to Host
**Fuente:** [TryHackMe - Containers - DoorDasher's Demise](https://tryhackme.com/r/room/container-security-aoc2025-z0x3v6n9m2)