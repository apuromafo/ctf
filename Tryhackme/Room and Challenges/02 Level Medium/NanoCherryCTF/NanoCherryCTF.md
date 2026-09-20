# NanoCherryCTF

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF | nanocherryctf | https://tryhackme.com/room/nanocherryctf | 02 Level Medium | TryHackMe | Email, credenciales, fuerza bruta, web | Compromiso total (flags + credenciales) |

---

**Contexto:** La sala **NanoCherryCTF** es un reto de hacking en varias etapas. Se consigue la primera flag a través de un **mail**, se descubren las **credenciales** en texto claro dentro del sistema y se explotan los almacenes de contraseñas para obtener las flags finales. El reto premia razonar y explotar por encima del modus operandi de un *script kiddie*: las pistas están en la forma de pensar del atacante, no solo en las herramientas.

## Solucionario

### Task 1: Presentación
**Explicación:**

Introducción al reto y despliegue de la máquina del laboratorio.

Respuesta: `No answer needed`

### Task 2: Explotación
**Explicación:**

Se recogen los artefactos del compromiso: la flag obtenida del **correo electrónico** (`THM{BL4CK_M4I1}`), las **credenciales** filtradas en el sistema (`n4n0ch3rry`, `w1llb3`, `7h3fu7ur3`), la flag de credenciales reunidas (`THM{P4SS3S_C0LL3CT3D}`) y la flag final que acredita el razonamiento del atacante (`THM{YOU_NEVER_WERE_A_SCRIPT_KIDDIE}`).

1. `THM{BL4CK_M4I1}`
2. `n4n0ch3rry`
3. `w1llb3`
4. `7h3fu7ur3`
5. `THM{P4SS3S_C0LL3CT3D}`
6. `THM{YOU_NEVER_WERE_A_SCRIPT_KIDDIE}`

### Task 3: Cierre
**Explicación:**

Reflexión final del CTF y de la cadena de ataque completada.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Presentación del reto | `No answer needed` |
| 2.1 | Flag del correo | `THM{BL4CK_M4I1}` |
| 2.2 | Primera credencial filtrada | `n4n0ch3rry` |
| 2.3 | Segunda credencial filtrada | `w1llb3` |
| 2.4 | Tercera credencial filtrada | `7h3fu7ur3` |
| 2.5 | Flag de credenciales recolectadas | `THM{P4SS3S_C0LL3CT3D}` |
| 2.6 | Flag final del atacante | `THM{YOU_NEVER_WERE_A_SCRIPT_KIDDIE}` |
| 3 | Cierre del CTF | `No answer needed` |

---

**Metodología:** Enumeración inicial → revisión del mail → recolección de credenciales en claro → explotación de almacenes de secretos → captura de las flags finales.

**Learning chain:** Mail → flag 1 → credenciales → flags de credenciales → razonamiento final → última flag.

**Lección:** *Los CTF premian el razonamiento: las credenciales filtradas se encadenan con las pistas del reto para llegar a la flag final; no basta con lanzar herramientas sin entenderlas.*

**MITRE ATT&CK:** T1087 Account Discovery · T1552 Unsecured Credentials.

**Fuente:** [TryHackMe - NanoCherryCTF](https://tryhackme.com/room/nanocherryctf)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.