# Supply Chain Attack Vectors

| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `supplychainattackvectors` |
| **Link** | [TryHackMe](https://tryhackme.com/room/supplychainattackvectors) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | supply chain / attack vectors / dependency confusion / CI/CD poisoning / typosquatting / open source |
| **Impacto** | Conocer los vectores de ataque a la cadena de suministro de software y cómo se abusa de dependencias, registros y CI/CD |

---

**Contexto:** Sala sobre vectores de ataque a la cadena de suministro de software: cómo los atacantes envenenan dependencias (dependency confusion, typosquatting), atacan registros y Compromete las pipelines CI/CD, y las estrategias de mitigación.

## Solucionario

### Task 1: Introduction

**Explicación:**

Introducción al tema de ataques a la cadena de suministro.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Intro) | `No answer needed` |

### Task 2: Understanding the Supply Chain

**Explicación:**

Cadena de suministro: los actores que publican y mantienen el software y sus repositorios se llaman **Maintainers**; el software preempaquetado que se integra a un proyecto se llama **Dependency**; una colección de dependencias concreta que forma una versión plausible y lista para publicar es un **Release**; y el resultado final empaquetado para el usuario se llama **Artifact**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What do we call the actors that publish and maintain software and their repositories? | `Maintainers` |
| 2 | What do we call prepackaged software that gets integrated into a project? | `Dependency` |
| 3 | What do we call a concrete collection of dependencies that is a plausible version and ready for release? | `Release` |
| 4 | What do we call a packaged final result for the user? | `Artifact` |

### Task 3: Dependency Confusion Attacks

**Explicación:**

Dependency confusion: en un ataque de dependency confusion, una dependencia maliciosa publicada con el **mismo nombre** que una dependencia privada interna puede ser resuelta primero por el registro público. La dirección de un paquete dentro de un registro es la **Supply Chain Address**; y el atributo que puntos to a la copia de un paquete en un registro es la **Package URL (purl) o referencia a la copia exacta**. También se abusa de la **lógica de resolución de versiones** que prioriza el CVSS/registro público sobre la interna.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | In a dependency confusion attack, how can one malicious dependency win over a private internal one? | `By being published with the same name` |
| 2 | What is a dependency package address within a registry? | `Supply Chain Address` |
| 3 | What points to a copy of a package in a registry? | `Package URL (purl) or exact copy reference` |

### Task 4: Typosquatting Attack

**Explicación:**

Typosquatting: el atacante publica slugs de paquetes muy similares pero con **errores de escritura** (typos). Algunas tácticas que mejoran el éxito: usar **nombres muy parecidos**, suplantar la **identidad (avatars/imágenes)** del autor, publicar de forma **frecuente** para ganar confianza, y actuar **rápidamente** (a menudo antes de que el paquete legítimo exista o tenga muchas descargas).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How do attackers improve the chances of a typosquatting attack succeeding? (Multiple answers) | `By using very similar names, By spoofing the author's identity, By publishing frequently, By acting quickly` |

### Task 5: Compromising Registries

**Explicación:**

Registros comprometidos: el atacante obtiene **acceso de nivel administrador** al registro o al equipo mantenedor, permitiendo modificar/inyectar malware en paquetes existentes o en los artefactos de build.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What kind of access is needed to compromise a registry directly? | `Admin-level access` |

### Task 6: Compromised CI/CD Environments

**Explicación:**

CI/CD comprometido: **cualquier** software de terceros dentro de la pipeline puede introducir vulnerabilidades a la cadena de suministro. También los **valores de configuración** (secretos, credenciales, tokens) guardados en la pipeline o en el repositorio pueden ser robados y usados para moverse lateralmente o envenenar builds.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What can introduce vulnerabilities into the supply chain? | `Any third-party software used within the CI/CD pipeline` |
| 2 | What can be stolen from CI/CD pipelines to compromise the supply chain? | `Configuration values (secrets, credentials, tokens)` |

### Task 7: The Future of Supply Chain Attacks

**Explicación:**

Para mitigar minimizando dependencias: **actualizar** cuando haya un parche, eliminar dependencias **no utilizadas**, y reducir su **número** (menos superficie de ataque). La escalada de cadena de suministro: al **envenenar dependencias ampliamente usadas**, afectar múltiples objetivos... la técnica que agrega malware a builds como dependency confusion es escalar por **infectar un paquete ampliamente usado** y así comprometer todo lo que lo usa.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How can we reduce the attack surface by minimizing dependencies? | `By updating them, removing unused ones, and reducing their number` |
| 2 | How can we future-proof against emerging attack vectors? | `By continuously monitoring and staying educated` |

### Task 8: Conclusion

**Explicación:**

Conclusión de la sala.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Conclusion) | `No answer needed` |

---

**Metodología:**

1. Distinguir los actores y artefactos de la cadena de suministro (maintainers, dependencies, releases, artifacts).
2. Dominar los vectores principales: dependency confusion (mismo nombre, registro público primero), typosquatting (nombres similares, spoofing de identidad), compromiso de registros (acceso admin) y CI/CD (software de terceros y valores de configuración).
3. Aplicar mitigaciones: minimizar y actualizar dependencias, vigilar la cadena de suministro y mantenerse educado ante vectores emergentes.

**Learning chain:** software supply chain -> maintainers/dependencies -> dependency confusion -> typosquatting -> registry compromise -> CI/CD poisoning -> mitigation (update/remove/reduce) -> flag

**Lección:** *La cadena de suministro de software es un objetivo enorme y creciente: la dependencia de paquetes externos, registros y pipelines CI/CD convierte cualquier eslabón débil (una dependencia con mismo nombre, un typo, un registro con acceso admin) en una puerta de entrada masiva.*

**MITRE ATT&CK:** T1195 (Supply Chain Compromise) · T1195.002 (Compromise Software Supply Chain) · T1195.001 (Compromise Software Dependencies) · CWE-1104 (Unmaintained Third-Party Component)

**Fuente:** [TryHackMe - Supply Chain Attack Vectors](https://tryhackme.com/room/supplychainattackvectors)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
