# The Witch's Cauldron

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | CTF / challenge | `thewitchscauldron` | https://tryhackme.com/room/thewitchscauldron | 01 Level Easy | TryHackMe | Diffie-Hellman / criptografía / openssl pkeyutl / aes-256-cbc / alice.key / bob.public / encrypted_spell.enc / shared secret | Compartir la receta secreta de Bob con Alice sin que Eve la robe: resolver el reto web (flag 1) y descifrar el hechizo cifrado derivando el secreto compartido Diffie-Hellman (flag 2). |

---

**Contexto:** Room de la ruta de criptografía que plantea: "¿Puedes compartir la receta secreta de Bob con Alice sin que Eve se entere?" Ambientada en un laboratorio mágico, la Witch Alice debe obtener la poción secreta que su amigo Witch Bob quiere compartir mientras Goblin Eve intenta robarla. La primera parte es un reto web (View Site) que entrega la primera flag. La segunda explica la teoría de Diffie-Hellman (base común, potiones secretas y públicas, qué ve Eve, operaciones de cifrado/descifrado) y plantea descifrar `encrypted_spell.enc` derivando la clave compartida con `openssl pkeyutl -derive -inkey alice.key -peerkey bob.public -out shared.bin` y descifrando con `openssl aes-256-cbc -d -in encrypted_spell.enc -pass file:shared.bin`.

> **ES:** Criptografía con Diffie-Hellman: completar el app web para la primera flag y, derivando el secreto compartido con `openssl pkeyutl -derive` (alice.key + bob.public), descifrar `encrypted_spell.enc` con `aes-256-cbc` para la segunda flag.
> **EN:** Diffie-Hellman cryptography: complete the web app for the first flag and, deriving the shared secret with `openssl pkeyutl -derive` (alice.key + bob.public), decrypt `encrypted_spell.enc` with `aes-256-cbc` for the second flag.

## Solucionario

### Task 1: The Witch's Cauldron / El caldero de la bruja

**Explicación:** Se inicia la app adjunta a la tarea con "View Site"; resolviendo el desafío de la aplicación (Witch Alice consigue la receta de Witch Bob sin que Eve la intercepte) se obtiene la primera flag.

**Respuesta original verbatim:**
```text
1. THM{y0u_br3w3d_7h3_53cr37}
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Cuál es la flag devuelta tras completar The Witch's Cauldron? / What is the flag that is returned after completing The Witch's Cauldron? | `THM{y0u_br3w3d_7h3_53cr37}` |

### Task 2: Componentes técnicos / The Technical Components

**Explicación:** Se repasa el fundamento de Diffie-Hellman (compartir un secreto sobre un canal inseguro sin enviar la clave), y se resuelve el desafío final: Bob cifró un hechizo con el secreto compartido. Con los ficheros `alice.key`, `bob.public` y `encrypted_spell.enc` se deriva `shared.bin` y se descifra el hechizo con AES-256-CBC.

**Respuesta original verbatim:**
```text
2. THM{525403e42fbda51dfd0572025d78062f}
```

```bash
cd /root/Rooms/cauldron
openssl pkeyutl -derive -inkey alice.key -peerkey bob.public -out shared.bin
openssl aes-256-cbc -d -in encrypted_spell.enc -pass file:shared.bin -out recipe.txt
cat recipe.txt
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Cuál es la flag devuelta tras descifrar encrypted_spell.enc? / What is the flag that is returned after decrypting encrypted_spell.enc? | `THM{525403e42fbda51dfd0572025d78062f}` |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Cuál es la flag devuelta tras completar The Witch's Cauldron? / What is the flag that is returned after completing The Witch's Cauldron? | `THM{y0u_br3w3d_7h3_53cr37}` |
| 2 | ¿Cuál es la flag devuelta tras descifrar encrypted_spell.enc? / What is the flag that is returned after decrypting encrypted_spell.enc? | `THM{525403e42fbda51dfd0572025d78062f}` |

---

**Metodología:** Abrir la app con "View Site" -> resolver el reto de compartir la receta -> flag 1 (THM{y0u_br3w3d_7h3_53cr37}) -> estudiar la teoría Diffie-Hellman (secretos compartidos, lo que observa Eve) -> obtener los ficheros (`alice.key`, `bob.public`, `encrypted_spell.enc`) -> derivar el secreto compartido (`openssl pkeyutl -derive ... shared.bin`) -> descifrar el hechizo con AES-256-CBC usando el secreto como pass -> flag 2 (THM{525403e42fbda51dfd0572025d78062f}).

### Cadena de ataque / Attack Chain

```text
View Site -> completar desafío web -> THM{y0u_br3w3d_7h3_53cr37} -> Diffie-Hellman teoría -> alice.key + bob.public -> pkeyutl -derive -> shared.bin -> aes-256-cbc -d encrypted_spell.enc -pass file:shared.bin -> THM{525403e42fbda51dfd0572025d78062f}
```

**Learning chain:** Criptografía -> Diffie-Hellman -> secreto compartido -> OpenSSL -> key derivation (pkeyutl) -> AES decryption -> flags.

**Lección:** *Diffie-Hellman permite a dos partes acordar un secreto compartido a través de un canal público sin enviarlo jamás; derivar ese secreto con OpenSSL es el puente para descifrar cualquier mensaje cifrado con él.*

**MITRE ATT&CK:** T1027 (Obfuscated Files or Information), T1552.001 (Unsecured Credentials: Credentials In Files) - contexto de laboratorio de criptografía.

**Fuente:** [TryHackMe - The Witch's Cauldron](https://tryhackme.com/room/thewitchscauldron)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.