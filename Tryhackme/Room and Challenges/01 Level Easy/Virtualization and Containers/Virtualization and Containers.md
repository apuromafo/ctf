# Virtualization and Containers

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `virtualizationandcontainers` | [TryHackMe](https://tryhackme.com/room/virtualizationandcontainers) | 01 Level Easy | THM | Virtualización, hipervisores, contenedores, Docker, Kubernetes, kubectl | Resolución completa de la sala teórico-práctica |

---

**Contexto:** Sala que explica la virtualización, los hipervisores (Type 1/Type 2), los contenedores y las plataformas Docker y Kubernetes. Incluye una parte práctica con Docker (flag en el puerto 5000) y un clúster Kubernetes donde se aplican comandos kubectl para enumerar pods, deployments, services, replica sets y borrar el deployment.

> **ES:** Sala teórico-práctica sobre virtualización, hipervisores, contenedores, Docker y Kubernetes: tipos de hipervisor, abstracción del host, flag de Docker en MACHINE_IP:5000 y enumeración kubectl del clúster.
> **EN:** Theory + practice room on virtualization, hypervisors, containers, Docker and Kubernetes: hypervisor types, host abstraction, Docker flag at MACHINE_IP:5000 and kubectl enumeration of the cluster.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de la sala. No requiere respuesta.

1. No answer needed

### Task 2: ¿Qué es la virtualización? / What is Virtualization

**Explicación:** Se introducen los conceptos de virtualización: la escalabilidad como beneficio principal (Y/N) y el sistema operativo de una máquina virtual (Guest OS).

1. `Y`
2. `guest OS`

### Task 3: Hipervisores / Hypervisors

**Explicación:** Se explican los tipos de hipervisor: VirtualBox como hipervisor Type 2 (hospedado) y los Type 1 (bare metal) sobre el hardware.

1. `type 2`
2. `bare metal hypervisors`

### Task 4: Contenedores / Containers

**Explicación:** Se introduce el concepto de contenedores y su relación con el sistema operativo host: los contenedores no están completamente abstraídos del host (N).

1. `N`

### Task 5: Docker / Docker

**Explicación:** Parte práctica de Docker: se ejecuta el contenedor y se obtiene la flag en MACHINE_IP:5000.

1. `THM{this_is_running_in_docker}`

### Task 6: Kubernetes / Kubernetes

**Explicación:** Parte práctica con kubectl sobre el clúster proporcionado: contar pods, system pods, identificar el pod y el deployment, el puerto expuesto por el servicio, los replica sets desplegados y el comando para eliminar el deployment.

1. No answer needed
2. `1`
3. `7`
4. `hello-tryhackme-66c4d4d69d-gb9nz`
5. `hello-tryhackme`
6. `443`
7. `1`
8. `hello-tryhackme-66c4d4d69d`
9. `kubectl delete deployment hello-tryhackme`

### Task 7: Conclusión / Conclusion

**Explicación:** Cierre de la sala. No requiere respuesta.

1. No answer needed

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|---|---|---|
| 1 | — | `No answer needed` |
| 2.1 | Is scalability a primary benefit of virtualization? (Y/N) | `Y` |
| 2.2 | What is the operating system of a virtual machine often referred to as? | `guest OS` |
| 3.1 | What type of hypervisor is VirtualBox considered? | `type 2` |
| 3.2 | What are type 1 hypervisors also known as? | `bare metal hypervisors` |
| 4 | Are containers completely abstracted from the host operating system? (Y/N) | `N` |
| 5 | What flag is obtained at MACHINE_IP:5000 after running the container? | `THM{this_is_running_in_docker}` |
| 6.1 | — | `No answer needed` |
| 6.2 | How many pods are running on the provided cluster? | `1` |
| 6.3 | How many system pods are running on the provided cluster? | `7` |
| 6.4 | What is the pod name on the provided cluster? | `hello-tryhackme-66c4d4d69d-gb9nz` |
| 6.5 | What is the deployment name on the provided cluster? | `hello-tryhackme` |
| 6.6 | What port is exposed by the service in question 5? | `443` |
| 6.7 | How many replica sets are deployed on the provided cluster? | `1` |
| 6.8 | What is the replica set name on the provided cluster? | `hello-tryhackme-66c4d4d69d` |
| 6.9 | What command would be used to delete the deployment from question 5? | `kubectl delete deployment hello-tryhackme` |
| 7 | — | `No answer needed` |

---

**Metodología:** 1) Repasar la teoría de virtualización (beneficio principal: escalabilidad; Guest OS). 2) Distinguir hypervisores Type 1 (bare metal) y Type 2 (VirtualBox). 3) Comprender que los contenedores no están completamente abstraídos del host. 4) Ejecutar el contenedor Docker y capturar la flag en MACHINE_IP:5000. 5) Enumerar el clúster Kubernetes con kubectl (pods, system pods, pod name, deployment, puerto del servicio, replica sets) y practicar el borrado del deployment.

### Cadena de ataque / Attack Chain

Virtualización (conceptos) → Hipervisores (Type 1/Type 2) → Contenedores → Docker (flag en :5000) → Kubernetes (kubectl get pods / -n kube-system / get deployments / get services / get rs) → kubectl delete deployment hello-tryhackme

**Learning chain:** Virtualization → Hypervisors (Type 1/Type 2) → Containers → Docker → Kubernetes → kubectl enumeration → deployment deletion

**Lección:** *La virtualización y los contenedores cambian el modelo de despliegue y también la superficie de ataque: conocer la arquitectura (hipervisores, contenedores, orquestadores como Kubernetes) es imprescindible para enumerar y explotar infraestructuras modernas con comandos como kubectl.*

**MITRE ATT&CK:** N/A (Room de fundamentos de virtualización y contenedores)

**Fuente:** [TryHackMe - Virtualization and Containers](https://tryhackme.com/room/virtualizationandcontainers)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.