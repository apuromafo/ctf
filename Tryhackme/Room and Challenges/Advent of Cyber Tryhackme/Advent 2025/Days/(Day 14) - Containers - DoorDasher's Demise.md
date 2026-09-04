# Advent 2025\Days [N/A]

- A **virtual machine** runs on a hypervisor (software that emulates and manages multiple operating systems on one physical host)
- **Containers** share the host OS kernel, isolating only applications and their dependencies, which makes them lightweight and fast to start

- Docker: build, deploy, and maintain containers; isolate application and use the host OS kernel
- A **container escape** is a technique that enables code running inside a container to obtain rights or execute on the host kernel (or other containers) beyond its isolated environment (escaping).

## Respuestas / Answers
- What exact command lists running Docker containers? : `docker ps`
- What file is used to define the instructions for building a Docker image? : `Dockerfile`
- What's the flag? : `THM{DOCKER_ESCAPE_SUCCESS}`
- Bonus Question: There is a secret code contained within the news site running on port 5002; this code also happens to be the password for the deployer user! They should definitely change their password. Can you find it? : `DeployMaster2025!`

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
