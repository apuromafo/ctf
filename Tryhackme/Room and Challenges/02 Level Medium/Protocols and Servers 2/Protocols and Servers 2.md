# Protocols and Servers 2

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Intro / Networking | protocolsandservers2 | https://tryhackme.com/room/protocolsandservers2 | 02 Level Medium | TryHackMe | Telnet, IMAP, DNS (DoT), OSINT de versiones, Telnet | Identificación de servicios y credenciales de acceso |

---

**Contexto:** La sala **Protocols and Servers 2** es una continuación introductoria sobre protocolos y servicios de red. El alumno practica con Telnet, identifica el banner de los servicios (p. ej. `port 23`, `imap`), resuelve conteos, diferencia DNS seguro (DoT), enumera versiones del sistema operativo y del paquete y, finalmente, obtiene una credencial a través de un servicio Telnet contra la máquina de laboratorio.

## Solucionario

### Task 1: Preparación / Preparation
**Explicación:**

Tarea de arranque en la que no se requiere respuesta; solo conectar con el entorno de laboratorio.

Respuesta: `No answer needed`

### Task 2: Identificación de servicios / Service identification
**Explicación:**

Se identifican los servicios por su puerto y protocolo: Telnet en el puerto 23 y el protocolo de correo `imap`.

1. `port 23`
2. `imap`

### Task 3: Conteo de resultados / Result counts
**Explicación:**

Las respuestas numéricas (3 y 3) reflejan los conteos que arroja la enumeración de los servicios y puertos de la máquina.

1. `3`
2. `3`

### Task 4: DNS seguro / Secure DNS
**Explicación:**

La variante de DNS que cifra las consultas se denomina DoT (DNS sobre TLS).

Respuesta: `DoT`

### Task 5: Versiones del sistema / System versions
**Explicación:**

Se enumeran las versiones del sistema operativo (núcleo) y el número de versión del paquete o servicio identificado.

1. `5.15.0-119-generic`
2. `415`

### Task 6: Credencial de acceso / Access credential
**Explicación:**

Tras autenticarse contra el servicio, se obtiene la credencial/usuario que permite seguir avanzando en el laboratorio.

Respuesta: `butterfly`

### Task 7: Cierre / Closing
**Explicación:**

Tarea final de cierre sin respuesta requerida.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tarea de preparación inicial | `No answer needed` |
| 2.1 | ¿Qué puerto usa Telnet? | `port 23` |
| 2.2 | ¿Qué protocolo de correo se detecta? | `imap` |
| 3.1 | Conteo de servicios/puertos detectados | `3` |
| 3.2 | Conteo de servicios/puertos detectados | `3` |
| 4 | ¿Qué variante de DNS cifra las consultas? | `DoT` |
| 5.1 | Versión del núcleo del sistema | `5.15.0-119-generic` |
| 5.2 | Número de versión del servicio | `415` |
| 6 | ¿Qué credencial se obtiene? | `butterfly` |
| 7 | Tarea final de cierre | `No answer needed` |

---

**Metodología:** Conexión a los servicios expuestos, identificación de puertos y banners por protocolo, conteo de resultados de escaneo, diferenciación entre DNS seguro (DoT) y no seguro, enumeración de versiones y autenticación para recuperar la credencial.

### Cadena de ataque / Attack Chain

```
Conexión a la máquina de laboratorio
        │
        ▼
Escaneo de puertos (23) y protocolos (imap)
        │
        ▼
Conteo de servicios detectados
        │
        ▼
Identificación DoT / versiones del sistema
        │
        ▼
Acceso vía Telnet → credencial (butterfly)
```

**Learning chain:** Reconocimiento de puertos → identificación de protocolo → enumeración → autenticación → credencial.

**Lección:** *Los banners de servicios (Telnet, IMAP) son una fuente inmediata de información en la fase de reconocimiento; el DNS debe cifrarse (DoT) por defecto en cualquier despliegue.*

**MITRE ATT&CK:** T1046 Network Service Discovery · T1078 Valid Accounts · T1021.001 Remote Services (Telnet).

**Fuente:** [TryHackMe - Protocols and Servers 2](https://tryhackme.com/room/protocolsandservers2)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.