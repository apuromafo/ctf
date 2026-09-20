# Tempus Fugit Durius

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Reto CTF | tempusfugitdurius | https://tryhackme.com/room/tempusfugitdurius | 03 Level Hard | TryHackMe | Escalada de privilegios, flag de usuario y de root | Alto |

---

**Contexto:**
> **ES:** Sala CTF en la que el objetivo es obtener una shell inicial, capturar la flag del usuario (Ben Clower) y elevar privilegios para rootear la máquina, entregando la flag de root.
> **EN:** CTF room in which the goal is to get an initial shell, capture the user flag (Ben Clower) and escalate privileges to root the box, submitting the root flag.

## Solucionario

### Task 1: Banderas del reto / Challenge flags
**Explicación:**
Contenido original de la tarea:

```text
1. 1. THM{Nice_Work_Got_Ben_Clower}
   2. THM{Great_work!_You_Rooted_TempusFugitDurius!}
```

### Preguntas y Respuestas / Questions and Answers

| Task | Respuesta / Answer |
|---|---|
| 1.1 | `THM{Nice_Work_Got_Ben_Clower}` |
| 1.2 | `THM{Great_work!_You_Rooted_TempusFugitDurius!}` |

---

**Metodología:**
1. Enumeración del entorno y localización del vector de entrada.
2. Obtención de una shell inicial y captura de la flag del usuario Ben Clower: `THM{Nice_Work_Got_Ben_Clower}`.
3. Enumeración de privilegios para escalar a root.
4. Rooteo de la máquina y captura de la flag de root: `THM{Great_work!_You_Rooted_TempusFugitDurius!}`.

### Cadena de ataque / Attack Chain
```text
Enumeración -> Shell inicial -> User flag -> Escalada de privilegios -> Root flag
```

**Learning chain:**
Enumeración -> Shell -> User flag -> Escalada -> Root flag.

**Lección:** *Rootear una máquina no es un salto sino una cadena: la escalada casi siempre se apoya en lo que la enumeración reveló antes.*

**MITRE ATT&CK:**
- T1190 Exploit Public-Facing Application
- T1068 Exploitation for Privilege Escalation
- T1059 Command and Scripting Interpreter

**Fuente:** [TryHackMe - Tempus Fugit Durius](https://tryhackme.com/room/tempusfugitdurius)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.