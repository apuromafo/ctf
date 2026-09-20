# Anonforce

| **Dificultad** | Easy |
| **Tipo** | CTF (boot2root) |
| **Slug** | `anonforce` |
| **Link** | [TryHackMe](https://tryhackme.com/room/anonforce) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | FTP anónimo, archivos de credenciales, GPG |
| **Impacto** | Compromiso total de la máquina a partir de un acceso FTP anónimo y material cifrado accesible |

---

**Contexto:** Máquina boot2root que parte del acceso FTP anónimo: se descargan los archivos del servicio, se extrae material sensible (como claves GPG) y se obtienen las dos banderas del room. El resumen original conserva únicamente las dos respuestas finales (hashes), sin los enunciados de las preguntas.

## Solucionario

### Task 1: Compromiso / Compromise

**Explicación:** Se accede al servicio FTP con el usuario anónimo, se enumeran y descargan los archivos disponibles, se procesa el material cifrado/encontrado y se obtienen las dos banderas del room.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `606083fd33beb1284fc51f411a706af8` |
| 2 | *(Pregunta 2 no especificada en el original)* | `f706456440c7af4187810c31c6cebdce` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `606083fd33beb1284fc51f411a706af8` |
| 2 | *(Pregunta 2 no especificada en el original)* | `f706456440c7af4187810c31c6cebdce` |

---

**Metodología:** Escaneo/enumeración → acceso FTP anónimo → descarga de archivos → extracción de credenciales y material cifrado → descifrado con GPG → obtención de las flags.

**Learning chain:** Enumeración de servicios → FTP anónimo → recuperación de material cifrado → cracking/descifrado GPG → obtención de banderas

**Lección:** *Un servicio por defecto como el FTP anónimo puede ser el punto de partida de un compromiso total cuando expone archivos de credenciales o material cifrado descifrable.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1078 (Valid Accounts), T1552 (Unsecured Credentials), T1145 (Private Keys)

**Fuente:** [TryHackMe - Anonforce](https://tryhackme.com/room/anonforce)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.