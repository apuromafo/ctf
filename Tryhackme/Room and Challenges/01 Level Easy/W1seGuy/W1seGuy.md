# W1seGuy

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | CTF | `w1seguy` | https://tryhackme.com/room/w1seguy | 01 Level Easy | TryHackMe | Criptografía XOR, reutilización de keystream, known-plaintext attack | Recuperación de los flags cifrados con XOR explotando la reutilización de la clave |

---

**Contexto:** Reto criptográfico centrado en XOR: el servicio cifra datos con un esquema de XOR cuya clave se reutiliza. Enviando un plaintext conocido se recupera el keystream y se descifran las dos flags de la sala. El resumen original conserva únicamente las respuestas posicionales, sin los enunciados de las preguntas.

> **ES:** Conecta al servicio, recupera la clave XOR reutilizada aprovechando un plaintext conocido y descifra las dos flags.
> **EN:** Connect to the service, recover the reused XOR key via a known plaintext and decrypt the two flags.

## Solucionario

### Task 1: Conexión / Connection

**Explicación:** Se conecta al servicio remoto (netcat) para obtener el desafío inicial y comprobar el funcionamiento del cifrado. No requiere respuesta.

```
1. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |

### Task 2: Descifrado XOR / XOR Decryption

**Explicación:** El servicio cifra contenido con XOR reutilizando el mismo keystream. Al conocer parte del plaintext se recupera la clave y se descifran los dos flags: el primero vía ataque known-plaintext y el segundo mediante fuerza bruta sobre el XOR.

```
2. 1. THM{p1alntExtAtt4ckcAnr3alLyhUrty0urxOr}
   2. THM{BrUt3_ForC1nG_XOR_cAn_B3_FuN_nO?}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `THM{p1alntExtAtt4ckcAnr3alLyhUrty0urxOr}` |
| 2 | *(Pregunta 2 no especificada en el original)* | `THM{BrUt3_ForC1nG_XOR_cAn_B3_FuN_nO?}` |

---

**Metodología:** Conexión al servicio → obtención del ciphertext → envío de un plaintext conocido → XOR(plaintext, ciphertext) recupera el keystream → reutilización del keystream para descifrar la primera flag → fuerza bruta de la segunda flag → lectura de los flags.

### Cadena de ataque / Attack Chain

```text
nc a la máquina del reto -> el servicio entrega texto cifrado XOR -> se envía plaintext conocido -> XOR(known_plaintext, ciphertext) == keystream -> la misma clave se reutiliza -> decrypt primera flag (known-plaintext) -> brute-force de la segunda flag -> THM{...}
```

**Learning chain:** Conexión al servicio → cifrado XOR → known-plaintext → recuperación del keystream → reutilización de clave → descifrado de flags

**Lección:** *Un one-time pad que se reutiliza degenera en un cifrado XOR trivial: conociendo una parte del plaintext se recupera la clave y se descifra todo el tráfico.*

**MITRE ATT&CK:** T1027 (Obfuscated Files or Information)

**Fuente:** [TryHackMe - W1seGuy](https://tryhackme.com/room/w1seguy)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.