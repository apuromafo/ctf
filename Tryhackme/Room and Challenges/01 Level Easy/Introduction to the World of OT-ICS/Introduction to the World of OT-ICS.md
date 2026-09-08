# Introduction to the World of OT/ICS

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `introductiontotheworldofotics` |
| **Link** | [TryHackMe](https://tryhackme.com/room/introductiontotheworldofotics) |
| **Sección** | 01 Level Easy |
| **Fuente** | Redacción oficial de TryHackMe + static-site con HMI interactivo |
| **Componentes** | OT/ICS definitions / PLC / sensors/outputs / HMI / Colonial Pipeline / Safety vs availability / Encryption gaps / IoT/ICS HMI |
| **Impacto** | Puerta de entrada al OT/ICS: entender qué es una planta, cómo controla un PLC un motor, por qué la seguridad del OT prioriza la **availability** y la **safety** sobre la confidencialidad. |

---

**Contexto:** OT = Operational Technology; ICS = Industrial Control Systems. Un PLC (Programmable Logic Controller) recibe datos de **sensors** (input) y envía señales de **output** (p.ej. apagar un motor). Un operador humano interactúa con el PLC desde un **HMI** (Human Machine Interface). El incidente que marcó un punto de inflexión para OT/ICS en 2021 fue **Colonial Pipeline** (después de él los ataques contra OT se duplicaron anualmente). La prioridad de OT es la **safety** (seguridad física de las personas) y la disponibilidad; muchas OT **no usan encryption**, lo que las hace vulnerables a sniffing. El HMI interactivo te sitúa en una planta de procesamiento de agua: sensor al 65%, alerta amarilla al 85%, shut-off al 95%, abrir la válvula de salida → **lowers** el nivel.

## Solucionario

### Task 1: Introducción

**Explicación:** Introducción a la sala y a los conceptos OT/ICS. Sin respuesta requerida.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - let's get started. | `No answer needed` |

### Task 2: Qué es OT/ICS? (What is OT/ICS?)

**Explicación:** **OT (Operational Technology):** hardware y software que detecta o causa cambios a través del monitoreo y/o control de dispositivos físicos/procesos. **ICS (Industrial Control Systems):** término paraguas que engloba SCADA, DCS, PLC, RTU, etc.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What does the **'O'** in OT stand for? | `Operational` |
| 2 | What does the **'C'** in ICS stand for? | `Control` |

### Task 3: Cómo Funciona OT/ICS? (How Does OT/ICS Work?)

**Explicación:** Bucle del PLC: **Sensors** (input) → PLC (logic) → **Outputs** (actuadores, relés) → proceso físico. La conexión que envía la señal de control al mundo real (p.ej. un voltaje a un relay) es una salida **output**; la fuente de datos ambientales que alimenta las entradas del PLC es un **sensor**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | When a PLC needs to send a signal to turn off a motor, it sends a signal through what type of connection? | `Output` |
| 2 | What source provides the environmental data that inputs feed into a PLC? | `Sensor` |

### Task 4: Seguridad OT/ICS (What is OT/ICS Cyber Security?)

**Explicación:** El **HMI (Human Machine Interface)** es la interfaz gráfica que muestra estado, permite control manual y configura alarmas. El incidente de **Colonial Pipeline** (mayo 2021): ransomware que paralizó el oleoducto más grande de EE.UU.; 6 días sin combustible; punto de inflexión de concienciación OT.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What type of system is used by a human operator to interact with a PLC and control a physical process? | `Human Machine Interface (HMI)` |
| 2 | Which **2021 incident** marked a turning point for OT/ICS security? | `Colonial Pipeline` |

### Task 5: Diferencias OT vs IT (Differences Between OT & IT Cyber Security)

**Explicación:** **Safety first:** availability/safety > confidentiality (al revés que en IT). Una parada no programada puede provocar daños físicos, lesiones o muerte. **Sin encryption:** muchos protocolos OT (Modbus, DNP3) originalmente sin cifrado → sniffing y manipulación de tráfico.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the **most important requirement** for OT/ICS cyber security? | `Safety` |
| 2 | What do many OT environments **not leverage**? | `Encryption` |

### Task 6: Lo que ve un Operador (What a Human Operator Sees)

**Explicación:** HMI interactivo (static-site) que te sitúa en una planta de procesamiento de agua (ICS environment). Nivel inicial del tanque: **65%**. Pulsas **START** (bomba) → el nivel sube; al llegar a **85%** aparece un banner amarillo (alerta). Continúas → al llegar a **95%** el sistema **apaga la bomba** (shutdown / interlock). Abres la válvula de salida (**OPEN**) → el nivel **baja** (*lowers*).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Based on a review of the HMI, what **type of environment** is this? | `ICS` (planta de proceso / water processing) |
| 2 | When you first look at the HMI, what is the **current percentage level** indicated by the tank level sensor? | `65` |
| 3 | Click **START** on the pump. At what percentage level do you first receive an alert in a yellow warning banner? | `85` |
| 4 | Continue to allow water to flow. At what percentage level does the control system **shut off the pump**? | `95` |
| 5 | Click **OPEN** on the valve on the outtake pipe. What happens to the water level in the tank? | `Lowers` |

### Task 7: Conclusión

**Explicación:** Cierre de la sala: resumen de los conceptos OT/ICS vistos. Sin respuesta requerida.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - nice job completing the room! | `No answer needed` |

---

**Metodología:**
1. Responder definiciones (T2–T5).
2. Abrir el HMI (static-site T6) y seguir el flujo: START → 65% → 85% (yellow alert) → 95% (shut-off) → OPEN valve → lowers.
3. Marcar respuestas con los porcentajes observados.

**Learning chain:** OT/ICS = Operational Technology + Industrial Control Systems → PLC: sensors (input) → logic → outputs (actuators) → HMI: interfaz del operador humano → prioridad: Safety > Availability > Confidentiality (opuesto a IT) → Colonial Pipeline (2021) punto de inflexión → ataques OT duplicados → muchas OT sin encryption (Modbus/DNP3) → sniffing → HMI interactivo: 65% → 85% (yellow) → 95% (shut-off) → valve → lowers.

**Lección:** *En OT, un botón equivocado puede quemar una planta: la seguridad empieza por entender qué hace cada señal, no por poner antivirus.*

**MITRE ATT&CK (ICS):** T0826 (Loss of Availability), T0831 (Manipulation of Control), T0886 (Remote Services - Engineering Workstations). Causa raíz: CWE-319 (Cleartext transmission of sensitive information).

**Fuente:** [TryHackMe - Introduction to the World of OT/ICS](https://tryhackme.com/room/introductiontotheworldofotics)