# IDOR - Santa’s Little IDOR

| **Dificultad** | Easy | **Tipo** | CTF (Free Room) | **Slug** | `day05idorsantaslittleidor` | | **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber25) | | **Sección** | Advent of Cyber Tryhackme | | **Fuente** | texto oficial THM + anotaciones propias | | **Componentes** | IDOR / Broken Access Control / Web Exploitation / Privilege Escalation / UUID | | **Impacto** | Día 05 del AoC 2025: identificación y explotación de IDOR (referencia directa insegura a objetos) y escalada de privilegios horizontal |

---

**Contexto:** Día 05 del calendario Advent of Cyber 2025 ("IDOR - Santa’s Little IDOR"). Reto web centrado en Insecure Direct Object Reference (IDOR): cambiar el identificador de un objeto en la URL/parámetro (p. ej. `view_accounts`) para acceder a datos ajenos. Se repasan conceptos de autenticación vs. autorización y de escalada de privilegios vertical/horizontal, así como la decodificación de UUID. Documento original bilingüe (ES/EN); se conservan apuntes y respuestas verbatim.

---

## Solucionario

### Día 05: IDOR - Santa’s Little IDOR

**Explicación:** Apuntes del laboratorio (notas bilingües originales):

- IDOR (insecure direct object reference): type of vulnerability
- web server should check to ensure you are allowed to view data (ex: `https://awesome.website.thm/TrackPackage?packageID=1001`, you would just have to change the ID to get information that ur not supposed to be able to access)
- Authentication: essentially, verification of who you are
- Authorization: verification of your permissions
- authentication first, then authorization
- `inspect` a web page to search for vulnerabilities
- UUID (universal unique identifier): [https://www.uuidtools.com/decode](url)

privilege escalation:
- vertical privilege escalation: gaining access to more features
- horizontal privilege escalation: gain access to features you are authorized to use, but data you are not supposed to have access to (like someone else's details)

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What does IDOR stand for? | `Insecure Direct Object Reference` |
| 2 | What type of privilege escalation are most IDOR cases? | `Horizontal` |
| 3 | Exploiting the IDOR found in the view_accounts parameter, what is the user_id of the parent that has 10 children? | `15` |

---

**Metodología:**

1. Definir el concepto de IDOR y diferenciar autenticación vs. autorización

2. Inspeccionar la página y localizar parámetros manipulables (view_accounts)

3. Iterar sobre los IDs (fuerza bruta manual/enumeración) para encontrar el usuario con 10 hijos

**Learning chain:** Broken Access Control -> IDOR -> Horizontal privilege escalation

**Lección:** *Un IDOR aparece cuando el servidor confía en el identificador enviado por el usuario sin verificar autorización; los casos típicos son escaladas horizontales (acceder a datos de otros usuarios con el mismo rol).*

**MITRE ATT&CK:**

- T1106 - Native API / T1590 - Gather Victim Network Information (enumeración de IDs)

- T1078 - Valid Accounts (acceso no autorizado con cuenta válida)

- T1213 - Data from Information Repositories

**Fuente:** [TryHackMe - IDOR - Santa’s Little IDOR](https://tryhackme.com/room/adventofcyber25)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.