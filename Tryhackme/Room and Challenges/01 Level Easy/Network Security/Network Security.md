# Network Security

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `networksecurity` | https://tryhackme.com/room/networksecurity | 01 Level Easy | TryHackMe | Firewall de host, reconocimiento, FTP, aplicación web | Alto — compromiso de servicios expuestos (FTP y librería) con recuperación de credenciales y flags de validación |

---

**Contexto:** Room práctica del módulo Network Security que recorre conceptos de seguridad de redes: el papel del firewall de host y las fases de reconocimiento. Concluye con un laboratorio guiado en el que, sobre los servicios expuestos, se compromete un servidor FTP y una cuenta de librería, recuperando la contraseña de acceso y las flags `THM{FTP_SERVER_OWNED}` y `THM{LIBRARIAN_ACCOUNT_COMPROMISED}`.

> **ES:** Conceptos de firewall de host y reconocimiento, más un laboratorio guiado que compromete servicios expuestos (FTP y librería) con recuperación de credenciales y flags.
> **EN:** Host firewall and reconnaissance concepts, plus a guided lab that compromises exposed services (FTP and a library account) recovering credentials and flags.

## Solucionario

### Task 1: Firewall de Host / Host Firewall

**Explicación:** Se presenta el papel del firewall de host: el elemento de seguridad local que filtra el tráfico entrante y saliente de un equipo. Sobre esta base se entienden las reglas que protegen los servicios del sistema.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el elemento de seguridad que protege un host filtrando el tráfico de red? | `Host Firewall` |

### Task 2: Reconocimiento / Recon

**Explicación:** Fase de reconocimiento: recolección de información del objetivo para identificar los servicios expuestos que servirán de superficie de ataque antes de explotarlos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué fase se emplea para recopilar información sobre el objetivo antes del ataque? | `Recon` |

### Task 3: Servicios Comprometidos / Compromised Services

**Explicación:** Laboratorio guiado: tras el reconocimiento se explotan los servicios expuestos. Se recupera la contraseña de acceso `ABC789xyz123` y las flags que validan el compromiso del servidor FTP (`THM{FTP_SERVER_OWNED}`) y de la cuenta de la librería (`THM{LIBRARIAN_ACCOUNT_COMPROMISED}`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la contraseña recuperada en el laboratorio? | `ABC789xyz123` |
| 2 | ¿Qué flag valida el compromiso del servidor FTP? | `THM{FTP_SERVER_OWNED}` |
| 3 | ¿Qué flag valida el compromiso de la cuenta de la librería? | `THM{LIBRARIAN_ACCOUNT_COMPROMISED}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el elemento de seguridad que protege un host filtrando el tráfico de red? | `Host Firewall` |
| 2 | ¿Qué fase se emplea para recopilar información sobre el objetivo antes del ataque? | `Recon` |
| 3 | ¿Cuál es la contraseña recuperada en el laboratorio? | `ABC789xyz123` |
| 4 | ¿Qué flag valida el compromiso del servidor FTP? | `THM{FTP_SERVER_OWNED}` |
| 5 | ¿Qué flag valida el compromiso de la cuenta de la librería? | `THM{LIBRARIAN_ACCOUNT_COMPROMISED}` |

---

**Metodología:** La room introduce la defensa con firewall de host y la fase de reconocimiento para localizar los servicios de la red. En el laboratorio práctico se explotan los servicios expuestos: primero el servidor FTP y después la aplicación de la librería, recuperando la contraseña de acceso y las flags que validan cada compromiso.

### Cadena de ataque / Attack Chain

```text
Firewall de host -> reconocimiento (detección de servicios) -> FTP comprometido -> cuenta de librería comprometida -> credencial + flags
```

**Learning chain:** firewall de host → reconocimiento → enumeración de servicios → acceso FTP → cuenta de librería → flags de validación.

**Lección:** *Los servicios expuestos y las credenciales débiles convierten un reconocimiento rutinario en un compromiso completo del host.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1110 (Brute Force), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - Network Security](https://tryhackme.com/room/networksecurity)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.