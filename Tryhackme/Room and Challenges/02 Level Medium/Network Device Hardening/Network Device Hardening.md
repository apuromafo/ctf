# Network Device Hardening

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
| Medium | Módulo / Laboratorio | networkdevicehardening | https://tryhackme.com/room/networkdevicehardening | Hardening de Dispositivos de Red | TryHackMe | Equipos de red (Cisco), SSH, syslog, ACL, VPN | High |

> **Objeto:** Endurecer (*hardenizar*) dispositivos de red: identificar equipos y amenazas, configurar gestión segura (SSH/Syslog), endurecer el servicio VPN, aplicar reglas de control de tráfico (ACL) y responder a las preguntas prácticas del laboratorio.

---

**Contexto:**

Esta sala del módulo de hardening aborda la seguridad de los dispositivos que forman la infraestructura de red: routers, switches y firewalls. Se repasan las categorías de dispositivos de red, los tipos de amenazas (como *Denial of Service*), la gestión segura mediante SSH y la monitorización con Syslog, el endurecimiento de configuraciones de VPN y la validación de las reglas aplicadas. El laboratorio pide interactuar con una máquina y aplicar hardening real sobre ella, verificando la configuración con los comandos de IOS.

> **ES:** Se aprende a clasificar dispositivos de red, mitigar amenazas como el Denial of Service, gestionar el equipo de forma segura (SSH y Syslog), endurecer la VPN, configurar ACLs para permitir solo el tráfico necesario (por ejemplo, `Allow-Ping`) y verificar los cambios con comandos de verificación, identificando las flags que confirman cada paso.

> **EN:** You learn to classify network devices, mitigate threats like Denial of Service, manage the equipment securely (SSH and Syslog), harden the VPN, configure ACLs to allow only the necessary traffic (e.g., `Allow-Ping`) and verify the changes with verification commands, identifying the flags that confirm each step.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:**

Se presentan los conceptos de hardening de dispositivos de red y los objetivos de la sala.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1 | `No answer needed` |

### Task 2: Tipos de dispositivos y amenazas / Device Types and Threats
**Explicación:**

Se identifican los tipos de dispositivos de red y los tipos de ataque que pueden sufrir.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. ¿Qué tipo de dispositivo es? / What type of device is it? | `Network device` |
| 2. ¿Qué tipo de ataque puede sufrir? / What type of attack can it suffer? | `Denial of Service` |

### Task 3: Gestión segura / Secure Management
**Explicación:**

Se configura el acceso de gestión seguro al dispositivo: elección de la opción correcta para la gestión y monitorización mediante Syslog.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Opción de gestión segura | `B` |
| 2. Protocolo de monitorización de logs | `Syslog` |

### Task 4: Endurecimiento de la VPN / VPN Hardening
**Explicación:**

Se endurece la configuración de VPN/IPsec: se actualizan los cifrados y autenticaciones por defecto, confirmando los cambios con las flags correspondientes, y se identifica el puerto de control usado.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Flag cipher update | `THM{CIPHER_UPDATED_1101}` |
| 2. Flag auth update | `THM{AUTH_UPDATED_123}` |
| 3. Puerto usado | `1194` |

### Task 5: Hardening práctico / Practical Hardening
**Explicación:**

Se realiza el hardening real sobre el equipo del laboratorio: se accede por SSH, se configuran los parámetros de seguridad de la consola (contraseña de sistema), los tiempos de espera y los valores de retransmisión, verificando cada cambio con su flag.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1 | `No answer needed` |
| 2. Puerto SSH | `22` |
| 3. Flag del sistema | `THM{SYSTEM101}` |
| 4. Valor de timeout | `64` |
| 5. Valor de retransmisión | `50` |

### Task 6: Reglas de tráfico (ACL) / Traffic Rules (ACL)
**Explicación:**

Se configuran las ACL del dispositivo para permitir únicamente el tráfico necesario, como el ICMP (`Allow-Ping`), se crea la regla de protección del puerto de gestión (`THM_PORT`) y se verifica la versión de la configuración aplicada.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Regla ICMP | `Allow-Ping` |
| 2. Regla de puerto | `THM_PORT` |
| 3. Versión de configuración | `2.12.2-1` |

### Task 7: Verificación / Verification
**Explicación:**

Se confirma que el hardening aplicado es el correcto tras la verificación.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 7. ¿Está endurecido? / Is it hardened? | `yea` |

### Task 8: Conclusiones / Conclusion
**Explicación:**

Se resume lo aprendido en la sala.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 8 | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Task 1 | `No answer needed` |
| 2 | 1. Tipo de dispositivo | `Network device` |
| 2 | 2. Tipo de ataque | `Denial of Service` |
| 3 | 1. Opción de gestión | `B` |
| 3 | 2. Monitorización | `Syslog` |
| 4 | 1. Flag cipher | `THM{CIPHER_UPDATED_1101}` |
| 4 | 2. Flag auth | `THM{AUTH_UPDATED_123}` |
| 4 | 3. Puerto | `1194` |
| 5 | 1 | `No answer needed` |
| 5 | 2. Puerto SSH | `22` |
| 5 | 3. Flag sistema | `THM{SYSTEM101}` |
| 5 | 4. Timeout | `64` |
| 5 | 5. Retransmisión | `50` |
| 6 | 1. Regla ICMP | `Allow-Ping` |
| 6 | 2. Regla puerto | `THM_PORT` |
| 6 | 3. Versión | `2.12.2-1` |
| 7 | ¿Está endurecido? | `yea` |
| 8 | Task 8 | `No answer needed` |

---

**Metodología:**

1. Identificación de dispositivos de red y sus amenazas (DoS).
2. Configuración de gestión segura (SSH) y monitorización (Syslog).
3. Endurecimiento de cifrados y autenticación de la VPN (IPsec), puerto `1194`.
4. Acceso SSH al laboratorio y hardening de consola/parámetros del sistema.
5. Configuración de ACL (`Allow-Ping`, `THM_PORT`) y verificación de la configuración (`2.12.2-1`).

### Cadena de ataque / Attack Chain

```
Identificar dispositivo y amenazas (DoS)
        |
        v
Gestión segura: SSH (22) + Syslog
        |
        v
Endurecer VPN: cifrados/auth updates (1194)
        |
        v
Hardening práctico: contraseña sistema, timeout 64, retransmisión 50
        |
        v
ACL: Allow-Ping, THM_PORT --> Verify: 2.12.2-1
```

**Learning chain:**

- ¿Qué tipos de dispositivos de red existen y qué amenazas pesan sobre ellos?
- ¿Por qué la gestión por SSH y la monitorización con Syslog son base del hardening?
- ¿Cómo se endurece una VPN y qué papel juega el puerto de control?
- ¿Cómo se aplican y verifican ACLs sobre un equipo real de laboratorio?

**Lección:**

*Un dispositivo de red bien endurecido se gestiona de forma segura, se monitorea y solo deja pasar el tráfico mínimo indispensable: cada regla innecesaria es una puerta más para el atacante.*

**MITRE ATT&CK:**

- T1035 / T1059 (Command and Scripting Interpreter)
- T1046 (Network Service Discovery)
- T1078 (Valid Accounts)
- T1498 (Network Denial of Service)

**Fuente:** [TryHackMe - Network Device Hardening](https://tryhackme.com/room/networkdevicehardening)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.