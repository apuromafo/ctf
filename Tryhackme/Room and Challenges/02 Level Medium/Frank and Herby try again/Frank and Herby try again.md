# Frank and Herby try again

| **Dificultad** | MEDIUM | **Tipo** | CTF (Free) | **Slug** | `frankandherbytryagain` |
| **Link** | [TryHackMe](https://tryhackme.com/room/frankandherbytryagain) | **Sección** | 02 Level Medium | **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Web Exploitation / Privilege Escalation / CTF | **Impacto** | Evalúa el encadenamiento de explotación web y escalada de privilegios para comprometer un sistema completo |

---

**Contexto:** Frank y Herby vuelven a intentarlo en esta sala CTF de nivel medio. El objetivo es comprometer el sistema, obtener acceso como usuario y escalar privilegios hasta conseguir la flag de root. Frank and Herby try again in this medium-level CTF room. The objective is to compromise the system, gain user access and escalate privileges to obtain the root flag.

## Solucionario

### Task 1: Flags de Usuario y Root

**Explicación:** Se enumera el sistema y se identifican vulnerabilidades web para obtener acceso inicial y conseguir la flag de usuario; después se realiza escalada de privilegios en el sistema para lograr acceso como root y obtener la flag final. En las salas CTF de tipo web es fundamental combinar la explotación de la aplicación accesible con una correcta enumeración del sistema para lograr escalar privilegios y completar la máquina.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | User flag? | `THM{I-2h0uld-f1r3-fr4nK}` |
| 2 | Root Flag? | `THM{frank-and-herby-still-suck}` |

---

**Metodología:**
1. Se enumera el sistema y se identifican vulnerabilidades web para obtener acceso inicial y conseguir la flag de usuario.
2. Se realiza escalada de privilegios en el sistema para lograr acceso como root y obtener la flag final.

**Learning chain:** Reconocimiento y enumeración → Explotación web para acceso inicial → Obtención de user flag → Escalada de privilegios → Obtención de root flag

**Lección:** *En las salas CTF de tipo web es fundamental combinar la explotación de la aplicación accesible con una correcta enumeración del sistema para lograr escalar privilegios y completar la máquina.*

**MITRE ATT&CK:** T1190 - Exploit Public-Facing Application; T1068 - Exploitation for Privilege Escalation

**Fuente:** [TryHackMe - Frank and Herby try again](https://tryhackme.com/room/frankandherbytryagain)