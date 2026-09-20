# Introduction to CryptOps

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `introductiontocryptops` | [TryHackMe](https://tryhackme.com/room/introductiontocryptops) | 01 Level Easy | TryHackMe | CryptOps, Key Management, HSM, PKI, Kerberos, PSK, ABAC, CRL, HashiCorp Vault | Gestión de operaciones criptográficas: ciclo de vida de claves, PKI, Kerberos, PSK, ABAC, HSM, CRL y práctica con HashiCorp Vault |

> **Objeto:** Conocer las operaciones de gestión criptográfica (CryptOps): almacenamiento seguro de claves, períodos de purga, revocación, generación segura (RNG, bastion hosts), acuerdos de clave (PKI, Kerberos, PSK), control de acceso (ABAC), HSM, CRLs y cryptoperiod, y practicar la gestión de secretos con HashiCorp Vault en un pipeline DevSecOps.

---

**Contexto:** Sala del path DevSecOps que explora cómo mejorar la seguridad del pipeline integrando HashiCorp Vault para la gestión de secretos. Se cubre el ciclo de vida de las claves (key storage, purge period, Key Revocation), la generación segura (Random number generators, bastion hosts), los acuerdos de clave (Public Key Infrastructure, Kerberos como ejemplo de KDC, PSK en VPNs), el control de acceso basado en atributos (ABAC), el almacenamiento con HSM, las listas de revocación (CRLs) y el cryptoperiod. La parte práctica usa Vault: vault status, el token_accessor tras el login y el TTL por defecto de los tokens.

> **ES:** Sala de operaciones criptográficas: gestión y ciclo de vida de claves, PKI, Kerberos, PSK, ABAC, HSM, CRL, cryptoperiod y práctica con HashiCorp Vault.
> **EN:** CryptOps room: key lifecycle management, PKI, Kerberos, PSK, ABAC, HSM, CRL, cryptoperiod and hands-on with HashiCorp Vault.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación de la sala: cómo integrar HashiCorp Vault en un pipeline DevSecOps para la gestión segura de secretos y las operaciones criptográficas.

No answer needed

### Task 2: Gestión de claves / Key Management
**Explicación:** Se aprende la gestión del ciclo de vida de las claves: el almacenamiento seguro (que puede implicar HSM), el período de purga para hacer la clave recuperable tras X días y la revocación para invalidar una clave antes de su caducidad.

1. key storage
2. purge period
3. Key Revocation

### Task 3: Generación y distribución de claves / Key Generation and Distribution
**Explicación:** Se aprenden los aspectos de generación y distribución de claves: qué significan los RNG y cómo se llaman los hosts cloud configurados de forma segura o servidores de salto en la generación de claves.

1. Random number generators
2. bastion hosts

### Task 4: Acuerdos de clave / Key Agreements
**Explicación:** Se presentan los acuerdos de clave: qué significa PKI, un ejemplo de protocolo para KDC (Kerberos) y el tipo de claves usado en VPNs (PSK por su acrónimo).

1. Public Key Infrastructure
2. Kerberos
3. PSK

### Task 5: Control de acceso y almacenamiento / Access Control and Storage
**Explicación:** Se revisan las estrategias de control de acceso y almacenamiento criptográfico: ABAC por atributos del usuario, recursos y entorno, y HSM como hardware a prueba de manipulaciones para generar, almacenar y gestionar claves.

1. ABAC
2. HSM

### Task 6: Revocación y rotación / Revocation and Rotation
**Explicación:** Se aprende qué son las CRLs (listas de certificados revocados) y el término que se refiere a la vida útil de una clave antes de su rotación (cryptoperiod).

1. certificate revocation lists
2. cryptoperiod

### Task 7: Práctica con HashiCorp Vault / HashiCorp Vault Practice
**Explicación:** Parte práctica con Vault: se usa el comando vault status para comprobar la información general, se obtiene el token_accessor tras iniciar sesión con el token root y se determina el TTL por defecto de un token en horas.

1. vault status
2. uSIMacGCxh8Hj14YHTYg6j0o
3. 768

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | Introducción a la sala | `No answer needed` |
| 2.1 | ¿Qué proceso de claves puede implicar el uso de HSM? | `key storage` |
| 2.2 | ¿Qué se puede configurar para que una clave sea recuperable tras X días? | `purge period` |
| 2.3 | ¿Qué proceso invalida una clave antes de su fecha de caducidad? | `Key Revocation` |
| 3.1 | ¿Qué significan las siglas RNG? | `Random number generators` |
| 3.2 | En la generación de claves, ¿cómo se llaman los host cloud o jump servers configurados de forma segura? | `bastion hosts` |
| 4.1 | ¿Qué significan las siglas PKI? | `Public Key Infrastructure` |
| 4.2 | ¿Qué protocolo es un ejemplo de KDC? | `Kerberos` |
| 4.3 | ¿Qué tipo de claves se usan en las VPN (acrónimo)? | `PSK` |
| 5.1 | ¿Qué estrategia de control de acceso se basa en atributos del usuario, recursos y entorno actual? | `ABAC` |
| 5.2 | ¿Qué solución de almacenamiento ofrece hardware a prueba de manipulaciones? | `HSM` |
| 6.1 | ¿Qué son las CRL? | `certificate revocation lists` |
| 6.2 | ¿Qué término se refiere a la vida de una clave antes de su rotación? | `cryptoperiod` |
| 7.1 | ¿Qué comando comprueba la información general de Vault? | `vault status` |
| 7.2 | Valor del token_accessor tras iniciar sesión con el token root | `uSIMacGCxh8Hj14YHTYg6j0o` |
| 7.3 | TTL por defecto de un token en Vault (en horas) | `768` |

---

**Metodología:** Revisión del ciclo de vida de las claves (almacenamiento, purga y revocación), identificación de los mecanismos de generación segura (RNG, bastion hosts), análisis de los acuerdos de clave (PKI, Kerberos, PSK), control de acceso por atributos (ABAC), almacenamiento con HSM, listas de revocación (CRL) y cryptoperiod, y por último la práctica con HashiCorp Vault (vault status, login y TTL) para cerrar la sala.

### Cadena de ataque / Attack Chain

Claves -> key storage (HSM) -> purge period -> Key Revocation -> RNG/bastion hosts -> PKI/Kerberos/PSK -> ABAC -> CRLs -> cryptoperiod -> HashiCorp Vault (status/login/TTL)

**Learning chain:** CryptOps -> key management -> key storage -> key generation -> key agreements (PKI/Kerberos/PSK) -> ABAC -> HSM -> CRL -> cryptoperiod -> HashiCorp Vault

**Lección:** *La criptografía solo es tan fuerte como su gestión operativa: el ciclo de vida completo de las claves (almacenamiento, purga, revocación y rotación) y las herramientas como Vault determinan la seguridad real de los secretos en un pipeline.*

**MITRE ATT&CK:** N/A (operaciones criptográficas defensivas).

**Fuente:** [TryHackMe - Introduction to CryptOps](https://tryhackme.com/room/introductiontocryptops)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.