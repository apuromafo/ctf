# Cicada-3301 Vol_1
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `cicada3301vol1` |
| **Link** | [TryHackMe](https://tryhackme.com/room/cicada3301vol1) |
| **Sección** | OSINT / Steganography & Cryptography |
| **Fuente** | Research de thmrevenant y thabobosvark (GitHub) |
| **Componentes** | OSINT, audio enlazado, Pastebin, cifrado/descifrado (passphrase), claves, Imgur, esteganografía (outguess), hashes (SHA512, cracking), bit.ly, búsqueda musical (The Instar Emergence) |
| **Impacto** | Sala Medium tipo cacería: replicar la primera etapa del rompecabezas Cicada 3301 — extraer de un audio un enlace a Pastebin, descifrar una passphrase para abrir un archivo cifrado, seguir la cadena Imgur → imagen oculta con outguess → hash SHA512 → crack → segunda Pastebin → bit.ly → identificar la canción enlazada. |
---
**Contexto:** La sala es una versión educativa del primer rompecabezas de Cicada 3301. La cadena: un audio esconde un enlace de Pastebin; su contenido da una passphrase cifrada que abre un archivo, revelando una clave, y continúa a un Imgur; con outguess se extrae un archivo oculto que es un hash SHA512; tras crackearlo se obtiene otra Pastebin y de ahí un bit.ly que acaba enlazando a la canción *The Instar Emergence*.
*EN: The room is an educational version of the first Cicada 3301 puzzle. The chain: an audio hides a Pastebin link; its content yields an encrypted passphrase that opens a file, revealing a key, and continues to an Imgur; with outguess a hidden file is extracted which is a SHA512 hash; after cracking it, another Pastebin is obtained and from there a bit.ly that ends up linking to the song *The Instar Emergence*.*
## Solucionario
### Task 1 — The Search Begins
**Explicación:** El reto arranca con un audio: con herramientas de audición/OCR o metadata se localiza un enlace de Pastebin dentro del propio audio (`wphPq0Aa`). En ese Pastebin aparece una passphrase cifrada que hay que descifrar.
*EN: The challenge starts with an audio: using listening/OCR tools or metadata, a Pastebin link found inside the audio itself (`wphPq0Aa`) is located. That Pastebin shows an encrypted passphrase that must be decrypted.*
### Task 2 — Decoding
**Explicación:** La passphrase descifrada (`Hm5R_4_P455mhp453!`) permite abrir el siguiente recurso cifrado. Los contenidos revelan una clave decifrada (`Cicada`) y conducen a una passphrase final (`Ju5T_4_P455phr453!`) con la que se accede al enlace de Imgur `https://imgur.com/a/c0ZSZga`.
*EN: The decrypted passphrase (`Hm5R_4_P455mhp453!`) unlocks the next encrypted resource. Its contents reveal a decrypted key (`Cicada`) and lead to a final passphrase (`Ju5T_4_P455phr453!`) that grants access to the Imgur link `https://imgur.com/a/c0ZSZga`.*
### Task 3 — Steganography
**Explicación:** En el álbum de Imgur hay una imagen; el archivo oculto se extrae con la herramienta *outguess*. Dentro aparece un hash, cuyo tipo hay que identificar: es SHA-512.
*EN: In the Imgur album there is an image; the hidden file is extracted with the *outguess* tool. Inside, a hash appears, whose type must be identified: it is SHA-512.*

```bash
# El nombre de archivo conocido es el hash: si el archivo es "xxxxx.txt"
# su nombre es el hash SHA512 -> tipo de hash sha512
# Pista: el texto extraído es en realidad un hash de 128 caracteres hex
```
### Task 4 — The Finale
**Explicación:** Se crackea el hash SHA-512 (wordlist) y el resultado conduce a otra Pastebin (`6FNiVLh5`). Ese contenido da un bit.ly (`https://bit.ly/39pw2NH`) que finalmente enlaza a la canción: *The Instar Emergence* (el tema vinculado al fin de la primera fase del rompecabezas).
*EN: The SHA-512 hash is cracked (wordlist) and the result leads to another Pastebin (`6FNiVLh5`). That content yields a bit.ly (`https://bit.ly/39pw2NH`) which finally links to the song: *The Instar Emergence* (the track tied to the end of the first phase of the puzzle).*

```bash
# También se puede crackear con hashcat o john
john --wordlist=rockyou.txt hash.sha512
# -> link pastebin -> bit.ly -> cancion
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the link inside of the audio? | `https://pastebin.com/wphPq0Aa` |
| 2 | What is the decrypted passphrase? | `Hm5R_4_P455mhp453!` |
| 3 | What is the decrypted key? | `Cicada` |
| 4 | What is the final passphrase | `Ju5T_4_P455phr453!` |
| 5 | What link is given? | `https://imgur.com/a/c0ZSZga` |
| 6 | What tool did you use to find the hidden file | `outguess` |
| 7 | What is the Hash type? | `SHA512` |
| 8 | What is the Link from the hash? | `https://pastebin.com/6FNiVLh5` |
| 9 | What is the link? | `https://bit.ly/39pw2NH` |
| 10 | What is the song linked? | `The Instar Emergence` |
---
**Metodología:** Escuchar/inspeccionar audio → enlace Pastebin → descifrar passphrase → abrir archivo → clave y passphrase final → Imgur → outguess (extraer archivo oculto) → identificar tipo de hash (SHA512) → crackear con john/hashcat → segunda Pastebin → bit.ly → identificar la canción final.
**Learning chain:** OSINT de audio → criptografía de passphrases → esteganografía (outguess) → hash identification & cracking (SHA512) → encadenado de URLs → resolución final (The Instar Emergence).
**Lección:** *Los rompecabezas tipo Cicada enseñan a no parar en la primera pista: cada capa "descifrada" es solo la llave de la siguiente, y la herramienta (outguess), el tipo de hash y las URLs acortadas son eslabones de una misma cadena OSINT.*
**MITRE ATT&CK:** T1593 (Gather Victim Org Information, OSINT), T1552.004 (Unsecured Credentials), T1114 (Email Collection, por el vector de enlaces), T1059, T1027 (Obfuscated Files - esteganografía), T1550 (Use Alternate Authentication Material - passphrases).
**Fuente:** [TryHackMe - Cicada-3301 Vol_1](https://tryhackme.com/room/cicada3301vol1)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.