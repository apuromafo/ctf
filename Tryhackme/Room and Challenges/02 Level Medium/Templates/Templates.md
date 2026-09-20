# Templates

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Web | templates | https://tryhackme.com/room/templates | 02 Level Medium | TryHackMe | Inyección de plantillas (SSTI), Motor de templates, Web | Ejecución de código en el lado del servidor (RCE) |

---

**Contexto:** La sala **Templates** es un reto web centrado en la **inyección de plantillas en el servidor (SSTI)**: la aplicación renderiza plantillas procesadas por el backend y acepta entrada sin filtrar. El alumno identifica el motor de plantillas, confirma la evaluación de expresiones y abusa del contexto de plantilla para lograr **ejecución de código** y leer la flag del sistema, que cierra el reto con una única respuesta.

## Solucionario

### Task 1: Flag del reto
**Explicación:**

Explotando la inyección de plantillas se ejecuta código en el contexto de la aplicación y se lee la flag que confirma el acceso al sistema.

Respuesta: `flag{3cfca66f3611059a0dfbc4191a0803b2}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag del reto | `flag{3cfca66f3611059a0dfbc4191a0803b2}` |

---

**Metodología:** Reconocimiento de la aplicación, detección de la entrada procesada por el motor de plantillas, prueba de delimitadores SSTI, exploitation del contexto para ejecutar comandos y lectura de la flag.

**Learning chain:** Reconocimiento → identificación de SSTI → validación del motor → RCE → lectura de la flag.

**Lección:** *Cualquier entrada que el servidor interpole dentro de una plantilla sin sanitizar es un candidato directo a RCE.*

**MITRE ATT&CK:** T1059 Command and Scripting Interpreter · T1190 Exploit Public-Facing Application · T1082 System Information Discovery.

**Fuente:** [TryHackMe - Templates](https://tryhackme.com/room/templates)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.