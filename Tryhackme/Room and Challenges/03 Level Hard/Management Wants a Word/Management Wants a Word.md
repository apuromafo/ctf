# Management Wants a Word

| **Dificultad** | Hard |
| **Tipo** | CTF |
| **Slug** | `hh-managementwantsaword-6bf3cc41` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/hh-managementwantsaword-6bf3cc41) |
| **Sección** | 03 Level Hard |
| **Fuente** | Web (API THM `api/v2/rooms/tasks?roomCode=hh-managementwantsaword-6bf3cc41` + websearch de walkthroughs) |
| **Componentes** | KAPE / secretsdump.py / hashcat / DPAPI / Chrome / VeraCrypt |
| **Impacto** | Cadena forense completa (hives SAM/SYSTEM → cracking → DPAPI MasterKey → Chrome → VeraCrypt) que culmina en la obtención de la flag desde un contenedor cifrado. |

---

**Contexto:** Sala gratuita de evento (Hacker Holidays 2026: The Byte Lotus Hotel). El tema es la cadena forense Windows + criptografía: triage KAPE descargable con el que se extraen hives SAM/SYSTEM, se crackea el NT hash de un usuario, y con su password + la MasterKey DPAPI se descifran las credenciales guardadas en Chrome, que finalmente abren un contenedor VeraCrypt con la flag en un PDF.

## Solucionario

### Task 1: Hacker Holidays Storyline: Act 4 – Sunrise

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Informational) | Tarea informativa de historia. Sin preguntas. |

### Task 2: Hacker Holidays: Day 14

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{1t_w4s_V3r4_A11_Al0ng?!}` |

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

**Learning chain:** Triage KAPE → Extracción de hives SAM/SYSTEM → Cracking NT hash → Localización de DPAPI MasterKey → Descifrado de credenciales Chrome → Montaje de contenedor VeraCrypt → Extracción de flag desde PDF

**MITRE ATT&CK:** T1003.002 (OS Credential Dumping: SAM), T1110.002 (Brute Force: Password Cracking), T1555.003 (Credentials from Password Stores: Windows Credential Manager), T1005 (Data from Local System)

**Fuente:** [TryHackMe - Management Wants a Word](https://tryhackme.com/r/room/hh-managementwantsaword-6bf3cc41)
