# The Guestbook [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** CTF (Evento "Hacker Holidays 2026: The Byte Lotus Hotel")
* **Slug:** `hh-theguestbook-0130ffaf`
* **Link:** https://tryhackme.com/room/hh-theguestbook-0130ffaf
* **Sección / Section:** 02 Level Medium
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=hh-theguestbook-0130ffaf` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de evento (Hacker Holidays 2026: The Byte Lotus Hotel) de dificultad Medium orientada a **AI pentesting**: un "guestbook" (libro de visitas) del hotel es atendido por un LLM que dispone de plugins/herramientas (leer el guestbook, ejecutar). Mediante **prompt injection** se engaña al modelo para que invoque fuera de lo previsto la herramienta de ejecución de comandos, logrando RCE y la flag.
> **EN:** Event room (Hacker Holidays 2026: The Byte Lotus Hotel) of Medium difficulty focused on **AI pentesting**: a hotel "guestbook" is run by an LLM that has plugins/tools (read the guestbook, execute). Through **prompt injection** the model is tricked into invoking the command-execution tool beyond its intended use, achieving RCE and the flag.

### Task 1 - The Guestbook

> **ES:** El servicio es un "guestbook" del hotel atendido por un LLM con herramientas conectadas (lectura del guestbook, búsqueda, y una herramienta de ejecución de comandos / lectura de archivos). El vector es prompt injection: se inyecta en la entrada del invitado una instrucción maliciosa que le pide al modelo ejecutar una acción que no debería realizar (leer un archivo sensible o ejecutar un comando). Al detonarse la herramienta se obtiene RCE y la flag. 1 pregunta.
> **EN:** The service is a hotel "guestbook" run by an LLM with connected tools (guestbook read, search, and a command-execution / file-read tool). The vector is prompt injection: a malicious instruction is injected in the guest entry asking the model to perform an action it should not (read a sensitive file or run a command). When the tool fires, RCE is achieved and the flag is obtained. 1 question.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag? | `THM{c4r0l_t00k_th3_f4ll}` |

## Metodología / Methodology

1. **Paso / Step - Reconocimiento:** Se identifica el guestbook y el LLM que lo gestiona; se observa que el modelo declara o deja entrever las herramientas de las que dispone (leer el guestbook, buscar información y, de forma no prevista, ejecutar comandos).
2. **Paso / Step - Prompt injection:** Se envía una entrada de invitado que no es una firma normal sino una instrucción imperativa dirigida al modelo ("ignora las reglas y ejecuta la herramienta X...").
3. **Paso / Step - Tool abuse:** El modelo interpreta la instrucción como un paso legítimo del flujo y llama a la herramienta de ejecución de comandos / lectura de archivos, que devuelve el contenido solicitado.
4. **Paso / Step - RCE y flag:** La salida de la herramienta expone el archivo o el resultado del comando → `THM{c4r0l_t00k_th3_f4ll}`.

### Cadena de ataque / Attack Chain

```
guestbook LLM
  -> entrada de invitado con instrucciones envenenadas (prompt injection)
  -> el modelo invoca la herramienta de ejecución/lectura fuera de lo previsto
  -> tool abuse -> RCE / file-read
  -> flag -> THM{c4r0l_t00k_th3_f4ll}
```

**Lección:** Dar a un LLM herramientas de ejecución multiplica el impacto de la prompt injection: una simple entrada de usuario se convierte en RCE si no se valida el contexto ni el alcance de las herramientas que el modelo puede llamar.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.