# Obfuscation Principles

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough | obfuscationprinciples | https://tryhackme.com/room/obfuscationprinciples | 02 Level Medium | TryHackMe | Obfuscación de malware, ofuscación de datos y de flujo de control, code stubs, técnicas anti-malware | Comprender los principios de ofuscación que usa el malware (datos, flujo de código y control, stubs) y cómo aplicarlos para evadir herramientas de detección y análisis. |

---

**Contexto:** La sala **Obfuscation Principles** introduce los fundamentos de la ofuscación de software aplicada al malware. Cubre la ofuscación por capas (nivel de ofuscación y su relación con la legibilidad del código), la ofuscación de **datos** y de **código y control**, las **code stubs**, el flujo de código y lógica, y la eliminación de información identificable. Se presentan 9 tareas que combinan teoría con ejercicios prácticos (respuestas hash de tipo THM{}).

> **ES:** Room que enseña los principios de ofuscación usados por el malware: capas, ofuscación de datos, flujo de código y control, stubs y eliminación de metadata identificable.
> **EN:** A room teaching the obfuscation principles used by malware: layers, data obfuscation, code/control flow, stubs, and stripping identifiable information.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación de la sala: se define el concepto de ofuscación y se presentan los temas que se verán a lo largo de las tareas (capas, datos, código/control, stubs). No hay pregunta que responder.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Indica que leíste la introducción (sin respuesta requerida). | `No answer needed` |

### Task 2: Ofuscación en Capas / Layered Obfuscation
**Explicación:** La ofuscación puede aplicarse en varias capas y cada capa adicional reduce la legibilidad del código. La **Layered Obfuscation Taxonomy** se compone de **4 capas** o sub-capas principales, y la sub-capa que engloba los **identificadores sin significado** es **Obfuscating Layout**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many core layers make up the Layered Obfuscation Taxonomy? / ¿Cuántas capas principales componen la taxonomía de ofuscación por capas? | `4` |
| 2 | What sub-layer of the Layered Obfuscation Taxonomy encompasses meaningless identifiers? / ¿Qué sub-capa engloba los identificadores sin significado? | `Obfuscating Layout` |

### Task 3: Ofuscación de Datos / Data Obfuscation
**Explicación:** La ofuscación de datos esconde la información que el malware localiza y exfiltra en el sistema de la víctima. **Data Splitting** rompe o divide un objeto en fragmentos, mientras que **Data Procedurization** reescribe datos estáticos con una llamada a procedimiento (se generan proceduralmente en tiempo de ejecución).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What obfuscation method will break or split an object? / ¿Qué método de ofuscación rompe o divide un objeto? | `Data Splitting` |
| 2 | What obfuscation method is used to rewrite static data with a procedure call? / ¿Qué método reescribe datos estáticos con una llamada a procedimiento? | `Data Procedurization` |

### Task 4: Práctica / Practice
**Explicación:** Ejercicio práctico de aplicación de las técnicas anteriores. La flag obtenida al **subir un fragmento correctamente ofuscado** es `THM{koNC473n473_4Ll_7H3_7H1n95}` (leet speak de "concatenate all the things").

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What flag is found after uploading a properly obfuscated snippet? / ¿Qué flag se obtiene tras subir un fragmento correctamente ofuscado? | `THM{koNC473n473_4Ll_7H3_7H1n95}` |

### Task 5: Ofuscación de Código y Control / Code and Control Obfuscation
**Explicación:** Las instrucciones basura (junk code) reciben el nombre de **Code Stubs**. La capa de ofuscación que confunde al analista manipulando el flujo de código y los árboles sintácticos abstractos es **Obfuscating Controls**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What are junk instructions referred to as in junk code? / ¿Cómo se llaman las instrucciones basura del junk code? | `Code Stubs` |
| 2 | What obfuscation layer aims to confuse an analyst by manipulating the code flow and abstract syntax trees? / ¿Qué capa de ofuscación confunde al analista manipulando el flujo de código? | `Obfuscating Controls` |

### Task 6: Flujo de Código y Lógica / Code Flow and Logic
**Explicación:** Se discuten técnicas que afectan a la ejecución del flujo. La pregunta teórica de la tarea es de verdadero/falso (T/F) y la respuesta es **T** (verdadero: un cambio en la lógica puede impactar en el flujo de control de un programa).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Can logic change and impact the control flow of a program? (T/F) / ¿Puede un cambio de lógica impactar en el flujo de control de un programa? (T/F) | `T` |

### Task 7: Patrones de Flujo de Control Arbitrarios / Arbitrary Control Flow Patterns
**Explicación:** Se amplía el concepto de ofuscación del flujo de control mediante patrones arbitrarios (bifurcaciones opacas, código muerto, saltos confusos). La flag obtenida al **revertir correctamente** el fragmento proporcionado es `THM{D3cod3d!!!}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What flag is found after properly reversing the provided snippet? / ¿Qué flag se obtiene tras revertir correctamente el fragmento? | `THM{D3cod3d!!!}` |

### Task 8: Protección y Eliminación de Info Identificable / Protecting and Stripping Identifiable Information
**Explicación:** Para dificultar el análisis, el malware elimina o protege la información que le identifica (nombres de archivo, autor, claves de compilación, rutas). La flag que se obtiene al **subir un fragmento correctamente ofuscado** es `THM{Y0Ur_1NF0_15_M1N3}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What flag is found after uploading a properly obfuscated snippet? / ¿Qué flag se obtiene tras subir un fragmento correctamente ofuscado? | `THM{Y0Ur_1NF0_15_M1N3}` |

### Task 9: Resumen / Summary
**Explicación:** Cierre de la sala; se repasan todas las técnicas vistas: capas de ofuscación, ofuscación de datos, stubs, flujo de control y eliminación de metadata.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Repasa los principios de ofuscación vistos en la sala (sin respuesta requerida). | `No answer needed` |

### Tabla unificada de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Task 1) Introducción a la sala. | `No answer needed` |
| 2 | (Task 2) How many core layers make up the Layered Obfuscation Taxonomy? | `4` |
| 3 | (Task 2) Sub-layer that encompasses meaningless identifiers. | `Obfuscating Layout` |
| 4 | (Task 3) Obfuscation method that breaks or splits an object. | `Data Splitting` |
| 5 | (Task 3) Method used to rewrite static data with a procedure call. | `Data Procedurization` |
| 6 | (Task 4) Flag after uploading a properly obfuscated snippet. | `THM{koNC473n473_4Ll_7H3_7H1n95}` |
| 7 | (Task 5) Junk instructions referred to as in junk code. | `Code Stubs` |
| 8 | (Task 5) Layer that confuses the analyst by manipulating code flow and ASTs. | `Obfuscating Controls` |
| 9 | (Task 6) Can logic change and impact the control flow of a program? (T/F) | `T` |
| 10 | (Task 7) Flag after properly reversing the provided snippet. | `THM{D3cod3d!!!}` |
| 11 | (Task 8) Flag after uploading a properly obfuscated snippet. | `THM{Y0Ur_1NF0_15_M1N3}` |
| 12 | (Task 9) Resumen de la sala. | `No answer needed` |

---

**Metodología:** Estudio teórico de referencia (obfuscation.xyz y referencias de la sala) → identificación de la técnica aplicada en cada muestra → aplicación práctica de la ofuscación por capas → cálculo/extracción de las flag de los ejercicios → repaso de técnicas anti-detección.

**Learning chain:** conceptos de ofuscación por capas → ofuscación de datos (splitting, procedurización) → ofuscación de código y control (stubs) → flujo de código y lógica → patrones de flujo de control arbitrarios → stripping de información identificable.

**Lección:** *La ofuscación no crea funciones nuevas: esconde las existentes para retrasar el análisis y la detección, equilibrándola siempre contra la legibilidad que el autor necesita conservar.*

**MITRE ATT&CK:** T1027 (Obfuscated Files or Information) · T1027.002 (Software Packing) · T1027.009 (Embedded Payloads) · T1027.010 (Command Obfuscation) · T1036 (Masquerading) · T1053 (Scheduled Task/Job).

**Fuente:** [TryHackMe - Obfuscation Principles](https://tryhackme.com/room/obfuscationprinciples)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.