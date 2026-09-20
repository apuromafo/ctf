# Atlas

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `atlas` |
| **Link** | [TryHackMe](https://tryhackme.com/room/atlas) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | RDP (3389), http-proxy (8080), xfreerdp, pivoting |
| **Impacto** | Acceso remoto a una máquina Windows, exploración de servicios internos a través de un proxy HTTP y captura de flags. |

---

**Contexto:** La sala Atlas es una máquina guiada de estilo red team en la que se realizan escaneos de red para descubrir los servicios expuestos, se accede por RDP a un sistema Windows y se emplea un proxy HTTP para alcanzar servicios internos. A lo largo del recorrido se practica la enumeración de servicios, la conexión remota, el movimiento lateral y la captura de las banderas del lab. El progreso se compone de tareas informativas (sin respuesta) intercaladas con preguntas concretas de puertos, servicios y flags.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Tarea de presentación de la sala. Se explican los objetivos y la mecánica del laboratorio, junto con el entorno de ataque que se utilizará. No hay respuesta que enviar.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la introducción de la sala y preparar el entorno de ataque. | `No answer needed` |

### Task 2: Descubrimiento de servicios / Service Discovery

**Explicación:** Se realiza un escaneo de puertos sobre la máquina objetivo que revela dos servicios abiertos: RDP en el puerto **3389** y un **http-proxy** en el puerto **8080**. Se confirma la exposición de la máquina Windows al exterior.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Ejecutar el escaneo de red solicitado sobre el objetivo. | `No answer needed` |
| 2 | ¿Qué puertos están abiertos en la máquina objetivo? | `3389,8080` |
| 3 | ¿Qué servicio se está ejecutando en el puerto 8080? | `http-proxy` |
| 4 | Registrar los resultados del escaneo para las siguientes tareas. | `No answer needed` |

### Task 3: Acceso inicial / Initial Access

**Explicación:** Tarea enfocada a la obtención del acceso inicial, estableciendo la conexión remota con la máquina comprometida. Es un paso práctico sin respuesta numérica que validar.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Completar el paso práctico de acceso inicial. | `No answer needed` |

### Task 4: Reconocimiento interno / Internal Reconnaissance

**Explicación:** Una vez dentro de la máquina, se llevan a cabo pasos de reconocimiento interno del sistema y de la red. Son tareas eminentemente prácticas orientadas a dejar el entorno listo para la siguiente fase de la cadena de ataque.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Realizar el reconocimiento interno (paso 1). | `No answer needed` |
| 2 | Realizar el reconocimiento interno (paso 2). | `No answer needed` |
| 3 | Realizar el reconocimiento interno (paso 3). | `No answer needed` |
| 4 | Realizar el reconocimiento interno (paso 4). | `No answer needed` |
| 5 | Realizar el reconocimiento interno (paso 5). | `No answer needed` |

### Task 5: Preparación del pivoteo / Pivoting Setup

**Explicación:** Tarea en la que se prepara el pivoteo a través del proxy HTTP para poder alcanzar servicios que no están expuestos directamente al exterior. Paso práctico sin respuesta que enviar.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Completar la preparación del pivoteo. | `No answer needed` |

### Task 6: Explotación avanzada / Advanced Exploitation

**Explicación:** Se explotan los servicios accesibles a través del proxy para profundizar en el compromiso de la máquina. Los pasos son prácticos y dejan evidencia de acceso para las tareas de banderas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Ejecutar el paso de explotación 1. | `No answer needed` |
| 2 | Ejecutar el paso de explotación 2. | `No answer needed` |
| 3 | Ejecutar el paso de explotación 3. | `No answer needed` |
| 4 | Ejecutar el paso de explotación 4. | `No answer needed` |
| 5 | Ejecutar el paso de explotación 5. | `No answer needed` |
| 6 | Ejecutar el paso de explotación 6. | `No answer needed` |
| 7 | Ejecutar el paso de explotación 7. | `No answer needed` |
| 8 | Ejecutar el paso de explotación 8. | `No answer needed` |

### Task 7: Captura de flags / Flag Capture

**Explicación:** Tarea final de recolección de banderas. Los primeros pasos verifican el acceso conseguido y, al completar la cadena, se localiza y reporta la flag que cierra la máquina.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Paso práctico de verificación 1. | `No answer needed` |
| 2 | Paso práctico de verificación 2. | `No answer needed` |
| 3 | Paso práctico de verificación 3. | `No answer needed` |
| 4 | Paso práctico de verificación 4. | `No answer needed` |
| 5 | Paso práctico de verificación 5. | `No answer needed` |
| 6 | Paso práctico de verificación 6. | `No answer needed` |
| 7 | ¿Cuál es la flag obtenida tras completar la cadena de ataque? | `c16444961f67af7eea7e420b65c8c3eb` |

### Task 8: Conclusión / Conclusion

**Explicación:** Recapitulación final de la sala: se repasan los servicios comprometidos, el uso del proxy para el pivoteo y las lecciones aprendidas. No hay respuesta que enviar.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la conclusión de la sala. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la introducción de la sala y preparar el entorno de ataque. | `No answer needed` |
| 2 | Ejecutar el escaneo de red solicitado sobre el objetivo. | `No answer needed` |
| 3 | ¿Qué puertos están abiertos en la máquina objetivo? | `3389,8080` |
| 4 | ¿Qué servicio se está ejecutando en el puerto 8080? | `http-proxy` |
| 5 | Registrar los resultados del escaneo para las siguientes tareas. | `No answer needed` |
| 6 | Completar el paso práctico de acceso inicial. | `No answer needed` |
| 7 | Realizar el reconocimiento interno (paso 1). | `No answer needed` |
| 8 | Realizar el reconocimiento interno (paso 2). | `No answer needed` |
| 9 | Realizar el reconocimiento interno (paso 3). | `No answer needed` |
| 10 | Realizar el reconocimiento interno (paso 4). | `No answer needed` |
| 11 | Realizar el reconocimiento interno (paso 5). | `No answer needed` |
| 12 | Completar la preparación del pivoteo. | `No answer needed` |
| 13 | Ejecutar el paso de explotación 1. | `No answer needed` |
| 14 | Ejecutar el paso de explotación 2. | `No answer needed` |
| 15 | Ejecutar el paso de explotación 3. | `No answer needed` |
| 16 | Ejecutar el paso de explotación 4. | `No answer needed` |
| 17 | Ejecutar el paso de explotación 5. | `No answer needed` |
| 18 | Ejecutar el paso de explotación 6. | `No answer needed` |
| 19 | Ejecutar el paso de explotación 7. | `No answer needed` |
| 20 | Ejecutar el paso de explotación 8. | `No answer needed` |
| 21 | Paso práctico de verificación 1. | `No answer needed` |
| 22 | Paso práctico de verificación 2. | `No answer needed` |
| 23 | Paso práctico de verificación 3. | `No answer needed` |
| 24 | Paso práctico de verificación 4. | `No answer needed` |
| 25 | Paso práctico de verificación 5. | `No answer needed` |
| 26 | Paso práctico de verificación 6. | `No answer needed` |
| 27 | ¿Cuál es la flag obtenida tras completar la cadena de ataque? | `c16444961f67af7eea7e420b65c8c3eb` |
| 28 | Leer la conclusión de la sala. | `No answer needed` |

---

**Metodología:**

1. Se escanea la máquina objetivo para descubrir los puertos abiertos: **3389** (RDP) y **8080** (http-proxy).
2. Se conecta por RDP (xfreerdp) a la máquina Windows para obtener una sesión interactiva.
3. Se realiza reconocimiento interno del sistema y de los servicios accesibles.
4. Se emplea el proxy HTTP del puerto 8080 para pivotar y alcanzar servicios internos no expuestos directamente.
5. Se explotan los servicios internos para profundizar el acceso y se recogen las banderas del laboratorio.
6. Se completa la cadena de ataque localizando la flag final de la máquina.

### Cadena de ataque / Attack Chain

```
Recon (nmap) -> 3389 RDP + 8080 http-proxy
  -> Acceso RDP -> xfreerdp
  -> Reconocimiento interno
  -> Preparación del pivoteo (proxy 8080)
  -> Explotación avanzada -> servicios internos
  -> Captura de flags
```

**Learning chain:** Escaneo de puertos → Identificación de RDP y proxy HTTP → Acceso remoto → Reconocimiento interno → Pivoteo vía proxy → Explotación interna → Banderas

**Lección:** *Una enumeración completa de puertos y el uso correcto de un proxy para pivotar son clave para comprometer una máquina Windows cuyos servicios internos no están expuestos al exterior.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1021.001 (Remote Services: Remote Desktop Protocol), T1105 (Ingress Tool Transfer), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - Atlas](https://tryhackme.com/room/atlas)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.