# AWS Security - S3cret Santa

| **Dificultad** | Easy | **Tipo** | Sala diaria (Advent of Cyber) | **Slug** | `day23awssecuritys3cretsanta` | | **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber25) | | **Sección** | Advent of Cyber Tryhackme | | **Fuente** | texto oficial THM + anotaciones propias | | **Componentes** | AWS / IAM / Policies / S3 / assume-role / bucket / cloud security | | **Impacto** | Auditoría de AWS centrada en IAM y S3: usuarios, políticas demasiado permisivas, roles asumibles y acceso a secrets en buckets mal configurados |

---

**Contexto:** Día 23 del Advent of Cyber 2025. Se audita una cuenta de AWS partiendo de conceptos fundamentales de IAM (Identity and Access Management), políticas IAM (documentos JSON que definen permisos, a menudo excesivamente permisivas) y S3 (servicio de almacenamiento de objetos, objetivo común por configuraciones incorrectas). El objetivo es enumerar usuarios IAM, descubrir las políticas asignadas a `sir.carrotbane`, asumir el rol `bucketmaster` y leer el archivo `cloud_password.txt`.

> **Note (EN mirror):** Day 23 of AoC 2025. AWS security audit: IAM users and policies (JSON permission documents; often overly permissive), S3 buckets (common misconfigurations), `aws sts get-caller-identity` to confirm the account, enumerate `sir.carrotbane` policies, and assume the `bucketmaster` role to read `cloud_password.txt`.

---

## Solucionario

### Día 23: AWS Security - S3cret Santa

**Explicación:**

#Conceptos Fundamentales de AWS

IAM (Identity and Access Management): Servicio de AWS utilizado para gestionar identidades, controlar quién tiene acceso a qué y definir permisos para los recursos de AWS. Es el núcleo de la seguridad en la nube.

Políticas de IAM (IAM Policies): Documentos escritos en JSON que definen los permisos. En entornos reales, estas políticas suelen terminar siendo excesivamente permisivas (overly permissive), lo que abre vectores para el escalamiento de privilegios o el movimiento lateral.

S3 (Simple Storage Service): El servicio de almacenamiento de objetos de AWS. Es un objetivo común en auditorías debido a configuraciones incorrectas en sus políticas de acceso o ACLs.

#Comandos de Enumeración de IAM

`aws iam list-users`: Lista todos los usuarios de IAM presentes en la cuenta. Útil para identificar objetivos potenciales.

`aws iam list-user-policies --user-name sir.carrotbane`: Devuelve los nombres de las políticas integradas (inline policies) que están directamente vinculadas al usuario.

`aws iam list-attached-user-policies --user-name sir.carrotbane`: Busca las políticas administradas que están adjuntas al usuario.

`aws iam list-groups-for-user --user-name sir.carrotbane`: Verifica la pertenencia a grupos del usuario, lo cual es clave para identificar permisos heredados.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Run aws sts get-caller-identity. What is the number shown for the "Account" parameter? | `123456789012` |
| 2 | What IAM component is used to describe the permissions to be assigned to a user or a group? | `policy` |
| 3 | What is the name of the policy assigned to sir.carrotbane? | `SirCarrotbanePolicy` |
| 4 | Apart from GetObject and ListBucket, what other action can be taken by assuming the bucketmaster role? | `ListAllMyBuckets` |
| 5 | What are the contents of the cloud_password.txt file? | `THM{more_like_sir_cloudbane}` |

---

**Metodología:**

1. Confirmar identidad y cuenta: `aws sts get-caller-identity` (Account `123456789012`)
2. Enumerar usuarios IAM: `aws iam list-users`
3. Enumerar políticas del usuario: `aws iam list-user-policies`, `aws iam list-attached-user-policies`, `aws iam list-groups-for-user` (usuario `sir.carrotbane`, política `SirCarrotbanePolicy`)
4. Asumir el rol `bucketmaster` (permisos adicionales: `ListAllMyBuckets`)
5. Listar y leer el bucket para obtener `cloud_password.txt` -> flag

**Learning chain:** aws sts get-caller-identity -> IAM users -> list-user/attached/group policies -> SirCarrotbanePolicy -> asumir bucketmaster -> ListAllMyBuckets -> cloud_password.txt -> THM{more_like_sir_cloudbane}

Cadena de ataque / Attack Chain:
```text
AWS CLI -> sts get-caller-identity (123456789012) -> iam list-users -> sir.carrotbane
-> list-user-policies / attached / groups -> SirCarrotbanePolicy -> assume bucketmaster (ListAllMyBuckets)
-> GetObject cloud_password.txt -> THM{more_like_sir_cloudbane}
```

**Lección:** *Las políticas IAM demasiado permisivas y los roles asumibles sin restricción permiten pasar de un usuario legítimo a la lectura de secrets en S3; enumerar sistemáticamente usuarios, políticas y grupos revela el camino de escalada en la nube.*

**MITRE ATT&CK:**

- T1078 - Valid Accounts
- T1213 - Data from Information Repositories
- T1552 - Unsecured Credentials
- T1530 - Data from Cloud Storage Object

**Fuente:** [TryHackMe - AWS Security - S3cret Santa](https://tryhackme.com/room/adventofcyber25)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.