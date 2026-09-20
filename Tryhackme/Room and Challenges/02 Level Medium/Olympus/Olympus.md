# Olympus

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF | olympus | https://tryhackme.com/room/olympus | 02 Level Medium | TryHackMe | Escaneo web, abuso de funcionalidades de la app, creación de PDF, exfiltración de archivos | Compromiso de la máquina a través de la explotación de una aplicación web con temática griega (Olympus): abusar de funcionalidades de la propia web para obtener la flag 1, exfiltrar archivos del sistema y leer las cuatro flags del reto (flag{...}). |

---

**Contexto:** La sala **Olympus** es un reto CTF de dificultad media basado en una aplicación web con temática de la mitología griega. El reto está pensado para resolverse aprovechando únicamente las funcionalidades legítimas de la propia web (abuso de características de la aplicación, abstracción de archivos, generador de PDF, etc.) en lugar de un exploit único. Se compone de una tarea inicial de despliegue y una tarea con las **cuatro flags** del reto, todas con formato `flag{...}`.

> **ES:** CTF medio de abuso de una aplicación web temática (mitología griega): explotar las funcionalidades de la propia web para extraer archivos y obtener las cuatro flags del reto.
> **EN:** A medium CTF about abusing a Greek-mythology-themed web app: abusing the app's own features to extract files and obtain the challenge's four flags.

## Solucionario

### Task 1: Despliegue / Deployment
**Explicación:** Tarea de despliegue de la máquina virtual del reto. Se pide que la máquina haya terminado de arrancar y que se escriba la respuesta de confirmación esperada.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Deploy the machine and confirm it is up (no answer required). / Despliega la máquina y confirma que está activa. | `No answer needed` |

### Task 2: Flags del CTF / CTF Flags
**Explicación:** Las cuatro flags se consiguen abusando de las funcionalidades de la aplicación web de Olympus. La **Flag 1** (`flag{Sm4rt!_k33P_d1gGIng}`) premia el reconocimiento: la pista de la propia web indica que **hay que seguir escarbando** (keep digging). La **Flag 2** (`flag{Y0u_G0t_TH3_l1ghtN1nG_P0w3R}`) se obtiene tras explotar la funcionalidad de creación de PDF/abstracción de archivos con los parámetros adecuados ("you got the lightning power", guiño a Zeus). La **Flag 3** (`flag{D4mN!_Y0u_G0T_m3_:)_}`) aparece tras leer el fichero de flags del sistema, y la **Flag 4** (`flag{Y0u_G0t_m3_g00d!}`) se consigue exfiltrando de la base de datos o del proceso de la aplicación la última flag del reto. La pregunta inicial del task es de confirmación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Confirmas que has terminado de desplegar? / Confirm you have finished deploying. | `No answer needed` |
| 2 | What is Flag 1? / ¿Cuál es la Flag 1? | `flag{Sm4rt!_k33P_d1gGIng}` |
| 3 | What is Flag 2? / ¿Cuál es la Flag 2? | `flag{Y0u_G0t_TH3_l1ghtN1nG_P0w3R}` |
| 4 | What is Flag 3? / ¿Cuál es la Flag 3? | `flag{D4mN!_Y0u_G0T_m3_:)_}` |
| 5 | What is Flag 4? / ¿Cuál es la Flag 4? | `flag{Y0u_G0t_m3_g00d!}` |

### Tabla unificada de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Task 1) Despliegue de la máquina. | `No answer needed` |
| 2 | (Task 2) Pregunta de confirmación del reto. | `No answer needed` |
| 3 | (Task 2) What is Flag 1? | `flag{Sm4rt!_k33P_d1gGIng}` |
| 4 | (Task 2) What is Flag 2? | `flag{Y0u_G0t_TH3_l1ghtN1nG_P0w3R}` |
| 5 | (Task 2) What is Flag 3? | `flag{D4mN!_Y0u_G0T_m3_:)_}` |
| 6 | (Task 2) What is Flag 4? | `flag{Y0u_G0t_m3_g00d!}` |

---

**Metodología:** Reconocimiento de la aplicación web de Olympus → lectura atenta de las pistas dentro del propio sitio (flag 1, "keep digging") → exploración de funcionalidades (PDF/parser, vistas de archivos) y abuso de parámetros → lectura de ficheros del sistema (flag 3) → profundización hasta la base de datos o proceso interno (flags 2 y 4).

**Learning chain:** web recon → organization/abuse of app features → file abstraction/PDF → system file read → flags 1-4.

**Lección:** *Las funcionalidades legítimas de una aplicación pueden ser el vector: una app que da a elegir qué archivo procesar o renderizar convierte un "feature" en LFI/RCE sin necesidad de un exploit conocido.*

**MITRE ATT&CK:** T1595 (Active Scanning) · T1190 (Exploit Public-Facing Application) · T1005 (Data from Local System) · T1083 (File and Directory Discovery).

**Fuente:** [TryHackMe - Olympus](https://tryhackme.com/room/olympus)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.