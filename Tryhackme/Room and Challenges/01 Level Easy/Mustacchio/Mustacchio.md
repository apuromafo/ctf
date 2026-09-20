# Mustacchio

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough (boT2root) | `mustacchio` | https://tryhackme.com/room/mustacchio | 01 Level Easy | TryHackMe | Reconocimiento web / explotación / escalada de privilegios / hashes/flag | Boot2root de nivel Easy: comprometer la máquina Mustacchio y recuperar las dos respuestas finales de la sala. |

---

**Contexto:** Sala tipo boot2root del catálogo de TryHackMe. El objetivo es comprometer la máquina Mustacchio, combinando enumeración web, explotación y escalada de privilegios. El registro de esta migración conserva únicamente las dos respuestas finales del recorrido (dos hashes de 32 caracteres en formato MD5).

> **ES:** Enumerar, explotar y escalar en la máquina Mustacchio para recuperar las dos respuestas finales.
> **EN:** Enumerate, exploit and escalate on the Mustacchio box to retrieve the two final answers.

## Solucionario

### Task 1: Flags de la máquina / Machine flags

**Explicación:** La última fase del reto entrega dos respuestas con formato de hash MD5 (32 caracteres hex), correspondientes a las fases de usuario y root del recorrido. Se conservan verbatim.

Contenido original de la tarea / Original task content:

```text
1. 1. 62d77a4d5f97d47c5aa38b3b2651b831
   2. 3223581420d906c4dd1a5f9b530393a5
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Primera respuesta final / First final answer | `62d77a4d5f97d47c5aa38b3b2651b831` |
| 2 | Segunda respuesta final / Second final answer | `3223581420d906c4dd1a5f9b530393a5` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Primera respuesta final / First final answer | `62d77a4d5f97d47c5aa38b3b2651b831` |
| 2 | Segunda respuesta final / Second final answer | `3223581420d906c4dd1a5f9b530393a5` |

---

**Metodología:** Recorrer las fases clásicas de un boot2root: reconocimiento y enumeración del objetivo, explotación para conseguir acceso, escalada de privilegios hasta obtener los privilegios máximos y captura de las respuestas finales.

### Cadena de ataque / Attack Chain

```text
Reconocimiento -> enumeración web -> explotación -> acceso inicial -> escalada de privilegios -> respuestas finales (62d77a4d... / 3223581...)
```

**Learning chain:** Enumeración -> acceso inicial -> escalada de privilegios -> captura de las respuestas finales.

**Lección:** *Completar un boot2root exige encadenar enumeración, explotación y escalada; registrar cada respuesta intermedia evita perder pistas que dan acceso a la siguiente fase.* 

**MITRE ATT&CK:** T1059 (Command and Scripting Interpreter), T1068 (Exploitation for Privilege Escalation), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - Mustacchio](https://tryhackme.com/room/mustacchio)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.