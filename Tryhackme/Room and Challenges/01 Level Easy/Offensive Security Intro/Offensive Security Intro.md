# Offensive Security Intro

| **Dificultad** | Easy |
| **Tipo** | walkthrough |
| **Slug** | `offensivesecurityintrokKx12` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/offensivesecurityintrokKx12) |
| **Sección** | Offensive Security |
| **Fuente** | THM |
| **Componentes** | FakeBank VM, hidden pages, admin attack |
| **Impacto** | Fundamentos ofensivos |

---

**Contexto:** Room introductorio a la seguridad ofensiva donde el usuario ataca un banco falso (FakeBank). Se despliega una máquina virtual, se descubren páginas ocultas con fuzzing, y se explota la página de administración para obtener un flag.

## Solucionario

### Task 1: Think like a Hacker!

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué opción representa simular las acciones de un hacker para encontrar vulnerabilidades? | Offensive Security |

### Task 2: Starting the Lab

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Desplegar la máquina virtual)* | Click en "Start Machine" |

### Task 3: Find Hidden Pages

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Nombre del directorio oculto encontrado | `admin` |

### Task 4: Attack the Admin Page

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el valor del flag? | (requiere máquina en vivo) |

---

**Metodología:** 1) Think like a Hacker - comprender la mentalidad ofensiva; 2) Starting the Lab - desplegar VM FakeBank; 3) Find Hidden Pages - usar gobuster/ffuf para enumerar directorios ocultos; 4) Attack the Admin Page - explotar la página admin para obtener el flag.

**Learning chain:** Mentalidad ofensiva → Despliegue de entorno → Enumeración de superficie de ataque → Explotación de vulnerabilidades

**MITRE ATT&CK:**
- T1595.002 - Active Scanning: Vulnerability Scanning
- T1592.004 - Gather Victim Host Information: Client Configurations
- T1190 - Exploit Public-Facing Application

**Fuente:** [TryHackMe - Offensive Security Intro](https://tryhackme.com/r/room/offensivesecurityintrokKx12)
