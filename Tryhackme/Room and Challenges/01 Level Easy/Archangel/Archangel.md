# Archangel

| **Dificultad** | Easy |
| **Tipo** | walkthrough |
| **Slug** | `archangel` |
| **Link** | [TryHackMe](https://tryhackme.com/room/archangel) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Virtual Hosting, LFI, LFI to RCE, cron, variables PATH |
| **Impacto** | Compromiso web vía LFI→RCE y doble escalada de privilegios (horizontal por cron y vertical por PATH) |

---

**Contexto:** Room que combina reconocimiento web con Local File Inclusion (LFI) hasta ejecución remota de código. Se resuelve el host virtual (`mafialive.thm`), se explota un LFI derivado en RCE con la flag intermedia y se escala privilegios en dos fases: horizontal abusando de un cron y vertical mediante la manipulación de la variable PATH. El resumen original conserva únicamente las respuestas posicionales, sin los enunciados de las preguntas.

## Solucionario

### Task 1: Despliegue / Deployment

**Explicación:** Se despliega la máquina y se prepara el entorno de ataque.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |

### Task 2: Web exploitation / Explotación web

**Explicación:** Se identifica el host virtual (`mafialive.thm`), se localiza `test.php`, se explota la inclusión local de ficheros (LFI) y se convierte en ejecución remota de código (RCE), obteniendo las flags intermedias.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `mafialive.thm` |
| 2 | *(Pregunta 2 no especificada en el original)* | `thm{f0und_th3_r1ght_h0st_n4m3}` |
| 3 | *(Pregunta 3 no especificada en el original)* | `test.php` |
| 4 | *(Pregunta 4 no especificada en el original)* | `thm{explo1t1ng_lf1}` |
| 5 | *(Pregunta 5 no especificada en el original)* | `thm{lf1_t0_rc3_1s_tr1cky}` |

### Task 3: Escalada de privilegios / Privilege Escalation

**Explicación:** Se escala privilegios en dos fases: horizontal abusando de un cronjob y vertical explotando la variable PATH, obteniendo las dos flags finales.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `thm{h0r1zont4l_pr1v1l3g3_2sc4ll4t10n_us1ng_cr0n}` |
| 2 | *(Pregunta 2 no especificada en el original)* | `thm{p4th_v4r1abl3_expl01tat1ion_f0r_v3rt1c4l_pr1v1l3g3_3sc4ll4t10n}` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Task 1, Pregunta 1 no especificada en el original)* | `No answer needed` |
| 2 | *(Task 2, Pregunta 1 no especificada en el original)* | `mafialive.thm` |
| 3 | *(Task 2, Pregunta 2 no especificada en el original)* | `thm{f0und_th3_r1ght_h0st_n4m3}` |
| 4 | *(Task 2, Pregunta 3 no especificada en el original)* | `test.php` |
| 5 | *(Task 2, Pregunta 4 no especificada en el original)* | `thm{explo1t1ng_lf1}` |
| 6 | *(Task 2, Pregunta 5 no especificada en el original)* | `thm{lf1_t0_rc3_1s_tr1cky}` |
| 7 | *(Task 3, Pregunta 1 no especificada en el original)* | `thm{h0r1zont4l_pr1v1l3g3_2sc4ll4t10n_us1ng_cr0n}` |
| 8 | *(Task 3, Pregunta 2 no especificada en el original)* | `thm{p4th_v4r1abl3_expl01tat1ion_f0r_v3rt1c4l_pr1v1l3g3_3sc4ll4t10n}` |

---

**Metodología:** Reconocimiento web → resolución de host virtual → Local File Inclusion (LFI) → conversión a RCE → escalada horizontal abusando de cron → escalada vertical por PATH hijacking → flags finales.

**Learning chain:** Virtual Hosting → LFI → LFI to RCE → cron abuse → PATH hijacking → privilegios root

**Lección:** *Un LFI no se queda en lectura de archivos: combinado con logs o técnicas de inclusión puede convertirse en RCE, y los permisos sobre cron/PATH son el siguiente eslabón para comprometer la máquina por completo.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059.006 (LFI to RCE), T1053 (Scheduled Task/Job), T1574.007 (PATH Hijacking)

**Fuente:** [TryHackMe - Archangel](https://tryhackme.com/room/archangel)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.