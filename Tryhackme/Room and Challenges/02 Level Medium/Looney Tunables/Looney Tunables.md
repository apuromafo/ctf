# Looney Tunables

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Teoría / Laboratorio | looneytunables | https://tryhackme.com/room/looneytunables | 02 Level Medium | TryHackMe | CVE-2023-4911, glibc, ld.so, LPE (Linux Privilege Escalation), PoC | Escalada de privilegios local en Linux mediante buffer overflow en glibc |

---

**Contexto:** La sala **Looney Tunables** estudia el CVE-2023-4911, un buffer overflow en el cargador dinámico `ld.so` de glibc explotable localmente para escalar a root en sistemas Linux. Se contextualiza el fallo, se reproducen los pasos de un PoC y se obtiene una flag que confirma la ejecución con privilegios elevados.

## Solucionario

### Task 1: Introducción
**Explicación:**

Se presenta la sala y la vulnerabilidad Looney Tunables (CVE-2023-4911) en el contexto de la escalada de privilegios local en Linux.

1. `No answer needed`

### Task 2: Funcionamiento interno de un exploit / How the exploit works
**Explicación:**

Se explica el funcionamiento interno del cargador dinámico glibc y por qué el overflow permite desencadenar ejecución arbitraria al procesar variables de entorno.

1. `No answer needed`

### Task 3: Preparando el entorno / Preparing the environment
**Explicación:**

Se despliega y verifica el entorno vulnerable sobre el que se lanzará el PoC.

1. `No answer needed`

### Task 4: Desarrollo del exploit / Building the exploit
**Explicación:**

Se compila y prepara el PoC que explota el buffer overflow en `ld.so` para obtener una shell con privilegios elevados.

1. `No answer needed`

### Task 5: Escalada de privilegios / Privilege Escalation
**Explicación:**

Se ejecuta el exploit y, al conseguir la shell como root, se captura la flag de la sala.

1. `THM{TH-TH-THATS-SECURE-FOLKS!}`

### Task 6: Mitigaciones y cierre
**Explicación:**

Se revisan las mitigaciones recomendadas (actualización de glibc) y se cierra la sala.

1. `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tarea de introducción | `No answer needed` |
| 2 | Funcionamiento interno del exploit | `No answer needed` |
| 3 | Preparación del entorno vulnerable | `No answer needed` |
| 4 | Desarrollo del exploit (PoC) | `No answer needed` |
| 5 | Flag obtenida tras escalar a root | `THM{TH-TH-THATS-SECURE-FOLKS!}` |
| 6 | Mitigaciones y cierre | `No answer needed` |

---

**Metodología:** Estudio y reproducción del CVE-2023-4911 (Looney Tunables): comprensión del overflow en el cargador dinámico `ld.so` de glibc, preparación del entorno vulnerable, compilación y ejecución del PoC para obtener una shell root y captura de la flag de confirmación.

**Learning chain:** Introducción → análisis del cargador dinámico (`ld.so`) → preparación del entorno → compilación del PoC → escalada a root → flag → mitigaciones (actualizar glibc).

**Lección:** *Una vulnerabilidad en el cargador dinámico (ld.so) es crítica porque afecta a cualquier binario del sistema: un simple buffer overflow al procesar el entorno puede convertirse en escalada local a root.*

**MITRE ATT&CK:** T1068 Exploitation for Privilege Escalation · T1059 Command and Scripting Interpreter · T1222 File and Directory Permissions Modification (mitigación).

**Fuente:** [TryHackMe - Looney Tunables](https://tryhackme.com/room/looneytunables)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.