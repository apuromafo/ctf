# Git and Crumpets

| **Dificultad** | MEDIUM | **Tipo** | CTF (Free) | **Slug** | `gitandcrumpets` |
| **Link** | [TryHackMe](https://tryhackme.com/room/gitandcrumpets) | **Sección** | 02 Level Medium | **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Git Exposure / Web Exploitation / Privilege Escalation / CTF | **Impacto** | Evalúa cómo explotar repositorios Git expuestos para filtrar credenciales y escalar privilegios |

---

**Contexto:** Esta sala CTF está centrada en el abuso de repositorios Git expuestos como vector de ataque. El objetivo es explotar información sensible filtrada por un repositorio para obtener acceso de usuario y luego escalar a root. This CTF room focuses on abusing exposed Git repositories as an attack vector. The objective is to exploit sensitive information leaked by a repository to obtain user access and then escalate to root.

## Solucionario

### Task 1: Flags de Usuario y Root

**Explicación:** Se identifica un repositorio Git expuesto en la aplicación web y se extrae información sensible (código, historial, credenciales) para obtener acceso inicial como usuario. Se utiliza la información filtrada para escalar privilegios y lograr acceso como root, obteniendo la flag final. Los repositorios Git expuestos en servidores web pueden filtrar historial, código fuente y credenciales. Es crucial proteger el directorio .git y asegurarse de que los metadatos de desarrollo no queden accesibles públicamente.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | User Flag | `thm{fd7ab9ffd409064f257cd70cf3d6aa16}` |
| 2 | Root Flag | `thm{6320228dd9e315f283b75887240dc6a1}` |

---

**Metodología:**
1. Se identifica un repositorio Git expuesto en la aplicación web y se extrae información sensible (código, historial, credenciales) para obtener acceso inicial como usuario.
2. Se utiliza la información filtrada para escalar privilegios y lograr acceso como root, obteniendo la flag final.

**Learning chain:** Enumeración web → Detección de repositorio Git expuesto → Extracción de código e historial → Recuperación de credenciales → Acceso inicial (user flag) → Escalada de privilegios → Root flag

**Lección:** *Los repositorios Git expuestos en servidores web pueden filtrar historial, código fuente y credenciales. Es crucial proteger el directorio .git y asegurarse de que los metadatos de desarrollo no queden accesibles públicamente.*

**MITRE ATT&CK:** T1190 - Exploit Public-Facing Application; T1552 - Unsecured Credentials; T1068 - Exploitation for Privilege Escalation

**Fuente:** [TryHackMe - Git and Crumpets](https://tryhackme.com/room/gitandcrumpets)