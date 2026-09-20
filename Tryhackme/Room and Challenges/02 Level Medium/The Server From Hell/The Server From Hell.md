# The Server From Hell
| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Challenge / Boot2Root | theserverfromhell | https://tryhackme.com/room/theserverfromhell | 02 Level Medium | TryHackMe | Linux, enumeración de puertos (reales y falsos), login por red, capabilities (getcap), escalada de privilegios | Compromiso del host "del infierno" desde el puerto 1337 hasta root, con captura de las tres flags |

> **Objeto:** Enfrentarse a un servidor que parece configurado y desplegado por Satanás y escalar privilegios hasta root.

---
**Contexto:** **The Server From Hell** es una sala boot2root de dificultad Media en la que el servidor está deliberadamente plagado de servicios y puertos engañosos. Se arranca desde el puerto **1337** y hay que enumerar hacia delante hasta distinguir los servicios falsos de los reales. Solo el servicio auténtico responderá a los intentos de login, y una vez dentro el camino hasta root pasa por abusar de capabilities mal configuradas (`getcap`). El objetivo es recuperar la flag `flag.txt`, la de usuario y la de root.
> **ES:** Enfréntate a un servidor que parece configurado y desplegado por Satanás. ¿Puedes escalar a root?
> **EN:** Face a server that feels as if it was configured and deployed by Satan himself. Can you escalate to root?

## Solucionario
### Task 1: Hackear el servidor / Hacking the server
**Explicación:** Se comienza la enumeración en el puerto `1337` y se recorren los puertos expuestos. Muchos servicios son falsos ("fake ports") y solo el servicio real responde a los intentos de login; identificarlo permite obtener una shell. Una vez dentro se localiza la flag `flag.txt`, se consigue la de usuario y, abusando de capabilities detectadas con `getcap`, se escala a root para leer la flag final.

Descripción original de la tarea:

> Start at port 1337 and enumerate your way.
> Good luck.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| flag.txt | `thm{h0p3_y0u_l1k3d_th3_f1r3w4ll}` |
| user.txt | `thm{sh3ll_3c4p3_15_v3ry_1337}` |
| root.txt | `thm{w0w_n1c3_3sc4l4t10n}` |

### Tabla de preguntas y respuestas
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | flag.txt | `thm{h0p3_y0u_l1k3d_th3_f1r3w4ll}` |
| 2 | user.txt | `thm{sh3ll_3c4p3_15_v3ry_1337}` |
| 3 | root.txt | `thm{w0w_n1c3_3sc4l4t10n}` |

---
**Metodología:** Enumeración a partir del puerto 1337 → discriminación de servicios falsos frente al real → intento de login en el servicio auténtico → shell inicial → lectura de `flag.txt` y `user.txt` → auditoría de capabilities con `getcap` → escalada a root → `root.txt`.

### Cadena de ataque / Attack Chain
```
Puerto 1337 -> enumeración de puertos (descartar fakes) -> servicio real responde al login
-> shell inicial -> flag.txt + user.txt -> getcap -> abuso de capabilities -> root -> root.txt
```
**Learning chain:** Enumeración → identificación del servicio real → acceso → flags de usuario → auditoría de capabilities → escalada → root.
**Lección:** *Los puertos "falsos" están para despistar; la clave es identificar el servicio real, y las capabilities mal asignadas son un vector habitual de escalada a root.*
**MITRE ATT&CK:** T1046 (Network Service Discovery), T1021 (Remote Services), T1548 (Abuse Elevation Control Mechanism), T1068 (Exploitation for Privilege Escalation), T1005 (Data from Local System).
**Fuente:** [TryHackMe - The Server From Hell](https://tryhackme.com/room/theserverfromhell)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
