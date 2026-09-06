# AWS Security - S3cret Santa [EASY]

### Información de la Sala / Room Information

| Propiedad / Property | Valor / Value |
| --- | --- |
| **Nombre / Name** | AWS Security - S3cret Santa |
| **Evento / Event** | Advent of Cyber 2025 — Día 23 |
| **Sala / Room URL** | https://tryhackme.com/room/adventofcyber25 |
| **Dificultad / Difficulty** | Easy |
| **Descripción / Description** | Día 23 del calendario AoC 2025 (AWS Security - S3cret Santa). Solución/respuestas del reto diario. |

---


#Conceptos Fundamentales de AWS
IAM (Identity and Access Management): Servicio de AWS utilizado para gestionar identidades, controlar quién tiene acceso a qué y definir permisos para los recursos de AWS. Es el núcleo de la seguridad en la nube.

Políticas de IAM (IAM Policies): Documentos escritos en JSON que definen los permisos. En entornos reales, estas políticas suelen terminar siendo excesivamente permisivas (overly permissive), lo que abre vectores para el escalamiento de privilegios o el movimiento lateral.

S3 (Simple Storage Service): El servicio de almacenamiento de objetos de AWS. Es un objetivo común en auditorías debido a configuraciones incorrectas en sus políticas de acceso o ACLs.

#Comandos de Enumeración de IAM
`aws iam list-users`: Lista todos los usuarios de IAM presentes en la cuenta. Útil para identificar objetivos potenciales.

`aws iam list-user-policies --user-name sir.carrotbane`: Devuelve los nombres de las políticas integradas (inline policies) que están directamente vinculadas al usuario.

`aws iam list-attached-user-policies --user-name sir.carrotbane`: Busca las políticas administradas que están adjuntas al usuario.

`aws iam list-groups-for-user --user-name sir.carrotbane`: Verifica la pertenencia a grupos del usuario, lo cual es clave para identificar permisos heredados.

## Respuestas / Answers
- Run aws sts get-caller-identity. What is the number shown for the "Account" parameter? : 
`123456789012`
- What IAM component is used to describe the permissions to be assigned to a user or a group? : `
policy`
- What is the name of the policy assigned to sir.carrotbane? : 
`SirCarrotbanePolicy`
- Apart from GetObject and ListBucket, what other action can be taken by assuming the bucketmaster role? : 
`ListAllMyBuckets`
- What are the contents of the cloud_password.txt file? : 
`THM{more_like_sir_cloudbane}`

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
