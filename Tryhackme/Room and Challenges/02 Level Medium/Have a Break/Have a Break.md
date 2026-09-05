# Have a Break [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** CTF
* **Slug:** `haveabreak`
* **Link:** https://tryhackme.com/room/haveabreak
* **Sección / Section:** 02 Level Medium
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=haveabreak` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de OSINT / análisis de email sobre el caso KitKat de marzo 2026 (Italia → Polonia). A partir de archivos descargados (memo PDF, email .eml, imagen de dashcam, acceso CSV y exportación de comunicaciones) se reconstruye quién, cómo y dónde: el proveedor VPN del remitente anónimo, la gasolinera donde se vio el vehículo, el momento del acceso sospechoso y las identidades del delator y del denunciante.
> **EN:** OSINT / email analysis room about the March 2026 KitKat case (Italy → Poland). From downloaded files (PDF memo, .eml email, dashcam image, access CSV and communications export) it reconstructs who, how and where: the VPN provider of the anonymous sender, the petrol station where the vehicle was seen, the moment of the suspicious access and the identities of the leaker and the whistleblower.

### Task 1 - Investigation

> **ES:** El briefing `ecta_memo.pdf` da el contexto del caso. `exhibit_a.eml`: en los headers, la IP `193.32.249.132` resuelve por whois a `31173 Services AB` → proveedor VPN Mullvad. `exhibit_b.png` (dashcam): triangulando las distancias (Brno 45 km, Olomouc 27 km) se ubica la gasolinera Orlen de Hulín (Kroměřížská 1281, 768 24). En `access_log.csv`: un export nocturno del 25-mar de `ROUTE_IT_PL_Q1_2026.pdf` corresponde a BR-0291 (el delator) y un login posterior a BR-0312 (el denunciante). `comms_export.txt` muestra un intento de acceso a la carpeta compartida desde `kraliknovak09@gmail.com`; un OSINT de email (Epieos) revela el perfil de Google de Radovan Blšťák. 6 preguntas.
> **EN:** The briefing `ecta_memo.pdf` gives the case context. `exhibit_a.eml`: in the headers, IP `193.32.249.132` resolves via whois to `31173 Services AB` → Mullvad VPN provider. `exhibit_b.png` (dashcam): triangulating the distances (Brno 45 km, Olomouc 27 km) locates the Orlen petrol station in Hulín (Kroměřížská 1281, 768 24). In `access_log.csv`: a night export on 25-Mar of `ROUTE_IT_PL_Q1_2026.pdf` maps to BR-0291 (the leaker) and a later login to BR-0312 (the whistleblower). `comms_export.txt` shows an attempted access to the shared folder from `kraliknovak09@gmail.com`; an email OSINT (Epieos) reveals the Google profile of Radovan Blšťák. 6 questions.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Which VPN service was used to send the anonymous email from the .eml file? | `Mullvad` |
| What is the full street address of the petrol station where the missing vehicle was last seen? | `Kroměřížská 1281, 768 24 Hulín, Czechia` |
| At what time did the suspicious action take place in the route planning system on March 25th, 2026? Format: HH:MM:SS | `22:14:09` |
| What is the employee ID of the person who sent the anonymous email? | `BR-0312` |
| What is the employee ID of the employee responsible for leaking the shipment details? | `BR-0291` |
| What is the leaker's full name? | `Radovan Blšťák` |

## Metodología / Methodology

1. **Paso / Step - Briefing:** Se lee `ecta_memo.pdf` para conocer el caso (KitKat, marzo 2026, Italia → Polonia).
2. **Paso / Step - Headers del email:** En `exhibit_a.eml` la IP de origen es `193.32.249.132`; whois → `31173 Services AB` → proveedor VPN Mullvad.
3. **Paso / Step - Dashcam:** En `exhibit_b.png`, triangulando con los odómetros (Brno 45 km, Olomouc 27 km) se localiza la gasolinera Orlen de Hulín, dirección `Kroměřížská 1281, 768 24 Hulín, Czechia`.
4. **Paso / Step - Access log:** El `access_log.csv` muestra un export nocturno (25-mar, `22:14:09`) de `ROUTE_IT_PL_Q1_2026.pdf` desde BR-0291 (delator) y un login posterior de BR-0312 (denunciante/remitente).
5. **Paso / Step - Comms export:** `comms_export.txt` revela el intento de acceso a la carpeta compartida desde `kraliknovak09@gmail.com`.
6. **Paso / Step - OSINT del email:** Epieos sobre el Gmail → perfil de Google → Radovan Blšťák.

### Cadena de ataque / Attack Chain

```
ecta_memo.pdf (briefing KitKat 03/2026)
  -> exhibit_a.eml -> headers -> IP 193.32.249.132
  -> whois -> 31173 Services AB -> Mullvad (VPN)
  -> exhibit_b.png (dashcam) -> triangulación Brno 45km / Olomouc 27km
  -> gasolinera Orlen Hulín -> Kroměřížská 1281, 768 24 Hulín
  -> access_log.csv -> export 25-mar 22:14:09 de ROUTE_IT_PL_Q1_2026.pdf
  -> BR-0291 (delator) / BR-0312 (denunciante)
  -> comms_export.txt -> kraliknovak09@gmail.com
  -> Epieos -> perfil Google -> Radovan Blšťák
```

**Lección:** Los logs de acceso y los headers de los emails son la cadena de evidencia; además, los proveedores de VPN "anti-log" aún dejan el whois del ASN como pista.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
