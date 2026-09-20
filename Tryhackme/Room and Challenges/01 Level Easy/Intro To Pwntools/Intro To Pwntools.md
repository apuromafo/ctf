# Intro To Pwntools

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `introtopwntools` | [TryHackMe](https://tryhackme.com/room/introtopwntools) | 01 Level Easy | TryHackMe | pwntools, Buffer Overflow, GDB, checksec, cyclic, ASLR, Shellcode, Exploit Development | Fundamentos de explotación de binarios con pwntools: análisis con checksec/GDB, buffer overflows, explotación local y remota, ASLR y captura de flags |

> **Objeto:** Aprender a usar pwntools para explotar binarios vulnerables: comprobar protecciones con checksec, generar patrones con cyclic, depurar con GDB, desbordar el stack, explotar binarios locales y remotos por red, y evadir ASLR con shellcode e NOP sled.

---

**Contexto:** Sala de pwn que enseña la librería pwntools paso a paso: comprobaciones de protecciones (FULL RELRO, RWX segments, NX, PIE, canary) con checksec, causa de buffer overflows en intro2pwn1/intro2pwn2 (Stack Smashing y Segmentation Fault), explotación de intro2pwn3 con cyclic y canary ausente para romper el binario local (usuario dizmas), explotación del servicio remoto en el puerto 1337 (con stack canary presente), y el binario final sin NX que requiere romper ASLR con cyclic, NOP sled y shellcode execve para obtener root y la flag.

> **ES:** Sala de pwn: pwntools, checksec, GDB, cyclic, buffer overflows, explotación local/remota y evasión de ASLR con shellcode.
> **EN:** Pwn room: pwntools, checksec, GDB, cyclic, buffer overflows, local/remote exploitation and ASLR bypass with shellcode.

## Solucionario

### Task 1: Configuración / Setup
**Explicación:** Preparación del entorno de trabajo: instalación de pwntools y comprobaciones iniciales de la sala.

1. No answer needed
2. No answer needed

### Task 2: Fundamentos / Fundamentals
**Explicación:** Se comprueban las protecciones de los binarios con checksec y se analiza qué ocurre al provocar un buffer overflow: se detecta Stack Smashing en intro2pwn1 y un Segmentation Fault en intro2pwn2.

1. Y
2. N
3. N
4. Y
5. Stack Smashing
6. Segmentation Fault

### Task 3: Primer exploit / First Exploit
**Explicación:** Se explota intro2pwn3 de forma local: se identifica al usuario dueño de las flags (dizmas), la protección ausente (canary), el patrón de letras 0x4a4a4a4a (JJJJ), la salida de "cyclic 12" (aaaabaaacaaa), el valor en hex con el que se sobrescribe el EIP (0x6161616a) y se obtiene la flag.

1. dizmas
2. canary
3. JJJJ
4. aaaabaaacaaa
5. 0x6161616a
6. No answer needed
7. flag{13@rning_2_pwn!}

### Task 4: Explotación remota / Network Exploitation
**Explicación:** Se explota el servicio remoto serve_test en el puerto 1337: se comprueba si tiene stack canary (Y), se interactúa con el servicio y se captura la flag del exploit remoto por red.

1. 1337
2. Y
3. No answer needed
4. flag{n3tw0rk!ng_!$_fun}

### Task 5: Evasión de ASLR / Bypassing ASLR
**Explicación:** Se explota el binario final (intro2pwnFinal) sin NX: se define ASLR (address space layout randomization), el dueño del binario (root), si NX está activada (N), el patrón que rellena el EIP (taaa), la señal al romper el breakpoint fuera de gdb (Trace/breakpoint trap), la función del shellcode (execve), el usuario obtenido (root) y la flag final.

1. address space layout randomization
2. root
3. N
4. taaa
5. Trace/breakpoint trap
6. execve
7. root
8. flag{pwn!ng_!$_fr33d0m}

### Task 6: Conclusión / Conclusion
**Explicación:** Cierre de la sala.

No answer needed

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1.1 | Comprobación inicial de la sala | `No answer needed` |
| 1.2 | Comprobación inicial de la sala | `No answer needed` |
| 2.1 | ¿Tiene intro2pwn1 FULL RELRO? (Y/N) | `Y` |
| 2.2 | ¿Tiene intro2pwn1 segmentos RWX? (Y/N) | `N` |
| 2.3 | ¿Tiene intro2pwn2 stack canary? (Y/N) | `N` |
| 2.4 | ¿Intro2pwn2 no tiene PIE? (Y/N) | `Y` |
| 2.5 | ¿Qué se detectó al desbordar intro2pwn1 con una cadena larga? | `Stack Smashing` |
| 2.6 | ¿Qué error se obtiene al desbordar intro2pwn2? | `Segmentation Fault` |
| 3.1 | Usuario dueño de flag.txt e intro2pwn3 | `dizmas` |
| 3.2 | Protección con temática de pájaro que le falta a intro2pwn3 | `canary` |
| 3.3 | Secuencia de letras ASCII para 0x4a4a4a4a | `JJJJ` |
| 3.4 | Salida de "cyclic 12" | `aaaabaaacaaa` |
| 3.5 | Patrón en hex con el que se desbordó el EIP | `0x6161616a` |
| 3.7 | Flag del exploit local | `flag{13@rning_2_pwn!}` |
| 4.1 | Puerto que sirve el reto | `1337` |
| 4.2 | ¿Serve_test tiene stack canary? (Y/N) | `Y` |
| 4.4 | Flag del exploit remoto | `flag{n3tw0rk!ng_!$_fun}` |
| 5.1 | ¿Qué significa ASLR? | `address space layout randomization` |
| 5.2 | ¿Quién es el dueño de intro2pwnFinal? | `root` |
| 5.3 | ¿Está NX activada en el binario final? (Y/N) | `N` |
| 5.4 | Secuencia de letras que rellena el EIP | `taaa` |
| 5.5 | Mensaje al romper el breakpoint fuera de gdb | `Trace/breakpoint trap` |
| 5.6 | Función del shellcode generado (i386.linux.sh) | `execve` |
| 5.7 | Usuario obtenido al ejecutar whoami tras el exploit | `root` |
| 5.8 | Flag final | `flag{pwn!ng_!$_fr33d0m}` |
| 6 | Cierre de la sala | `No answer needed` |

---

**Metodología:** Análisis de protecciones con checksec, generación y uso de patrones con cyclic, depuración con GDB para localizar el offset y el valor del EIP, construcción de exploits con pwntools para desbordar el stack de binarios locales (sin canary), explotación de un servicio remoto por red en el puerto 1337 y evasión de ASLR sobre un binario sin NX usando NOP sled y shellcode execve para obtener una shell de root y las flags.

### Cadena de ataque / Attack Chain

checksec -> identificacion de protecciones -> buffer overflow (Stack Smashing/SegFault) -> cyclic pattern -> offset/EIP -> pwntools exploit local (dizmas) -> servicio remoto (1337) -> ASLR -> NOP sled + shellcode execve -> shell root -> flags

**Learning chain:** pwntools -> checksec -> buffer overflow -> GDB -> cyclic -> exploit local -> remote exploitation -> ASLR -> shellcode -> root shell

**Lección:** *La combinación de checksec, GDB y pwntools permite convertir un desbordamiento del stack en una ejecución de shellcode; conocer las protecciones (canary, NX, ASLR, PIE) es la clave para elegir la técnica de explotación adecuada.*

**MITRE ATT&CK:** T1068 (Exploitation for Privilege Escalation) / T1203 (Exploitation for Client Execution).

**Fuente:** [TryHackMe - Intro To Pwntools](https://tryhackme.com/room/introtopwntools)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.