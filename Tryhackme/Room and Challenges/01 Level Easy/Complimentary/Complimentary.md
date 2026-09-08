# Complimentary

| **Dificultad** | Easy |
| **Tipo** | CTF |
| **Slug** | `hh-complimentary-05e0b604` |
| **Link** | [TryHackMe](https://tryhackme.com/room/hh-complimentary-05e0b604) |
| **Sección** | 01 Level Easy |
| **Fuente** | Web (API THM `api/v2/rooms/tasks?roomCode=hh-complimentary-05e0b604` + websearch de walkthroughs) |
| **Componentes** | AWS / Cognito / Identity Pool / DynamoDB / IAM / aws CLI / Event Hacker Holidays |
| **Impacto** | Aprovecha una política IAM abierta en un identity pool de AWS para leer con `GetItem` el dato protegido de una tabla DynamoDB y obtener la flag. |

---

**Contexto:** Sala de Cloud AWS (target en vivo, sin descarga) del evento Hacker Holidays. Una aplicación web ofrece una cuenta "complementaria" gratuita con autenticación vía AWS Cognito. La app expone un *identity pool* que otorga credenciales temporales con permisos `GetItem` sobre una tabla DynamoDB, sin restringirlas por rol; al realizar `GetItem` directamente sobre la tabla se lee el dato protegido que contiene la flag. El fallo es un exceso de permisos/política IAM abierta más que un fallo de la app en sí.

## Solucionario

### Task 1: Complimentary

**Explicación:** El registro/identidad en Cognito no valida los atributos custom del usuario, y el *identity pool* entrega credenciales temporales que, por una política IAM mal configurada, permiten `GetItem` sobre la tabla DynamoDB sin restricción de rol. Con las credenciales obtenidas se consulta la tabla (con la herramienta `aws` CLI o desde la propia app) y la flag está guardada en un atributo del ítem: `THM{fr33_app_fr33_d4t4!}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{fr33_app_fr33_d4t4!}` |

---

**Metodología:**
1. **Registro público en Cognito:** se accede a la app web y se crea una cuenta gratuita; el registro/identidad no valida los atributos custom del usuario.
2. **Obtención de credenciales temporales:** el *identity pool* de AWS entrega credenciales temporales; por una política IAM mal configurada, estas permiten `GetItem` sobre la tabla DynamoDB sin restricción de rol.
3. **Lectura de la tabla:** con las credenciales se ejecuta `GetItem` sobre la tabla expuesta; la flag está almacenada en un atributo del ítem: `THM{fr33_app_fr33_d4t4!}`.

**Learning chain:** registro en Cognito (atributos custom sin validar) → identity pool → credenciales temporales con GetItem irrestricto en DynamoDB → GetItem sobre la tabla → flag.

**MITRE ATT&CK:** T1078.004 (Valid Accounts: Cloud Accounts), T1005 (Data from Local System), T1595 (Active Scanning).

**Fuente:** [TryHackMe - Complimentary](https://tryhackme.com/room/hh-complimentary-05e0b604)