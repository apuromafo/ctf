# PalsForLife

| **Dificultad** | MEDIUM | **Tipo** | CTF (Free) | **Slug** | `palsforlife` |
| **Link** | [TryHackMe](https://tryhackme.com/room/palsforlife) | **Sección** | Linux / Kubernetes / CTF | **Fuente** | TryHackMe |
| **Componentes** | Gitea, Webhook secrets, Kubernetes, kubectl, Service Account Tokens, Pod breakout, Container escape, PDF cracking (john) | **Impacto** | Compromiso total de un clúster Kubernetes mal configurado: ejecución remota de código vía Gitea, acceso a secrets del clúster y escape del pod como root en el nodo host |

---

**Contexto:** Esta sala es un CTF que abusa de un clúster Kubernetes mal configurado. La cadena comienza en una aplicación web con un PDF protegido por contraseña que revela credenciales de Gitea; tras autenticarse como `leeroy`, se explota un webhook (flag 1) con su secret y un hook de Gitea (CVE-2020-14144) para ejecutar comandos como el usuario `git` (flag 2). Dentro del pod se obtiene el service account token de Kubernetes para consultar secrets en `kube-system` (flag 3) y finalmente se crea un pod privilegiado que monta el filesystem del host para escapar del contenedor y leer el root flag.

> **ES:** Explotación de un clúster Kubernetes mal configurado desde la web: credenciales en un PDF, abuso de Gitea y sus webhooks, ejecución de comandos en el pod, lectura de secrets de Kubernetes y escape de contenedor para obtener las cuatro flags.
> **EN:** Exploitation of a misconfigured Kubernetes cluster from the web: credentials in a PDF, abuse of Gitea and its webhooks, command execution in the pod, reading Kubernetes secrets and container escape to obtain the four flags.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Se presenta el escenario: un clúster Kubernetes mal configurado expuesto a través de una aplicación Gitea. El participante debe obtener acceso autenticado y progresar dentro del clúster.

1. No answer needed

### Task 2: Captura de Flags 1-4 / Flags 1-4 Capture

**Explicación:** La Flag 1 se encuentra como el secret del webhook del repositorio de Gitea (visible inspeccionando la página de webhooks o con Developer Tools). La Flag 2 se localiza en `/root/flag2.txt`, accesible por el usuario `git` tras la ejecución de comandos en el pod (por ejemplo mediante el exploit de git hooks de Gitea). La Flag 3 se obtiene consultando el secret `flag3` del namespace `kube-system` con kubectl usando el token del service account del pod. La Flag 4 es el root flag final en `/root/root.txt`, leído tras escapar del contenedor creando un pod privilegiado que monta el filesystem del host.

1. 1. flag{Stick_to_the_plan!}
   2. flag{_G0ddamit_Leeroy_}
   3. flag{Its_n0t_my_fault!}
   4. flag{At_least_I_have_chicKen}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2.1 | Flag 1 (Webhook secret de Gitea) | `flag{Stick_to_the_plan!}` |
| 2.2 | Flag 2 (/root/flag2.txt como usuario git) | `flag{_G0ddamit_Leeroy_}` |
| 2.3 | Flag 3 (secret flag3 en kube-system) | `flag{Its_n0t_my_fault!}` |
| 2.4 | Flag 4 (/root/root.txt tras el escape del pod) | `flag{At_least_I_have_chicKen}` |

---

**Metodología:** Tras la extracción de un PDF protegido (exportado de base64 en `/team/`) y el cracking de su contraseña con john contra rockyou, se obtienen las credenciales de `leeroy` para Gitea en el puerto 31111. Se inspecciona el webhook del repositorio `jenkins` para leer el secret (flag 1). Se explota la ejecución remota de código autenticada de Gitea (CVE-2020-14144) o los git hooks para ganar una shell como `git` y leer `/root/flag2.txt` (flag 2). Dentro del pod se lee el token del service account en `/var/run/secrets/kubernetes.io/serviceaccount` y, con kubectl contra la API en el puerto 6443, se consulta el secret `flag3` en `kube-system` (flag 3). Finalmente se despliega un pod privilegiado (hostPath de `/`, privileged, nsenter a `/proc/1/ns/mnt`) que monta el filesystem del nodo para leer `/root/root.txt` (flag 4).

**Learning chain:** Reconocimiento web (puerto 30180 con PDF en base64) → Cracking del PDF (john/rockyou) → Login en Gitea como leeroy (31111) → Webhook secret (flag 1) → RCE vía git hooks de Gitea / MSF `gitea_git_hooks_rce` → Shell como git → /root/flag2.txt (flag 2) → Service account token del pod → kubectl → secret flag3 en kube-system (flag 3) → Pod privilegiado con montaje del host → Escape del contenedor → /root/root.txt (flag 4).

**Lección:** *Un clúster Kubernetes mal configurado entrega el control del host por completo: el exceso de permisos del service account, la ausencia de restricciones RBAC y la posibilidad de desplegar pods privilegiados son vector de abuso crítico. Además, Gitea con hooks ejecutables convierte la autenticación web en ejecución remota de código.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1213 (Data from Information Repositories), T1059 (Command and Scripting Interpreter), T1610 (Deploy Container), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - PalsForLife](https://tryhackme.com/room/palsforlife)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.