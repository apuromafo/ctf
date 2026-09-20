# Source Code Security
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `sourcecodesecurity` |
| **Link** | [TryHackMe](https://tryhackme.com/room/sourcecodesecurity) |
| **Sección** | Secure Coding / DevSecOps / AppSec |
| **Fuente** | TryHackMe |
| **Componentes** | Git, GitHub, secretos en código, variables de entorno, CI/CD, GitLab CI, código Python |
| **Impacto** | Buenas prácticas para proteger el código fuente: gestión de secretos, evitar credenciales hardcodeadas, entender Git/GitHub y asegurar pipelines de CI/CD. |
---
**Contexto:** Esta room aborda la seguridad del código fuente desde la perspectiva del desarrollo seguro. Cubre los fundamentos de Git y GitHub (historia, modelo distribuido, ramas, remotos), el riesgo de exponer secretos en el código y en el historial de commits, el uso correcto de variables de entorno y la gestión de secretos en pipelines de integración continua (CI/CD). El objetivo es que el desarrollador identifique y evite fugas de credenciales en el ciclo de vida del software.
## Solucionario
### Task 1: Introduction / Introducción
**Explicación:** Presentación de la sala y de los objetivos de seguridad sobre el código fuente. Sin preguntas.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| Introducción a la sala (sin preguntas). | `No answer needed` |
### Task 2: Version Control History / Historia del control de versiones
**Explicación:** Origen del control de versiones distribuido. Git fue creado en **2005** por Linus Torvalds tras el conflicto con la herramienta propietaria anterior, **BitKeeper**, que dejó de ser gratuita para el desarrollo del kernel Linux.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. In what year was Git created? | `2005` |
| 2. What was the previous version control system used? | `BitKeeper` |
### Task 3: Git Model / Modelo de Git
**Explicación:** El modelo de Git es **distributed**: cada desarrollador tiene una copia completa del repositorio con todo el historial, lo que permite trabajar sin conexión y aumenta la resiliencia frente a fallos del servidor central.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Is Git centralized or distributed? | `Distributed` |
### Task 4: GitHub / GitHub
**Explicación:** **GitHub** se lanzó en **2007** y popularizó el alojamiento de **repositories** Git en la nube, añadiendo colaboración (issues, pull requests, forks) sobre el modelo distribuido de Git.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. In what year was GitHub founded? | `2007` |
| 2. What is hosted on GitHub? | `repositories` |
### Task 5: Secrets in Source Code / Secretos en el código
**Explicación:** Las credenciales y claves nunca deben hardcodearse en el código. El lugar correcto para almacenarlas son las **environment variables** (variables de entorno) o un gestor de secretos. Si un secreto se filtra (por ejemplo, en el historial de Git), la respuesta es **No**: commitear un secreto lo expone incluso si luego se borra, porque permanece en el historial.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Where should secrets be stored instead of the source code? | `environment variables` |
| 2. Does deleting a secret from the code remove it from Git history? | `No` |
### Task 6: Git Commands / Comandos de Git
**Explicación:** Comandos fundamentales de Git: **branches** (ramas para desarrollo aislado), **origin** (nombre por defecto del remoto) y **git clone** (descargar una copia local de un repositorio remoto).
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What are used to develop features in isolation? | `branches` |
| 2. What is the default name of the remote repository? | `origin` |
| 3. What command copies a remote repository locally? | `git clone` |
### Task 7: Code Analysis / Análisis de código
**Explicación:** Reto de análisis de un fragmento de código Python: la librería **os** permite interactuar con el sistema operativo/variables de entorno, donde aparecía un secreto expuesto. La flag obtenida es `THM-3LL3N-RIPL3Y`.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What Python library interacts with the operating system/environment? | `os` |
| 2. What is the flag found in the source code? | `THM-3LL3N-RIPL3Y` |
### Task 8: CI/CD Security / Seguridad en CI/CD
**Explicación:** Protección de secretos en pipelines de integración continua. Se obtiene la flag `THM_S3CUr3_4L13NS` y se identifica que la solución es la **secret management** (gestión de secretos) en lugar de variables en texto plano. En GitLab CI, los secretos y la definición del pipeline viven en el fichero **.gitlab-ci.yml**.
| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. What is the flag related to CI/CD security? | `THM_S3CUr3_4L13NS` |
| 2. What is the recommended practice to handle secrets in CI/CD? | `secret management` |
| 3. What is the GitLab CI configuration file? | `.gitlab-ci.yml` |
---
**Metodología:** Entender el control de versiones (Git/GitHub) → identificar el riesgo de secretos en código e historial → usar variables de entorno/gestores de secretos → analizar código en busca de credenciales → proteger pipelines CI/CD.
### Cadena de ataque / Attack Chain
```
Secreto hardcodeado -> commit en el repositorio -> exposición en el historial de Git -> fuga de credenciales -> compromiso de servicios/CI-CD
```
**Learning chain:** historia de Git → modelo distribuido → hosting en GitHub → riesgo de secretos → análisis de código → seguridad en CI/CD.
**Lección:** *Un secreto commiteado, aunque se borre después, permanece para siempre en el historial de Git; la única defensa fiable es gestionarlo con variables de entorno o un secret manager y rotarlo si se filtra.*
**MITRE ATT&CK:** T1552.001 (Unsecured Credentials: Credentials In Files), T1552.004 (Private Keys), T1552.007 (Container API), T1213.003 (Data from Information Repositories: Code Repositories).
**Fuente:** [TryHackMe - Source Code Security](https://tryhackme.com/room/sourcecodesecurity)
---
## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
