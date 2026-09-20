# IDOR - Santa's Little IDOR

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | walkthrough | `idor-aoc2025-zl6MywQid9` | [TryHackMe](https://tryhackme.com/room/idor-aoc2025-zl6MywQid9) | Advent of Cyber 2025 | THM | IDOR, horizontal escalation, API enumeration | Acceso no autorizado a datos de otros usuarios vía IDOR |

> **Objeto:** Explotar un IDOR en la API de la plataforma de Santa (Advent of Cyber 2025, Día 5) para acceder a cuentas de otros padres/madres y explotar los endpoints de hijos y de cupones.

---

**Contexto:** Durante el Advent of Cyber 2025 (Día 5), la plataforma de Santa contiene una API mal diseñada que expone objetos referenciados directamente por identificadores (IDOR). Al manipular el parámetro `view_accounts` es posible acceder a cuentas de otros padres/madres sin autorización, un caso típico de escalada horizontal. El reto también incluye endpoints de hijos codificados en base64 o MD5, así como un sistema de cupones (`vouchers`) con un mecanismo de reclamación explotable.

> **ES:** Reto del Advent of Cyber 2025 centrado en un IDOR sobre el parámetro `view_accounts`: manipulando el identificador se accede a cuentas de otros usuarios (escalada horizontal), y se explotan endpoints secundarios de hijos (base64/MD5) y de reclamación de cupones.
> **EN:** An Advent of Cyber 2025 challenge focused on an IDOR in the `view_accounts` parameter: by tampering with the identifier you reach other users' accounts (horizontal escalation), then abuse secondary child endpoints (base64/MD5) and a voucher claiming mechanism.

## Solucionario

### Task 1: Conceptos IDOR / IDOR Concepts

**Explicación:** Repaso conceptual del IDOR y de la escalada de privilegios asociada: la mayoría de los IDOR permiten una escalada horizontal, accediendo a datos de otros usuarios del mismo nivel.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What does IDOR stand for? | `Insecure Direct Object Reference` |
| 2 | What type of privilege escalation are most IDOR cases? | `Horizontal` |

### Task 2: Explotando el IDOR / Exploiting the IDOR

**Explicación:** Se explota la referencia directa del parámetro `view_accounts` variando el identificador para recorrer las cuentas y localizar al progenitor con 10 hijos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Exploiting the IDOR found in the view_accounts parameter, what is the user_id of the parent that has 10 children? | `15` |

### Task 3: Bonus - Endpoints de hijos y cupones / Bonus - Child endpoints and vouchers

**Explicación:** Parte opcional: los endpoints de hijos admiten identificadores codificados en base64 o MD5, permitiendo descubrir el `id_number` del hijo nacido el 2019-04-17; después se abusa del endpoint `/parents/vouchers/claim` para reclamar el cupón válido el 20 de noviembre de 2025.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Using base64 or md5 child endpoint, find the id_number of the child born on 2019-04-17? | `19` |
| 2 | Using /parents/vouchers/claim, find the voucher valid on 20 Nov 2025 (generated 20:00-24:00 UTC). Voucher code? | `22643e00-c655-11f0-ac99-026ccdf7d769` |

---

**Metodología:** Se enumeró la API de la plataforma identificando el parámetro `view_accounts`, que devuelve los datos del usuario referenciado por su ID. Al variar el identificador se confirmó la ausencia de control de acceso a nivel de objeto (función directa), logrando leer cuentas de otros usuarios (escalada horizontal). Para la parte bonus se explotó el endpoint de hijos, localizando la fecha de nacimiento objetivo y extrayendo su `id_number`. Finalmente se abusó de `/parents/vouchers/claim` para reclamar un cupón generado en la franja horaria UTC indicada, obteniendo el código de voucher.

### Cadena de ataque / Attack Chain

Enumeración de la API → detección de acceso a objetos por ID → manipulación de `view_accounts` → escalada horizontal a cuentas ajenas → explotación del endpoint de hijos (base64/MD5) → abuso de `/parents/vouchers/claim` → obtención del código de cupón.

**Learning chain:** Enumeración de API → detección de acceso a objetos por ID → IDOR → escalada horizontal → explotación de endpoints secundarios (hijos, vouchers).

**Lección:** *Una API no debe confiar en el identificador enviado por el cliente: cada petición sobre un objeto debe validar la autorización del usuario. Los endpoints "bonus" (hijos, cupones) amplían la superficie de explotación cuando heredan la misma falta de control de acceso.*

**MITRE ATT&CK:** T1087 (Account Discovery), T1213 (Data from Information Repositories), T1106 (Native API abuse), T1530 (Data from Cloud Storage).

**Fuente:** [TryHackMe - IDOR - Santa's Little IDOR](https://tryhackme.com/room/idor-aoc2025-zl6MywQid9)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.