# IDOR - Santa’s Little IDOR [EASY]

### Información de la Sala / Room Information

| Propiedad / Property | Valor / Value |
| --- | --- |
| **Nombre / Name** | IDOR - Santa’s Little IDOR |
| **Evento / Event** | Advent of Cyber 2025 — Día 05 |
| **Sala / Room URL** | https://tryhackme.com/room/adventofcyber25 |
| **Dificultad / Difficulty** | Easy |
| **Descripción / Description** | Día 05 del calendario AoC 2025 (IDOR - Santa’s Little IDOR). Solución/respuestas del reto diario. |

---


- IDOR(insecure direct object reference): type of vulnerability
- web server should check to ensure you are allowed to view data (ex: `https://awesome.website.thm/TrackPackage?packageID=1001`, you would just have to change the ID to get information that ur not supposed to be able to access)

- Authentication: essentially, verification of who you are 
- Authorization: verification of your permissions

- authentication first, then authorization
- `inspect` a web page to search for vulnerabilities
- UUID (universal unique identifier): [https://www.uuidtools.com/decode](url)

privilege escalation: 
- vertical privilege escalation: gaining access to more features
- horizontal privilege escalation: gain access to features you are authorized to use, but data you are not supposed to have access to (like someone else's details) 

## Respuestas / Answers
- What does IDOR stand for? : `Insecure Direct Object Reference`
- What type of privilege escalation are most IDOR cases? : `Horizontal`
- Exploiting the IDOR found in the view_accounts parameter, what is the user_id of the parent that has 10 children? : `15`

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
