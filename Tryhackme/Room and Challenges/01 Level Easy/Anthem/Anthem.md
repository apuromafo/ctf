# Anthem

| **Dificultad** | Easy |
| **Tipo** | walkthrough |
| **Slug** | `anthem` |
| **Link** | [TryHackMe](https://tryhackme.com/room/anthem) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Enumeración web, Umbraco CMS, metadatos HTML, credenciales, explotación de CMS |
| **Impacto** | Obtención de flags vía reconocimiento web, metadatos y acceso al CMS Umbraco |

---

**Contexto:** Room de amenaza WEB centrado en la enumeración de un sitio construido sobre Umbraco: se descubren los puertos del servicio, se identifican el CMS, el dominio y personajes a partir del contenido y metadatos, se obtienen flags ocultas en comentarios/metadatos y se finaliza explotando el CMS para obtener la shell y las banderas restantes. El resumen original conserva únicamente las respuestas posicionales, sin los enunciados de las preguntas.

## Solucionario

### Task 1: Reconocimiento del sitio / Website Reconnaissance

**Explicación:** Se reconocen los puertos web abiertos, se identifica el CMS (Umbraco), el dominio (`anthem.com`) y los datos personales expuestos (Solomon Grundy, `SG@anthem.com`), junto con la contraseña encontrada.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |
| 2 | *(Pregunta 2 no especificada en el original)* | `80` |
| 3 | *(Pregunta 3 no especificada en el original)* | `3389` |
| 4 | *(Pregunta 4 no especificada en el original)* | `UmbracoIsTheBest!` |
| 5 | *(Pregunta 5 no especificada en el original)* | `Umbraco` |
| 6 | *(Pregunta 6 no especificada en el original)* | `anthem.com` |
| 7 | *(Pregunta 7 no especificada en el original)* | `Solomon Grundy` |
| 8 | *(Pregunta 8 no especificada en el original)* | `SG@anthem.com` |

### Task 2: Metadatos y flags / Metadata & Flags

**Explicación:** Se revisan los metadatos y comentarios del sitio web para recuperar las flags ocultas en el contenido.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `THM{L0L_WH0_US3S_M3T4}` |
| 2 | *(Pregunta 2 no especificada en el original)* | `THM{G!T_G00D}` |
| 3 | *(Pregunta 3 no especificada en el original)* | `THM{L0L_WH0_D15}` |
| 4 | *(Pregunta 4 no especificada en el original)* | `THM{AN0TH3R_M3TA}` |

### Task 3: Explotación del CMS / CMS Exploitation

**Explicación:** Se explota el CMS Umbraco para obtener acceso a la máquina, se recoge la flag de usuario y se escala hasta obtener la flag final `THM{Y0U_4R3_1337}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |
| 2 | *(Pregunta 2 no especificada en el original)* | `THM{N00T_NO0T}` |
| 3 | *(Pregunta 3 no especificada en el original)* | `ChangeMeBaby1MoreTime` |
| 4 | *(Pregunta 4 no especificada en el original)* | `THM{Y0U_4R3_1337}` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Task 1, Pregunta 1 no especificada en el original)* | `No answer needed` |
| 2 | *(Task 1, Pregunta 2 no especificada en el original)* | `80` |
| 3 | *(Task 1, Pregunta 3 no especificada en el original)* | `3389` |
| 4 | *(Task 1, Pregunta 4 no especificada en el original)* | `UmbracoIsTheBest!` |
| 5 | *(Task 1, Pregunta 5 no especificada en el original)* | `Umbraco` |
| 6 | *(Task 1, Pregunta 6 no especificada en el original)* | `anthem.com` |
| 7 | *(Task 1, Pregunta 7 no especificada en el original)* | `Solomon Grundy` |
| 8 | *(Task 1, Pregunta 8 no especificada en el original)* | `SG@anthem.com` |
| 9 | *(Task 2, Pregunta 1 no especificada en el original)* | `THM{L0L_WH0_US3S_M3T4}` |
| 10 | *(Task 2, Pregunta 2 no especificada en el original)* | `THM{G!T_G00D}` |
| 11 | *(Task 2, Pregunta 3 no especificada en el original)* | `THM{L0L_WH0_D15}` |
| 12 | *(Task 2, Pregunta 4 no especificada en el original)* | `THM{AN0TH3R_M3TA}` |
| 13 | *(Task 3, Pregunta 1 no especificada en el original)* | `No answer needed` |
| 14 | *(Task 3, Pregunta 2 no especificada en el original)* | `THM{N00T_NO0T}` |
| 15 | *(Task 3, Pregunta 3 no especificada en el original)* | `ChangeMeBaby1MoreTime` |
| 16 | *(Task 3, Pregunta 4 no especificada en el original)* | `THM{Y0U_4R3_1337}` |

---

**Metodología:** Enumeración web y de puertos → identificación del CMS Umbraco y del dominio → revisión de metadatos y comentarios para flags → explotación del CMS → shell y escalada → banderas finales.

**Learning chain:** Reconocimiento → fingerprinting de CMS → metadatos HTML → credenciales → exploit de Umbraco → recogida de banderas

**Lección:** *El contenido visible (metadatos, comentarios, nombres) es tan valioso como el código: muchas banderas y credenciales se esconden en la capa de información, no en la de explotación.*

**MITRE ATT&CK:** T1083 (File and Directory Discovery), T1190 (Exploit Public-Facing Application), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - Anthem](https://tryhackme.com/room/anthem)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.