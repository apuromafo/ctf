# Precision

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|------|------|------|---------|--------|-------------|---------|
| Hard | CTF | `hfb1precision` | [TryHackMe](https://tryhackme.com/room/hfb1precision) | 03 Level Hard | Web (API THM `api/v2/rooms/tasks?roomCode=hfb1precision` + websearch de walkthroughs) | Binary Exploitation / Pwn / x86-64 (AMD64) / GDB / pwntools / Ret2win / Ripping / Offset + ROP | Sala pwn de dificultad Hard: práctica de desarrollo de exploits sobre binarios Linux, análisis estático (Holes/ROP) y explotación de la ejecución de código para obtener el flag. |

---

**Contexto:**

> **ES:** **Precision** es una sala pwn (Binary Exploitation) de dificultad Hard enfocada en "Practice your advanced Linux Exploit Development skills." (la descripción oficial de la sala). Se trabaja sobre un binario Linux x86-64 con un programa vulnerable que se analiza de forma estática y dinámica: con GDB se localiza la función vulnerable y el desbordamiento de buffer, con herramientas/pwntools se calcula el offset necesario y se construye un payload (ret2win/ROP) que desvía el flujo de ejecución hacia la rutina que imprime el flag. El reto es un homenaje a tomar decisiones precisas con el puntero de ejecución; de ahí el nombre y el flag configurado: `t4k3_a_chance_with_precision_THMpwn` ("toma la oportunidad con Precision").
> **EN:** **Precision** is a pwn (Binary Exploitation) room of Hard difficulty focused on "Practice your advanced Linux Exploit Development skills." (the room's official description). The work happens on a vulnerable x86-64 Linux binary analyzed both statically and dynamically: with GDB the vulnerable function and the buffer overflow are located, with tools/pwntools the needed offset is computed and a payload (ret2win/ROP) is built that redirects the execution flow toward the routine that prints the flag. The challenge pays homage to taking precise decisions with the instruction pointer; hence the name and the configured flag: `t4k3_a_chance_with_precision_THMpwn`.

---

## Solucionario

### Task 1: Obtain the flag / Obtén el flag

**Explicación:**
Explotando el binario vulnerable (desarrollo de un exploit para el desbordamiento de buffer, con retorno a la "win function") se imprime el flag solicitado.

1. THM{t4k3_a_chance_with_precision_THMpwn}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{t4k3_a_chance_with_precision_THMpwn}` |

---

**Metodología:**

1. Reconocimiento/entrega del binario: la sala entrega un binario ELF x86-64 (o acceso a un servicio remoto en `<IP>:<PORT>`). Primeras comprobaciones con `file`, `checksec` y `strings`.
2. Análisis estático: desensamblado/Ghidra o `objdump` para identificar funciones clave (una "win" / `flag`) y la vulnerabilidad (`gets`/`strcpy`/fgets sin límite, lectura de input).
3. Análisis dinámico correcto: ejecutar el binario y provocar el crash (segfault) para confirmar el overflow.
4. Cálculo del offset: con pwntools `cyclic` + `cyclic_find`, o `pattern create/offset` de gdb/gef, se determina exactamente cuántos bytes se necesitan hasta el RIP.
5. Construcción del payload: `payload = b"A"*offset + p64(<dirección de la win/flag>)`; si el binario tiene protecciones, aquí entra el ret2win/ROP con gadgets para alinear la pila y saltar correctamente.
6. Envío del exploit: `python3 exploit.py` (pwntools) o `(cat payload; cat) | ./binary` → ejecución de la win → impresión del flag → responder.

### Cadena de ataque / Attack Chain

`file + checksec del binario → Análisis estático (win/flag) → Fuzzing del input → Overflow detectado → Offset con cyclic/pwntools → Construcción de payload (ret2win/ROP) → Envío → Flag`

**Learning chain:**

Reconocimiento de binarios ELF → Uso de checksec/file/checksec para mitigaciones → Localización de funciones y vuln en el desensamblado → Determinación del offset con cyclic → Desarrollo de exploit con pwntools → Ejecución remota/local → Lectura de flag.

*Lección:* La explotación de binarios no es magia: es precisión. Saber la mitigación exacta, el offset exacto y la dirección exacta del gadget hace la diferencia entre un crash y una win. Controlar el RIP con exactitud (de ahí "Precision") permite que un simple overflow se convierta en la ejecución de la función que imprime la flag.

**MITRE ATT&CK:**

T1068 (Exploitation for Privilege Escalation), T1059.006 (Command and Scripting Interpreter: Python), T1210 (Exploitation of Remote Services), T1140 (Deobfuscate/Decode Files or Information)

**Fuente:** [TryHackMe - Precision](https://tryhackme.com/room/hfb1precision)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.