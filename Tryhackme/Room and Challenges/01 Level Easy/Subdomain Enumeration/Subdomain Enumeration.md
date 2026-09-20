# Subdomain Enumeration

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `subdomainenumeration` | [TryHackMe](https://tryhackme.com/room/subdomainenumeration) | 01 Level Easy | TryHackMe | DNS, OSINT, crt.sh, Brute Force, Virtual Hosting | Descubrimiento de subdominios y vhosts mediante técnicas OSINT, fuerza bruta y virtual hosting |

---

**Contexto:** Sala educativa sobre las tres técnicas principales de enumeración de subdominios: OSINT, fuerza bruta y virtual hosting. Se descubren subdominios de `tryhackme.com` y de `acmeitsupport.thm`, incluyendo los subdominios de segundo nivel `api.acmeitsupport.thm` y `web55.acmeitsupport.thm`. El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

> **ES:** Se enumeran subdominios de `tryhackme.com` (OSINT y fuerza bruta) y de `acmeitsupport.thm`, encontrando `store.tryhackme.com`, `api.acmeitsupport.thm` y `web55.acmeitsupport.thm`; la parte de virtual hosting revela los valores `delta` y `yellow`.
> **EN:** Subdomains of `tryhackme.com` (OSINT and brute force) and `acmeitsupport.thm` are enumerated, finding `store.tryhackme.com`, `api.acmeitsupport.thm` and `web55.acmeitsupport.thm`; the virtual hosting section reveals the values `delta` and `yellow`.

## Solucionario

### Task 1: Métodos de enumeración / Enumeration Methods

**Explicación:** Se identifican los tres métodos de enumeración de subdominios que se practican en la sala: fuerza bruta, OSINT y virtual hosting. Todo el contenido original se conserva verbatim:

1. 1. Brute Force
   2. OSINT
   3. Virtual Host

### Task 2: Subdominio encontrado por OSINT / OSINT-Discovered Subdomain

**Explicación:** Se descubre mediante OSINT el primer subdominio perteneciente al dominio objetivo. Todo el contenido original se conserva verbatim:

2. store.tryhackme.com

### Task 3: Subdominio del dominio principal / Main-Domain Subdomain

**Explicación:** Se confirma el subdominio del dominio principal mediante la enumeración. Todo el contenido original se conserva verbatim:

3. store.tryhackme.com

### Task 4: Subdominio por fuerza bruta / Brute-Force Subdomain

**Explicación:** Se aplica fuerza bruta DNS para descubrir un subdominio del dominio `acmeitsupport.thm`. Todo el contenido original se conserva verbatim:

4. api.acmeitsupport.thm

### Task 5: Sub-subdominio por fuerza bruta / Brute-Force Sub-subdomain

**Explicación:** Se continúa la fuerza bruta sobre el subdominio descubierto hasta encontrar un sub-subdominio adicional. Todo el contenido original se conserva verbatim:

5. web55.acmeitsupport.thm

### Task 6: Virtual Host / Virtual Hosting

**Explicación:** Se aplica la técnica de virtual hosting para descubrir los hosts virtuales del servidor. Todo el contenido original se conserva verbatim:

6. 1. delta
   2. yellow

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Método de enumeración 1 / Enumeration method 1 | `Brute Force` |
| 2 | Método de enumeración 2 / Enumeration method 2 | `OSINT` |
| 3 | Método de enumeración 3 / Enumeration method 3 | `Virtual Host` |
| 4 | Subdominio descubierto / Discovered subdomain | `store.tryhackme.com` |
| 5 | Subdominio del dominio principal / Main-domain subdomain | `store.tryhackme.com` |
| 6 | Subdominio de acmeitsupport.thm / acmeitsupport.thm subdomain | `api.acmeitsupport.thm` |
| 7 | Sub-subdominio de acmeitsupport.thm / acmeitsupport.thm sub-subdomain | `web55.acmeitsupport.thm` |
| 8 | Primer valor del virtual host / First virtual host value | `delta` |
| 9 | Segundo valor del virtual host / Second virtual host value | `yellow` |

---

**Metodología:** Enumeración pasiva mediante OSINT con crt.sh y otros servicios → fuerza bruta de subdominios de `tryhackme.com` y `acmeitsupport.thm` → roteo de sub-subdominios → comprobación de virtual hosts en el servidor objetivo.

### Cadena de ataque / Attack Chain

```text
OSINT (crt.sh) -> store.tryhackme.com -> fuerza bruta DNS -> api.acmeitsupport.thm -> web55.acmeitsupport.thm -> virtual hosting -> delta -> yellow
```

**Learning chain:** OSINT --> crt.sh --> store.tryhackme.com --> DNS brute force --> api.acmeitsupport.thm --> sub-subdomain brute force --> web55.acmeitsupport.thm --> virtual host enumeration --> delta/yellow

**Lección:** *La enumeración de subdominios combina fuentes OSINT, fuerza bruta DNS y virtual hosting para ampliar la superficie de ataque y descubrir servicios ocultos de una organización.*

**MITRE ATT&CK:** T1596 (Search Open Technical Databases – DNS/crt.sh), T1590 (Gather Victim Network Information), T1046 (Network Service Discovery – virtual hosting)

**Fuente:** [TryHackMe - Subdomain Enumeration](https://tryhackme.com/room/subdomainenumeration)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.