# Management Wants a Word [HARD]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** HARD
* **Tipo / Type:** CTF (Evento "Hacker Holidays 2026: The Byte Lotus Hotel")
* **Slug:** `hh-managementwantsaword-6bf3cc41`
* **Link:** https://tryhackme.com/room/hh-managementwantsaword-6bf3cc41
* **Sección / Section:** 03 Level Hard
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=hh-managementwantsaword-6bf3cc41` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala gratuita de evento (Hacker Holidays 2026: The Byte Lotus Hotel). El tema es la **cadena forense Windows + criptografía**: triage KAPE descargable con el que se extraen hives SAM/SYSTEM, se crackea el NT hash de un usuario, y con su password + la MasterKey DPAPI se descifran las credenciales guardadas en Chrome, que finalmente abren un contenedor VeraCrypt con la flag en un PDF.
> **EN:** Free event room (Hacker Holidays 2026: The Byte Lotus Hotel). The theme is a **Windows forensics + crypto chain**: a downloadable KAPE triage from which SAM/SYSTEM hives are extracted, a user's NT hash is cracked, and with that password plus the DPAPI MasterKey the credentials stored in Chrome are decrypted, which finally open a VeraCrypt container holding the flag in a PDF.

### Task 1 - Hacker Holidays Storyline: Act 4 – Sunrise

> **ES:** Tarea narrativa introductoria que cierra la historia del evento: el equipo logra escapar del hotel Byte Lotus mientras "Management" (la directiva comprometida) finalmente "wants a word" (quiere hablar / pedir cuentas). No contiene preguntas; solo prepara el contexto para la tarea forense del Day 14.
> **EN:** Introductory narrative task that closes the event story: the team escapes the Byte Lotus hotel while "Management" (the compromised executive) finally "wants a word". No questions; it only sets the context for the Day 14 forensics task.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| (Informational) | Tarea informativa de historia. Sin preguntas. |

### Task 2 - Hacker Holidays: Day 14

> **ES:** Se descarga un triage KAPE de la máquina Windows del usuario `vera`. Con `secretsdump.py SAMP/SYSTEM` del hive se obtiene el NT hash `1241186a4aac4f34f4bf7ace71b396a8`, que se crackea con hashcat y rockyou → `minivera`. Con el SID `S-1-5-21-2529683458-431225740-1723070931-1000` se localiza la MasterKey DPAPI `c90719ef-5b98-474e-b934-136d606a702a`, que descifra las credenciales del perfil "Chrome For Testing" → password `Wh4t1sV3raD0inG0nTh1sH0st`. La pista `1.26.29` apunta a VeraCrypt: se monta el contenedor `C:\Users\vera\Documents\backup` (100 MB, AES-256-XTS, SHA-512, 500k iteraciones) con esa password → dentro, `important_invoice_byte_lotus.pdf` contiene la flag (en una imagen del PDF). 1 pregunta.
> **EN:** A KAPE triage of the Windows machine of user `vera` is downloaded. `secretsdump.py SAM/SYSTEM` from the hive yields the NT hash `1241186a4aac4f34f4bf7ace71b396a8`, cracked with hashcat + rockyou → `minivera`. Using SID `S-1-5-21-2529683458-431225740-1723070931-1000` the DPAPI MasterKey `c90719ef-5b98-474e-b934-136d606a702a` is located, which decrypts the "Chrome For Testing" profile credentials → password `Wh4t1sV3raD0inG0nTh1sH0st`. The hint `1.26.29` points to VeraCrypt: mount the `C:\Users\vera\Documents\backup` container (100 MB, AES-256-XTS, SHA-512, 500k iterations) with that password → inside, `important_invoice_byte_lotus.pdf` holds the flag (in an image of the PDF). 1 question.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag? | `THM{1t_w4s_V3r4_A11_Al0ng?!}` |

## Metodología / Methodology

1. **Paso / Step - Triage KAPE:** Se descarga el triage del host Windows y se descomprime. Aparecen hives de registro (SAM, SYSTEM), perfiles de usuario y la estructura de `AppData` de Chrome.
2. **Paso / Step - Extracción de hives:** Con `secretsdump.py SAM SYSTEM` de `impacket` se vuelcan los hashes locales; del usuario `vera` se obtiene el NT hash `1241186a4aac4f34f4bf7ace71b396a8`.
3. **Paso / Step - Cracking:** `hashcat -m 1000` con rockyou crackea el NT hash → password `minivera`.
4. **Paso / Step - MasterKey DPAPI:** Con el SID del usuario (`S-1-5-21-2529683458-431225740-1723070931-1000`) se localiza su MasterKey DPAPI `c90719ef-5b98-474e-b934-136d606a702a`; su descifrado en Windows usa derivación "domain" sobre la password del usuario (`minivera`).
5. **Paso / Step - Credenciales de Chrome:** Con la MasterKey se descifran las credenciales del perfil "Chrome For Testing" (`Login Data` DPAPI) → password guardada `Wh4t1sV3raD0inG0nTh1sH0st`.
6. **Paso / Step - VeraCrypt:** La pista `1.26.29` (versión de VeraCrypt) indica montar el contenedor `C:\Users\vera\Documents\backup` (100 MB, AES-256-XTS, SHA-512, 500k iteraciones) con esa password.
7. **Paso / Step - Flag:** Dentro del contenedor está `important_invoice_byte_lotus.pdf`; leyendo el PDF (la flag aparece en una imagen incrustada) se obtiene `THM{1t_w4s_V3r4_A11_Al0ng?!}`.

### Cadena de ataque / Attack Chain

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

**Lección:** El password reuse entre cuentas y contenedores, unido al DPAPI que protege las credenciales del navegador, convierte una cadena forense completa (hives → cracking → MasterKey → Chrome → VeraCrypt) en una sola flag.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.