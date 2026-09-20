# Linux Incident Surface

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | linuxincidentsurface | [TryHackMe](https://tryhackme.com/room/linuxincidentsurface) | 01 Level Easy | THM | systemd, /etc/systemd/system, servicios, persistencia, c2comm, ssh, puertos, análisis de logs | Identificación de la superficie de incidentes en Linux: servicios maliciosos, persistencia y comunicación C2 |

---

**Contexto:** Sala de análisis de incidentes en Linux centrada en la superficie de ataque. Se examinan conexiones sospechosas hacia una IP externa (`68.53.23.246:443`), un servicio de persistencia creado en `/etc/systemd/system` (`benign.service`), canales de comunicación C2 (`c2comm`) y un usuario (`saqib`) conectándose desde una IP interna.

> **EN:**
> 1. No answer needed
> 2. 3
> 3. No answer needed
> 4. 1. 68.53.23.246
>    2. 443
> 5. 1. /etc/systemd/system
>    2. benign.service
>    3. benign
>    4. 7
> 6. 1. 6
>    2. c2comm
> 7. 1. saqib
>    2. 10.11.75.247
> 8. No answer needed

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presenta el objetivo: analizar la superficie de incidentes de un sistema Linux comprometido para mapear dónde se esconde la actividad maliciosa (servicios, puertos, usuarios y canales de C2).

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | No se requiere respuesta / No answer needed | `No answer needed` |

### Task 2: Primeras evidencias / First evidence

**Explicación:** Se examinan los primeros indicadores recopilados del sistema para entender el alcance del incidente y cuántos elementos sospechosos están involucrados.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Cuál es el número de evidencias iniciales identificadas? / What is the number of initial evidence items identified? | `3` |

### Task 3: Preparación / Preparation

**Explicación:** Se prepara el entorno de análisis y las herramientas necesarias antes de profundizar en los logs y servicios sospechosos.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | No se requiere respuesta / No answer needed | `No answer needed` |

### Task 4: Conexión maliciosa / Malicious connection

**Explicación:** Se identifica la comunicación externa maliciosa: la IP del adversario (`68.53.23.246`) y el puerto usado (`443`), típico de exfiltración o C2 camuflado como HTTPS.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Cuál es la IP de la conexión maliciosa? / What is the IP of the malicious connection? | `68.53.23.246` |
| 2 | ¿Qué puerto utiliza? / What port does it use? | `443` |

### Task 5: Persistencia con systemd / systemd persistence

**Explicación:** Se encuentra un servicio de persistencia recién creado dentro de `/etc/systemd/system` llamado `benign.service`, un nombre diseñado para pasar desapercibido. El análisis del servicio revela el usuario `benign` y la configuración del mismo.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿En qué directorio se creó el servicio? / In which directory was the service created? | `/etc/systemd/system` |
| 2 | ¿Cómo se llama el servicio malicioso? / What is the malicious service called? | `benign.service` |
| 3 | ¿Qué usuario ejecuta el servicio? / Which user runs the service? | `benign` |
| 4 | ¿Cuántos campos/líneas clave tiene la definición del servicio? / How many key fields/lines does the service definition have? | `7` |

### Task 6: Canal de comunicación / Communication channel

**Explicación:** Se detecta el canal encargado de la comunicación con el adversario, identificando el mecanismo de C2 usado por el servicio malicioso.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Cuántos elementos forman el canal de comunicación? / How many elements make up the communication channel? | `6` |
| 2 | ¿Cómo se denomina el canal de C2? / What is the C2 channel called? | `c2comm` |

### Task 7: Usuario y origen / User and source

**Explicación:** Se identifica al usuario implicado en el incidente (`saqib`) y la IP de origen desde la que se establece la comunicación (`10.11.75.247`), completando el mapa de la superficie de ataque.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | ¿Qué usuario está implicado en el incidente? / Which user is involved in the incident? | `saqib` |
| 2 | ¿Desde qué IP se origina la comunicación? / From which IP does the communication originate? | `10.11.75.247` |

### Task 8: Conclusión / Conclusion

**Explicación:** Se consolidan todos los hallazgos (IP, puerto, servicio systemd, canal C2 y usuario) para cerrar el análisis de la superficie de incidentes.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | No se requiere respuesta / No answer needed | `No answer needed` |

---

**Metodología:** Correlacionar los logs de conexión para aislar la IP externa `68.53.23.246` y el puerto `443`. Listar los servicios de systemd y comparar con la línea base para descubrir `benign.service` en `/etc/systemd/system`; inspeccionar su definición (user `benign`) y su configuración. Seguir el tráfico del proceso para descubrir el canal `c2comm` y rastrear el usuario `saqib` conectándose desde `10.11.75.247`, reconstruyendo así toda la superficie de incidentes.

### Cadena de ataque / Attack Chain

Reconocimiento de conexiones → IP maliciosa (`68.53.23.246:443`) → descubrimiento de `benign.service` en `/etc/systemd/system` → análisis de configuración del servicio → detección del canal C2 (`c2comm`) → atribución al usuario `saqib` desde `10.11.75.247`

**Learning chain:** logs de conexión → 68.53.23.246:443 → /etc/systemd/system → benign.service → benign → c2comm → saqib → 10.11.75.247

**Lección:** *Los atacantes ocultan la persistencia en Linux bajo nombres inocuos como `benign.service` dentro de `/etc/systemd/system`; la correlación entre conexiones de red, servicios recién creados y usuarios activos es clave para reconstruir la superficie completa del incidente.*

**MITRE ATT&CK:** T1543.002 (Create or Modify System Process: Systemd Service), T1071 (Application Layer Protocol), T1041 (Exfiltration Over C2 Channel), T1057 (Process Discovery), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - Linux Incident Surface](https://tryhackme.com/room/linuxincidentsurface)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.