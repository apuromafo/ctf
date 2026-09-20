# Kitty

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Explotación Web | kitty | https://tryhackme.com/room/kitty | 02 Level Medium | TryHackMe | Web, SSTI, RCE, Linux | Ejecución remota de comandos y captura de flags en un host Linux |

---

**Contexto:** La sala **Kitty** es un CTF web en el que una aplicación vulnerable permite inyectar plantillas o contenido procesado por el servidor. Aprovechando la falla de plantillas (template injection) se deduce la versión del framework vulnerable, se consigue **ejecución remota de comandos** y se capturan las flags de usuario. La sala termina con un paso "No answer needed" tras completar la resolución.

## Solucionario

### Task 1: Flags del reto
**Explicación:**

Se enumera la aplicación y se identifica el motor de plantillas vulnerable al inyectar expresiones en la entrada controlada. Se confirma la versión del framework mediante la evaluación de comandos y se obtiene un shell o lectura directa de archivos para capturar las dos flags del sistema.

```bash
# Detección de template injection
# Evaluación de comando para confirmar RCE y leer flags
```

Respuesta:

1. `THM{31e606998972c3c6baae67bab463b16a}`
2. `THM{581bfc26b53f2e167a05613eecf039bb}`

### Task 2: Registro del resultado
**Explicación:**

Se confirma que se ha completado el reto de forma satisfactoria. No requiere respuesta escrita.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag 1 | `THM{31e606998972c3c6baae67bab463b16a}` |
| 1 | Flag 2 | `THM{581bfc26b53f2e167a05613eecf039bb}` |
| 2 | Registro del resultado | `No answer needed` |

---

**Metodología:** Enumeración de la aplicación → detección de template injection → fingerprinting del motor de plantillas → ejecución remota de comandos → lectura de flags.

**Learning chain:** Web vulnerable → inyección en plantillas → RCE → flags.

**Lección:** *Cualquier entrada reflejada y procesada por el servidor de plantillas es candidata a SSTI: detectarla y confirmar la versión del framework permite escalar a RCE en un paso.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1059 Command and Scripting Interpreter · T1055.001 (dyld/plantilla) · T1083 File and Directory Discovery.

**Fuente:** [TryHackMe - Kitty](https://tryhackme.com/room/kitty)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.