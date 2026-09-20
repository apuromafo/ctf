# AWS Security - S3cret Santa

| **Dificultad** | Easy |
| **Tipo** | walkthrough |
| **Slug** | `cloudenum-aoc2025-y4u7i0o3p6` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/cloudenum-aoc2025-y4u7i0o3p6) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | AWS CLI, IAM, S3, sts get-caller-identity |
| **Impacto** | Enumeration — enumeración de entorno AWS para descubrir planes del Secret Santa |

---

**Contexto:** Durante el Día 23 del Advent of Cyber 2025, debemos enumerar un entorno AWS usando la CLI para encontrar los planes secretos del Secret Santa. Comenzamos obteniendo la identidad del caller y luego exploramos IAM policies, roles y buckets S3 para localizar el archivo con la contraseña cloud. La sala combina la enumeración de la identidad (STS), el análisis de políticas IAM y el acceso a buckets S3 mediante la asunción de roles.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Primer contacto con el entorno AWS del reto. Ejecutando `aws sts get-caller-identity` se obtiene la identidad asociada a las credenciales configuradas, y de la salida se extrae el número mostrado en el parámetro "Account" de la respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Run aws sts get-caller-identity. What is the number shown for the "Account" parameter? | `123456789012` |

### Task 2: Enumeración IAM / IAM Enumeration

**Explicación:** Se enumeran los componentes de IAM del entorno: se identifica qué componente describe los permisos que se asignan a un usuario o grupo (una **Policy**) y se obtiene el nombre de la política asignada a la cuenta `sir.carrotbane`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What IAM component is used to describe the permissions to be assigned to a user or a group? | `Policy` |
| 2 | What is the name of the policy assigned to sir.carrotbane? | `SirCarrotbanePolicy` |

### Task 3: Enumeración S3 / S3 Enumeration

**Explicación:** Se exploran los buckets S3 y los roles disponibles. Asumiendo el rol `bucketmaster` se obtienen permisos adicionales, y de la lista de acciones permitidas se identifica la acción extra que puede realizarse además de `GetObject` y `ListBucket`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Apart from GetObject and ListBucket, what other action can be taken by assuming the bucketmaster role? | `ListAllMyBuckets` |

### Task 4: Los planes del Secret Santa / The Secret Santa Plans

**Explicación:** Con el acceso al bucket se localiza el archivo `cloud_password.txt` y se leen sus contenidos, revelando los planes secretos del Secret Santa y la flag de la sala.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What are the contents of the cloud_password.txt file? | `THM{more_like_sir_cloudbane}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Run aws sts get-caller-identity. What is the number shown for the "Account" parameter? | `123456789012` |
| 2 | What IAM component is used to describe the permissions to be assigned to a user or a group? | `Policy` |
| 3 | What is the name of the policy assigned to sir.carrotbane? | `SirCarrotbanePolicy` |
| 4 | Apart from GetObject and ListBucket, what other action can be taken by assuming the bucketmaster role? | `ListAllMyBuckets` |
| 5 | What are the contents of the cloud_password.txt file? | `THM{more_like_sir_cloudbane}` |

---

**Metodología:** Se utilizó AWS CLI para enumerar la identidad del caller con `aws sts get-caller-identity`, luego se exploraron IAM users/policies para descubrir permisos asignados a sir.carrotbane, y finalmente se enumeraron buckets S3 asumiendo el rol bucketmaster para acceder al archivo cloud_password.txt.

### Cadena de ataque / Attack Chain

```
aws sts get-caller-identity -> Account 123456789012
  -> Enumeración IAM -> Policy + SirCarrotbanePolicy
  -> Enumeración S3 -> asumir rol bucketmaster
  -> Acción extra ListAllMyBuckets
  -> Acceso a bucket -> cloud_password.txt
  -> THM{more_like_sir_cloudbane}
```

**Learning chain:** AWS STS → IAM Policies & Users → S3 Enumeration → Bucket Access via Role Assumption → Secret Extraction

**Lección:** *La enumeración metódica de un entorno AWS con la CLI (identidad STS, políticas IAM y buckets S3) y la asunción de roles permite descubrir y acceder a recursos que exponen información sensible, como la contraseña cloud del Secret Santa.*

**MITRE ATT&CK:** T1078.004 - Valid Accounts: Cloud Accounts, T1580 - Cloud Infrastructure Discovery

**Fuente:** [TryHackMe - AWS Security - S3cret Santa](https://tryhackme.com/r/room/cloudenum-aoc2025-y4u7i0o3p6)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.