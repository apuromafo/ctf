# Cryptosystem

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | Cryptography / RSA CTF | `cryptosystem` | https://tryhackme.com/room/cryptosystem | 01 Level Easy | TryHackMe | RSA / exponente público pequeño (small e) / criptoanálisis / Python (criptografía) | Reto de criptografía RSA: explotar un exponente de cifrado demasiado pequeño (small e attack) para descifrar un mensaje y recuperar la bandera. |

---

**Contexto:** Reto de criptografía basado en RSA. Se entrega un módulo y un exponente de cifrado, o un mensaje cifrado de longitud pequeña, de forma que el criptosistema es vulnerable al ataque de exponente pequeño ("small e"): al ser `m^e < n`, la raíz e-ésima del ciphertext recupera directamente el mensaje en claro sin necesidad de factorizar el módulo.

> **ES:** "Un criptosistema RSA mal configurado con un exponente de cifrado pequeño: aplicar el ataque de raíz e-ésima para descifrar el mensaje sin factorizar n."
> **EN:** "An RSA cryptosystem with a small public exponent: apply the small-e attack (e-th root) to decrypt the message without factoring n."

## Solucionario

### Task 1: Descifra el mensaje / Decrypt the message

**Explicación:** Se analiza el fichero/parámetros RSA del reto: primos pequeños o exponente `e` muy pequeño. Con un exponente pequeño (típicamente `e=3`) y un plaintext corto, se cumple `m^e < n`, así que el ciphertext es directamente `m^e`. Se calcula la raíz cúbica (o e-ésima) del número cifrado con Python y se convierte el resultado a bytes para obtener la bandera `THM{Just_s0m3_small_amount_of_RSA!}`.

```python
import gmpy2

c = <ciphertext_int>
e = 3
m = gmpy2.iroot(c, e)[0]        # raíz e-ésima exacta
flag = bytes.fromhex(hex(m)[2:]).decode()
print(flag)
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la bandera del criptosistema? / What is the flag of the cryptosystem? | `THM{Just_s0m3_small_amount_of_RSA!}` |

---

| # | Task | Pregunta | Respuesta |
|---|------|----------|-----------|
| 1 | Task 1 | ¿Cuál es la bandera? / What is the flag? | `THM{Just_s0m3_small_amount_of_RSA!}` |

---

**Metodología:** Inspeccionar los parámetros RSA (n, e, c) -> comprobar que se cumple `m^e < n` (plaintext corto y `e` pequeño) -> calcular la raíz e-ésima entera del ciphertext con `gmpy2.iroot` -> pasar el entero resultante a hexadecimal y luego a ASCII -> leer la bandera.

### Cadena de ataque / Attack Chain

```text
Parámetros RSA -> e pequeño (3) y msg corto -> c = m^e -> iroot(c, 3) = m -> hex -> ascii -> THM{...}
```

**Learning chain:** RSA -> c=pow(m,e,n) -> small e -> raíz e-ésima -> gmpy2.iroot -> bytes -> flag.

**Lección:** *En RSA, un exponente público diminuto con mensajes cortos permite romper el cifrado con la raíz e-ésima; el tamaño del exponente y el padding son tan importantes como el módulo.*

**MITRE ATT&CK:** N/A (reto de criptografía RSA)

**Fuente:** [TryHackMe - Cryptosystem](https://tryhackme.com/room/cryptosystem)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.