# Super Secret TIp

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Ofensivo / Web | supersecrettip | https://tryhackme.com/room/supersecrettip | 02 Level Medium | TryHackMe | LFI, Local File Inclusion, Cronjobs, cURL, PHP | Lectura de archivos sensibles y ejecución con cron sin autenticación |

---

**Contexto:** La sala **Super Secret TIp** explota una **Local File Inclusion (LFI)**: leyendo archivos sensibles del servidor se obtiene la primera flag y se descubren las rutas y parámetros internos de la aplicación (incluido un valor numérico de tiempo/fecha). El siguiente eslabón es un **cronjob** que ejecuta `curl` contra un archivo controlado por el atacante, permitiendo combinar entrada de archivo con `curl` para lograr la segunda flag, ya con ejecución en el servidor comprometido.

## Solucionario

### Task 1: Cadena LFI → cronjob + cURL
**Explicación:**

Se abusa de la inclusión local para leer la primera flag y extraer el valor numérico del entorno (fecha/parámetro interno). Después se identifica el trabajo programado (`cronjob`) que invoca `curl`, y se abusa de esa combinación (archivo de entrada + `curl`) para conseguir la flag final.

1. `THM{LFI_1s_Pr33Ty_Aw3s0Me_1337}`
2. `110920001386`
3. `THM{cronjobs_F1Le_iNPu7_cURL_4re_5c4ry_Wh3N_C0mb1n3d_t0g3THeR}`

### Task 2: Cierre
**Explicación:**

La práctica se da por concluida sin requerir respuesta adicional.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Flag de la LFI | `THM{LFI_1s_Pr33Ty_Aw3s0Me_1337}` |
| 1.2 | Valor numérico obtenido del entorno | `110920001386` |
| 1.3 | Flag de la combinación cronjob + curl | `THM{cronjobs_F1Le_iNPu7_cURL_4re_5c4ry_Wh3N_C0mb1n3d_t0g3THeR}` |
| 2 | Tarea de cierre | `No answer needed` |

---

**Metodología:** Enumeración de la aplicación, detección y explotación de LFI para leer archivos locales, análisis del cronjob invocando `curl`, envenenamiento/control del archivo de entrada y captura de la flag con ejecución indirecta.

**Learning chain:** Reconocimiento web → LFI → lectura de código y configuración → descubrimiento del cronjob → abuso de `curl` → flag final.

**Lección:** *Un cronjob que ejecuta `curl` sobre un archivo controlable (LFI o upload) es un RCE en diferido: cualquier cron es superficie de escalada si consume entrada del atacante.*

**MITRE ATT&CK:** T1185 Browser Session Hijacking (no aplica) · T1005 Data from Local System · T1059 Command and Scripting Interpreter · T1053 Scheduled Task/Job.

**Fuente:** [TryHackMe - Super Secret TIp](https://tryhackme.com/room/supersecrettip)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.