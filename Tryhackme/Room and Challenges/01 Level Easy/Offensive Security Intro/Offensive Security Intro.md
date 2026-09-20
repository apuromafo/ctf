# Offensive Security Intro

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `offensivesecurityintrokKx12` | [TryHackMe](https://tryhackme.com/room/offensivesecurityintrokKx12) | `Offensive Security` | THM | FakeBank VM, hidden pages, admin attack | Fundamentos ofensivos |

> **Objeto:** Atacar un banco ficticio (FakeBank): desplegar la máquina virtual, descubrir páginas ocultas mediante fuzzing y explotar la página de administración para recuperar el flag final.

---

**Contexto:** Room introductorio a la seguridad ofensiva donde el usuario ataca un banco falso (FakeBank). Se despliega una máquina virtual, se descubren páginas ocultas con fuzzing, y se explota la página de administración para obtener un flag.

> **ES:** Room introductorio a la seguridad ofensiva donde el usuario ataca un banco falso (FakeBank). Se despliega una máquina virtual, se descubren páginas ocultas con fuzzing, y se explota la página de administración para obtener un flag.

> **EN:** Introductory offensive security room where the user attacks a fake bank (FakeBank). A virtual machine is deployed, hidden pages are discovered with fuzzing, and the administration page is exploited to obtain a flag.

## Solucionario

### Task 1: Think like a Hacker! / Think like a Hacker!

**Explicación:** Se introduce el concepto de seguridad ofensiva: simular las acciones de un hacker permite encontrar vulnerabilidades en un sistema de forma autorizada y controlada.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué opción representa simular las acciones de un hacker para encontrar vulnerabilidades? | Offensive Security |

### Task 2: Starting the Lab / Starting the Lab

**Explicación:** La tarea consiste en desplegar el entorno de laboratorio: la máquina virtual FakeBank se inicializa pulsando "Start Machine".

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Desplegar la máquina virtual)* | Click en "Start Machine" |

### Task 3: Find Hidden Pages / Find Hidden Pages

**Explicación:** Se enumeran los directorios del servidor web con herramientas de fuzzing (gobuster/ffuf) para descubrir páginas ocultas. El directorio oculto encontrado es `admin`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Nombre del directorio oculto encontrado | `admin` |

### Task 4: Attack the Admin Page / Attack the Admin Page

**Explicación:** Se explota la página de administración para obtener el flag final. El flag requiere la máquina en vivo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el valor del flag? | (requiere máquina en vivo) |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué opción representa simular las acciones de un hacker para encontrar vulnerabilidades? | `Offensive Security` |
| 2 | *(Desplegar la máquina virtual)* | `Click en "Start Machine"` |
| 3 | Nombre del directorio oculto encontrado | `admin` |
| 4 | ¿Cuál es el valor del flag? | `(requiere máquina en vivo)` |

---

**Metodología:** 1) Think like a Hacker - comprender la mentalidad ofensiva; 2) Starting the Lab - desplegar VM FakeBank; 3) Find Hidden Pages - usar gobuster/ffuf para enumerar directorios ocultos; 4) Attack the Admin Page - explotar la página admin para obtener el flag.

### Cadena de ataque / Attack Chain

1. Adopción de la mentalidad ofensiva sobre el objetivo FakeBank.
2. Despliegue del laboratorio y de la máquina virtual.
3. Enumeración de páginas ocultas con fuzzing (gobuster/ffuf) → `admin`.
4. Explotación de la página de administración → flag.

**Learning chain:** Mentalidad ofensiva → Despliegue de entorno → Enumeración de superficie de ataque → Explotación de vulnerabilidades

**Lección:** *La seguridad ofensiva empieza por pensar como un atacante: enumerar la superficie de exposición y explotar el eslabón más débil del sistema es el ciclo completo del compromiso.*

**MITRE ATT&CK:**
- T1595.002 - Active Scanning: Vulnerability Scanning
- T1592.004 - Gather Victim Host Information: Client Configurations
- T1190 - Exploit Public-Facing Application

**Fuente:** [TryHackMe - Offensive Security Intro](https://tryhackme.com/room/offensivesecurityintrokKx12)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.