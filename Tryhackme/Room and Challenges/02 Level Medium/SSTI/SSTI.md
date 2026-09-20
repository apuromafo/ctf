# SSTI

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Ofensivo / Web | ssti | https://tryhackme.com/room/ssti | 02 Level Medium | TryHackMe | SSTI, Jinja2, Flask, Sintaxis de plantillas, Payloads | Ejecución de código arbitrario en el servidor (RCE) |

---

**Contexto:** La sala **SSTI** explica la inyección de plantillas en el servidor (*Server-Side Template Injection*): cómo identificar el motor de plantillas (Flask con **Jinja2**), reconocer los delimitadores de expresión (`{{ }}`) y de comentario (`{#`), descubrir el usuario del servicio (`jake`) y ejecutar operaciones aritméticas dentro de la plantilla como prueba de ejecución. El recorrido se cierra confirmando el payload de cálculo `{{ '7'*7 }}`.

## Solucionario

### Task 1: Bienvenida
**Explicación:**

Se configura el entorno y se confirma el acceso a la aplicación vulnerable, sin respuesta requerida.

Respuesta: `No answer needed`

### Task 2: Sintaxis de expresión
**Explicación:**

Para probar la inyección se identifica el delimitador de expresiones que emplea el motor de plantillas para evaluar contenido (doble llave de apertura).

Respuesta: `{{`

### Task 3: Motor de plantillas
**Explicación:**

El framework empleado por la aplicación usa el motor de plantillas Jinja2.

Respuesta: `Jinja2`

### Task 4: Sintaxis de comentario
**Explicación:**

Se identifica el delimitador de comentarios del motor de plantillas, que sirve para confirmar la sintaxis sin ejecutar código.

Respuesta: `{#`

### Task 5: Usuario del servicio
**Explicación:**

La inyección permite consultar información del sistema operativo y revela el usuario bajo el que corre la aplicación.

Respuesta: `jake`

### Task 6: Confirmación del motor
**Explicación:**

Se comprueba de forma práctica el comportamiento de la plantilla ante la sintaxis identificada, sin respuesta requerida.

Respuesta: `No answer needed`

### Task 7: Validación de ejecución
**Explicación:**

Se valida que la aplicación efectivamente interpreta el contenido delimitado por el motor, sin respuesta requerida.

Respuesta: `No answer needed`

### Task 8: Payload final
**Explicación:**

El payload de cierre ejecuta una operación dentro de la plantilla (multiplicación de cadenas) que demuestra la ejecución de código en el servidor.

Respuesta: `{{ '7'*7 }}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Bienvenida | `No answer needed` |
| 2 | Delimitador de expresiones | `{{` |
| 3 | Motor de plantillas | `Jinja2` |
| 4 | Delimitador de comentarios | `{#` |
| 5 | Usuario del servicio | `jake` |
| 6 | Confirmación del motor | `No answer needed` |
| 7 | Validación de ejecución | `No answer needed` |
| 8 | Payload de cierre | `{{ '7'*7 }}` |

---

**Metodología:** Detección del delimitador de plantillas, fingerprinting del motor (Jinja2/Flask), prueba de comentarios, enumeración de contexto y payload aritmético para confirmar la ejecución de código.

**Learning chain:** Reconocimiento → identificación de SSTI → detección del motor → validación de sintaxis → enumeración → RCE.

**Lección:** *Si la aplicación devuelve el resultado de multiplicar cadenas dentro de `{{ }}`, el motor de plantillas ya es una vía directa hacia ejecución de código.*

**MITRE ATT&CK:** T1059 Command and Scripting Interpreter · T1190 Exploit Public-Facing Application · T1082 System Information Discovery.

**Fuente:** [TryHackMe - SSTI](https://tryhackme.com/room/ssti)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.