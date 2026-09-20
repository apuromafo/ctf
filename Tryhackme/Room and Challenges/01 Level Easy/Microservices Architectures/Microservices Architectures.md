# Microservices Architectures

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `microservicesarchitectures` | [TryHackMe](https://tryhackme.com/room/microservicesarchitectures) | 01 Level Easy | THM | Kubernetes, Pod Security, Istio, Envoy, mTLS, Sidecar | Seguridad en arquitecturas de microservicios |

> **Objeto:** Comprender los conceptos de seguridad en arquitecturas de microservicios: estándares de Pod Security, el tráfico este-oeste, el cifrado mTLS y la malla de servicios Istio.

---

**Contexto:** Sala centrada en la seguridad de arquitecturas de microservicios: se analizan los estándares de Pod Security de Kubernetes (Restricted, Privileged, Enforce), los modelos de comunicación entre servicios (Monolithic, Unencrypted vs. mTLS), el patrón Sidecar, y la malla de servicios Istio con sus componentes Envoy, Data Plane e Istiod, además del recurso `security.istio.io/v1`.

> **ES:** Sala sobre seguridad en microservicios: Pod Security, comunicación mTLS entre servicios y malla Istio (Envoy, Istiod).
> **EN:** Microservices security room: Pod Security, mTLS service communication and the Istio service mesh (Envoy, Istiod).

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación de la sala y de los conceptos básicos de las arquitecturas de microservicios.

No answer needed

### Task 2: Pod Security / Pod Security
**Explicación:** Se identifican los estándares de Pod Security de Kubernetes y la etiqueta de enforcement.

1. Restricted
2. Privileged
3. Enforce
4. pod-security.kubernetes.io/enforce=restricted

### Task 3: Comunicación entre servicios / Service communication
**Explicación:** Se comparan los modelos de comunicación entre microservicios y el cifrado del tráfico.

1. Monolithic
2. Unencrypted
3. mTLS

### Task 4: Patrón de despliegue / Deployment pattern
**Explicación:** Se identifican los patrones de despliegue y los proxies laterales en los microservicios.

1. Business
2. Sidecar

### Task 5: Service Mesh / Service mesh
**Explicación:** Se analiza la malla de servicios Istio y sus componentes: Envoy, Data Plane e Istiod.

1. Istio
2. Envoy
3. Data Plane
4. Istiod

### Task 6: Recursos de seguridad / Security resources
**Explicación:** Se identifica la API/recursos de seguridad de la malla que aplica las políticas.

1. security.istio.io/v1

### Task 7: Conclusión / Conclusion
**Explicación:** Cierre de la sala y repaso de los conceptos de seguridad en microservicios.

No answer needed

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | — | `No answer needed` |
| 2.1 | Estándar de Pod Security 1 | `Restricted` |
| 2.2 | Estándar de Pod Security 2 | `Privileged` |
| 2.3 | Modo de aplicación | `Enforce` |
| 2.4 | Etiqueta de enforcement | `pod-security.kubernetes.io/enforce=restricted` |
| 3.1 | Modelo de despliegue | `Monolithic` |
| 3.2 | Tráfico sin cifrar | `Unencrypted` |
| 3.3 | Cifrado entre servicios | `mTLS` |
| 4.1 | Lógica de negocio | `Business` |
| 4.2 | Proxy acompañante | `Sidecar` |
| 5.1 | Malla de servicios | `Istio` |
| 5.2 | Proxy de datos | `Envoy` |
| 5.3 | Plano de datos | `Data Plane` |
| 5.4 | Plano de control | `Istiod` |
| 6.1 | Versión de la API de seguridad | `security.istio.io/v1` |
| 7 | — | `No answer needed` |

---

**Metodología:** Revisión de los estándares de Pod Security de Kubernetes y su enforcement mediante etiquetas, comparación de los modelos de comunicación entre microservicios (monolítico, sin cifrar, mTLS), identificación del patrón Sidecar, y análisis de la malla de servicios Istio: proxy Envoy en el Data Plane, plano de control Istiod y recursos de la API `security.istio.io`.

### Cadena de ataque / Attack Chain

Microservicios → Pod Security (Restricted/Privileged) → comunicación (mTLS) → Sidecar → malla Istio (Envoy/Istiod) → políticas de seguridad.

**Learning chain:** Microservicios → Kubernetes Pod Security → mTLS → Service Mesh (Istio) → política de seguridad

*Lección:* Endurecer microservicios implica combinar estándares de Pod Security, cifrado mTLS entre nodos y una malla de servicios que centralice la política de comunicación.

**MITRE ATT&CK:** T1552 - Unsecured Credentials, T1040 - Network Sniffing.

**Fuente:** [TryHackMe - Microservices Architectures](https://tryhackme.com/room/microservicesarchitectures)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.