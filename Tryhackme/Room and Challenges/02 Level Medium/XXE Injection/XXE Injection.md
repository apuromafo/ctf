# XXE Injection

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough | xxeinjection | https://tryhackme.com/room/xxeinjection | 02 Level Medium | TryHackMe | XXE, XML, Web Security | Explotación de la vulnerabilidad XXE (XML External Entity): In-Band, Out-of-Band y lectura de archivos |

---

**Contexto:** La sala **XXE Injection** explica la vulnerabilidad de inyección de entidades externas XML. El alumno repasa los fundamentos de XML (SGML y DTD), los distintos parsers XML (como DOM Parser) y los dos vectores de ataque principales: XXE In-Band y XXE Out-of-Band. Finalmente se explota la vulnerabilidad en un servicio real para exfiltrar archivos del sistema mediante entidades externas, obteniendo la flag.

## Solucionario

### Task 1: Introducción

**Explicación:**

La sala presenta el concepto de XXE y el contexto de una aplicación que procesa XML de forma insegura.

Respuesta: `No answer needed`

### Task 2: Fundamentos de XML

**Explicación:**

Se repasan los predecesores y bloques de construcción de XML: el lenguaje de marcado generalizado estándar (SGML) y la definición de tipo de documento (DTD).

1. `Standard Generalized Markup Language`
2. `Document Type Definition`

### Task 3: Parser XML

**Explicación:**

Se identifica el parser XML involucrado en el procesamiento de los documentos por parte de la aplicación.

- `DOM Parser`

### Task 4: XXE In-Band

**Explicación:**

Se explota la primera variante de XXE, la In-Band, en la que la respuesta del servidor refleja la entidad externa cargada: el tipo de ataque se confirma como `In-Band XXE` y la flag obtenida es la primera de la sala.

1. `In-Band XXE`
2. `THM{1N_b4Nd_1$_34sYY}`

### Task 5: XXE Out-of-Band

**Explicación:**

Se estudia la segunda variante, la XXE Out-of-Band, en la que la exfiltración se realiza mediante canales externos porque la respuesta del servidor no refleja el contenido.

- `Out-of-Band XXE`

### Task 6: Explotación para exfiltración de archivos

**Explicación:**

Se explota la vulnerabilidad para leer archivos del sistema a través de entidades externas: la flag exfiltrada y el valor numérico asociado a la explotación.

1. `THM{0O8_xx3!!} `
2. `81`

### Task 7: Consideraciones adicionales

**Explicación:**

Se plantean las consideraciones adicionales sobre la explotación de XXE en entornos reales.

Respuesta: `No answer needed`

### Task 8: Conclusión

**Explicación:**

La sala concluye tras conseguir la exfiltración de archivos mediante la vulnerabilidad XXE.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lectura de la introducción | `No answer needed` |
| 2.1 | Lenguaje de marcado generalizado estándar | `Standard Generalized Markup Language` |
| 2.2 | Definición de tipo de documento | `Document Type Definition` |
| 3 | Parser XML | `DOM Parser` |
| 4.1 | Tipo de XXE | `In-Band XXE` |
| 4.2 | Flag de la sala | `THM{1N_b4Nd_1$_34sYY}` |
| 5 | Tipo de XXE alternativo | `Out-of-Band XXE` |
| 6.1 | Flag exfiltrada | `THM{0O8_xx3!!} ` |
| 6.2 | Valor de la explotación | `81` |
| 7 | Consideraciones adicionales | `No answer needed` |
| 8 | Conclusión | `No answer needed` |

---

**Metodología:** Estudio de la vulnerabilidad XXE: fundamentos de XML y DTD, identificación del parser, explotación In-Band con respuesta reflejada, explotación Out-of-Band mediante canales externos y exfiltración de archivos del sistema.

**Learning chain:** XML → SGML/DTD → Parser → In-Band XXE → Out-of-Band XXE → exfiltración → conclusión.

**Lección:** *Un parser XML mal configurado convierte el procesamiento de documentos en una lectura arbitraria de archivos: las entidades externas no deben cargar recursos locales sin validación.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1005 Data from Local System · T1030 Data Transfer Size Limits.

**Fuente:** [TryHackMe - XXE Injection](https://tryhackme.com/room/xxeinjection)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.