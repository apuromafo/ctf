# Weasel

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `weasel` |
| **Link** | [TryHackMe](https://tryhackme.com/room/weasel) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | web exploit / Python processes / privesc / Linux CTF |
| **Impacto** | Explotar una webapp y abusar de procesos/scripts Python elevados para escalar a root |

---

**Contexto:** CTF de Linux que combina la explotación inicial de una aplicación web y el abuso de procesos de Python para comprometer la máquina, obtener las flags de usuario y escalar privilegios hasta root.

## Solucionario

### Task 1: Flags de Usuario y Root / User and Root Flags

**Explicación:**

Enumerando el objetivo y explotando la aplicación web se obtiene una shell inicial en la máquina. Tras identificar y abusar de procesos o scripts de Python con permisos elevados se lee `user.txt` y, tras la escalada, `root.txt`. **user.txt:** `THM{w3as3ls_@nd_pyth0ns}`; **root.txt:** `THM{evelated_w3as3l_l0ngest_boi}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user.txt flag? | `THM{w3as3ls_@nd_pyth0ns}` |
| 2 | What is the root.txt flag? | `THM{evelated_w3as3l_l0ngest_boi}` |

---

**Metodología:**

1. Enumerar el objetivo y explotar la aplicación web para obtener una shell inicial en la máquina.
2. Identificar procesos o scripts de Python con permisos elevados y aprovecharlos (writers/ejecución de código) para escalar privilegios dentro del sistema.
3. Leer `user.txt` y, tras la escalada, `root.txt`.

**Learning chain:** enumeración -> webapp explotada -> shell (www-data/user) -> abuso de procesos Python en ejecución -> user.txt -> privesc (elevated Python) -> root.txt

**Lección:** *Los procesos de Python que corren con permisos elevados son objetivos valiosos para la escalada de privilegios; una librería o script modificable puede convertirse en una puerta directa a root.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application) · T1059.002 (Python) · T1068 (Exploitation for Privilege Escalation) · CWE-732 (Incorrect Permission Assignment)

**Fuente:** [TryHackMe - Weasel](https://tryhackme.com/room/weasel)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
