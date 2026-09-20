# Windows Internals

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough / Conceptos | windowsinternals | https://tryhackme.com/room/windowsinternals | 02 Level Medium | TryHackMe | Procesos, manejadores (handles), memoria, binarias PE, cabeceras PE, volcado de procesos | Comprensión del interior de Windows para análisis de malware y depuración |

---

**Contexto:** La sala **Windows Internals** profundiza en el funcionamiento interno de Windows: anatomía de procesos y manejadores, asignación de memoria, prioridades y estructura de las binarias **PE** (Portable Executable). Los ejercicios piden valores extraídos de un proceso de laboratorio y de su imagen en memoria, incluyendo direcciones de módulos, regiones de memoria y campos concretos de las cabeceras PE, hasta recuperar la flag de la sala.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:**

Presentación de la sala y del proceso de laboratorio que se analizará durante los ejercicios. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 2: Proceso objetivo / Target process
**Explicación:**

Se identifica el proceso de laboratorio y se anotan sus características básicas: identificador, puerto asociado y nivel de prioridad.

1. `No answer needed`
2. `5984`
3. `3412`
4. `High`

### Task 3: Manejadores del proceso / Process handles
**Explicación:**

Se consultan los manejadores (handles) del proceso, anotando los identificadores de los objetos relevantes.

1. `No answer needed`
2. `5908`
3. `6584`

### Task 4: Memoria del proceso / Process memory
**Explicación:**

Se examina el espacio de direcciones del proceso: tamaño de la memoria virtual reservada, directiva de reserva (`increaseuserva`) y la dirección base del módulo principal.

1. `No answer needed`
2. `4 GB`
3. `increaseuserva`
4. `No answer needed`
5. `0x7ff652ec0000`

### Task 5: Regiones de memoria / Memory regions
**Explicación:**

Se recorren las regiones de memoria del proceso para extraer direcciones y tamaños de las secciones y módulos cargados.

1. `No answer needed`
2. `0x7ffd0be20000`
3. `0x1ec000`
4. `51`

### Task 6: Análisis de la binaria PE / PE binary analysis
**Explicación:**

Se inspeccionan las cabeceras de la imagen PE: el stub DOS, la entrada al código y otros campos característicos de la estructura.

1. `No answer needed`
2. `DOS Stub`
3. `No answer needed`
4. `000000014001acd0`
5. `0006`
6. `00024000`
7. `Microsoft.Notepad`

### Task 7: Flag final / Final flag
**Explicación:**

Aplicando los conocimientos de Windows Internals (inyección en procesos y manipulación de la memoria) se obtiene la flag de la sala.

1. `No answer needed`
2. `THM{1Nj3c7_4lL_7H3_7h1NG2}`

### Task 8: Cierre / Conclusion
**Explicación:**

Recapitulación final de los conceptos vistos. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Introducción a Windows Internals | `No answer needed` |
| 2.1 | Pregunta inicial de identificación | `No answer needed` |
| 2.2 | Identificador del proceso | `5984` |
| 2.3 | Puerto asociado al proceso | `3412` |
| 2.4 | Prioridad del proceso | `High` |
| 3.1 | Pregunta inicial de manejadores | `No answer needed` |
| 3.2 | Primer manejador identificado | `5908` |
| 3.3 | Segundo manejador identificado | `6584` |
| 4.1 | Pregunta inicial de memoria | `No answer needed` |
| 4.2 | Tamaño de la memoria virtual | `4 GB` |
| 4.3 | Directiva de reserva de memoria | `increaseuserva` |
| 4.4 | Pregunta intermedia de memoria | `No answer needed` |
| 4.5 | Dirección base del módulo | `0x7ff652ec0000` |
| 5.1 | Pregunta inicial de regiones | `No answer needed` |
| 5.2 | Dirección de la región/módulo | `0x7ffd0be20000` |
| 5.3 | Tamaño de la región | `0x1ec000` |
| 5.4 | Conteo de secciones/regiones | `51` |
| 6.1 | Pregunta inicial del análisis PE | `No answer needed` |
| 6.2 | Bloque inicial que identifica la binaria | `DOS Stub` |
| 6.3 | Pregunta intermedia del análisis PE | `No answer needed` |
| 6.4 | Dirección de entrada (Entry Point) | `000000014001acd0` |
| 6.5 | Valor de cabecera PE | `0006` |
| 6.6 | Valor de alineación/desplazamiento | `00024000` |
| 6.7 | Identificador de la binaria | `Microsoft.Notepad` |
| 7.1 | Pregunta previa a la flag | `No answer needed` |
| 7.2 | Flag de la sala | `THM{1Nj3c7_4lL_7H3_7h1NG2}` |
| 8 | Cierre de la sala | `No answer needed` |

---

**Metodología:** Análisis estático y dinámico de un proceso Windows de laboratorio: inspección de procesos/manejadores con herramientas del sistema, examen de memoria virtual y directivas (increaseuserva), y análisis de la estructura PE (stub DOS, entry point y campos de cabecera) para relacionar cada valor con su artefacto interno.

**Learning chain:** Proceso objetivo → identificadores y prioridad → manejadores → espacio de direcciones → regiones de memoria → estructura PE → inyección/manipulación → flag.

**Lección:** *Conocer la anatomía de procesos, memoria y cabeceras PE permite interpretar cualquier binaria Windows sin depender de cajas negras de análisis.*

**MITRE ATT&CK:** T1055 Process Injection · T1036 Masquerading · T1059 Command and Scripting Interpreter · T1105 Ingress Tool Transfer · T1012 Query Registry.

**Fuente:** [TryHackMe - Windows Internals](https://tryhackme.com/room/windowsinternals)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.