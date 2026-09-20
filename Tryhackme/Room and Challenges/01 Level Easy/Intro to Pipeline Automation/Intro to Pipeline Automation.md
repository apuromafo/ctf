# Intro to Pipeline Automation

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `introtopipelineautomation` | [TryHackMe](https://tryhackme.com/room/introtopipelineautomation) | 01 Level Easy | TryHackMe | CI/CD, GitHub, GitLab, GittyLeaks, Dependencies, SAST, DAST, Build, Environments | Fundamentos de automatización de pipelines CI/CD: entornos, plataformas, dependencias, escaneos SAST/DAST, componentes de build y riesgos de entorno |

> **Objeto:** Aprender los fundamentos de la automatización de pipelines DevOps y sus riesgos de seguridad: dónde se despliega el producto, plataformas de Git, búsqueda de secretos en commits, gestión de dependencias, escaneos SAST y DAST, componentes de build (orquestador y agente) y los entornos DEV/UAT/PrePROD.

---

**Contexto:** Sala del path DevSecOps que introduce la automatización de pipelines y sus implicaciones de seguridad: la fase donde se despliega el producto (Environments), las plataformas de Git (GitHub, GitLab), la búsqueda de secretos en commits con GittyLeaks, las dependencias internas/externas y PyPi con el caso de Log4j, los escaneos SAST y DAST (que no sustituyen un pentest), los componentes de build (Build Orchestrator y Build Agent), los entornos DEV/UAT/PrePROD con sus riesgos (Developer Bypasses) y una flag final tras construir el pipeline.

> **ES:** Sala de introducción a la automatización de pipelines CI/CD: entornos, plataformas Git, secretos, dependencias, SAST/DAST, componentes de build y riesgos de entorno.
> **EN:** Introduction to CI/CD pipeline automation room: environments, Git platforms, secrets, dependencies, SAST/DAST, build components and environment risks.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación de la sala: qué es la automatización de pipelines y por qué es relevante para la seguridad en DevSecOps.

No answer needed

### Task 2: Pipelines DevOps explicados / DevOps Pipelines Explained
**Explicación:** Se explica el diagrama de un pipeline típico y dónde se despliega el producto final: en la fase de entornos (Environments).

Environments

### Task 3: Gestión de código fuente / Source Code Management
**Explicación:** Se presentan las plataformas de gestión del código fuente: GitHub como mayor proveedor online de Git, GitLab para alojar tu propio servidor Git y GittyLeaks para escanear los commits de un repositorio en busca de información sensible.

1. Github
2. Gitlab
3. GittyLeaks

### Task 4: Gestión de dependencias / Dependency Management
**Explicación:** Se aprenden los tipos de dependencias: internas (creadas por la organización) y externas (como JQuery), el repositorio público de paquetes de Python (PyPi) y la vulnerabilidad 0day Log4j de 2021.

1. Internal
2. External
3. PyPi
4. Log4j

### Task 5: Pruebas automatizadas / Automated Testing
**Explicación:** Se comparan las herramientas de análisis de código: SAST escanea el código en busca de vulnerabilidades y DAST ejecuta el código e inyecta casos de prueba; ninguna de las dos sustituye a una prueba de penetración (Nay).

1. SAST
2. DAST
3. Nay

### Task 6: Integración y entrega continua / CI/CD and Build Infrastructure
**Explicación:** Se definen los componentes del build: Continuous Integration y Continuous Delivery (CI/CD), el elemento de infraestructura que controla todos los builds (Build Orchestrator) y el que realiza el build (Build Agent).

1. Continuous Integration
2. Continuous Delivery
3. Build Orchestrator
4. Build Agent

### Task 7: Entornos / Environments
**Explicación:** Se revisan los entornos de despliegue: DEV (el más débil en seguridad), UAT (para probar la aplicación), PrePROD (similar a PROD) y la clase de vulnerabilidades que aparecen en PROD por código inseguro procedente de DEV (Developer Bypasses).

1. DEV
2. UAT
3. PrePROD
4. Developer Bypasses

### Task 8: Flag del pipeline / Flag
**Explicación:** Tras construir correctamente el pipeline, se obtiene la flag final de la sala.

THM{Pipeline.Automation.Is.Fun}

### Task 9: Conclusión / Conclusion
**Explicación:** Cierre de la sala.

No answer needed

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | Introducción a la sala | `No answer needed` |
| 2 | ¿Dónde se despliega el producto final en el pipeline? | `Environments` |
| 3.1 | ¿Qué proveedor es el mayor proveedor online de Git? | `Github` |
| 3.2 | ¿Qué producto Git se usa para alojar tu propio servidor Git? | `Gitlab` |
| 3.3 | ¿Qué herramienta escanea los commits de un repo en busca de información sensible? | `GittyLeaks` |
| 4.1 | Tipo de dependencia creada por nuestra organización (Internal/External) | `Internal` |
| 4.2 | Tipo de dependencia de JQuery (Internal/External) | `External` |
| 4.3 | Nombre del repositorio público de dependencias de Python | `PyPi` |
| 4.4 | Vulnerabilidad 0day de dependencias que encendió la alerta mundial en 2021 | `Log4j` |
| 5.1 | Tipo de herramienta que escanea el código en busca de vulnerabilidades | `SAST` |
| 5.2 | Tipo de herramienta que ejecuta el código e inyecta casos de prueba | `DAST` |
| 5.3 | ¿Pueden SAST y DAST sustituir a los pentest? (Yea/Nay) | `Nay` |
| 6.1 | ¿Qué significa CI en CI/CD? | `Continuous Integration` |
| 6.2 | ¿Qué significa CD en CI/CD? | `Continuous Delivery` |
| 6.3 | Elemento de infraestructura que controla todos los builds | `Build Orchestrator` |
| 6.4 | Elemento de infraestructura que realiza el build | `Build Agent` |
| 7.1 | Entorno que suele tener la configuración de seguridad más débil | `DEV` |
| 7.2 | Entorno usado para probar la aplicación | `UAT` |
| 7.3 | Entorno similar a PROD para verificar antes de desplegar | `PrePROD` |
| 7.4 | Clase de vulnerabilidades descubiertas en PROD por código inseguro de DEV | `Developer Bypasses` |
| 8 | Flag recibida tras construir el pipeline | `THM{Pipeline.Automation.Is.Fun}` |
| 9 | Cierre de la sala | `No answer needed` |

---

**Metodología:** Revisión del diagrama del pipeline y la fase de entornos, identificación de plataformas de Git (GitHub, GitLab) y herramientas de escaneo de secretos (GittyLeaks), clasificación de dependencias internas/externas con el caso PyPi/Log4j, comparación de SAST y DAST frente al pentest, definición de los componentes de build y análisis de los entornos DEV/UAT/PrePROD y sus riesgos (Developer Bypasses) hasta obtener la flag.

### Cadena de ataque / Attack Chain

Pipeline -> Environments -> source code (GitHub/GitLab) -> GittyLeaks (secretos) -> dependencias (internal/external/PyPi/Log4j) -> SAST/DAST -> CI/CD -> Build Orchestrator/Agent -> entrenos DEV/UAT/PrePROD -> Developer Bypasses -> flag

**Learning chain:** pipeline automation -> environments -> source control -> secret scanning -> dependency management -> SAST/DAST -> CI/CD -> build infrastructure -> environment security

**Lección:** *Un pipeline automatizado acelera la entrega de software, pero cada fase (código, dependencias, builds y entornos) introduce superficie de ataque; integrar seguridad en cada etapa es la esencia de DevSecOps.*

**MITRE ATT&CK:** T1195 (Supply Chain Compromise).

**Fuente:** [TryHackMe - Intro to Pipeline Automation](https://tryhackme.com/room/introtopipelineautomation)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.