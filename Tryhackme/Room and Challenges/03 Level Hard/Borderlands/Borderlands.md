# Borderlands

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Reto CTF • Red | borderlands | https://tryhackme.com/room/borderlands | 03 Level Hard | TryHackMe | Webapp, Router, UDP, TCP, puertas traseras | Crítico |

---

**Contexto:**
> **ES:** Desafío tipo CTF de red basado en la frontera "Borderlands": descubrir credenciales y explotar puertas traseras en Webapp, Router, UDP y TCP para capturar las banderas.
> **EN:** Borderlands network CTF challenge: discover credentials and exploit backdoors across Webapp, Router, UDP and TCP to capture the flags.

## Solucionario

### Task 1: Banderas de la frontera / Borderland flags
**Explicación:**
1. ANDVOWLDLAS5Q8OQZ2tuIPGcOu2mXk
2. WEBLhvOJAH8d50Z4y5G5g4McG1GMGD
3. GITtFi80llzs4TxqMWtCotiTZpf0HC
4. {FLAG:Webapp:48a5f4bfef44c8e9b34b926051ad35a6}
5. {FLAG:Router1:c877f00ce2b886446395150589166dcd}
6. {FLAG:UDP:3bb271d020df6cbe599a46d20e9fcb3c}
7. {FLAG:TCP:8fb04648d6b2bd40af6581942fcf483e}

### Preguntas y Respuestas / Questions and Answers

| Task | Respuesta / Answer |
|---|---|
| 1.1 | `ANDVOWLDLAS5Q8OQZ2tuIPGcOu2mXk` |
| 1.2 | `WEBLhvOJAH8d50Z4y5G5g4McG1GMGD` |
| 1.3 | `GITtFi80llzs4TxqMWtCotiTZpf0HC` |
| 1.4 | `{FLAG:Webapp:48a5f4bfef44c8e9b34b926051ad35a6}` |
| 1.5 | `{FLAG:Router1:c877f00ce2b886446395150589166dcd}` |
| 1.6 | `{FLAG:UDP:3bb271d020df6cbe599a46d20e9fcb3c}` |
| 1.7 | `{FLAG:TCP:8fb04648d6b2bd40af6581942fcf483e}` |

---

**Metodología:**
Escaneo de red y puertos, reconocimiento de servicios web, explotación del router, y análisis de tráfico UDP y TCP para extraer credenciales y banderas de cada vector de la frontera.

### Cadena de ataque / Attack Chain
1. Descubrimiento de hosts y servicios en la red.
2. Auditoría de la Webapp y obtención de credenciales.
3. Compromiso del Router1 a través de su superficie expuesta.
4. Captura y análisis de tráfico UDP.
5. Interceptación del canal TCP y extracción de la última bandera.

**Learning chain:**
Enumeración de red -> Explotación Webapp -> Router -> Tráfico UDP -> Tráfico TCP.

**Lección:** *En una frontera la superficie de ataque es distribuida: cada protocolo y cada servicio deben auditarse como un punto de entrada propio.*

**MITRE ATT&CK:**
- T1595 Active Scanning
- T1046 Network Service Discovery
- T1078 Valid Accounts
- T1041 Exfiltration Over C2 Channel

**Fuente:** [TryHackMe - Borderlands](https://tryhackme.com/room/borderlands)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.