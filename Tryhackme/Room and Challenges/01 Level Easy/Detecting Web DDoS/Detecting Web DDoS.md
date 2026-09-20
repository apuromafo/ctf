# Detecting Web DDoS

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `detectingwebddos` | https://tryhackme.com/room/detectingwebddos | 01 Level Easy | TryHackMe | DDoS / Denial-of-Service / Botnet / logs web / análisis de tráfico / CAPTCHA | Detección de ataques DDoS sobre aplicaciones web: tipos, motivaciones y análisis de logs y tráfico. |

---

**Contexto:** Sala defensiva centrada en la detección de ataques de denegación de servicio distribuida (DDoS) sobre aplicaciones web. Se explican los conceptos de Denial-of-Service y Botnet, las motivaciones típicas de estos ataques (daño reputacional y hacktivismo) y se analizan logs y capturas de tráfico para identificar la IP atacante, los endpoints objetivo y los patrones de peticiones (User-Agent, número de solicitudes y códigos de estado). Finaliza con las mitigaciones aplicables, como CAPTCHA y balanceo de carga.

> **ES:** Detección de DDoS: conceptos de DoS y botnets, motivaciones, análisis de logs web y mitigaciones (CAPTCHA, load-balancing).
> **EN:** DDoS detection: DoS and botnet concepts, motivations, web log analysis and mitigations (CAPTCHA, load-balancing).

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de la sala sobre detección de ataques DDoS. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |

### Task 2: Conceptos de DDoS / DDoS Concepts

**Explicación:** Se introduce el concepto de ataque de denegación de servicio (Denial-of-Service) y cómo un atacante aprovecha una red de máquinas comprometidas o infectadas (Botnet) para lanzar el ataque de forma distribuida.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué tipo de ataque busca dejar un servicio inaccesible? / Which attack aims to make a service unavailable? | `Denial-of-Service` |
| 2 | ¿Cómo se llama la red de dispositivos comprometidos usada para lanzar el ataque? / What is the network of compromised devices used to launch the attack called? | `Botnet` |

### Task 3: Motivaciones del atacante / Attacker Motivations

**Explicación:** Se analizan las motivaciones detrás de los ataques DDoS: dañar la imagen o confianza en la organización (Reputational Damage) y el activismo o razones ideológicas (Hacktivism).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué daño busca el atacante sobre la imagen de la organización? / Which damage does the attacker seek on the organisation's image? | `Reputational Damage` |
| 2 | ¿Cómo se llama la motivación basada en activismo o razones ideológicas? / What is the motivation based on activism or ideological reasons called? | `Hacktivism` |

### Task 4: Análisis de logs web / Web Log Analysis

**Explicación:** Se analizan los logs de acceso del servidor web para detectar el ataque. Se identifica la IP del atacante (`203.12.23.195`), el endpoint objetivo (`/login`) y el código de estado devuelto por el servidor bajo la presión del ataque (`503`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la IP del atacante identificada en los logs? / What is the attacker IP found in the logs? | `203.12.23.195` |
| 2 | ¿Qué endpoint o ruta recibe el ataque? / Which endpoint or path receives the attack? | `/login` |
| 3 | ¿Qué código de estado devuelve el servidor durante el ataque? / Which status code does the server return during the attack? | `503` |

### Task 5: Análisis de tráfico / Traffic Analysis

**Explicación:** Se analiza una captura de tráfico para caracterizar el ataque: el recurso más solicitado es `/search`, la IP del atacante es `203.0.113.7`, se registran `60` solicitudes, el User-Agent usado es `Java/1.8.0_181`, se obtienen `207` respuestas y el objetivo final del tráfico es la IP `10.10.0.27`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué recurso es el más solicitado en la captura? / Which resource is the most requested in the capture? | `/search` |
| 2 | ¿Cuál es la IP del atacante en la captura? / What is the attacker IP in the capture? | `203.0.113.7` |
| 3 | ¿Cuántas solicitudes se realizan? / How many requests are made? | `60` |
| 4 | ¿Qué User-Agent se utiliza en el ataque? / Which User-Agent is used in the attack? | `Java/1.8.0_181` |
| 5 | ¿Cuántas respuestas se obtienen? / How many responses are obtained? | `207` |
| 6 | ¿Cuál es la IP de destino del tráfico? / What is the destination IP of the traffic? | `10.10.0.27` |

### Task 6: Mitigación / Mitigation

**Explicación:** Se presentan las contramedidas para mitigar un DDoS: el CAPTCHA para distinguir humanos de bots y el balanceo de carga (Load-balancing) para distribuir el tráfico entre varios servidores y absorber el volumen del ataque.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué medida obliga a los clientes a resolver un reto para demostrar que son humanos? / Which measure forces clients to solve a challenge to prove they are human? | `CAPTCHA` |
| 2 | ¿Qué técnica distribuye el tráfico entre varios servidores? / Which technique distributes traffic across multiple servers? | `Load-balancing` |

### Task 7: Conclusión / Conclusion

**Explicación:** Cierre de la sala con el resumen de las técnicas de detección y mitigación de DDoS. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la conclusión de la sala. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |
| 2 | ¿Qué tipo de ataque busca dejar un servicio inaccesible? | `Denial-of-Service` |
| 3 | ¿Cómo se llama la red de dispositivos comprometidos usada para lanzar el ataque? | `Botnet` |
| 4 | ¿Qué daño busca el atacante sobre la imagen de la organización? | `Reputational Damage` |
| 5 | ¿Cómo se llama la motivación basada en activismo o razones ideológicas? | `Hacktivism` |
| 6 | ¿Cuál es la IP del atacante identificada en los logs? | `203.12.23.195` |
| 7 | ¿Qué endpoint o ruta recibe el ataque? | `/login` |
| 8 | ¿Qué código de estado devuelve el servidor durante el ataque? | `503` |
| 9 | ¿Qué recurso es el más solicitado en la captura? | `/search` |
| 10 | ¿Cuál es la IP del atacante en la captura? | `203.0.113.7` |
| 11 | ¿Cuántas solicitudes se realizan? | `60` |
| 12 | ¿Qué User-Agent se utiliza en el ataque? | `Java/1.8.0_181` |
| 13 | ¿Cuántas respuestas se obtienen? | `207` |
| 14 | ¿Cuál es la IP de destino del tráfico? | `10.10.0.27` |
| 15 | ¿Qué medida obliga a los clientes a resolver un reto para demostrar que son humanos? | `CAPTCHA` |
| 16 | ¿Qué técnica distribuye el tráfico entre varios servidores? | `Load-balancing` |
| 17 | Lee la conclusión de la sala. | `No answer needed` |

---

**Metodología:** El room combina teoría y práctica para detectar DDoS. Primero se fijan los conceptos (Denial-of-Service y Botnet) y las motivaciones (Reputational Damage y Hacktivism). Después se analizan los logs de acceso del servidor web para identificar la IP atacante (`203.12.23.195`), el endpoint golpeado (`/login`) y el código de estado `503`. El análisis de la captura de tráfico revela el patrón completo del ataque: `/search`, IP `203.0.113.7`, `60` solicitudes, User-Agent `Java/1.8.0_181`, `207` respuestas y destino `10.10.0.27`. Finalmente se aplican las mitigaciones: CAPTCHA y balanceo de carga.

### Cadena de ataque / Attack Chain

```text
Botnet de atacante -> lanzamiento del DDoS -> objetivo /login (IP 203.12.23.195, status 503) -> tráfico a /search (IP 203.0.113.7, 60 req/s, UA Java/1.8.0_181, 207 respuestas, destino 10.10.0.27) -> mitigación: CAPTCHA + Load-balancing
```

**Learning chain:** Denial-of-Service → Botnet → motivaciones (reputacional, hacktivismo) → análisis de logs web (IP, endpoint, status) → análisis de tráfico (recurso, UA, volúmenes, IPs) → mitigaciones (CAPTCHA, balanceo de carga).

**Lección:** *Detectar un DDoS exige correlacionar logs y tráfico: una IP anómala, un endpoint golpeado, un volumen alto de solicitudes y códigos de estado como el 503 delatan el ataque antes de que la mitigación (CAPTCHA y balanceo de carga) entre en juego.*

**MITRE ATT&CK:** T1498 (Network Denial of Service), T1499 (Endpoint Denial of Service), T1071 (Application Layer Protocol)

**Fuente:** [TryHackMe - Detecting Web DDoS](https://tryhackme.com/room/detectingwebddos)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.