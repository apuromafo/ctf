# 🛡️ Machine: Bizness

**Flags obtenidas:** system, user

**Estado:** Pwned

**Info:** 26.12.2025

## ##Área de Interés

* Aplicación Web
* Aplicaciones Comunes
* Bases de Datos

## ##Vulnerabilidad

* Credenciales Débiles
* Ejecución Remota de Comandos (RCE)
* Configuración Incorrecta
* Diseño Inseguro

## ##Lenguaje

* Python
* Java

## ##Tecnología

* NGINX
* Apache OFBiz

## ##Técnica

* Reconocimiento
* Descubrimiento de Estructura de Sitio Web
* Análisis de Configuración
* Reutilización de Contraseñas
* Cracking de Contraseñas

---

## 📝 Descripción

Bizness es una máquina Linux fácil que presenta una ejecución remota de comandos (RCE) pre-autenticación en Apache OFBiz, clasificada como [CVE-2023-49070](https://nvd.nist.gov/vuln/detail/CVE-2023-49070). El exploit se aprovecha para obtener una shell en la máquina, donde la enumeración de la configuración de OFBiz revela un hash de contraseña en la base de datos Derby del servicio. A través de la investigación y una pequeña revisión de código, el hash se transforma en un formato más común que puede ser crackeado por herramientas estándar de la industria. La contraseña obtenida se utiliza para iniciar sesión en la máquina como usuario root.

## 📑 Registro de Cambios de la Máquina

**Última actualización:** hace 2 años

**Marzo, 2024** `[~] Cambio`

`Parche CVE-2024-1086`

`Se actualizó la caja para eliminar la vulnerabilidad a CVE-2024-1086.`

**Enero, 2024** `[~] Cambio`

`Eliminado Artefacto de Prueba`

`Se eliminó un artefacto de prueba del directorio personal del usuario que causaba confusión y llevaba a los usuarios a un callejón sin salida (rabbit hole).`

---
 
 ```
 {
    "data": [
        {
            "id": 3484,
            "title": "Task 1",
            "description": "How many TCP ports are listening on Bizness?",
            "hint": "Start by enumerating the host with `nmap`.",
            "type": {
                "id": 0,
                "text": "task"
            },
            "task_type": {
                "id": 0,
                "text": "text"
            },
            "prerequisite_id": null,
            "completed": false,
            "masked_flag": "number, such as 3, 17, or 4567",
            "options": []
        },
        {
            "id": 3485,
            "title": "Task 2",
            "description": "What Enterprise Resource Plannning (ERP) backend is in use?",
            "hint": "Perform a directory scan on the target web server and enumerate the discovered endpoints to obtain information about the underlying service.",
            "type": {
                "id": 0,
                "text": "task"
            },
            "task_type": {
                "id": 0,
                "text": "text"
            },
            "prerequisite_id": 3484,
            "completed": false,
            "masked_flag": "****** *****",
            "options": []
        },
        {
            "id": 3486,
            "title": "Task 3",
            "description": "What version of OFBiz is running on the target system?",
            "hint": "Look at the OFBiz-related pages' footer.",
            "type": {
                "id": 0,
                "text": "task"
            },
            "task_type": {
                "id": 0,
                "text": "text"
            },
            "prerequisite_id": 3485,
            "completed": false,
            "masked_flag": "**.**",
            "options": []
        },
        {
            "id": 3487,
            "title": "Task 4",
            "description": "What is the 2023 CVE ID for a pre-authentication, remote code execution vulnerability on this version of OFBiz?",
            "hint": "Search for disclosures using keywords such as \"ofbiz version 18.12\", \"rce\", and \"cve\".",
            "type": {
                "id": 0,
                "text": "task"
            },
            "task_type": {
                "id": 0,
                "text": "text"
            },
            "prerequisite_id": 3486,
            "completed": false,
            "masked_flag": "***-****-*****",
            "options": []
        },
        {
            "id": 3488,
            "title": "Task 5",
            "description": "What user is the OFBiz service running as?",
            "hint": "Look for public Proof-of-Concepts that exploit CVE-2023-49070 and use them to obtain a shell on the target. Your shell will land as the same user running OFBiz.",
            "type": {
                "id": 0,
                "text": "task"
            },
            "task_type": {
                "id": 0,
                "text": "text"
            },
            "prerequisite_id": 3487,
            "completed": false,
            "masked_flag": "username",
            "options": []
        },
        {
            "id": 3489,
            "title": "Submit User Flag",
            "description": "Submit the flag located in the ofbiz user's home directory.",
            "hint": null,
            "type": {
                "id": 1,
                "text": "user"
            },
            "task_type": {
                "id": 0,
                "text": "text"
            },
            "prerequisite_id": null,
            "completed": true,
            "flag": "User flag owned",
            "flag_rating": 3,
            "masked_flag": "32 hex characters",
            "options": []
        },
        {
            "id": 3490,
            "title": "Task 7",
            "description": "What is the full path of the directory that OFBiz is installed in?",
            "hint": "Enumerate the filesystem, or research the documentation to find default installation paths.",
            "type": {
                "id": 0,
                "text": "task"
            },
            "task_type": {
                "id": 0,
                "text": "text"
            },
            "prerequisite_id": 3489,
            "completed": false,
            "masked_flag": "full path of directory",
            "options": []
        },
        {
            "id": 3491,
            "title": "Task 8",
            "description": "What hashing algorithm is the OFBiz installation configured to use for passwords?",
            "hint": "The `framework\/` directory hosts OFBiz components. `security\/` is one such component, in which you will find configuration files related to the service's security parameters.",
            "type": {
                "id": 0,
                "text": "task"
            },
            "task_type": {
                "id": 0,
                "text": "text"
            },
            "prerequisite_id": 3490,
            "completed": false,
            "masked_flag": "***",
            "options": []
        },
        {
            "id": 3492,
            "title": "Task 9",
            "description": "What database is used by Apache OFBiz, by default?",
            "hint": "Research the default installation of OFBiz, specifically database-related sections of the documentation.",
            "type": {
                "id": 0,
                "text": "task"
            },
            "task_type": {
                "id": 0,
                "text": "text"
            },
            "prerequisite_id": 3491,
            "completed": false,
            "masked_flag": "****** *****",
            "options": []
        },
        {
            "id": 3493,
            "title": "Task 10",
            "description": "In which directory are the Derby-related files stored on Bizness?",
            "hint": "Research OFBiz and Derby-specific documentation and\/or forum posts for information, or manually enumerate the `\/opt\/ofbiz` directory.",
            "type": {
                "id": 0,
                "text": "task"
            },
            "task_type": {
                "id": 0,
                "text": "text"
            },
            "prerequisite_id": 3492,
            "completed": false,
            "masked_flag": "full path of directory",
            "options": []
        },
        {
            "id": 3494,
            "title": "Task 11",
            "description": "Using derby-tools and the `ij` command-line utility, what is the command within `ij` to connect to a database stored in `.\/ofbiz`?",
            "hint": "The `connect` directive within `ij` can be used to load the database; research the correct syntax of how to specify the jdbc derby connection URL.",
            "type": {
                "id": 0,
                "text": "task"
            },
            "task_type": {
                "id": 0,
                "text": "text"
            },
            "prerequisite_id": 3493,
            "completed": false,
            "masked_flag": "******* *****:*****:.\/*******",
            "options": []
        },
        {
            "id": 3495,
            "title": "Task 12",
            "description": "Which table contains the SHA-1 hash of the `admin` user?",
            "hint": "Query the database using typical SQL statements. You can list tables with `SHOW TABLES;`.",
            "type": {
                "id": 0,
                "text": "task"
            },
            "task_type": {
                "id": 0,
                "text": "text"
            },
            "prerequisite_id": 3494,
            "completed": false,
            "masked_flag": "*****.****_*****",
            "options": []
        },
        {
            "id": 3496,
            "title": "Task 13",
            "description": "What is the hex version of the discovered hash?",
            "hint": "The hash's data is Base64URL-encoded, without padding. You will have to decode it in the same way, and get the hex of the decoded bytes.",
            "type": {
                "id": 0,
                "text": "task"
            },
            "task_type": {
                "id": 0,
                "text": "text"
            },
            "prerequisite_id": 3495,
            "completed": false,
            "masked_flag": "****************************************",
            "options": []
        },
        {
            "id": 3497,
            "title": "Task 14",
            "description": "What is the root user's password?",
            "hint": "Crack the transformed hash, making sure to specify the salt that was used. Once you have obtained the password, see if it can be reused.",
            "type": {
                "id": 0,
                "text": "task"
            },
            "task_type": {
                "id": 0,
                "text": "text"
            },
            "prerequisite_id": 3496,
            "completed": false,
            "masked_flag": "*************",
            "options": []
        },
        {
            "id": 3498,
            "title": "Submit Root Flag",
            "description": "Submit the flag located in the root user's home directory.",
            "hint": null,
            "type": {
                "id": 2,
                "text": "root"
            },
            "task_type": {
                "id": 0,
                "text": "text"
            },
            "prerequisite_id": null,
            "completed": true,
            "flag": "Root flag owned",
            "flag_rating": 3,
            "masked_flag": "32 hex characters",
            "options": []
        }
    ]
}
 ```
