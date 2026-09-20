# Obscure

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF | obscure | https://tryhackme.com/room/obscure | 02 Level Medium | TryHackMe | FTP anónimo, ingeniería inversa de binarios, deserialización pickle, evasión de defensas, pivoting / red interna | Compromiso completo de la máquina: acceso inicial vía FTP anónimo e ingeniería inversa de un binario, explotación de una deserialización insegura (pickle) y escalada/flag de root. |

---

**Contexto:** La sala **Obscure** es un reto CTF de dificultad media cuyo nombre y diseño giran en torno a la ocultación de pistas. El camino comienza con un **FTP anónimo** que expone un archivo de texto y un binario; la **ingeniería inversa** del binario (strings, desensamblado) revela credenciales y una API oculta. La explotación inicial aprovecha una **deserialización insegura de pickle** y requiere eludir restricciones del entorno. Las tres flag del reto (initial, user y root) se distribuyen a lo largo de la cadena de compromiso.

> **ES:** CTF medio centrado en la ocultación: FTP anónimo, ingeniería inversa, deserialización pickle, evasión de defensas y movimiento lateral por la red interna.
> **EN:** A medium CTF focused on hiding: anonymous FTP, reverse engineering, pickle deserialization, defence evasion, and lateral movement through the internal network.

## Solucionario

### Task 1: Flag Inicial / Initial Flag
**Explicación:** El acceso inicial combina FTP anónimo, análisis del binario expuesto (que revela el funcionamiento de la API) y la explotación de la aplicación web. Tras eludir las comprobaciones de la aplicación se alcanza la primera flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the initial flag? / ¿Cuál es la flag inicial? | `THM{1243b64a3a01a8732ccb96217f593520}` |

### Task 2: Flag de Usuario / User Flag
**Explicación:** Con una shell inicial en el objetivo se enumera el sistema y se abusa de una **deserialización insegura de pickle** (payload que se ejecuta al deserializarse) para ganar ejecución como un usuario distinto o profundizar en el compromiso, obteniendo la flag de usuario.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the user flag? / ¿Cuál es la flag de usuario? | `THM{43b0b68ba2755dd6cac3b8bf5454db94}` |

### Task 3: Flag de Root / Root Flag
**Explicación:** La última fase escala privilegios o pivota dentro de la red interna (la máquina interactúa con un servicio en la red interna, p. ej. sobre el puerto 4444, como apunta la cadena de movimientos laterales del reto). El compromiso total entrega la flag de root.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the root flag? / ¿Cuál es la flag de root? | `THM{8bbc6221d009576d37e28acdd9da7aba}` |

### Tabla unificada de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the initial flag? / ¿Cuál es la flag inicial? | `THM{1243b64a3a01a8732ccb96217f593520}` |
| 2 | What's the user flag? / ¿Cuál es la flag de usuario? | `THM{43b0b68ba2755dd6cac3b8bf5454db94}` |
| 3 | What's the root flag? / ¿Cuál es la flag de root? | `THM{8bbc6221d009576d37e28acdd9da7aba}` |

---

**Metodología:** Reconocimiento (Nmap, FTP sin credenciales) → análisis del binario con strings/desensamblador → identificación de credenciales y API oculta → explotación de la deserialización pickle con payload ejecutable → evasión de las comprobaciones de la app → shell en el objetivo → enumeración y escalada → flag de root.

**Learning chain:** FTP anónimo → RE del binario → credenciales → abuso de la API → pickle deserialization → RCE → escalada de privilegios → compromiso total.

**Lección:** *Los datos que llegan de fuentes no confiables no deben deserializarse nunca de forma automática: una entrada controlada convierte la deserialización en ejecución remota de código.*

**MITRE ATT&CK:** T1046 (Network Service Discovery) · T1190 (Exploit Public-Facing Application) · T1055 (Process Injection) · T1203 (Exploitation for Client Execution) · T1059.006 (Python) · T1068 (Exploitation for Privilege Escalation) · T1027 (Obfuscated Files or Information).

**Fuente:** [TryHackMe - Obscure](https://tryhackme.com/room/obscure)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.