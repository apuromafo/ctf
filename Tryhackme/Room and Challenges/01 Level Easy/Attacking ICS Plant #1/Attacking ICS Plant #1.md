# Attacking ICS Plant #1

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `attackingicsplant1` |
| **Link** | [TryHackMe](https://tryhackme.com/room/attackingicsplant1) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Modbus, PLC, holding registers, coil register write, semáforo industrial |
| **Impacto** | Interacción directa con un PLC industrial vía protocolo Modbus: lectura y escritura de registros para manipular los estados de un semáforo. |

---

**Contexto:** La sala introduce los fundamentos de la seguridad en entornos industriales (ICS) y el protocolo **Modbus**, mostrando cómo interactuar con un PLC. Se practican las funciones de lectura y escritura de registros (`read_holding_registers` y `write_register`), se manipulan las coils y registros de un semáforo industrial para cambiar sus estados, y se responde a un reto final sobre los valores de los registros. Cierra con tareas de verificación prácticas sin respuesta numérica.

## Solucionario

### Task 1: Fundamentos industriales / ICS Basics

**Explicación:** Introducción a los sistemas de control industrial, los PLC y el protocolo Modbus, así como el entorno del laboratorio de la planta. Tarea informativa sin respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la introducción a la planta industrial. | `No answer needed` |

### Task 2: Funciones de Modbus / Modbus Functions

**Explicación:** Se enumeran las funciones de Modbus disponibles en el entorno. La lectura de los registros holding se realiza con la función `read_holding_registers`, y la escritura de un valor concreto sobre un registro se efectúa con `write_register`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué función de Modbus permite leer los registros holding? | `read_holding_registers` |
| 2 | ¿Qué función de Modbus permite escribir en un registro? | `write_register` |

### Task 3: Manipulación de registros / Register Manipulation

**Explicación:** Se manipula el semáforo industrial escribiendo secuencialmente sobre sus registros y coils para completar los estados solicitados. Cada respuesta corresponde al valor que debe escribirse en cada paso de la secuencia, incluyendo las señales de color `red` y `green` y los valores binarios de las coils.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Valor de la operación de escritura (paso 1). | `3` |
| 2 | Valor de la operación de escritura (paso 2). | `2` |
| 3 | Valor de la operación de escritura (paso 3). | `3` |
| 4 | Valor de la operación de escritura (paso 4). | `16` |
| 5 | Valor de la operación de escritura (paso 5). | `4` |
| 6 | Valor de la operación de escritura (paso 6). | `0` |
| 7 | Valor de la operación de escritura (paso 7). | `1` |
| 8 | Valor de la operación de escritura (paso 8). | `16` |
| 9 | Valor de la operación de escritura (paso 9). | `2 4` |
| 10 | Valor de la operación de escritura (paso 10). | `1 3` |
| 11 | Color de la señal que debe encenderse en este paso. | `red` |
| 12 | Color de la señal que debe encenderse en este paso. | `green` |
| 13 | Valor de la operación de escritura (paso 13). | `3` |
| 14 | Valor de la operación de escritura (paso 14). | `1` |

### Task 4: Reto final de registros / Final Register Challenge

**Explicación:** Se resuelve el reto final de la planta, en el que se debe confirmar el valor resultante solicitado por la sala tras la manipulación completa de los registros y del estado del semáforo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el valor solicitado al completar el reto de la planta? | `4` |

### Task 5: Verificación final / Final Verification

**Explicación:** Pasos de verificación práctica del estado de la planta tras la manipulación: comprobación de las coils, del funcionamiento esperado del semáforo y del cierre del laboratorio. Tareas sin respuesta numérica.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Verificar el estado del semáforo (paso 1). | `No answer needed` |
| 2 | Verificar el estado del semáforo (paso 2). | `No answer needed` |
| 3 | Verificar el estado del semáforo (paso 3). | `No answer needed` |
| 4 | Verificar el estado del semáforo (paso 4). | `No answer needed` |
| 5 | Verificar el estado del semáforo (paso 5). | `No answer needed` |
| 6 | Verificar el estado del semáforo (paso 6). | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la introducción a la planta industrial. | `No answer needed` |
| 2 | ¿Qué función de Modbus permite leer los registros holding? | `read_holding_registers` |
| 3 | ¿Qué función de Modbus permite escribir en un registro? | `write_register` |
| 4 | Valor de la operación de escritura (paso 1). | `3` |
| 5 | Valor de la operación de escritura (paso 2). | `2` |
| 6 | Valor de la operación de escritura (paso 3). | `3` |
| 7 | Valor de la operación de escritura (paso 4). | `16` |
| 8 | Valor de la operación de escritura (paso 5). | `4` |
| 9 | Valor de la operación de escritura (paso 6). | `0` |
| 10 | Valor de la operación de escritura (paso 7). | `1` |
| 11 | Valor de la operación de escritura (paso 8). | `16` |
| 12 | Valor de la operación de escritura (paso 9). | `2 4` |
| 13 | Valor de la operación de escritura (paso 10). | `1 3` |
| 14 | Color de la señal que debe encenderse en este paso. | `red` |
| 15 | Color de la señal que debe encenderse en este paso. | `green` |
| 16 | Valor de la operación de escritura (paso 13). | `3` |
| 17 | Valor de la operación de escritura (paso 14). | `1` |
| 18 | ¿Cuál es el valor solicitado al completar el reto de la planta? | `4` |
| 19 | Verificar el estado del semáforo (paso 1). | `No answer needed` |
| 20 | Verificar el estado del semáforo (paso 2). | `No answer needed` |
| 21 | Verificar el estado del semáforo (paso 3). | `No answer needed` |
| 22 | Verificar el estado del semáforo (paso 4). | `No answer needed` |
| 23 | Verificar el estado del semáforo (paso 5). | `No answer needed` |
| 24 | Verificar el estado del semáforo (paso 6). | `No answer needed` |

---

**Metodología:**

1. Se comprenden los fundamentos de ICS, PLC y protocolo Modbus dentro del laboratorio de la planta.
2. Se identifican las funciones de Modbus necesarias: `read_holding_registers` para leer y `write_register` para escribir registros.
3. Se inspeccionan los registros holding y las coils del PLC que controlan el semáforo industrial.
4. Se envía la secuencia de escrituras (valores de registros y coils, incluidos `red` y `green`) para llevar el semáforo al estado solicitado.
5. Se resuelve el reto final confirmando el valor resultante.
6. Se verifican prácticamente los estados finales de la planta.

### Cadena de ataque / Attack Chain

```
Fundamentos ICS/Modbus -> PLC de la planta
  -> read_holding_registers (lectura de registros)
  -> write_register (escritura de registros/coils)
  -> Secuencia de estados del semáforo (red / green)
  -> Reto final -> valor de registro resultante
  -> Verificación del estado de la planta
```

**Learning chain:** ICS Basics → Modbus → Funciones de lectura/escritura → Manipulación de registros y coils → Semáforo industrial → Reto final

**Lección:** *El protocolo Modbus carece de autenticación: cualquiera con acceso a la red industrial puede leer y escribir en los registros de un PLC, permitiendo manipular directamente los procesos físicos de una planta.*

**MITRE ATT&CK:** T0855 (Unauthorized Command Message), T0869 (Standard Application Layer Protocol: Modbus), T0882 (Unauthorized Device Control)

**Fuente:** [TryHackMe - Attacking ICS Plant #1](https://tryhackme.com/room/attackingicsplant1)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.