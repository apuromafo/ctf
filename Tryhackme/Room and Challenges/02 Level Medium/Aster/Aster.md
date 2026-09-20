# Aster

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Explotación | aster | https://tryhackme.com/room/aster | 02 Level Medium | TryHackMe | Asterisk, SIP/VOIP, Java, Reversing | Compromiso del host vía PBX y reversing Java |

---

**Contexto:** La sala **Aster** es un CTF que combina explotación de un servicio **Asterisk (PBX/VOIP)** con retos de ingeniería inversa en **Java**. La primera parte explota una vulnerabilidad conocida del servidor de telefonía para ganar acceso a la máquina; la segunda exige descomponer una aplicación Java para descubrir la lógica que oculta la flag final. Las respuestas documentan cada flag obtenida en las dos etapas.

## Solucionario

### Task 1: Explotación del servicio Asterisk
**Explicación:**

Se enumera la máquina y se identifica el servicio **Asterisk** expuesto. Se explota una vulnerabilidad del PBX (inyección/evaluación de código en el dialplan) para ejecutar comandos en el servidor y obtener la primera flag.

Respuesta: `thm{bas1c_aster1ck_explotat1on}`

### Task 2: Reversing de la aplicación Java
**Explicación:**

Se descarga y descompila la aplicación **Java** entregada al final del compromiso. Analizando el bytecode (decompilador Java y depuración de la lógica de autenticación), se recupera la credeencial/flujo que libera la flag final.

Respuesta: `thm{fa1l_revers1ng_java}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de la explotación de Asterisk | `thm{bas1c_aster1ck_explotat1on}` |
| 2 | Flag del reversing de Java | `thm{fa1l_revers1ng_java}` |

---

**Metodología:** Enumeración de servicios, explotación de vulnerabilidad en Asterisk/PBX (RCE), ingeniería inversa de una aplicación Java (descompilación del bytecode) y captura de flags.

**Learning chain:** Reconocimiento → fingerprint del PBX → explotación de Asterisk → acceso → reversing Java → flag final.

**Lección:** *Los servicios PBX/VOIP reciben menos atención que web y AD, pero un dialplan inseguro es tan RCE como cualquier otro endpoint.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1059 Command and Scripting Interpreter · T1587 Develop Capabilities (reversing) · T1068 Exploitation for Privilege Escalation.

**Fuente:** [TryHackMe - Aster](https://tryhackme.com/room/aster)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.