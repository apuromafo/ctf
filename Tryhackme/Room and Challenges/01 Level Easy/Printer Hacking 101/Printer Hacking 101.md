# Printer Hacking 101

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `printerhacking101` | [TryHackMe](https://tryhackme.com/room/printerhacking101) | 01 Level Easy | THM | IPP (631), PJL, Puerto 9100, Buffer Overflow, Seguridad de impresoras | Seguridad de impresoras y dispositivos de red |

---

**Contexto:** Laboratorio de hacking de impresoras: identifica el servicio de impresión (IPP) en el puerto 631 y el acceso directo a la impresora (9100), y recorre la historia real de un ataque que mantiene una conexión abierta a la impresora y la satura con datos para provocar un Buffer Overflow, culminando con la recuperación de contenido desde el lugar del atacante.

> **ES:** Aprende a hackear impresoras: puertos IPP (631) y 9100, abuso del puerto de impresión para saturar el dispositivo y producción de un Buffer Overflow con fines educativos.
> **EN:** Learn to hack printers: IPP (631) and port 9100, abuse of the raw printing port to flood the device and cause a Buffer Overflow for educational purposes.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presenta las impresoras como superficie de ataque y explica por qué suelen estar poco protegidas dentro de las redes corporativas.

1. No answer needed

### Task 2: Puerto de impresión / Printing Port

**Explicación:** Identifica el servicio asociado a la impresión en red (IPP), que corre habitualmente en el puerto 631.

2. 631

### Task 3: El ataque / The Attack

**Explicación:** Narra el ataque real sobre una impresora: el atacante mantiene abierta una conexión al puerto 9100 con un bucle de netcat y envía una gran cantidad de datos (1k) para desbordar el buffer de la impresora y provocar una caída (Buffer Overflow), mientras explota la vulnerabilidad desde su propio sótano (Skidy's basement).

3. 1. while true; do nc printer 9100; done
   2. Buffer Overflow
   3. Skidy's basement
   4. 1k

### Task 4: Cierre / Conclusion

**Explicación:** Resume las lecciones sobre seguridad de impresoras y las medidas de mitigación. No se requiere respuesta.

4. 1. No answer needed
   2. No answer needed

| Pregunta | Respuesta |
|---|---|
| T1: Tarea introductoria sin respuesta | `No answer needed` |
| ¿Qué puerto corre el servicio de impresión IPP? | `631` |
| ¿Qué comando mantiene abierta la conexión a la impresora (puerto 9100)? | `while true; do nc printer 9100; done` |
| ¿Qué tipo de ataque se produce contra la impresora? | `Buffer Overflow` |
| ¿Desde dónde atacó el actor malicioso? | `Skidy's basement` |
| ¿Qué cantidad de datos se envía para saturar la impresora? | `1k` |
| T4: Primer paso de cierre sin respuesta | `No answer needed` |
| T4: Segundo paso de cierre sin respuesta | `No answer needed` |

---

**Metodología:** Reconocimiento de servicios de impresión (IPP/631, raw 9100), mantenimiento de una sesión contra el puerto 9100 con netcat, envío de datos en bucle para saturar el buffer del dispositivo y análisis de un Buffer Overflow real con fines educativos.

### Cadena de ataque / Attack Chain
Escaneo de la red para descubrir la impresora y sus puertos (631, 9100) -> Mantenimiento de la conexión al puerto raw 9100 (while true; do nc printer 9100; done) -> Envío masivo de datos (1k) para desbordar el buffer -> Caída de la impresora por Buffer Overflow -> Explotación remota desde la infraestructura del atacante (Skidy's basement).

**Learning chain:** Puerto IPP 631 y puerto raw de impresión 9100, uso de netcat para interactuar con el dispositivo y origen de los Buffer Overflows en servicios de red.

**Lección:** *El puerto 9100 abierto sin autenticación permite a cualquier actor inundar la impresora y tumbar el dispositivo: los equipos de red deben segmentarse y sus puertos de gestión restringirse.*

**MITRE ATT&CK:** T0883 Modbus/TCP no aplica; afín a T1190 Exploit Public-Facing Application y T0869 (ICS) Standard Application Layer Protocol abuse. Frameworks relevantes: ejercicios de hacking de impresoras (PJL/raw printing) dentro de la categoría de dispositivos IoT/OT.

**Fuente:** [TryHackMe - Printer Hacking 101](https://tryhackme.com/room/printerhacking101)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.