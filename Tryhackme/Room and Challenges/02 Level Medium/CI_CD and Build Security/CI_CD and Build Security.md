# CI/CD and Build Security [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Walkthrough (Premium)
* **Slug:** `cicdandbuildsecurity`
* **Link:** https://tryhackme.com/room/cicdandbuildsecurity
* **Sección / Section:** DevSecOps / CI/CD
* **Fuente / Source:** Writeup de thmrevenant (GitHub)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Esta sala explora la seguridad en pipelines de CI/CD, cubriendo fundamentos, seguridad de repositorios, gestión de secretos, autenticación y aislamiento de entornos.
> **EN:** This room explores CI/CD pipeline security, covering fundamentals, repository security, secret management, authentication, and environment isolation.

---

### Task 1 — Fundamentos de CI/CD / CI/CD Fundamentals

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What element of a CI/CD pipeline coordinates and manages the automation of build and deployment environments? | `build orchestrator` |
| What element of a CI/CD pipeline builds, tests, and packages code? | `build agents` |
| What fundamental of CI/CD promotes developers in having access to the latest builds and code in order to understand and see the changes that have been made? | `maximum visibility` |
| What is the name of the build agent that can be used with Gitlab? | `Gitlab Runner` |
| What is the value of the flag you receive once authenticated to Timekeep? | `THM{Welcome.to.CICD.Pipelines}` |

---

### Task 2 — Seguridad del Repositorio / Repository Security

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Which file specifies which directories and files should be excluded for version control? | `.gitignore` |
| What can you protect to ensure direct pushes and vulnerable code changes are avoided? | `branches` |
| What issue does lack of access control and unauthorised code changes lead to? | `unauthorised tampering` |
| What is the API key stored within the Mobile application that can be accessed by any Gitlab user? | `THM{You.Found.The.API.Key}` |
| Where should you store artefacts to prevent tampering? | `secure registry` |
| What mechanism should you always use to store and inject sensitive data? | `secret management` |

---

### Task 3 — Seguridad del Build y Despliegue / Build & Deployment Security

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What attack can malicious actors perform to inject malicious code in the build process? | `dependency confusion` |
| Authenticate to Mother and follow the process to claim Flag 1. What is Flag 1? | `THM{7753f7e9-6543-4914-90ad-7153609831c3}` |
| What can be used to ensure that remote access to the build server can be performed securely? | `VPN` |
| What can be used to add an additional layer of authentication security for build agents? | `Token-based authentication` |
| Authenticate to Mother and follow the process to claim Flag 2. What is Flag 2? | `THM{1769f776-e03c-40b6-b2eb-b298297c15cc}` |

---

### Task 4 — Control de Merges y Entornos / Merge Control & Environments

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What can we add so that merges are raised for review instead of pushing the changes to code directly? | `merge requests` |
| What should we do so that only trusted runners execute CI/CD jobs? | `limit runner access` |
| Authenticate to Mother and follow the process to claim Flag 3. What is Flag 3? | `THM{2411b26f-b213-462e-b94c-39d974e503e6}` |
| What should you do so that a compromised environment doesn't affect other environments? | `isolate environments` |
| Authenticate to Mother and follow the process to claim Flag 4 from the DEV environment. What is Flag 4? | `THM{28f36e4a-7c35-4e4d-bede-be698ddf0883}` |
| Authenticate to Mother and follow the process to claim Flag 5 from the PROD environment. What is Flag 5? | `THM{e9f99dbe-6bae-4849-adf7-18a449c93fe6}` |

---

### Task 5 — Gestión de Secretos / Secrets Management

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Is using environment variables enough to protect the build secrets? (yay or nay) | `nay` |
| What is the value of the PROD API_KEY? | `THM{Secrets.are.meant.to.be.kept.Secret}` |

---

## Metodología / Methodology

1. **Paso 1 / Step 1:** Se exploran los fundamentos de CI/CD, identificando los componentes clave como build orchestrators y build agents, y se obtiene la primera flag autenticándose en Timekeep.
2. **Paso 2 / Step 2:** Se evalúa la seguridad del repositorio revisando archivos .gitignore, protección de branches, control de acceso, almacenamiento de artefactos en registries seguros y uso de secret management para datos sensibles.
3. **Paso 3 / Step 3:** Se identifican vectores de ataque como dependency confusion y se refuerza la seguridad con VPN y autenticación basada en tokens para build agents remotos.
4. **Paso 4 / Step 4:** Se implementan merge requests para revisiones de código, se limita el acceso a runners de confianza y se aíslan entornos (DEV/PROD) para contener compromisos.
5. **Paso 5 / Step 5:** Se demuestra que las variables de entorno por sí solas no son suficiente para proteger secretos del build y se obtiene la clave API de PROD desde un entorno protegido.

### Cadena de ataque / Attack Chain

```
Reconocimiento de pipeline CI/CD → Identificación de .gitignore y branches → Obtención de API key expuesta → Prueba de dependency confusion → Autenticación remota vía VPN + Token → Configuración de merge requests → Aislamiento de entornos → Exposición de secretos en variables de entorno
```

**Lección:** La seguridad en pipelines CI/CD requiere múltiples capas: protección de repositorios, gestión adecuada de secretos, aislamiento de entornos y autenticación robusta. Las variables de entorno por sí solas no son un mecanismo seguro para proteger secretos críticos.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
