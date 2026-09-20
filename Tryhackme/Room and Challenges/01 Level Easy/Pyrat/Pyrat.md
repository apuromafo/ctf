# Pyrat

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `pyrat` | https://tryhackme.com/room/pyrat | 01 Level Easy | THM | Python code execution, Git repo, SSH, Fuzzing, Privilege escalation | Boot-to-root en servicio web con ejecución Python |

---

**Contexto:** Boot-to-root que explora ejecución de código Python a través de un servicio HTTP vulnerable en el puerto 8000. Mediante enumeración del filesystem, obtención de credenciales de un repositorio Git, login SSH como usuario `think` y fuzzing de un endpoint admin del servicio Python personalizado, se logra escalada a root.

> **ES:** Boot-to-root que explora ejecución de código Python a través de un servicio HTTP vulnerable en el puerto 8000; se combina enumeración, un repositorio Git con credenciales, acceso SSH y la explotación de un endpoint admin para escalar a root.
> **EN:** A boot-to-root exploring Python code execution through a vulnerable HTTP service on port 8000; combines enumeration, a Git repository with credentials, SSH access and exploitation of an admin endpoint to escalate to root.

## Solucionario

### Task 1: Pyrat / Pyrat

**Explicación:** Se conecta al servicio HTTP que ejecuta el input como código Python, se enumeran los archivos del sistema, se extraen credenciales del repositorio de la aplicación, se entra por SSH como `think` y se explota el endpoint admin para conseguir una shell como root.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user.txt flag? | `996bdb1f619a68361417cabca5454705` |
| 2 | What is the root.txt flag? | `ba5ed03e9e74bb98054438480165e221` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user.txt flag? | `996bdb1f619a68361417cabca5454705` |
| 2 | What is the root.txt flag? | `ba5ed03e9e74bb98054438480165e221` |

---

**Metodología:** Identificar el servicio en el puerto 8000 que ejecuta código Python → enumerar el filesystem y la aplicación → inspeccionar el repositorio Git para encontrar credenciales → acceder por SSH como `think` → fuzzing del endpoint admin del servicio → conseguir RCE como root.

### Cadena de ataque / Attack Chain

```text
Conectar al servicio Python (puerto 8000) → ejecutar código Python → enumerar filesystem (bash exec) → revisar repo Git de la aplicación → obtener credenciales SSH → login como think → fuzzing del endpoint admin → explotar el servicio root (eval/super()) → shell root → flags
```

**Learning chain:** Service discovery → Python RCE → Filesystem enumeration → Git credential harvesting → SSH lateral access → Admin endpoint fuzzing → Root shell

**Lección:** *Un servicio que ejecuta input arbitrario como código Python es RCE inmediato; combinado con malas prácticas (credenciales en repos), endpoints de administración sin proteger y servicios corriendo como root, una sola superficie expuesta compromete toda la máquina.*

**MITRE ATT&CK:** T1505.003 (Web Shell), T1552.001 (Credentials In Files), T1613 (Container and Resource Discovery), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Pyrat](https://tryhackme.com/room/pyrat)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.