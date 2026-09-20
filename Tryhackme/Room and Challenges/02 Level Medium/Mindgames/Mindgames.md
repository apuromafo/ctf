# Mindgames

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Pwn | mindgames | https://tryhackme.com/room/mindgames | 02 Level Medium | TryHackMe | Brainfuck, intérprete vulnerable, ROP, Linux | RCE y captura de ambas flags |

---

**Contexto:** La sala **Mindgames** es un CTF descrito como *"Just a terrible idea..."* cuyo objetivo es *capturar las flags*. El texto original de la sala indica: `https://tryhackme.com/room/mindgames` · *Mindgames — Just a terrible idea...* · `# Mindgames [MEDIUM]` · *Capture the flags* · `Start Machine` · *No hints. Hack it. Don't give up if you get stuck, enumerate harder.* El reto gira en torno a explotar un **intérprete de Brainfuck** mal implementado que permite escribir fuera de los límites de su array y secuestrar el flujo de ejecución para obtener una shell y leer las flags de usuario y de root.

## Solucionario

### Task 1: Flag de usuario
**Explicación:**

Tras enumerar el host, se encuentra un servicio que interpreta código **Brainfuck**. El intérprete permite mover el puntero de datos fuera de los límites del array, otorgando un primitivo de **escritura arbitraria** (`write-what-where`). Con él se corrompe el flujo de control (retorno/pila) y se construye una **ROP chain** para ganar una shell, con la que se lee la flag del usuario.

```text
thm{411f7d38247ff441ce4e134b459b6268}
```

### Task 2: Flag de root
**Explicación:**

Con la misma técnica de explotación del intérprete (o abusando de la ejecución del servicio) se consigue acceso con privilegios y se lee la flag final del sistema.

```text
thm{1974a617cc84c5b51411c283544ee254}
```

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de usuario | `thm{411f7d38247ff441ce4e134b459b6268}` |
| 2 | Flag de root | `thm{1974a617cc84c5b51411c283544ee254}` |

---

**Metodología:** Enumeración del servicio Brainfuck → análisis del intérprete (validación de límites del puntero) → write-what-where → hijack de ejecución con ROP → shell → captura de la flag de usuario → escalada → flag de root.

**Learning chain:** Reconocimiento → identificación del intérprete Brainfuck → abuso del puntero fuera de límites → control del flujo de instrucciones → ROP → shell → escalada → flags.

**Lección:** *Incluso un lenguaje esotérico e inofensivo es una puerta de entrada cuando su intérprete no valida límites; si te atas, enumera más.*

**MITRE ATT&CK:** T1203 Exploitation for Client Execution · T1068 Exploitation for Privilege Escalation.

**Fuente:** [TryHackMe - Mindgames](https://tryhackme.com/room/mindgames)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.