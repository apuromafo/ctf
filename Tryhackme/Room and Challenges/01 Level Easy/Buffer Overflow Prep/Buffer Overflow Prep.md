# Buffer Overflow Prep [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** CTF (Free)
* **Slug:** `bufferoverflowprep`
* **Link:** https://tryhackme.com/room/bufferoverflowprep
* **Sección / Section:** Offensive Security Path (prep OSCP)
* **Fuente / Source:** Writeup de AfvanMoopen (GitHub) + Steflan's Security Blog

---

## Solucionario de Tareas / Task Solutions

> **ES:** Esta room practica buffer overflows de pila (stack) sobre un binario Windows de 32 bits (`oscp.exe`) con Immunity Debugger y mona. Es preparación para el examen OSCP. No hay flags; cada tarea pide el **offset de EIP** y los **badchars** de cada uno de los 10 comandos OVERFLOW.
> **EN:** This room practices stack buffer overflows on a 32-bit Windows binary (`oscp.exe`) with Immunity Debugger and mona. It is OSCP exam prep. There are no flags; each task asks for the **EIP offset** and **badchars** of each of the 10 OVERFLOW commands.

---

### Task 1 — Deploy VM

Máquina Windows 7 de 32 bits con Immunity Debugger y Putty preinstalados. Firewall y Defender deshabilitados. Acceso por RDP:

```
xfreerdp /u:admin /p:password /cert:ignore /v:MACHINE_IP
```

Credenciales: `admin` / `password`. En el escritorio está la carpeta `vulnerable-apps` con varios binarios vulnerables, incluido el binario personalizado `oscp` con 10 buffer overflows (cada uno con distinto offset de EIP y set de badchars).

**Respuesta / Answer:** `No answer needed`

---

### Task 2 — oscp.exe OVERFLOW1

Abrir `oscp.exe` en Immunity Debugger como administrador y ejecutarlo (F9). Escucha en el puerto 1337. Conectar con netcat:

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

**Respuestas / Answers:**

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the EIP offset for OVERFLOW1? | `1978` |
| In byte order and including the null byte \x00, what were the badchars for OVERFLOW1? | `\x00\x07\x2e\xa0` |

---

### Task 3 — oscp.exe OVERFLOW2

Repetir el proceso para el comando OVERFLOW2. El fuzzer crashea a los 700 bytes; patrón de 1300 bytes.

**Respuestas / Answers:**

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the EIP offset for OVERFLOW2? | `634` |
| In byte order and including the null byte \x00, what were the badchars for OVERFLOW2? | `\x00\x23\x3c\x83\xba` |

---

### Task 4 — oscp.exe OVERFLOW3

**Respuestas / Answers:**

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the EIP offset for OVERFLOW3? | `1274` |
| In byte order and including the null byte \x00, what were the badchars for OVERFLOW3? | `\x00\x11\x40\x5f\xb8\xee` |

---

### Task 5 — oscp.exe OVERFLOW4

**Respuestas / Answers:**

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the EIP offset for OVERFLOW4? | `2026` |
| In byte order and including the null byte \x00, what were the badchars for OVERFLOW4? | `\x00\xa9\xcd\xd4` |

---

### Task 6 — oscp.exe OVERFLOW5

**Respuestas / Answers:**

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the EIP offset for OVERFLOW5? | `314` |
| In byte order and including the null byte \x00, what were the badchars for OVERFLOW5? | `\x00\x16\x2f\xf4\xfd` |

---

### Task 7 — oscp.exe OVERFLOW6

**Respuestas / Answers:**

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the EIP offset for OVERFLOW6? | `1034` |
| In byte order and including the null byte \x00, what were the badchars for OVERFLOW6? | `\x00\x08\x2c\xad` |

---

### Task 8 — oscp.exe OVERFLOW7

**Respuestas / Answers:**

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the EIP offset for OVERFLOW7? | `1306` |
| In byte order and including the null byte \x00, what were the badchars for OVERFLOW7? | `\x00\x8c\xae\xbe\xfb` |

---

### Task 9 — oscp.exe OVERFLOW8

**Respuestas / Answers:**

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the EIP offset for OVERFLOW8? | `1786` |
| In byte order and including the null byte \x00, what were the badchars for OVERFLOW8? | `\x00\x1d\x2e\xc7\xee` |

---

### Task 10 — oscp.exe OVERFLOW9

**Respuestas / Answers:**

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the EIP offset for OVERFLOW9? | `1514` |
| In byte order and including the null byte \x00, what were the badchars for OVERFLOW9? | `\x00\x04\x3e\x3f\xe1` |

---

### Task 11 — oscp.exe OVERFLOW10

**Respuestas / Answers:**

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the EIP offset for OVERFLOW10? | `537` |
| In byte order and including the null byte \x00, what were the badchars for OVERFLOW10? | `\x00\xa0\xad\xbe\xde\xef` |

---

## Metodología / Methodology

1. **Fuzzing:** enviar cadenas crecientes de "A" hasta que el servidor crashee (identificar el tamaño aproximado del buffer).
2. **Control de EIP:** generar un patrón cíclico (pattern_create) mayor que el crash, enviarlo y usar `!mona findmsp` para hallar el offset exacto de EIP.
3. **Badchars:** generar un bytearray con mona (`!mona bytearray -b "\x00"`), enviar la cadena de badchars y comparar (`!mona compare`) hasta que el resultado sea "Unmodified".
4. **Jump point:** `!mona jmp -r esp -cpb "<badchars>"` para encontrar una instrucción `jmp esp` sin badchars.
5. **Payload:** generar reverse shell con msfvenom excluyendo badchars, prepend NOPs, y explotar.

---

*Documentación para propósitos educativos y registro de CTF.*
