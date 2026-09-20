# The Docker Rodeo
| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough / Docker | thedockerrodeo | https://tryhackme.com/room/thedockerrodeo | 02 Level Medium | TryHackMe | Docker, registro de imágenes, ingeniería inversa de imágenes, daemon expuesto, namespaces, privilegios, escape de contenedores | Recorrido guiado por siete vulnerabilidades de Docker que van desde el abuso de un registry hasta el escape total del contenedor |

> **Objeto:** Aprender una amplia variedad de vulnerabilidades de Docker en una demostración guiada.

---
**Contexto:** **The Docker Rodeo** es una sala guiada (walkthrough) que presenta una amplia variedad de vulnerabilidades de Docker. Tras una fase de preparación e introducción, se encadenan siete fallos típicos de entornos contenerizados: abuso de un Docker Registry, ingeniería inversa de imágenes, subida de imágenes maliciosas, RCE a través de un daemon expuesto, escape mediante el daemon, namespaces compartidos y privilegios mal configurados. Cada vulnerabilidad incorpora sus propias preguntas y respuestas, y la sala finaliza con una sección de hardening y material adicional. No se explota una máquina externa: el foco está en comprender y abusar de la configuración de Docker.
> **ES:** Aprende una amplia variedad de vulnerabilidades de Docker en esta demostración guiada.
> **EN:** Learn a wide variety of Docker vulnerabilities in this guided showcase.

## Solucionario
### Task 1: Prefacio: preparar Docker para esta sala (Deploy #1) / Preface: Setting up Docker for this Room (Deploy #1)
**Explicación:** Se prepara el entorno Docker necesario para realizar el resto de la sala y se despliega la primera máquina de laboratorio.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Task 1 | `No answer needed` |

### Task 2: Introducción a Docker / Introduction to Docker
**Explicación:** Repaso de los conceptos básicos de Docker (imágenes, contenedores y su modelo de aislamiento) para contextualizar las vulnerabilidades posteriores.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Task 2 | `Nay` |

### Task 3: Vulnerabilidad #1: abusar de un Docker Registry / Vulnerability #1: Abusing a Docker Registry
**Explicación:** Introducción al abuso de un Docker Registry mal protegido como primera vulnerabilidad de la sala.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Task 3 | `No answer needed` |

### Task 4: ¿Qué es un Docker Registry? / What is a Docker Registry?
**Explicación:** Definición y funcionamiento de un Docker Registry (almacén de imágenes) y por qué es un objetivo interesante para un atacante.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Task 4 | `No answer needed` |

### Task 5: Interactuar con un Docker Registry / Interacting with a Docker Registry
**Explicación:** Se interactúa con el registry expuesto para enumerar y descargar imágenes. Las respuestas documentan el puerto del registry, la imagen encontrada, el tag y las credenciales/usuarios observados.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Task 5 (1) | `7000` |
| Task 5 (2) | `securesolutions/webserver` |
| Task 5 (3) | `production` |
| Task 5 (4) | `admin` |
| Task 5 (5) | `production_admin` |

### Task 6: Vulnerabilidad #2: ingeniería inversa de imágenes Docker / Vulnerability #2: Reverse Engineering Docker Images
**Explicación:** Se descarga una imagen del registry y se analiza su contenido (capas/configuración) para extraer información sensible.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Task 6 (1) | `2a0a63ea5d88` |
| Task 6 (2) | `7` |
| Task 6 (3) | `uogctf` |

### Task 7: Vulnerabilidad #3: subir imágenes Docker maliciosas / Vulnerability #3: Uploading Malicious Docker Images
**Explicación:** Se demuestra cómo subir imágenes maliciosas a un registry para comprometer a quien las descargue.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Task 7 | `No answer needed` |

### Task 8: Vulnerabilidad #4: RCE vía daemon Docker expuesto / Vulnerability #4: RCE via Exposed Docker Daemon
**Explicación:** Con el daemon de Docker accesible por red, se abusa de él para ejecutar comandos de forma remota en el host.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Task 8 | `No answer needed` |

### Task 9: Vulnerabilidad #5: escape vía daemon Docker expuesto / Vulnerability #5: Escape via Exposed Docker Daemon
**Explicación:** Se aprovecha el daemon expuesto para escapar del contenedor y alcanzar el sistema anfitrión.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Task 9 | `No answer needed` |

### Task 10: Vulnerabilidad #6: namespaces compartidos / Vulnerability #6: Shared Namespaces
**Explicación:** Los namespaces compartidos entre contenedor y host permiten romper el aislamiento y acceder a recursos del anfitrión.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Task 10 | `No answer needed` |

### Task 11: Vulnerabilidad #7: privilegios mal configurados (Deploy #2) / Vulnerability #7: Misconfigured Privileges (Deploy #2)
**Explicación:** Se despliega la segunda máquina y se explota una configuración de privilegios incorrecta para escapar del contenedor, obteniendo la flag final.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Task 11 | `thm{you_escaped_the_chains}` |

### Task 12: Asegurar tu contenedor / Securing Your Container
**Explicación:** Buenas prácticas de hardening para evitar las vulnerabilidades vistas a lo largo de la sala.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Task 12 | `No answer needed` |

### Task 13: Bonus: determinar si estamos dentro de un contenedor / Bonus: Determining if we're in a container
**Explicación:** Técnicas para detectar desde dentro si el entorno en el que se ejecuta es un contenedor Docker.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Task 13 | `No answer needed` |

### Task 14: Material adicional / Additional Material
**Explicación:** Recursos y lecturas adicionales para profundizar en la seguridad de contenedores.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Task 14 | `No answer needed` |

### Tabla de preguntas y respuestas
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Task 1 | `No answer needed` |
| 2 | Task 2 | `Nay` |
| 3 | Task 3 | `No answer needed` |
| 4 | Task 4 | `No answer needed` |
| 5 | Task 5 | `No answer needed` |
| 5.1 | Task 5 (1) | `7000` |
| 5.2 | Task 5 (2) | `securesolutions/webserver` |
| 5.3 | Task 5 (3) | `production` |
| 5.4 | Task 5 (4) | `admin` |
| 5.5 | Task 5 (5) | `production_admin` |
| 6.1 | Task 6 (1) | `2a0a63ea5d88` |
| 6.2 | Task 6 (2) | `7` |
| 6.3 | Task 6 (3) | `uogctf` |
| 7 | Task 7 | `No answer needed` |
| 8 | Task 8 | `No answer needed` |
| 9 | Task 9 | `No answer needed` |
| 10 | Task 10 | `No answer needed` |
| 11 | Task 11 | `thm{you_escaped_the_chains}` |
| 12 | Task 12 | `No answer needed` |
| 13 | Task 13 | `No answer needed` |
| 14 | Task 14 | `No answer needed` |

---
**Metodología:** Configuración del entorno Docker → introducción a Docker → abuso de registry → ingeniería inversa de imágenes → subida de imágenes maliciosas → RCE vía daemon → escape vía daemon → namespaces compartidos → privilegios mal configurados → hardening → detección dentro de contenedor.

### Cadena de ataque / Attack Chain
```
Setup Docker -> Intro a Docker -> Abuso de Docker Registry -> Reversing de imágenes
-> Imágenes maliciosas -> RCE vía daemon expuesto -> Escape vía daemon
-> Namespaces compartidos -> Privilegios mal configurados -> Escape del contenedor
-> Hardening / detección en contenedor
```
**Learning chain:** Entorno → conceptos → abuso de registry → reversing de imágenes → imágenes maliciosas → RCE → escape → aislamiento de namespaces → privilegios → defensa.
**Lección:** *La mayoría de los escapes de contenedor no explotan Docker en sí, sino configuraciones débiles: registries abiertos, daemon expuesto, namespaces compartidos y privilegios excesivos.*
**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1611 (Escape to Host), T1552 (Unsecured Credentials), T1083 (File and Directory Discovery).
**Fuente:** [TryHackMe - The Docker Rodeo](https://tryhackme.com/room/thedockerrodeo)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
