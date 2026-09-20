# Content Security Policy

| Campo | Valor |
|---|---|
| Dificultad | Medium |
| Tipo | CTF |
| Slug | contentsecuritypolicy |
| Link | https://tryhackme.com/room/contentsecuritypolicy |
| Sección | 02 Level Medium |
| Fuente | TryHackMe |
| Componentes | CSP, XSS, headers, seguridad web |
| Impacto | Comprensión y bypass de políticas de seguridad de contenido |

---

**Contexto:** Content Security Policy es una sala de TryHackMe de dificultad media que enseña sobre las Políticas de Seguridad de Contenido (CSP) y su rol en la mitigación de XSS. Cubre directivas como script-src, media-src, report-uri, el uso de hashes SHA para scripts inline, y técnicas de bypass como JSONP, CDN y data URIs para exfiltrar datos.

## Solucionario

### Task 1: Introducción a CSP

**Explicación:** Se identificó qué es CSP, por qué es importante contra XSS y cómo se implementa mediante headers.

1. Content Security Policy
2. XSS
3. header

### Task 2: Directivas CSP

**Explicación:** Se reconocieron las directivas principales: script-src para scripts, media-src para multimedia y report-uri para reportes de violaciones.

1. script-src
2. media-src
3. report-uri

### Task 3: Configuración de directivas

**Explicación:** Se configuraron directivas CSP con unsafe-eval y script-src 'none' para restringir ejecución de código.

1. 'unsafe-eval'
2. script-src 'none'

### Task 4: Hashes y validación

**Explicación:** Se utilizó SHA como algoritmo para hashear scripts inline y se validó su correcto funcionamiento.

1. SHA
2. Yes

### Task 5: Verificación

**Explicación:** Se verificó que la política CSP estaba correctamente implementada.

Yes

### Task 6: Tarea adicional

**Explicación:** Tarea adicional sin respuesta requerida.

No answer needed

### Task 7: Flags de bypass CSP

**Explicación:** Se completaron todas las flags de bypass de CSP utilizando técnicas como JSONP, CDN, audio, imágenes, style y fuentes de datos.

1. THM{Th4t_W4s_Pr3tty_3asy}
2. THM{Us1ng_data:_1snt_Any_S4fer}
3. THM{Th4ts_N0t_4n_1m4ge!!}
4. THM{Style_Y0ur_W3bs1teS}
5. THM{N0_JSONP_D0mains_Plz}
6. THM{Trust_N0_CDN}
7. THM{Th1s_4udio_S0unds_N1ce}

### Task 8: Flags avanzadas

**Explicación:** Se obtuvieron las flags avanzadas de bypass de CSP mediante técnicas de inyección y control de fuentes externas.

1. THM{N0_0utside_S0urces}
2. THM{M4k3_Sure_Y0ur_N0nce_1s_R4ndom}
3. THM{Hash_Y0ur_1nl1ne_Scr1pts}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Introducción a CSP | `Content Security Policy`, `XSS`, `header` |
| 2 | Directivas CSP | `script-src`, `media-src`, `report-uri` |
| 3 | Configuración | `'unsafe-eval'`, `script-src 'none'` |
| 4 | Hashes y validación | `SHA`, `Yes` |
| 5 | Verificación | `Yes` |
| 6 | Tarea adicional | `No answer needed` |
| 7 | Flag bypass 1 | `THM{Th4t_W4s_Pr3tty_3asy}` |
| 7 | Flag bypass 2 | `THM{Us1ng_data:_1snt_Any_S4fer}` |
| 7 | Flag bypass 3 | `THM{Th4ts_N0t_4n_1m4ge!!}` |
| 7 | Flag bypass 4 | `THM{Style_Y0ur_W3bs1teS}` |
| 7 | Flag bypass 5 | `THM{N0_JSONP_D0mains_Plz}` |
| 7 | Flag bypass 6 | `THM{Trust_N0_CDN}` |
| 7 | Flag bypass 7 | `THM{Th1s_4udio_S0unds_N1ce}` |
| 8 | Flag avanzada 1 | `THM{N0_0utside_S0urces}` |
| 8 | Flag avanzada 2 | `THM{M4k3_Sure_Y0ur_N0nce_1s_R4ndom}` |
| 8 | Flag avanzada 3 | `THM{Hash_Y0ur_1nl1ne_Scr1pts}` |

---

**Metodología:** Estudio de directivas CSP, análisis de configuraciones, bypass mediante JSONP/CDN/audio/estilos y validación con hashes SHA.

**Learning chain:** Concepto de CSP → directivas principales → configuración → hashes SHA → bypass con JSONP → bypass con CDN → bypass con audio/estilos → flags avanzadas.

**Lección:** *Una política CSP mal configurada puede ser bypassada mediante técnicas creativas como JSONP, CDN y elementos multimedia, por lo que debe auditarse exhaustivamente.*

**MITRE ATT&CK:** T1189 - Drive-by Compromise, T1059.007 - JavaScript

**Fuente:** [TryHackMe - Content Security Policy](https://tryhackme.com/room/contentsecuritypolicy)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.