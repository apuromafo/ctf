# Containers - DoorDasher's Demise

| **Dificultad** | Easy | **Tipo** | walkthrough | **Slug** | `day14containersdoordashersdemise` |
| **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber25) |
| **Sección** | Advent of Cyber Tryhackme |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Docker / containers / virtual machines / hypervisor / container escape / Dockerfile / docker ps |
| **Impacto** | Escapar de un contenedor Docker comprometido hacia el host |

---

**Contexto:** Día 14 del Advent of Cyber 2025. Se comparan las máquinas virtuales (hipervisor que emula varios SO en un host físico) con los contenedores (comparten el kernel del SO anfitrión y aíslan solo la aplicación y sus dependencias). Se presenta Docker como herramienta para construir, desplegar y mantener contenedores, y el concepto de **container escape**: técnica que permite al código de dentro de un contenedor obtener derechos o ejecutarse en el kernel del host más allá del entorno aislado.

## Solucionario

### Día 14: Containers - DoorDasher's Demise

**Explicación:**

- A **virtual machine** runs on a hypervisor (software that emulates and manages multiple operating systems on one physical host)
- **Containers** share the host OS kernel, isolating only applications and their dependencies, which makes them lightweight and fast to start

- Docker: build, deploy, and maintain containers; isolate application and use the host OS kernel
- A **container escape** is a technique that enables code running inside a container to obtain rights or execute on the host kernel (or other containers) beyond its isolated environment (escaping).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What exact command lists running Docker containers? | `docker ps` |
| 2 | What file is used to define the instructions for building a Docker image? | `Dockerfile` |
| 3 | What's the flag? | `THM{DOCKER_ESCAPE_SUCCESS}` |
| 4 | Bonus Question: There is a secret code contained within the news site running on port 5002; this code also happens to be the password for the deployer user! They should definitely change their password. Can you find it? | `DeployMaster2025!` |

---

**Metodología:** Se enumeraron los contenedores activos con `docker ps` y se revisó la imagen Docker para inspeccionar su configuración. Se construyó una imagen personalizada mediante `Dockerfile` para lograr el container escape, obteniendo el flag. Además, se accedió al sitio de noticias del puerto 5002 para extraer el código secreto que resultó ser la contraseña del usuario deployer.
**Learning chain:** docker ps (enumeration) -> Dockerfile (construcción de imagen) -> container escape -> acceso al host -> flag THM{DOCKER_ESCAPE_SUCCESS} -> secret code en :5002 -> password deployer

Cadena de ataque / Attack Chain:
```
docker ps -> inspección de imágenes -> Dockerfile malicioso (mount/privileged) -> container escape -> root en host -> flag THM{DOCKER_ESCAPE_SUCCESS} -> news site :5002 -> secret code = DeployMaster2025! (password deployer)
```

**Lección:** *Los contenedores comparten el kernel del host: un escape de contenedor equivale a comprometer el host entero; por eso se deben auditar los flags de Docker (privileged, mounts) y nunca reutilizar contraseñas como la del usuario deployer.*

**MITRE ATT&CK:** T1611 - Escape to Host

**Fuente:** [TryHackMe - Containers - DoorDasher's Demise](https://tryhackme.com/room/adventofcyber25)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.