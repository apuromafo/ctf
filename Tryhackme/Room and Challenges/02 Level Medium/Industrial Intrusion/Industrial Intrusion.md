# Industrial Intrusion

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | ICS / OT / CTF | industrialintrusion | https://tryhackme.com/room/industrialintrusion | 02 Level Medium | TryHackMe | Node-RED, Modbus (502), OpenPLC (8080), S7 (102), EtherNet/IP (44818) | Manipulación de PLC / apertura de puerta industrial |

---

**Contexto:** Room ambientado en un entorno **ICS/OT** (Industrial Control Systems / Operational Technology) que simula un sistema de apertura de una puerta protegida por autenticación de **badge** y **detector de movimiento**. El objetivo es abrir la puerta (bypass del badge) explotando debilidades en la infraestructura de control. El escaneo completo de puertos revela un ambiente industrial: HTTP en 80 (página de estado del gate), **OpenPLC** en 8080, **Node-RED** en 1880, y protocolos industriales **Modbus 502**, S7 102 y EtherNet/IP 44818. La clave está en el dashboard de Node-RED expuesto sin autenticación y en la manipulación de **coils Modbus**; la flag aparece en la respuesta de la API del gate al abrirlo.

## Solucionario

### Task 1: Reconocimiento
**Explicación:**

Se hace un escaneo completo de puertos (obligatorio, el hint advierte de revisar todos los puertos). Destacan los servicios ICS: 502 (Modbus), 102 (S7), 44818 (EtherNet/IP), **1880** (Node-RED) y 8080 (OpenPLC). En el puerto 80 se observa la página *Gate Monitor* con el estado "Gate CLOSED"; su JavaScript consulta el endpoint `fetch('/api/gate')` y espera `data.status` y `data.flag`.

Respuesta: `No answer needed`

### Task 2: Enumeración de la infraestructura de control
**Explicación:**

Con `nmap`/`rustscan` y `gobuster` se confirma el entorno. En **Node-RED** (`http://<IP>:1880`) el editor está expuesto sin autenticación; su **dashboard** vive en la ruta `/ui` (convención de Node-RED). El dashboard muestra los controles del flujo de la puerta, incluyendo los toggles **Motion Detector** (coil 20) y **Badge** (coil 25), gestionados vía **Modbus**.

Respuesta: `No answer needed`

### Task 3: Breach (abrir la puerta)
**Explicación:**

Dos rutas equivalentes logran el bypass:

1. **Desde el dashboard Node-RED** (`http://<IP>:1880/ui`): apagar (toggle off) los controles **Motion Detector** y **Badge**, y refrescar la página del puerto 80, que pasa de `Gate CLOSED` a `Gate OPENED` mostrando la flag.
2. **Manipulando Modbus**: con un cliente Modbus (`mbtget`, `rodbus-client`, etc.) se enumeran los coils (20 a 30). Los coils **20** (motion detector) y **25** (badge) están en `true`; se escriben a `false`, p. ej.:
   ```
   mbtget -w5 1 -u 1 -a 20 <IP>
   mbtget -w5 1 -u 1 -a 25 <IP>
   ```
   Al desactivar ambos, la lógica del gate se invierte y se abre.

Tras abrir la puerta, la flag aparece en `/api/gate` (y en la web). Nota de gestión de fechas del CTF: `27 jun3`.

Respuesta: `THM{s4v3_th3_d4t3_27_jun3}`

### Task 4: Cierre
**Explicación:**

Se completan las tareas del escenario ICS tras el bypass del control de acceso y manipulación de los coils Modbus, consolidando lo aprendido sobre exposición de interfaces de control industriales.

Respuesta: `THM{thanks_for_playing}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tarea de reconocimiento | `No answer needed` |
| 2 | Tarea de enumeración del control | `No answer needed` |
| 3 | Flag tras abrir la puerta (BREACH) | `THM{s4v3_th3_d4t3_27_jun3}` |
| 4 | Flag final del escenario | `THM{thanks_for_playing}` |

---

**Metodología:** Reconocimiento ICS con `nmap -p-`/`rustscan` (servicios Modbus/S7/EtherNet-IP/Node-RED/OpenPLC), enumeración web con `gobuster`, explotación de la superficie de control: dashboard Node-RED sin autenticación (`/ui`) y escritura de **coils Modbus** (`mbtget -w5 1 -u 1 -a 20|25 <IP>`) para desactivar motion detector y badge, forzando la apertura del gate.

**Learning chain:** Port scan → servicios ICS → dashboard Node-RED expuesto → controles de gate → escritura de coils Modbus → gate abierto → flag.

**Lección:** *En OT/ICS la seguridad depende de la segmentación: una interfaz de control (Node-RED) expuesta sin autenticación permite manipular directamente los coils del PLC y anular los controles físicos (badge y movimiento).*

**MITRE ATT&CK:** T1595 Active Scanning · T1046 Network Service Discovery · T1190 Exploit Public-Facing Application · T1078 Valid Accounts (ausencia de autenticación) · T1059.007 Command and Scripting Interpreter: JavaScript (Node-RED) · T1485 Data Destruction (impacto potencial sobre procesos ICS).

**Fuente:** [TryHackMe - Industrial Intrusion](https://tryhackme.com/room/industrialintrusion)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.