# Networking Secure Protocols

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `networkingsecureprotocols` | https://tryhackme.com/room/networkingsecureprotocols | 01 Level Easy | TryHackMe | SSL/TLS, certificados, IMAP, SSH/OpenSSH, VPN | Formativo — identificación de protocolos de red seguros |

---

**Contexto:** Sala de protocolos de red seguros: se repasan SSL y los certificados (incluidos los self-signed), los protocolos de correo (IMAP), SSH con su servidor OpenSSH y las VPN, con las flags de validación `THM{Protocols_secur3d}` y `THM{B8WM6P}`.

> **ES:** Protocolos de red seguros: SSL/TLS, certificados (self-signed), correo (IMAP), SSH (OpenSSH) y VPN, con sus flags de validación.
> **EN:** Secure networking protocols: SSL/TLS, certificates (self-signed), mail (IMAP), SSH (OpenSSH) and VPN, with their validation flags.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Introducción de la sala sobre los protocolos de red seguros. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |

### Task 2: Certificados / Certificates

**Explicación:** Seguridad de la capa de transporte: se identifica `SSL` y el tipo de certificado self-signed como opciones del ejercicio.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué protocolo de seguridad se indica en el ejercicio? | `SSL` |
| 2 | ¿Qué tipo de certificado se indica en el ejercicio? | `self-signed certificate` |

### Task 3: Protocolos de Correo (Valores) / Mail Protocols (Values)

**Explicación:** Valores numéricos del ejercicio de correo en protocolos seguros.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el primer valor indicado en el ejercicio de correo? | `8` |
| 2 | ¿Cuál es el segundo valor indicado en el ejercicio de correo? | `10` |

### Task 4: Protocolo de Correo / Mail Protocol

**Explicación:** Se identifica `IMAP` como el protocolo de correo del ejercicio.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué protocolo de correo se identifica en el ejercicio? | `IMAP` |

### Task 5: SSH / SSH

**Explicación:** Se identifica el servidor SSH del laboratorio: `OpenSSH`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué servidor SSH se identifica en el ejercicio? | `OpenSSH` |

### Task 6: Flag de Validación 1 / Validation Flag 1

**Explicación:** Flag que valida la parte práctica de protocolos seguros: `THM{Protocols_secur3d}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué flag valida la parte práctica de la sala? | `THM{Protocols_secur3d}` |

### Task 7: VPN / VPN

**Explicación:** Se identifica la tecnología de red privada virtual del ejercicio: `VPN`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué tecnología de red segura se identifica en el ejercicio? | `VPN` |

### Task 8: Flag de Validación 2 / Validation Flag 2

**Explicación:** Flag final que valida el cierre del laboratorio: `THM{B8WM6P}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué flag valida el cierre del laboratorio? | `THM{B8WM6P}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |
| 2 | ¿Qué protocolo de seguridad se indica en el ejercicio? | `SSL` |
| 3 | ¿Qué tipo de certificado se indica en el ejercicio? | `self-signed certificate` |
| 4 | ¿Cuál es el primer valor indicado en el ejercicio de correo? | `8` |
| 5 | ¿Cuál es el segundo valor indicado en el ejercicio de correo? | `10` |
| 6 | ¿Qué protocolo de correo se identifica en el ejercicio? | `IMAP` |
| 7 | ¿Qué servidor SSH se identifica en el ejercicio? | `OpenSSH` |
| 8 | ¿Qué flag valida la parte práctica de la sala? | `THM{Protocols_secur3d}` |
| 9 | ¿Qué tecnología de red segura se identifica en el ejercicio? | `VPN` |
| 10 | ¿Qué flag valida el cierre del laboratorio? | `THM{B8WM6P}` |

---

**Metodología:** Repaso de los protocolos seguros: SSL/TLS y los tipos de certificados (enfatizando los self-signed), los valores y protocolos de correo (IMAP), el servidor SSH OpenSSH y la tecnología VPN, recogiendo las flags que validan cada apartado del laboratorio.

### Cadena de ataque / Attack Chain

```text
SSL/TLS -> certificados self-signed -> ejercicio de correo (8/10, IMAP) -> OpenSSH -> flag THM{Protocols_secur3d} -> VPN -> flag THM{B8WM6P}
```

**Learning chain:** SSL/TLS → certificados → IMAP → OpenSSH → VPN → flags de validación.

**Lección:** *Elevar el tráfico a protocolos cifrados (SSL/SSH/VPN) no elimina el riesgo: las malas configuraciones y los certificados autofirmados siguen siendo superficie de ataque.*

**MITRE ATT&CK:** T1071.001 (Application Layer Protocol: Web), T1573.001 (Encrypted Channel: Symmetric Cryptography), T1046 (Network Service Discovery)

**Fuente:** [TryHackMe - Networking Secure Protocols](https://tryhackme.com/room/networkingsecureprotocols)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.