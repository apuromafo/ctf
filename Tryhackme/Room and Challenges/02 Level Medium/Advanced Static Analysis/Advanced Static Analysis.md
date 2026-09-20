# Advanced Static Analysis

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Malware Analysis | advancedstaticanalysis | https://tryhackme.com/room/advancedstaticanalysis | 02 Level Medium | TryHackMe | x32dbg, PE, Process Injection, Malware | Análisis y detección de muestras maliciosas |

---

**Contexto:** La sala **Advanced Static Analysis** entrena el análisis manual de binarios maliciosos con un debugger (x32dbg/Immunity Debugger) y herramientas de análisis estático. El alumno identifica arquitectura del binario, secciones, llamadas a funciones de la API de Windows (MessageBoxA, WriteProcessMemory), flujo de control con condiciones y estructuras de datos, y desentraña una técnica avanzada de **process injection** (hollowing) descubriendo el inyector, el proceso objetivo y las rutas involucradas. Todas las respuestas salen de leer el código y la memoria del ejecutable, sin ejecutarlo.

## Solucionario

### Task 1: Preparación del laboratorio
**Explicación:**

Se configura el entorno de análisis con el debugger y se abren las muestras del desafío.

Respuesta: `No answer needed`

### Task 2: Arquitectura del binario
**Explicación:**

Se responde si la muestra está compilada para arquitectura de 64 bits, resultado negativo (`nay`): el binario es de 32 bits.

Respuesta: `nay`

### Task 3: Estructura del ejecutable
**Explicación:**

Se inspeccionan las secciones del binario y se anota la cantidad de secciones presentes en el PE.

1. `No answer needed`
2. `5`

### Task 4: Funciones de la API
**Explicación:**

Se identifican las llamadas críticas a la API de Windows en el flujo del programa: el número de veces que se invoca una función de mensajería, la función llamada (**MessageBoxA**) y la dirección de memoria donde se ubica la llamada.

1. `1`
2. `MessageBoxA`
3. `1`
4. `004073d7`

### Task 5: Análisis del flujo de control
**Explicación:**

Se sigue el flujo condicional del programa: se extrae la cadena ofuscada del binario, el tamaño de la estructura utilizada, la dirección del comparador, el mensaje que se muestra y la dirección de la condición.

1. `_ITs_Fun_to_Learn_at_THM_`
2. `4`
3. `00401543`
4. `This program demonstrates if-else statement`
5. `00401509`

### Task 6: Valores de memoria
**Explicación:**

Se leen valores concretos desde la memoria del proceso durante el debugging (valor marcador en hexadecimal).

1. `0x00000004`
2. `No answer needed`

### Task 7: Técnicas de ofuscación
**Explicación:**

Se analiza el uso de técnicas de anti-análisis/ofuscación presentes en la muestra.

Respuesta: `No answer needed`

### Task 8: Función clave del inyector
**Explicación:**

Se identifica la función de la API encargada de escribir la carga maliciosa en el proceso remoto durante el hollowing.

Respuesta: `WriteProcessMemory()`

### Task 9: Análisis del proceso de inyección
**Explicación:**

Se desmonta paso a paso la técnica de **process hollowing**: el hash de la muestra, los contadores de hilos/secciones y las direcciones y nombres de cada fase (proceso legítimo `iexplore.exe`, inyección de `evil.exe`, rutas y la llamada a `NtUnmapViewOfSection`).

1. `e60a461b80467a4b1187ae2081f8ca24`
2. `2`
3. `0040108f`
4. `iexplore.exe`
5. `004010f0`
6. `evil.exe`
7. `00401101`
8. `NtUnmapViewOfSection`
9. `2`
10. `C:\Users\THM-Attacker\Desktop\Injectors\evil.exe`

### Task 10: Conclusión
**Explicación:**

Se consolidan las conclusiones del análisis estático de la muestra.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Preparación del laboratorio | `No answer needed` |
| 2 | ¿El binario es de 64 bits? | `nay` |
| 3.1 | Denominación descriptiva previa al conteo | `No answer needed` |
| 3.2 | Número de secciones del PE | `5` |
| 4.1 | Veces que se invoca la función de mensajería | `1` |
| 4.2 | Función de la API invocada | `MessageBoxA` |
| 4.3 | Segundo contador de llamadas | `1` |
| 4.4 | Dirección de la llamada | `004073d7` |
| 5.1 | Cadena ofuscada extraída | `_ITs_Fun_to_Learn_at_THM_` |
| 5.2 | Tamaño de la estructura | `4` |
| 5.3 | Dirección del comparador | `00401543` |
| 5.4 | Mensaje mostrado por el programa | `This program demonstrates if-else statement` |
| 5.5 | Dirección de la condición | `00401509` |
| 6.1 | Valor marcador en memoria | `0x00000004` |
| 6.2 | Valor adicional de memoria | `No answer needed` |
| 7 | Técnicas de anti-análisis | `No answer needed` |
| 8 | Función clave del proceso de inyección | `WriteProcessMemory()` |
| 9.1 | Hash de la muestra | `e60a461b80467a4b1187ae2081f8ca24` |
| 9.2 | Primer contador de procesos | `2` |
| 9.3 | Dirección de la primera fase | `0040108f` |
| 9.4 | Proceso legítimo objetivo | `iexplore.exe` |
| 9.5 | Dirección de la segunda fase | `004010f0` |
| 9.6 | Carga maliciosa inyectada | `evil.exe` |
| 9.7 | Dirección de la tercera fase | `00401101` |
| 9.8 | Llamada que descarta la imagen original | `NtUnmapViewOfSection` |
| 9.9 | Segundo contador | `2` |
| 9.10 | Ruta absoluta del inyector | `C:\Users\THM-Attacker\Desktop\Injectors\evil.exe` |
| 10 | Conclusión del análisis | `No answer needed` |

---

**Metodología:** Análisis estático de malware asistido por debugger: inspección de secciones PE, seguimiento del flujo de control, lectura de strings y memoria, y desmontaje de una cadena de process hollowing (supervisión de la API de Windows).

**Learning chain:** Arquitectura → estructura PE → APIs utilizadas → flujo condicional → lectura de memoria → ofuscación → process injection → síntesis de la muestra.

**Lección:** *El debugger es un microscopio: avanzando instrucción a instrucción se reconstruye la intención completa de un binario sin necesidad de ejecutarlo.*

**MITRE ATT&CK:** T1055 Process Injection · T1622 Debugger Evasion · T1027 Obfuscated Files or Information.

**Fuente:** [TryHackMe - Advanced Static Analysis](https://tryhackme.com/room/advancedstaticanalysis)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.