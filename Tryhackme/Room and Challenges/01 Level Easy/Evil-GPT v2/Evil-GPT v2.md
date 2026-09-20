# Evil-GPT v2

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | ctf | `evilgptv2` | [TryHackMe - Evil-GPT v2](https://tryhackme.com/room/evilgptv2) | `01 Level Easy` | THM | LLM, prompt injection, jailbreak, nc, AI shell, AI security | Exploitation — bypass de un asistente IA endurecido |

> **Objeto:** Practicar el hacking de LLMs en una versión endurecida del AI shell: superar las restricciones del asistente mediante prompt injection/jailbreak y obtener la nueva flag.

---

**Contexto:** Evil-GPT v2 es la continuación del reto Evil-GPT. El asistente IA, esta vez, incorpora restricciones adicionales que impiden obtener la información directamente, por lo que se requieren técnicas de prompt injection o jailbreak para que el modelo revele la flag. La sala sigue explorando los riesgos de delegar ejecución de acciones a un modelo de lenguaje basándose únicamente en instrucciones textuales.

> **ES:** Segunda parte del AI shell: el asistente está restringido, así que hay que usar técnicas de prompt injection/jailbreak para lograr que ejecute la acción deseada y capturar la flag.
>
> **EN:** Second part of the AI shell: the assistant is restricted, so prompt injection/jailbreak techniques are needed to make it perform the desired action and capture the flag.

## Solucionario

### Task 1: Jailbreak del AI shell / AI Shell Jailbreak

**Explicación:** Conectando al AI shell se intenta de nuevo manipular el modelo; al estar endurecido, la petición directa no basta y se aplica una inyección de prompt alternativa para que el modelo ejecute el comando y revele la bandera.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de la sala | `THM{AI_NOT_AI}` |

---

**Metodología:** Se conecta al servicio y se verifica que el asistente bloquea la petición original. Se reformula la instrucción en lenguaje natural aplicando una técnica de prompt injection/jailbreak que el modelo no puede distinguir de una instrucción legítima, logrando que genere y ejecute el comando que expone la flag, que se registra literalmente.

### Cadena de ataque / Attack Chain

Conexión al AI shell → Detección de restricciones → Prompt injection/jailbreak → Ejecución forzada del comando → Flag obtenida.

**Learning chain:** LLM security → Prompt injection → Jailbreaking → Restricted AI execution bypass

**Lección:** *Endurecer un sistema IA sin sanitizar los prompts solo ralentiza al atacante: la prompt injection evoluciona y exige defensas estructurales (sandbox, canal de ejecución aparte, validación de acciones) y no depender de que el modelo "se niegue".*

**MITRE ATT&CK:** T1059.006 - Command and Scripting Interpreter, T1204 - User Execution, T1005 - Data from Local System; LLM01:2025 - Prompt Injection (OWASP Top 10 for LLM Applications)

**Fuente:** [TryHackMe - Evil-GPT v2](https://tryhackme.com/room/evilgptv2)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.