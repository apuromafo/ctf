# Management Wants a Word

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | CTF | hh-managementwantsaword-6bf3cc41 | https://tryhackme.com/room/hh-managementwantsaword-6bf3cc41 | 03 Level Hard | Web (API THM `api/v2/rooms/tasks?roomCode=hh-managementwantsaword-6bf3cc41` + websearch de walkthroughs) | KAPE / secretsdump.py / hashcat / DPAPI / Chrome / VeraCrypt | Cadena forense completa (hives SAM/SYSTEM → cracking → DPAPI MasterKey → Chrome → VeraCrypt) que culmina en la obtención de la flag desde un contenedor cifrado. |

---

**Contexto:**
> **ES:** Sala gratuita de evento (Hacker Holidays 2026: The Byte Lotus Hotel). El tema es la cadena forense Windows + criptografía: triage KAPE descargable con el que se extraen hives SAM/SYSTEM, se crackea el NT hash de un usuario, y con su password + la MasterKey DPAPI se descifran las credenciales guardadas en Chrome, que finalmente abren un contenedor VeraCrypt con la flag en un PDF.
> **EN:** Free event room (Hacker Holidays 2026: The Byte Lotus Hotel). The theme is the Windows forensics + cryptography chain: a downloadable KAPE triage extracts SAM/SYSTEM hives, an NT hash is cracked, and with that password plus the DPAPI MasterKey the credentials stored in Chrome are decrypted, finally opening a VeraCrypt container with the flag inside a PDF.

## Solucionario

### Task 1: Hacker Holidays Storyline: Act 4 – Sunrise
**Explicación:** Tarea informativa de la historia de Hacker Holidays. No contiene preguntas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Informational) | Tarea informativa de historia. Sin preguntas. |

### Task 2: Hacker Holidays: Day 14
**Explicación:** La cadena forense KAPE → SAM/SYSTEM → NT hash (`1241186a4aac4f34f4bf7ace71b396a8`) → cracking (`minivera`) → MasterKey DPAPI → credenciales Chrome (`Wh4t1sV3raD0inG0nTh1sH0st`) → contenedor VeraCrypt culmina con la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{1t_w4s_V3r4_A11_Al0ng?!}` |

### Preguntas y Respuestas / Questions and Answers

| Task | Respuesta / Answer |
|---|---|
| 1.1 | `(Informational)` |
| 2.1 | `THM{1t_w4s_V3r4_A11_Al0ng?!}` |

---

**Metodología:**

1. Se descarga el triage KAPE del host Windows y se descomprime. Aparecen hives de registro (SAM, SYSTEM), perfiles de usuario y la estructura de `AppData` de Chrome.
2. Con `secretsdump.py SAM SYSTEM` de `impacket` se vuelcan los hashes locales; del usuario `vera` se obtiene el NT hash `1241186a4aac4f34f4bf7ace71b396a8`.
3. `hashcat -m 1000` con rockyou crackea el NT hash → password `minivera`.
4. Con el SID del usuario (`S-1-5-21-2529683458-431225740-1723070931-1000`) se localiza su MasterKey DPAPI `c90719ef-5b98-474e-b934-136d606a702a`; su descifrado en Windows usa derivación "domain" sobre la password del usuario (`minivera`).
5. Con la MasterKey se descifran las credenciales del perfil "Chrome For Testing" (`Login Data` DPAPI) → password guardada `Wh4t1sV3raD0inG0nTh1sH0st`.
6. La pista `1.26.29` (versión de VeraCrypt) indica montar el contenedor `C:\Users\vera\Documents\backup` (100 MB, AES-256-XTS, SHA-512, 500k iteraciones) con esa password.
7. Dentro del contenedor está `important_invoice_byte_lotus.pdf`; leyendo el PDF (la flag aparece en una imagen incrustada) se obtiene la flag.

```
KAPE triage (Windows)
  -> secretsdump.py SAM/SYSTEM -> NT hash 1241186a4aac4f34f4bf7ace71b396a8
  -> hashcat -m 1000 (rockyou) -> minivera
  -> SID S-1-5-21-2529683458-431225740-1723070931-1000
  -> DPAPI MasterKey c90719ef-5b98-474e-b934-136d606a702a
  -> Chrome (Chrome For Testing) creds -> Wh4t1sV3raD0inG0nTh1sH0st
  -> VeraCrypt container C:\Users\vera\Documents\backup (AES-256-XTS, SHA-512)
  -> important_invoice_byte_lotus.pdf (imagen en el PDF) -> THM{1t_w4s_V3r4_A11_Al0ng?!}
```

### Cadena de ataque / Attack Chain
1. Triage KAPE del host Windows.
2. Volcado de los hives SAM/SYSTEM y extracción del NT hash.
3. Cracking del hash con hashcat.
4. Localización y descifrado de la MasterKey DPAPI.
5. Descifrado de las credenciales de Chrome.
6. Montaje del contenedor VeraCrypt.
7. Extracción de la flag desde el PDF.

**Learning chain:** Triage KAPE → Extracción de hives SAM/SYSTEM → Cracking NT hash → Localización de DPAPI MasterKey → Descifrado de credenciales Chrome → Montaje de contenedor VeraCrypt → Extracción de flag desde PDF

**Lección:** *Las credenciales protegidas por DPAPI se convierten en un eslabón de la cadena: password + MasterKey abren Chrome y, con ello, el contenedor cifrado final.*

**MITRE ATT&CK:** T1003.002 (OS Credential Dumping: SAM), T1110.002 (Brute Force: Password Cracking), T1555.003 (Credentials from Password Stores: Windows Credential Manager), T1005 (Data from Local System)

**Fuente:** [TryHackMe - Management Wants a Word](https://tryhackme.com/room/hh-managementwantsaword-6bf3cc41)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.