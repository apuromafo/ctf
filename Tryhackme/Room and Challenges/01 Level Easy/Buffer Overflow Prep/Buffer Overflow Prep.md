# Buffer Overflow Prep

| **Dificultad** | Easy |
| **Tipo** | CTF |
| **Slug** | `bufferoverflowprep` |
| **Link** | [TryHackMe](https://tryhackme.com/room/bufferoverflowprep) |
| **Sección** | 01 Level Easy |
| **Fuente** | Writeup de AfvanMoopen (GitHub) + Steflan's Security Blog |
| **Componentes** | Immunity Debugger / mona.py / msfvenom / pattern_create / xfreerdp / netcat / badchars / EIP offset |
| **Impacto** | Practica buffer overflows de pila sobre un binario Windows de 32 bits y obtén los offsets de EIP y badchars de los 10 comandos OVERFLOW, preparación OSCP. |

---

**Contexto:** Esta room practica buffer overflows de pila (stack) sobre un binario Windows de 32 bits (`oscp.exe`) con Immunity Debugger y mona. Es preparación para el examen OSCP. No hay flags; cada tarea pide el **offset de EIP** y los **badchars** de cada uno de los 10 comandos OVERFLOW.

## Solucionario

### Task 1: Deploy VM

**Explicación:** Máquina Windows 7 de 32 bits con Immunity Debugger y Putty preinstalados. Firewall y Defender deshabilitados. Acceso por RDP:

```
xfreerdp /u:admin /p:password /cert:ignore /v:MACHINE_IP
```

Credenciales: `admin` / `password`. En el escritorio está la carpeta `vulnerable-apps` con varios binarios vulnerables, incluido el binario personalizado `oscp` con 10 buffer overflows (cada uno con distinto offset de EIP y set de badchars).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - deploy the VM. | `No answer needed` |

### Task 2: oscp.exe OVERFLOW1

**Explicación:** Abrir `oscp.exe` en Immunity Debugger como administrador y ejecutarlo (F9). Escucha en el puerto 1337. Conectar con netcat:

```
nc MACHINE_IP 1337
```

Escribir `HELP` muestra los 10 comandos OVERFLOW1-10. Configurar la carpeta de trabajo de mona:

```
!mona config -set workingfolder c:\mona\%p
```

**Fuzzing:** script `fuzzer.py` que envía cadenas de "A" crecientes (100→3000 bytes). El servidor crashea a los 2000 bytes.

**Crash Replication & Controlling EIP:** generar un patrón cíclico 400 bytes mayor que el crash:

```
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 2400
```

Enviarlo con `exploit.py` y usar mona para hallar el offset:

```
!mona findmsp -distance 2400
```

**Finding Bad Characters:** generar bytearray y comparar:

```
!mona bytearray -b "\x00"
!mona compare -f C:\mona\oscp\bytearray.bin -a <address>
```

**Finding a Jump Point:**

```
!mona jmp -r esp -cpb "\x00\x07\x2e\xa0"
```

**Generate Payload** con msfvenom (excluyendo badchars) y **prepend NOPs** (`padding = "\x90" * 16`). Explotar para obtener reverse shell.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the EIP offset for OVERFLOW1? | `1978` |
| 2 | In byte order and including the null byte \x00, what were the badchars for OVERFLOW1? | `\x00\x07\x2e\xa0` |

### Task 3: oscp.exe OVERFLOW2

**Explicación:** Repetir el proceso para el comando OVERFLOW2. El fuzzer crashea a los 700 bytes; patrón de 1300 bytes.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the EIP offset for OVERFLOW2? | `634` |
| 2 | In byte order and including the null byte \x00, what were the badchars for OVERFLOW2? | `\x00\x23\x3c\x83\xba` |

### Task 4: oscp.exe OVERFLOW3

**Explicación:** Repetir el proceso para el comando OVERFLOW3 (fuzzing → patrón → findmsp → bytearray/compare → jmp esp → payload).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the EIP offset for OVERFLOW3? | `1274` |
| 2 | In byte order and including the null byte \x00, what were the badchars for OVERFLOW3? | `\x00\x11\x40\x5f\xb8\xee` |

### Task 5: oscp.exe OVERFLOW4

**Explicación:** Repetir el proceso para el comando OVERFLOW4.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the EIP offset for OVERFLOW4? | `2026` |
| 2 | In byte order and including the null byte \x00, what were the badchars for OVERFLOW4? | `\x00\xa9\xcd\xd4` |

### Task 6: oscp.exe OVERFLOW5

**Explicación:** Repetir el proceso para el comando OVERFLOW5.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the EIP offset for OVERFLOW5? | `314` |
| 2 | In byte order and including the null byte \x00, what were the badchars for OVERFLOW5? | `\x00\x16\x2f\xf4\xfd` |

### Task 7: oscp.exe OVERFLOW6

**Explicación:** Repetir el proceso para el comando OVERFLOW6.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the EIP offset for OVERFLOW6? | `1034` |
| 2 | In byte order and including the null byte \x00, what were the badchars for OVERFLOW6? | `\x00\x08\x2c\xad` |

### Task 8: oscp.exe OVERFLOW7

**Explicación:** Repetir el proceso para el comando OVERFLOW7.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the EIP offset for OVERFLOW7? | `1306` |
| 2 | In byte order and including the null byte \x00, what were the badchars for OVERFLOW7? | `\x00\x8c\xae\xbe\xfb` |

### Task 9: oscp.exe OVERFLOW8

**Explicación:** Repetir el proceso para el comando OVERFLOW8.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the EIP offset for OVERFLOW8? | `1786` |
| 2 | In byte order and including the null byte \x00, what were the badchars for OVERFLOW8? | `\x00\x1d\x2e\xc7\xee` |

### Task 10: oscp.exe OVERFLOW9

**Explicación:** Repetir el proceso para el comando OVERFLOW9.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the EIP offset for OVERFLOW9? | `1514` |
| 2 | In byte order and including the null byte \x00, what were the badchars for OVERFLOW9? | `\x00\x04\x3e\x3f\xe1` |

### Task 11: oscp.exe OVERFLOW10

**Explicación:** Repetir el proceso para el comando OVERFLOW10.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the EIP offset for OVERFLOW10? | `537` |
| 2 | In byte order and including the null byte \x00, what were the badchars for OVERFLOW10? | `\x00\xa0\xad\xbe\xde\xef` |

---

**Metodología:**
1. Desplegar la máquina Windows 7 de 32 bits y acceder por RDP con `xfreerdp /u:admin /p:password /cert:ignore /v:MACHINE_IP`; abrir `oscp.exe` en Immunity Debugger como administrador y ejecutarlo (F9); escucha en el puerto 1337.
2. Configurar la carpeta de trabajo de mona con `!mona config -set workingfolder c:\mona\%p`.
3. **Fuzzing:** enviar cadenas de "A" crecientes (100→3000 bytes) con `fuzzer.py` hasta que el servidor crashee e identificar el tamaño aproximado del buffer.
4. **Crash Replication & Controlling EIP:** generar un patrón cíclico 400 bytes mayor que el crash con `pattern_create.rb -l <size>`, enviarlo con `exploit.py` y usar `!mona findmsp -distance <size>` para hallar el offset exacto de EIP.
5. **Finding Bad Characters:** generar el bytearray con `!mona bytearray -b "\x00"`, enviar la cadena de badchars y comparar con `!mona compare -f C:\mona\oscp\bytearray.bin -a <address>` hasta obtener "Unmodified".
6. **Finding a Jump Point:** `!mona jmp -r esp -cpb "<badchars>"` para localizar una instrucción `jmp esp` sin badchars; generar el payload con msfvenom excluyendo los badchars, prepend `padding = "\x90" * 16` NOPs y explotar para obtener la reverse shell.

**Learning chain:** fuzzing (crash) → pattern_create → mona findmsp (EIP offset) → bytearray/compare (badchars) → jmp esp → msfvenom payload → NOP sled → reverse shell.

**MITRE ATT&CK:** T1203 (Exploitation for Client Execution), T1055 (Process Injection), T1569.002 (Service Execution).

**Fuente:** [TryHackMe - Buffer Overflow Prep](https://tryhackme.com/room/bufferoverflowprep)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
