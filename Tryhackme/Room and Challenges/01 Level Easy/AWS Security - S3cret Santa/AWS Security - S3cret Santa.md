# AWS Security - S3cret Santa

| **Dificultad** | Easy |
| **Tipo** | walkthrough |
| **Slug** | `cloudenum-aoc2025-y4u7i0o3p6` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/cloudenum-aoc2025-y4u7i0o3p6) |
| **Sección** | Advent of Cyber 2025 |
| **Componentes** | AWS CLI, IAM, S3, sts get-caller-identity |
| **Impacto** | Enumeration — enumeración de entorno AWS para descubrir planes del Secret Santa |

---

**Contexto:** Durante el Día 23 del Advent of Cyber 2025, debemos enumerar un entorno AWS usando la CLI para encontrar los planes secretos del Secret Santa. Comenzamos obteniendo la identidad del caller y luego exploramos IAM policies, roles y buckets S3 para localizar el archivo con la contraseña cloud.

## Solucionario

### Task 1: Introduction

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Run aws sts get-caller-identity. What is the number shown for the "Account" parameter? | `123456789012` |

### Task 2: IAM Enumeration

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What IAM component is used to describe the permissions to be assigned to a user or a group? | `Policy` |
| 2 | What is the name of the policy assigned to sir.carrotbane? | `SirCarrotbanePolicy` |

### Task 3: S3 Enumeration

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Apart from GetObject and ListBucket, what other action can be taken by assuming the bucketmaster role? | `ListAllMyBuckets` |

### Task 4: The Secret Santa Plans

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What are the contents of the cloud_password.txt file? | `THM{more_like_sir_cloudbane}` |

---

**Metodología:** Se utilizó AWS CLI para enumerar la identidad del caller con `aws sts get-caller-identity`, luego se exploraron IAM users/policies para descubrir permisos asignados a sir.carrotbane, y finalmente se enumeraron buckets S3 asumiendo el rol bucketmaster para acceder al archivo cloud_password.txt.
**Learning chain:** AWS STS → IAM Policies & Users → S3 Enumeration → Bucket Access via Role Assumption → Secret Extraction
**MITRE ATT&CK:** T1078.004 - Valid Accounts: Cloud Accounts, T1580 - Cloud Infrastructure Discovery
**Fuente:** [TryHackMe - AWS Security - S3cret Santa](https://tryhackme.com/r/room/cloudenum-aoc2025-y4u7i0o3p6)
