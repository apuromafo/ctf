# Frank & Herby make an app
| **Dificultad** | Medium |
| **Tipo** | CTF (Boot2Root Linux) |
| **Slug** | `frankherbymakeanapp` |
| **Link** | [TryHackMe](https://tryhackme.com/room/frankherbymakeanapp) |
| **Sección** | 02 Level Medium |
| **Fuente** | Web (TryHackMe room `frankherbymakeanapp` + walkthroughs públicos: BJConway, psechoPATH, MeetCyber) |
| **Componentes** | Linux, nginx, Meteor/Node, SSH, `.git-credentials`, MicroK8s/Kubernetes, kubectl, Docker, escape de contenedor, escalada de privilegios |
| **Impacto** | Un artefacto de desarrollo expuesto (`.git-credentials`) filtra credenciales válidas que dan acceso SSH; a partir de ahí una mala configuración de **MicroK8s** (usuario con acceso al cluster) permite escapar del contenedor y comprometer el host como root. |
---
**Contexto:** "Frank & Herby make an app" arranca con un descuido operativo: en un servidor web **nginx** (puerto 31337) que sirve la aplicación de Frank queda expuesto el archivo de credenciales de Git **`.git-credentials`**. Esas credenciales son reutilizadas para autenticarse por **SSH** como el usuario `frank`, lo que entrega el primer flag. La segunda fase abusa de una instalación de **MicroK8s** mal configurada: el usuario tiene acceso al cluster de Kubernetes, y desplegando un pod privilegiado con montaje del sistema de archivos del host se logra el **escape de contenedor** y `root`.
*EN: "Frank & Herby make an app" starts with an operational oversight: on an **nginx** web server (port 31337) serving Frank's app, the Git credentials file **`.git-credentials`** is exposed. Those credentials are reused to authenticate over **SSH** as user `frank`, yielding the first flag. The second phase abuses a misconfigured **MicroK8s** install: the user has cluster access, and by deploying a privileged pod that mounts the host filesystem a **container escape** to `root` is achieved.*
## Solucionario
### Task 1: Frank & Herby make an app
**Explicación:** Fases del reto:
1. **Reconocimiento (nmap).** Se descubren servicios: `22/tcp` (OpenSSH 8.2p1), `3000/tcp` (aplicación web Meteor) y `31337/tcp` (**nginx 1.21.3** sirviendo una plantilla Bootstrap).
2. **Artefacto expuesto.** Se enumera contenido del sitio en 31337 y se encuentra el archivo de credenciales de Git:
```bash
curl http://<IP>:31337/.git-credentials
```
que revela credenciales del usuario `frank` (usuario:contraseña en formato de URL).
3. **Foothold (SSH).** Las credenciales se reutilizan para el acceso SSH:
```bash
ssh frank@<IP>
cat /home/frank/user.txt
```
4. **Escalada (MicroK8s).** Como `frank` tiene acceso al cluster de **MicroK8s**, se comprueba con `microk8s kubectl get pods` / `kubectl get nodes`. Se aprovecha una configuración insegura desplegando un pod/explotación que monta el sistema de archivos del host (`hostPath` / contenedor privilegiado) para leer `root.txt` o directamente obtener una shell de root:
```bash
microk8s kubectl get nodes
# desplegar pod privilegiado con hostPath=/ y leer /root/root.txt
```
*EN: The challenge phases: nmap recon (22 SSH, 3000 Meteor app, 31337 nginx); exposed `.git-credentials` retrieved via curl; credential reuse for SSH as `frank` (user flag); MicroK8s misconfiguration exploited by deploying a privileged host-mounting pod to escape the container and read `root.txt`.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What port has a webpage frank was able to stand up? | `31337` |
| 2 | What did frank leave exposed on the site? | `.git-credentials` |
| 3 | What is the user.txt flag? | `THM{F@nkth3T@nk}` |
| 4 | What is the root.txt flag? | `THM{M1cr0K8s_13_FUN}` |
---
**Metodología:** Enumeración de puertos (nmap) → descubrimiento de contenido web → lectura de `.git-credentials` → reutilización de credenciales por SSH → user flag → enumeración del cluster MicroK8s → despliegue de pod privilegiado con montaje del host → escape de contenedor → root flag.
**Learning chain:** fuga de artefactos de desarrollo → reutilización de credenciales → acceso al orquestador → abuso de RBAC/MicroK8s para escapar del contenedor.
**Lección:** *Nunca exponer artefactos de desarrollo (`.git-credentials`, repos, backups); la reutilización de credenciales amplifica el daño y un cluster de Kubernetes con permisos de más es equivalente a root sobre el host.*
**MITRE ATT&CK:** T1046 (Network Service Discovery), T1083 (File and Directory Discovery), T1552.001 (Credentials In Files), T1078 (Valid Accounts), T1021.004 (Remote Services: SSH), T1611 (Escape to Host), T1610 (Deploy Container).
**Fuente:** [TryHackMe - Frank & Herby make an app](https://tryhackme.com/room/frankherbymakeanapp)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
