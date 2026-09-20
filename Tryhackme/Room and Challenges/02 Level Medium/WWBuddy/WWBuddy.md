# WWBuddy

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough | wwbuddy | https://tryhackme.com/room/wwbuddy | 02 Level Medium | TryHackMe | Android, CTF, Reverse Engineering | Máquina CTF Android con tres stages de flags que requieren burlar la seguridad de la app |

---

**Contexto:** La sala **WWBuddy** presenta una máquina CTF de hacking basada en Android. El reto se divide en tres stages donde el alumno debe interactuar con la aplicación móvil, evitar los controles de seguridad implementados y explotar el entorno de la app para obtener las tres flags consecutivas. Es un ejercicio práctico de análisis de aplicaciones móviles y bypasseo de mecanismos de protección.

## Solucionario

### Task 1: Flags de la máquina

**Explicación:**

Se resuelven los tres stages de la máquina: la primera flag se obtiene al ejecutar correctamente la app, la segunda al superar la validación del entorno/detección, y la tercera al cambiar el entorno de ejecución para engañar a la aplicación.

1. `THM{d0nt_try_4nyth1ng_funny}`
2. `THM{g4d0_d+_kkkk}`
3. `THM{ch4ng3_th3_3nv1r0nm3nt}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Flag del stage 1 | `THM{d0nt_try_4nyth1ng_funny}` |
| 1.2 | Flag del stage 2 | `THM{g4d0_d+_kkkk}` |
| 1.3 | Flag del stage 3 | `THM{ch4ng3_th3_3nv1r0nm3nt}` |

---

**Metodología:** Análisis de la aplicación Android: ejecución de la app, identificación de las validaciones del entorno de ejecución y modificación del entorno para satisfacer los checks que liberan cada flag.

**Learning chain:** Ejecución de la app → primera flag → validación del entorno → segunda flag → cambio de entorno → tercera flag.

**Lección:** *Los checks de entorno de una app son evasibles: comprender qué valida cada stage permite manipular el veredicto de la aplicación.*

**MITRE ATT&CK:** T1204 User Execution · T1059 Command and Scripting Interpreter · T1622 Debugger Evasion.

**Fuente:** [TryHackMe - WWBuddy](https://tryhackme.com/room/wwbuddy)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.