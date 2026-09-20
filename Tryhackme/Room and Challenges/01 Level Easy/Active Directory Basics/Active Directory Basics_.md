# Active Directory Basics

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `activedirectorybasics` | https://tryhackme.com/room/activedirectorybasics | 01 Level Easy | TryHackMe | Active Directory / Domain Controller / OUs / GPOs (SYSVOL) / Kerberos / NetNTLM / Trees & Forests | Fundamentos de Active Directory: dominios, DCs, grupos, OUs, delegación, GPOs, autenticación Kerberos/NetNTLM y árboles/forests. |

---

**Contexto:** Room introductoria de la Cyber Security 101 ruta que explica qué es y cómo funciona Active Directory. Recorre el dominio de Windows (Active Directory y Domain Controller), la estructura de objetos (grupos, cuentas de máquina con `$`, Organizational Units), la gestión de equipos y la delegación de privilegios, las GPO y su distribución por SYSVOL, los dos métodos de autenticación (Kerberos con tickets y NetNTLM), y el modelo jerárquico de árboles y forests con relaciones de confianza. Cada sección cierra con preguntas tipo yay/nay muy directas.

> **ES:** "Active Directory Basics" — ¿qué es AD?, ¿qué es un Domain Controller? y cómo se organiza todo en dominios, OUs, GPOs y autenticación Kerberos/NetNTLM.
> **EN:** "Active Directory Basics" — what is AD?, what is a Domain Controller? and how everything is organized across domains, OUs, GPOs and Kerberos/NetNTLM authentication.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de la room: Active Directory es el núcleo de cualquier red corporativa Windows. La tarea solo introduce los conceptos que se verán (dominios, DC, OUs, GPOs, autenticación, árboles y forests). No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la room. | `No answer needed` |

### Task 2: Dominios de Windows / Windows Domains

**Explicación:** Antes de AD, una red Windows era un *workgroup*: cada equipo se gestiona de forma aislada. Con un dominio, las credenciales se centralizan en un repositorio llamado Active Directory, que es gestionado por el servidor que ejecuta los servicios de directorio: el Domain Controller (DC). Esto permite administrar usuarios y equipos de forma centralizada.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | In a Windows domain, credentials are stored in a centralised repository called... / En un dominio de Windows, las credenciales se almacenan en un repositorio centralizado llamado... | `Active Directory` |
| 2 | The server in charge of running the Active Directory services is called... / El servidor encargado de ejecutar los servicios de Active Directory se llama... | `Domain Controller` |

### Task 3: Active Directory

**Explicación:** AD organiza el dominio en objectos. Se presentan tres elementos clave: el grupo que administra por defecto todos los equipos y recursos del dominio (`Domain Admins`), las *machine accounts* de los equipos (formato `NOMBRE$`, p. ej. `TOM-PC$`) y los contenedores recomendados para agrupar usuarios con políticas comunes: las Organizational Units (OUs).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which group normally administrates all computers and resources in a domain? / ¿Qué grupo administra normalmente todos los equipos y recursos de un dominio? | `Domain Admins` |
| 2 | What would be the name of the machine account associated with a machine named TOM-PC? / ¿Cuál sería el nombre de la cuenta de máquina asociada a un equipo llamado TOM-PC? | `TOM-PC$` |
| 3 | Suppose our company creates a new department for Quality Assurance. What type of containers should we use to group all Quality Assurance users so that policies can be applied consistently to them? / Si creamos un nuevo departamento de QA, ¿qué tipo de contenedores deberíamos usar para agrupar a sus usuarios y aplicarles políticas de forma consistente? | `Organizational Units` |

### Task 4: Gestión de equipos en AD / Managing Computers in AD

**Explicación:** Los equipos se organizan en OUs y se pueden aplicar directivas mediante GPOs. Además se cubre el proceso de *delegación*: otorgar a un usuario privilegios concretos sobre una OU u otro objeto de AD sin darle control total del dominio. En la parte práctica se recupera una flag desde el escritorio de un usuario del laboratorio (Sophie).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What was the flag found on Sophie's desktop? / ¿Cuál era la flag encontrada en el escritorio de Sophie? | `THM{thanks_for_contacting_support}` |
| 2 | The process of granting privileges to a user over some OU or other AD Object is called... / El proceso de otorgar privilegios a un usuario sobre una OU u otro objeto de AD se llama... | `delegation` |

### Task 5: Organizar equipos en OUs / Organising Computers

**Explicación:** Se practica la organización de los equipos del laboratorio en OUs separadas para equipos de sobremesa y servidores. Tras la organización, en la OU de Workstations acabaron 7 equipos y la pregunta lanza la recomendación de mantener separadas las OUs de Servers y Workstations.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | After organising the available computers, how many ended up in the Workstations OU? / Tras organizar los equipos disponibles, ¿cuántos acabaron en la OU de Workstations? | `7` |
| 2 | Is it recommendable to create separate OUs for Servers and Workstations? (yay/nay) / ¿Es recomendable crear OUs separadas para Servers y Workstations? (yay/nay) | `yay` |

### Task 6: Objetos de directiva de grupo / Group Policy

**Explicación:** Las GPO son conjuntos de ajustes aplicados a usuarios y equipos de una OU. Se distribuyen a través del recurso compartido de red SYSVOL, almacenado por defecto en cada DC. Una GPO puede aplicar configuración tanto a usuarios como a equipos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the network share used to distribute GPOs to domain machines? / ¿Cómo se llama el recurso compartido de red que distribuye las GPO a los equipos del dominio? | `sysvol` |
| 2 | Can a GPO be used to apply settings to users and computers? (yay/nay) / ¿Puede una GPO aplicar configuración tanto a usuarios como a equipos? (yay/nay) | `yay` |

### Task 7: Autenticación / Authentication

**Explicación:** Kerberos es el protocolo predeterminado en cualquier versión moderna de Windows: usa un sistema de tickets emitido por el KDC (típicamente en el DC) y el TGT permite pedir más tickets (TGS) para servicios concretos sin volver a validar credenciales. NetNTLM es el protocolo legado de challenge-response: en una versión moderna no se usa como preferido por defecto y el hash/contraseña del usuario nunca viaja por la red de forma legible (se usa el hash NT retado).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Will a current version of Windows use NetNTLM as the preferred authentication protocol by default? (yay/nay) / ¿Una versión actual de Windows usaría NetNTLM como protocolo de autenticación preferido por defecto? (yay/nay) | `nay` |
| 2 | When referring to Kerberos, what type of ticket allows us to request further tickets known as TGS? / En Kerberos, ¿qué tipo de ticket permite solicitar más tickets conocidos como TGS? | `Ticket Granting Ticket` |
| 3 | When using NetNTLM, is a user's password transmitted over the network at any point? (yay/nay) / Con NetNTLM, ¿se transmite en algún momento la contraseña del usuario por la red? (yay/nay) | `nay` |

### Task 8: Árboles y forests / Trees and Forests

**Explicación:** Los dominios de Windows se agrupan jerárquicamente: el grupo de dominios que comparten un namespace común es un *Tree*, y la conexión lógica que permite a usuarios de un dominio acceder a recursos de otro es una relación de confianza (*Trust Relationship*).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is a group of Windows domains that share the same namespace called? / ¿Cómo se llama un grupo de dominios de Windows que comparten el mismo namespace? | `Tree` |
| 2 | What is the mechanism that allows users in one domain to access resources in another domain called? / ¿Cómo se llama el mecanismo que permite a los usuarios de un dominio acceder a recursos de otro? | `A Trust Relationship` |

### Task 9: Conclusión / Conclusion

**Explicación:** Cierre de la room con un resumen de lo aprendido. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la conclusión de la room. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | In a Windows domain, credentials are stored in a centralised repository called... | `Active Directory` |
| 2 | The server in charge of running the Active Directory services is called... | `Domain Controller` |
| 3 | Which group normally administrates all computers and resources in a domain? | `Domain Admins` |
| 4 | What would be the name of the machine account associated with a machine named TOM-PC? | `TOM-PC$` |
| 5 | Suppose our company creates a new department for Quality Assurance. What type of containers should we use to group all Quality Assurance users so that policies can be applied consistently to them? | `Organizational Units` |
| 6 | What was the flag found on Sophie's desktop? | `THM{thanks_for_contacting_support}` |
| 7 | The process of granting privileges to a user over some OU or other AD Object is called... | `delegation` |
| 8 | After organising the available computers, how many ended up in the Workstations OU? | `7` |
| 9 | Is it recommendable to create separate OUs for Servers and Workstations? (yay/nay) | `yay` |
| 10 | What is the name of the network share used to distribute GPOs to domain machines? | `sysvol` |
| 11 | Can a GPO be used to apply settings to users and computers? (yay/nay) | `yay` |
| 12 | Will a current version of Windows use NetNTLM as the preferred authentication protocol by default? (yay/nay) | `nay` |
| 13 | When referring to Kerberos, what type of ticket allows us to request further tickets known as TGS? | `Ticket Granting Ticket` |
| 14 | When using NetNTLM, is a user's password transmitted over the network at any point? (yay/nay) | `nay` |
| 15 | What is a group of Windows domains that share the same namespace called? | `Tree` |
| 16 | What is the mechanism that allows users in one domain to access resources in another domain called? | `A Trust Relationship` |

---

**Metodología:** Leer cada sección teórica (dominios, AD, OUs, GPO, autenticación, árboles) y responder las preguntas directas de repaso. En las tareas prácticas se maneja ADUC/MMC del laboratorio para delegar control, organizar OUs, aplicar GPOs y comprobar comportamientos de autenticación respuestas 'yay/nay'.

### Cadena de ataque / Attack Chain

```text
Dominio (AD + DC) -> Grupos y cuentas de máquina (TOM-PC$) -> OUs -> Delegación -> GPOs vía SYSVOL -> Kerberos (TGT/TGS) vs NetNTLM -> Tree/Forest con Trust Relationships
```

**Learning chain:** Workgroup vs Domain -> Active Directory & Domain Controller -> objetos (grupos, machine accounts, OUs) -> delegación -> GPO/SYSVOL -> Kerberos & NetNTLM -> Trees & Forests.

**Lección:** *Active Directory centraliza identidad y política; saber diferenciar Kerberos (tickets) de NetNTLM (challenge-response) y entender OUs/GPOs es la base para operar y atacar cualquier red Windows.*

**MITRE ATT&CK:** T1078 (Valid Accounts), T1558 (Steal or Forge Kerberos Tickets), T1484 (Domain Policy Modification)

**Fuente:** [TryHackMe - Active Directory Basics](https://tryhackme.com/room/activedirectorybasics)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.