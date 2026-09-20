# Flag Vault 2

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | Binary Exploitation / pwn | `flagvault2` | https://tryhackme.com/room/flagvault2 | 01 Level Easy | TryHackMe | format string / printf / fgets / %N$s / pwntools | Reto pwn: abusar de una vulnerabilidad de format string en `printf()` para filtrar la flag guardada en memoria. |

---

> **Objeto:** Explotar una vulnerabilidad de format string en un binario remoto (puerto 1337) que pasa la entrada del usuario directamente a `printf()`, usando especificadores posicionales `%N$s` para leer el buffer `flag` de la pila.

**Contexto:** Segunda parte de Flag Vault. El binario lee el nombre de usuario y lo pasa directamente a `printf(username)` sin cadena de formato: una vulnerabilidad clásica de format string. La flag se carga desde `flag.txt` en un buffer `char flag[200]`, pero la llamada `printf("%s", flag)` está comentada, así que la flag permanece en memoria sin mostrarse. Enviando especificadores como `%1$s`, `%2$s`, etc. se puede recorrer la pila hasta la posición donde reside `flag` y exfiltrarla.

> **ES:** "Version 2.0: sin flags visibles" — explotar `printf(username)` con format strings para filtrar el buffer `flag` almacenado en la pila.
> **EN:** A format string vulnerability: user input goes straight into `printf()` without a fixed format string, so positional specifiers like `%5$s` can leak the `flag` buffer from the stack.

## Solucionario

### Task 1: Explotación binaria: Flag Vault 2 / Binary Exploitation: Flag Vault 2

**Explicación:** La función lee `flag.txt` con `fgets()` en `char flag[200]` y después se imprime el saludo con `printf(username)`, usando la entrada del usuario como cadena de formato. Al no usar `printf("%s", username)`, un especificador como `%5$s` interpreta el quinto argumento de la pila como puntero a cadena, que resulta ser el buffer `flag` recién leído. Como `gets()` tampoco limita la longitud, se puede enviar el especificador y el servidor responde con `Hello, THM{...}`.

```python
from pwn import *

conn = remote('<IP>', 1337)
conn.recvuntil(b'Username:')
conn.sendline(b'%5$s')          # posición de la pila donde reside el buffer flag
print(conn.recvall().decode())
```

Para localizar la posición correcta se puede probar en bucle `%1$s`, `%2$s`, ... hasta encontrar la posición `N` cuya salida contenga `THM{`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? / ¿Cuál es la flag? | `THM{format_issues}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? / ¿Cuál es la flag? | `THM{format_issues}` |

---

**Metodología:** Identificar que `printf(username)` usa la entrada del usuario como cadena de formato en lugar de imprimirla como argumento. Probar posiciones de la pila con `%N$s` en orden ascendente hasta que el especificador apunte al buffer `flag` (en este caso `%5$s`) y la respuesta incluya la flag.

### Cadena de ataque / Attack Chain

```text
Revisar el binario -> printf(username) sin formato -> probar %N$s de forma iterativa -> %5$s apunta al buffer flag -> respuesta "Hello, THM{format_issues}" -> flag
```

**Learning chain:** format string vuln -> printf misuse -> positional args (%N$s) -> stack leak -> flag.

**Lección:** *Pasar entrada del usuario directamente a `printf()` sin una cadena de formato fija permite leer (y escribir) memoria; siempre hay que usar `printf("%s", input)`.*

**MITRE ATT&CK:** N/A (reto educativo de binary exploitation / format string)

**Fuente:** [TryHackMe - Flag Vault 2](https://tryhackme.com/room/flagvault2)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.