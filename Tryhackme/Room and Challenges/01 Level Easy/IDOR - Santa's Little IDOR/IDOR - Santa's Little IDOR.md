# IDOR - Santa's Little IDOR

| **Dificultad** | Medium |
| **Tipo** | walkthrough |
| **Slug** | `idor-aoc2025-zl6MywQid9` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/idor-aoc2025-zl6MywQid9) |
| **Sección** | Advent of Cyber 2025 |
| **Fuente** | THM |
| **Componentes** | IDOR, horizontal escalation, API enumeration |
| **Impacto** | Acceso no autorizado a datos de otros usuarios vía IDOR |

---

**Contexto:** Durante el Advent of Cyber 2025 (Día 5), la plataforma de Santa contiene una API mal diseñada que expone objetos referenciados directamente por identificadores (IDOR). Al manipular el parámetro `view_accounts` es posible acceder a cuentas de otros padres/madres sin autorización, un caso típico de escalada horizontal. El reto también incluye endpoints de hijos codificados en base64 o MD5, así como un sistema de cupones (`vouchers`) con un mecanismo de reclamación explotable.

## Solucionario

### Task 1: Conceptos IDOR

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What does IDOR stand for? | `Insecure Direct Object Reference` |
| 2 | What type of privilege escalation are most IDOR cases? | `Horizontal` |

### Task 2: Explotando el IDOR

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Exploiting the IDOR found in the view_accounts parameter, what is the user_id of the parent that has 10 children? | `15` |

### Task 3: Bonus - Endpoints de hijos y cupones

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Using base64 or md5 child endpoint, find the id_number of the child born on 2019-04-17? | `19` |
| 2 | Using /parents/vouchers/claim, find the voucher valid on 20 Nov 2025 (generated 20:00-24:00 UTC). Voucher code? | `22643e00-c655-11f0-ac99-026ccdf7d769` |

---

**Metodología:** Se enumeró la API de la plataforma identificando el parámetro `view_accounts`, que devuelve los datos del usuario referenciado por su ID. Al variar el identificador se confirmó la ausencia de control de acceso a nivel de objeto (función directa), logrando leer cuentas de otros usuarios (escalada horizontal). Para la parte bonus se explotó el endpoint de hijos, localizando la fecha de nacimiento objetivo y extrayendo su `id_number`. Finalmente se abusó de `/parents/vouchers/claim` para reclamar un cupón generado en la franja horaria UTC indicada, obteniendo el código de voucher.

**Learning chain:** Enumeración de API → detección de acceso a objetos por ID → IDOR → escalada horizontal → explotación de endpoints secundarios (hijos, vouchers).

**MITRE ATT&CK:** T1087 (Account Discovery), T1213 (Data from Information Repositories), T1106 (Native API abuse), T1530 (Data from Cloud Storage).

**Fuente:** [TryHackMe - IDOR - Santa's Little IDOR](https://tryhackme.com/r/room/idor-aoc2025-zl6MywQid9)
