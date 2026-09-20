# Network Security Solutions

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
| Medium | Módulo / Laboratorio | networksecuritysolutions | https://tryhackme.com/room/networksecuritysolutions | Soluciones de Seguridad de Red | TryHackMe | IDS/IPS, Nmap, PowerCat, C2, netcat | High |

> **Objeto:** Aprender a desplegar y usar soluciones de seguridad de red: comparar IDS/IPS y sus firmas, usar Nmap para escaneos furtivos, trabajar con PowerCat para transferencias cifradas y brevés de red, y profundizar en conceptos de C2 (frameworks, sockets, jitter).

---

**Contexto:**

Esta sala combina teoría y práctica sobre soluciones de seguridad de red. Se repasan los sistemas de detección y prevención de intrusiones (IDS/IPS) y sus métodos de detección (firmas y anomalías). En el laboratorio se usa Nmap con técnicas furtivas y opciones avanzadas (`-g`, `-sF`, `-ff`, `-w`, filtros) contra la máquina objetivo, se aprovecha PowerCat (`ncat`) en el puerto 23 y 8080 para transferencias con cifrado y certificados, y se terminan conceptos de frameworks de C2 (HTTP/SOCKS4, jitter).

> **ES:** En el laboratorio se ejecutan escaneos de Nmap contra la IP 10.14.17.226 con opciones como `-g 161`, `ncat -lvnp 23`, `-ff`, `-sF` y `-w`. Con PowerCat/Ncat se montan transferencias y se responde con el payload base64 `Y2F0IC9ldGMvcGFzc3dkCg==`, el listener `ncat -l 8080` y los marcadores de certificado/llave privada, obteniendo la credencial `redteamnetsec`. También se identifican los tipos de socket en un C2 (HTTP SOCKS4) y el parámetro `Jitter`.

> **EN:** In the lab, Nmap scans are run against IP 10.14.17.226 with options such as `-g 161`, `ncat -lvnp 23`, `-ff`, `-sF` and `-w`. With PowerCat/Ncat transfers are set up answering with the base64 payload `Y2F0IC9ldGMvcGFzc3dkCg==`, the listener `ncat -l 8080` and the certificate/private key markers, obtaining the credential `redteamnetsec`. The C2 socket types (HTTP SOCKS4) and the `Jitter` parameter are also identified.

## Solucionario

### Task 1: IDS y IPS / IDS and IPS
**Explicación:**

Se comparan los sistemas de detección y prevención de intrusiones y sus diferencias fundamentales.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Sistema que bloquea activamente | `Intrusion Prevention System` |
| 2. Sistema que solo detecta | `Intrusion Detection System` |

### Task 2: Métodos de detección / Detection Methods
**Explicación:**

Se clasifican los métodos de detección de intrusos según su enfoque: firmas conocidas, comportamiento anómalo o combinación.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Método basado en patrones conocidos | `signature-based` |
| 2. Método basado en desviaciones del comportamiento | `anomaly-based` |
| 3. Método para malware conocido | `signature-based` |

### Task 3: Reconocimiento / Recon
**Explicación:**

Se identifica la IP del host objetivo para los ejercicios de escaneo.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 3. IP del objetivo | `10.14.17.226` |

### Task 4: Escaneo furtivo con Nmap / Stealth Scanning with Nmap
**Explicación:**

Se ejecutan escaneos con Nmap usando opciones para evadir detección: fijar el puerto fuente (`-g 161`), usar un listener auxiliar (`ncat -lvnp 23`) y fragmentar paquetes con distintas banderas (`-ff`, `-sF`, `-w`).

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Opción para fijar el puerto fuente | `-g 161` |
| 2. Comando del listener | `ncat -lvnp 23` |
| 3. Opción de fragmentación | `-ff` |
| 4. Opción de scan tipo FIN | `-sF` |
| 5. Opción de tiempo/ventana | `-w` |

### Task 5: PowerCat / PowerCat
**Explicación:**

Se usan las capacidades de transferencia de PowerCat/Ncat: codificar la lectura de `/etc/passwd` en base64 (`Y2F0IC9ldGMvcGFzc3dkCg==`), montar el listener `ncat -l 8080`, y diferenciar los marcadores de certificado (`-----BEGIN CERTIFICATE-----`) y de llave privada (`-----END PRIVATE KEY-----`) del cifrado, obteniendo la credencial `redteamnetsec`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Codificación base64 del comando | `Y2F0IC9ldGMvcGFzc3dkCg==` |
| 2. Comando del listener de PowerCat | `ncat -l 8080` |
| 3. Marcador de certificado | `-----BEGIN CERTIFICATE-----` |
| 4. Marcador de llave privada | `-----END PRIVATE KEY-----` |
| 5. Credencial obtenida | `redteamnetsec` |

### Task 6: Frameworks de C2 / C2 Frameworks
**Explicación:**

Se identifican los tipos de socket usados por los frameworks de C2 para comunicarse con los agents.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 6. Tipos de socket del C2 | `HTTP SOCKS4` |

### Task 7: Marcado de tareas / Task Marking
**Explicación:**

El paso de marcado de tareas del laboratorio de C2.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 7 | `No answer needed` |

### Task 8: Opciones de evasión / Evasion Options
**Explicación:**

Se repasa el parámetro del framework C2 que introduce retardo aleatorio entre check-ins para evadir detección.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 8. Parámetro de retardo | `Jitter` |

### Task 9: Cierre del laboratorio / Lab Wrap-up
**Explicación:**

Finalización del laboratorio de la sala.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 9 | `No answer needed` |

### Task 10: Conclusiones / Conclusions
**Explicación:**

Resumen de la sala de soluciones de seguridad de red.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 10 | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | 1. Sistema que bloquea | `Intrusion Prevention System` |
| 1 | 2. Sistema que detecta | `Intrusion Detection System` |
| 2 | 1. Método por firmas | `signature-based` |
| 2 | 2. Método por anomalías | `anomaly-based` |
| 2 | 3. Método malware conocido | `signature-based` |
| 3 | IP del objetivo | `10.14.17.226` |
| 4 | 1. Puerto fuente | `-g 161` |
| 4 | 2. Listener | `ncat -lvnp 23` |
| 4 | 3. Fragmentación | `-ff` |
| 4 | 4. Scan FIN | `-sF` |
| 4 | 5. Opción -w | `-w` |
| 5 | 1. Base64 | `Y2F0IC9ldGMvcGFzc3dkCg==` |
| 5 | 2. Listener PowerCat | `ncat -l 8080` |
| 5 | 3. Certificado | `-----BEGIN CERTIFICATE-----` |
| 5 | 4. Llave privada | `-----END PRIVATE KEY-----` |
| 5 | 5. Credencial | `redteamnetsec` |
| 6 | Tipos de socket del C2 | `HTTP SOCKS4` |
| 7 | Task 7 | `No answer needed` |
| 8 | Parámetro de retardo | `Jitter` |
| 9 | Task 9 | `No answer needed` |
| 10 | Task 10 | `No answer needed` |

---

**Metodología:**

1. Comparación teórica de IDS/IPS y métodos de detección.
2. Identificación del objetivo (`10.14.17.226`) y escaneo furtivo con Nmap.
3. Uso de opciones de evasión (`-g 161`, `-sF`, `-ff`, `-w`) y listeners Netcat (`ncat -lvnp 23`).
4. Transferencias con PowerCat (`ncat -l 8080`), payload base64 y certificado/llave para la credencial `redteamnetsec`.
5. Identificación de socket C2 (HTTP SOCKS4) y parámetro `Jitter`.

### Cadena de ataque / Attack Chain

```
Recon: IP objetivo 10.14.17.226
        |
        v
Nmap furtivo: -g 161, -ff, -sF, -w  +  ncat -lvnp 23
        |
        v
PowerCat: ncat -l 8080 + payload base64 (cat /etc/passwd)
        |
        v
Cifrado con certificado/llave privada --> credencial redteamnetsec
        |
        v
C2: sockets HTTP/SOCKS4, Jitter para evasión
```

**Learning chain:**

- ¿Qué diferencias hay entre IDS e IPS y entre detección por firmas y por anomalías?
- ¿Cómo se usan las opciones avanzadas de Nmap para escaneo furtivo?
- ¿Cómo se realizan transferencias cifradas con PowerCat y qué significan los marcadores de certificado?
- ¿Qué papel juegan los sockets HTTP/SOCKS4 y el `Jitter` en un framework de C2?

**Lección:**

*Las soluciones de seguridad de red solo son eficaces si se entiende cómo evadirlas: conocer los métodos de detección permite construir defensas reales, y dominar Nmap y PowerCat permite ver cómo un atacante las sortea.*

**MITRE ATT&CK:**

- T1059.001 (PowerShell) — PowerCat
- T1571 (Non-Standard Port)
- T1046 (Network Service Discovery)
- T1021 / T1071.001 (Application Layer Protocol: Web) — C2

**Fuente:** [TryHackMe - Network Security Solutions](https://tryhackme.com/room/networksecuritysolutions)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.