# Flip

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | ctf | `flip` | https://tryhackme.com/room/flip | 01 Level Easy | TryHackMe | AES-CBC / bit flipping / error-based padding oracle / cookie manipulation / webshell | Ofensivo: descifrar el cifrado AES-CBC de la cookie de sesión manipulando bits (IV prepended) para reemplazar el nombre de usuario por `admin` y subir una webshell. |

---

> **Objeto:** Aprovechar un ataque de bit flipping sobre AES-CBC en una aplicación web: la cookie de sesión está cifrada y el atacante modifica el IV (antepuesto al ciphertext) para transformar el nombre de usuario `bdmin` en `admin`, obteniendo acceso administrativo y una webshell para recuperar la flag.

**Contexto:** La aplicación cifra la cookie de sesión con AES-CBC (estilo Flask). El valor encriptado está compuesto por `IV + ciphertext`, y el servidor descifra y deserializa el valor legible. Como se conoce el plaintext original (`bdmin`), basta con alterar deliberadamente los bytes del IV en las posiciones que corresponden a los caracteres que se quieren cambiar (`b`→`a`): en CBC corromper un byte del IV modifica solo el bloque de plaintext correspondiente, sin romper la integridad general. Con la cookie manipulada (`{username: admin}`), la sesión de administrador permite subir una webshell al servidor que entrega la flag.

> **ES:** "Flip" — bit flipping en AES-CBC sobre la cookie de sesión para convertir `bdmin` en `admin`.
> **EN:** A classical AES-CBC bit-flipping attack where mutating the prepended IV turns the session username `bdmin` into `admin`, granting an admin upload area to drop a webshell and grab the flag.

## Solucionario

### Task 1: Exploración de la aplicación web / Web Application Exploration

**Explicación:** Pregunta de inicio para conectarse a la máquina virtual e iniciar el laboratorio. No requiere ninguna respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Follow the instructions and deploy the machine. / Despliega la máquina. | `No answer needed` |

### Task 2: Explotación / Exploitation

**Explicación:** La página tiene un formulario de login. Interceptando la petición en Burp Suite se observa que la cookie de sesión está cifrada (71 caracteres: IV de 32 hex + ciphertext). Sabiendo que el plaintext descifrado contiene `bdmin`, se calcula el nuevo IV: se XOR el byte del IV original con el byte del plaintext y con el byte deseado (`IV'[pos] = IV[pos] XOR 'b' XOR 'a'`). Enviamos la cookie modificada (saltando el campo `username` del formulario) y el servidor la descifra como `admin`, cargando el panel de administración.

```python
from pwn import xor

cookie = bytes.fromhex('<cookie original>')
iv, ciphertext = cookie[:16], cookie[16:]
for pos, (b, new) in enumerate(zip(b'bdmin', b'admin')):   # cambiar 'b' -> 'a'
    iv[pos] ^= b ^ new
print((iv + ciphertext).hex())
```

Con la sesión de admin se sube una webshell (`.php`). La flag se encuentra en el servidor tras la subida.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2 | What is the flag? / ¿Cuál es la flag? | `THM{FliP_DaT_B1t_oR_G3t_Fl1pP3d}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Deploy the machine. | `No answer needed` |
| 2 | What is the flag? | `THM{FliP_DaT_B1t_oR_G3t_Fl1pP3d}` |

---

**Metodología:** Analizar el flujo de login y detectar la cookie cifrada en la respuesta. Reconocer el formato `IV + ciphertext` de AES-CBC y aplicar bit flipping: calcular `IV'[pos] = IV[pos] XOR b ORIG XOR b DESEADO` para convertir `bdmin` en `admin` dentro del plaintext. Reenviar la cookie manipulada, obtener el panel de administración, subir una webshell y leer la flag.

### Cadena de ataque / Attack Chain

```text
Login -> cookie cifrada (IV+ciphertext) -> identificar CBC y plaintext conocido -> XOR del IV (b->a) -> cookie admin -> panel admin -> upload webshell -> flag
```

**Learning chain:** AES-CBC -> IV manipulation -> bit flipping / byte flipping -> known plaintext -> cookie forgery -> privilege change (user->admin) -> webshell upload -> flag.

**Lección:** *En AES-CBC, modificar un byte del IV altera el byte equivalente del primer bloque de plaintext sin corromper el resto: los tokens cifrados deben incluir autenticación (MAC/ES) además de confidencialidad, si no son vulnerables a bit flipping.*

**MITRE ATT&CK:** T1190 — Exploit Public-Facing Application; T1562.??? — N/A; T1098 — Account Manipulation (abuso de sesión)

**Fuente:** [TryHackMe - Flip](https://tryhackme.com/room/flip)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.