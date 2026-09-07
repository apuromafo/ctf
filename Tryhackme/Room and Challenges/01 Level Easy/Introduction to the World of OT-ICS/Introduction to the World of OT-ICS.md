# Introduction to the World of OT/ICS [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough (Free)
* **Slug:** `introductiontotheworldofotics`
* **Link:** https://tryhackme.com/room/introductiontotheworldofotics
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Redacción oficial de TryHackMe + static-site con HMI interactivo
* **Componentes:** OT/ICS definitions · PLC · sensors/outputs · HMI · Colonial Pipeline · Safety vs availability · Encryption gaps · IoT/ICS HMI
* **Impacto rol:** Puerta de entrada al OT/ICS: entender qué es una planta, cómo controla un PLC un motor, por qué la seguridad del OT prioriza la **availability** y la **safety** sobre la confidencialidad.

## Solucionario de Tareas / Task Solutions

> **ES:** OT = Operational Technology; ICS = Industrial Control Systems. Un PLC (Programmable Logic Controller) recibe datos de **sensors** (input) y envía señales de **output** (p.ej. apagar un motor). Un operador humano interactúa con el PLC desde un **HMI** (Human Machine Interface). El incidente que marcó un punto de inflexión para OT/ICS en 2021 fue **Colonial Pipeline** (después de él los ataques contra OT se duplicaron anualmente). La prioridad de OT es la **safety** (seguridad física de las personas) y la disponibilidad; muchas OT **no usan encryption** (encryption), lo que las hace vulnerables a sniffing. El HMI interactivo te sitúa en una planta de procesamiento de agua: sensor al 65%, alerta amarilla al 85%, shut-off al 95%, abrir la válvula de salida → **lowers** el nivel.
> **EN:** OT = Operational Technology; ICS = Industrial Control Systems. A PLC (Programmable Logic Controller) receives **sensor** data (input) and sends **output** signals (e.g. turn off a motor). A human operator interacts with the PLC through an **HMI** (Human Machine Interface). The 2021 incident that marked an inflection point for OT/ICS security was **Colonial Pipeline** (after which OT cyberattacks doubled annually). OT priorities are **safety** (physical safety of people) and availability; many OT environments don't use **encryption**, making them vulnerable to sniffing. The interactive HMI places you in a water processing plant: sensor at 65%, yellow alert at 85%, shut-off at 95%, opening the outtake valve → water level **lowers**.

### Task 1 — Introducción / Introduction

* **Check:** `Let's get started!`

### Task 2 — Qué es OT/ICS? / What is OT/ICS?

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What does the **'O'** in OT stand for? | `Operational` |
| What does the **'C'** in ICS stand for? | `Control` |

* **OT / Operational Technology:** hardware y software que detecta o causa cambios a través del monitoreo y/o control de dispositivos físicos/procesos.
* **ICS / Industrial Control Systems:** término paraguas que engloba SCADA, DCS, PLC, RTU, etc.

### Task 3 — Cómo Funciona OT/ICS? / How Does OT/ICS Work?

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| When a PLC needs to send a signal to turn off a motor, it sends a signal through what type of connection? | `Output` |
| What source provides the environmental data that inputs feed into a PLC? | `Sensor` |

* **PLC loop:** **Sensors** (input) → PLC (logic) → **Outputs** (actuadores, relés) → proceso físico.
* **Output / analog-digital:** la conexión que envía la señal de control al mundo real (p.ej. voltaje a un relay).

### Task 4 — Seguridad OT/ICS / What is OT/ICS Cyber Security?

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What type of system is used by a human operator to interact with a PLC and control a physical process? | `Human Machine Interface (HMI)` |
| Which **2021 incident** marked a turning point for OT/ICS security? | `Colonial Pipeline` |

* **HMI:** interfaz gráfica que muestra estado, permite control manual y configura alarmas.
* **Colonial Pipeline (May 2021):** ransomware que paralizó el oleoducto más grande de EE.UU.; 6 días sin combustible; punto de inflexión de concienciación OT.

### Task 5 — Diferencias OT vs IT / Differences Between OT & IT Cyber Security

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the **most important requirement** for OT/ICS cyber security? | `Safety` |
| What do many OT environments **not leverage**? | `Encryption` |

* **Safety first:** availability/safety > confidentiality (al revés que IT). Una parada no programada puede provocar daños físicos, lesiones o muerte.
* **Sin encryption / Encryption:** muchos protocolos OT (Modbus, DNP3) originalmente sin cifrado → sniffing y manipulación de tráfico.

### Task 6 — Lo que ve un Operador / What a Human Operator Sees *(static-site)*

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Based on a review of the HMI, what **type of environment** is this? | `ICS` (planta de proceso / water processing) |
| When you first look at the HMI, what is the **current percentage level** indicated by the tank level sensor? | `65` |
| Click **START** on the pump. At what percentage level do you first receive an alert in a yellow warning banner? | `85` |
| Continue to allow water to flow. At what percentage level does the control system **shut off the pump**? | `95` |
| Click **OPEN** on the valve on the outtake pipe. What happens to the water level in the tank? | `Lowers` |

* **HMI interactivo / Simulador:** el HMI te sitúa en una planta de procesamiento de agua (ICS environment).
  * Nivel inicial del tanque: **65%**.
  * Pulsas **START** (bomba) → el nivel sube; al llegar a **85%** aparece un banner amarillo (alerta).
  * Continúas → al llegar a **95%** el sistema **apaga la bomba** (shutdown / interlock).
  * Abres la válvula de salida (**OPEN**) → el nivel **baja** (*lowers*).

### Task 7 — Conclusión / Conclusion

* **Check:** `Nice job completing the room!`

## Metodología / Methodology

1. **Paso / Step:** Responder definiciones (T2–T5).
2. **Paso / Step:** Abrir el HMI (static-site T6) y seguir el flujo: START → 65% → 85% (yellow alert) → 95% (shut-off) → OPEN valve → lowers.
3. **Paso / Step:** Marcar respuestas con los porcentajes observados.

### Cadena de aprendizaje / Learning Chain

```
OT/ICS = Operational Technology + Industrial Control Systems
  -> PLC: sensors (input) -> logic -> outputs (actuators)
  -> HMI: interfaz del operador humano
  -> prioridad: Safety > Availability > Confidentiality (opuesto a IT)
  -> Colonial Pipeline (2021) punto de inflexión -> ataques OT duplicados
  ->許多 OT sin encryption (Modbus/DNP3) -> sniffing
  -> HMI interactivo: 65% -> 85% (yellow) -> 95% (shut-off) -> valve -> lowers
```

**Mapeo MITRE ATT&CK:** T0826 (Loss of Availability) · T0831 (Manipulation of Control) · T0886 (Remote Services - Engineering Workstations). Causa raíz: CWE-319 (Cleartext transmission of sensitive information).

**Lección:** *En OT, un botón equivocado puede quemar una planta: la seguridad empieza por entender qué hace cada señal, no por poner antivirus.*

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.