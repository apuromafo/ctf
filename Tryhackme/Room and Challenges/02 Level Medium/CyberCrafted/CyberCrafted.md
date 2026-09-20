# CyberCrafted

| Campo | Valor |
|-------|-------|
| **Dificultad** | Medium |
| **Tipo** | CTF / Web + PrivEsc |
| **Slug** | cybercrafted |
| **Link** | https://tryhackme.com/room/cybercrafted |
| **Sección** | 02 Level Medium |
| **Fuente** | TryHackMe |
| **Componentes** | Web Enumeration, SQL Injection, File Upload, Privilege Escalation, Minecraft |
| **Impacto** | Alto — Cadena completa de ataque desde reconocimiento web hasta root |

---

**Contexto:** CyberCrafted es una máquina que combina enumeración web, inyección SQL, subida de archivos y escalada de privilegios. Incluye un servidor web con tienda online, un juego Minecraft vinculado y múltiples vectores de explotación que conducen a la obtención de flags en cada fase.

## Solucionario

### Task 1: Reconocimiento inicial

**Explicación:** Se identifica el lenguaje/framework del servidor web.

1. Go

### Task 2: Explotación completa

**Explicación:** Se realiza la cadena completa de ataque: enumeración de directorios, explotación de SQLi, obtención de credenciales, acceso a servicios internos y escalada de privilegios.

2. 1. 3
   2. minecraft
   3. admin store www
   4. search.php
   5. xXUltimateCreeperXx
   6. THM{bbe315906038c3a62d9b195001f75008}
   7. THM{ba93767ae3db9f5b8399680040a0c99e}
   8. LoginSystem
   9. THM{b4aa20aaf08f174473ab0325b24a45ca}
   10. THM{8bb1eda065ceefb5795a245568350a70}

### Task 3: Cierre

**Explicación:** Pregunta final de la sala.

3. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lenguaje del servidor | `Go` |
| 2.1 | Número de directorios | `3` |
| 2.2 | Servicio encontrado | `minecraft` |
| 2.3 | Directorio admin | `admin store www` |
| 2.4 | Endpoint vulnerable | `search.php` |
| 2.5 | Usuario | `xXUltimateCreeperXx` |
| 2.6 | Flag web | `THM{bbe315906038c3a62d9b195001f75008}` |
| 2.7 | Flag SQLi | `THM{ba93767ae3db9f5b8399680040a0c99e}` |
| 2.8 | Sistema de login | `LoginSystem` |
| 2.9 | Flag escalate | `THM{b4aa20aaf08f174473ab0325b24a45ca}` |
| 2.10 | Flag root | `THM{8bb1eda065ceefb5795a245568350a70}` |
| 3 | Cierre | `No answer needed` |

---

**Metodología:** Enumeración de directorios → Identificación de endpoints → Explotación de SQLi → Obtención de credenciales → Acceso a servicios internos → Escalada de privilegios.

**Learning chain:** Directory busting → SQL injection → Credential extraction → Internal service access → Privilege escalation → Root flag

**Lección:** *Una cadena de ataque completa demuestra que la seguridad es tan fuerte como su eslabón más débil.*

**MITRE ATT&CK:**
- T1190 — Exploit Public-Facing Application
- T1078 — Valid Accounts
- T1068 — Exploitation for Privilege Escalation

**Fuente:** [TryHackMe - CyberCrafted](https://tryhackme.com/room/cybercrafted)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.