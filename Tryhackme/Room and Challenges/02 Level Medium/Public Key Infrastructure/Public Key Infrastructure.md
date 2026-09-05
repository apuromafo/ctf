# Public Key Infrastructure [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Walkthrough
* **Slug:** `publickeyinfrastructure`
* **Link:** https://tryhackme.com/room/publickeyinfrastructure
* **Sección / Section:** 02 Level Medium
* **Fuente / Source:** sornphut (Medium), sehgalrudra07 (Medium), RosanaFSS (Medium), tryhackme.com/room/publickeyinfrastructure

## Solucionario de Tareas / Task Solutions

> **ES:** Sala teórica (Premium) sobre Public Key Infrastructure: qué es un certificado digital, los componentes de un PKI (autoridad certificadora, certificados, cadenas de confianza), el ciclo de vida de los certificados y las mejores prácticas (revocación, OCSP/CRL, gestión de claves).
> **EN:** A theoretical Premium room about Public Key Infrastructure: what a digital certificate is, the components of a PKI (Certificate Authority, certificates, trust chains), the certificate lifecycle, and best practices (revocation, OCSP/CRL, key management).

### Task 1 - Introduction to Public Key Infrastructure

> **ES:** Introducción al framework de PKI para la gestión segura y eficiente de certificados digitales, componentes críticos al desplegar servicios y proteger comunicaciones.
> **EN:** Introduction to the PKI framework for the secure and efficient management of digital certificates, critical components when deploying services and securing communications.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Continue to the next task | No answer needed |

### Task 2 - Certificates

> **ES:** Un certificado digital actúa como una tarjeta de identidad digital que prueba la identidad de una persona, dispositivo o servicio. Contiene la clave pública del titular, la información del emisor (CA), la validez y la firma digital. La confianza se establece a través de una cadena de certificados: root → intermediate → end-entity.
> **EN:** A digital certificate acts as a digital ID card proving the identity of a person, device, or service. It contains the subject's public key, the issuer (CA) information, validity, and a digital signature. Trust is established through a certificate chain: root → intermediate → end-entity.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Complete the task based on the reading | `THM{...redacted...}` |

### Task 3 - Certificate Authorities and trust

> **ES:** La Autoridad Certificadora (CA) es la entidad de confianza que emite y firma certificados. Existe una CA raíz (root) autofirmada y, normalmente, CAs intermedias que emiten los certificados de usuario/máquina. Los clientes validan la cadena de confianza hasta la CA raíz que tienen en su almacén de confianza. El certificado que se instala en los dispositivos intermedios de la cadena se conoce como certificado intermedio.
> **EN:** A Certificate Authority (CA) is the trusted entity that issues and signs certificates. There is a self-signed root CA and, usually, intermediate CAs that issue end-user/machine certificates. Clients validate the trust chain up to the root CA stored in their trust store. The certificate installed on intermediate chain links is known as the intermediate certificate.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Which type of certificate is used to bridge the root CA and end-entity certificates in the trust chain? | `intermediate certificate` |

### Task 4 - Certificate lifecycle

> **ES:** El ciclo de vida de un certificado abarca: generación de claves y CSR (Certificate Signing Request), solicitud a la CA, emisión y publicación, uso, renovación y, finalmente, revocación o expiración. La revocación retira un certificado antes de su expiración (por ejemplo, por compromiso de la clave privada).
> **EN:** The certificate lifecycle covers: key generation and CSR (Certificate Signing Request), request to the CA, issuance and publication, use, renewal, and finally revocation or expiration. Revocation retires a certificate before it expires (e.g., due to private key compromise).

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Complete the task based on the reading | `THM{...redacted...}` |

### Task 5 - PKI best practices and challenges

> **ES:** Las mejores prácticas incluyen proteger la clave privada (HSM), separar CA raíz offline de CAs intermedias, revisar los certificados emitidos y comprobar el estado de revocación antes de confiar en un certificado. El estado de revocación se consulta de forma estándar mediante **OCSP** (Online Certificate Status Protocol) o listas de revocación (CRL).
> **EN:** Best practices include protecting the private key (HSM), keeping the root CA offline separate from intermediate CAs, reviewing issued certificates, and checking the revocation status before trusting a certificate. Revocation status is queried in a standard way using **OCSP** (Online Certificate Status Protocol) or CRLs.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the best way to check a certificate's revocation status? | `OCSP` |

### Task 6 - Conclusion

> **ES:** Resumen de la sala: importancia de PKI para asegurar el ciclo de vida de los certificados y las comunicaciones.
> **EN:** Room summary: importance of PKI to secure certificate lifecycles and communications.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Complete the room | No answer needed |

## Metodología / Methodology

1. **Paso / Step - Comprender los certificados:** Un certificado liga una identidad a una clave pública y es firmado por una CA.
2. **Paso / Step - Modelar la confianza:** Se construye una cadena jerárquica root → intermediate → end-entity; los clientes confían en la root de su almacén.
3. **Paso / Step - Ciclo de vida:** Tras generar el par de claves y el CSR, la CA emite, publica y firma el certificado.
4. **Paso / Step - Validación:** El cliente verifica firma, validez temporal y estado de revocación (CRL/OCSP).
5. **Paso / Step - Renovación y revocación:** Se renueva antes de expirar o se revoca cuando la clave privada se compromete.

### Cadena de ataque / Attack Chain

```
Cliente genera claves + CSR
        │
        ▼
CA Raíz (offline, autofirmada)
        │ emite
        ▼
CA Intermedia  ──►  "intermediate certificate"
        │ emite
        ▼
Certificado end-entity (clave pública + identidad)
        │
        ▼
Cliente valida: firma + validez + OCSP/CRL
```

**Lección:** La confianza en PKI depende de proteger agresivamente la clave privada de las CA raíz y de comprobar siempre el estado de revocación (OCSP) antes de confiar en cualquier certificado; un certificado comprometido no confirma identidad.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
