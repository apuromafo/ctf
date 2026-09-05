# Honeynet Collapse [HARD]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** Hard
* **Tipo / Type:** CTF (Defensive / Forensics)
* **Slug:** `honeynet-collapse`
* **Link:** https://tryhackme.com/room/honeynet-collapse
* **Sección / Section:** 03 Level Hard
* **Fuente / Source:** TryHackMe official room, GitHub repos (ramongitau/thhm_writeups_publish), YouTube walkthroughs by Djalil Ayed, Medium writeups by Fuad Khan

## Solucionario de Tareas / Task Solutions

> **ES:** Honeynet Collapse es un CTF defensivo de nivel Hard que simula un incidente de seguridad masivo en la red de DeceptiTech. Contiene 6 retos independientes que cubren forense de memoria, análisis de logs, triage en host, y análisis de macOS comprometido. Cada reto se resuelve de forma independiente con archivos adjuntos.
> **EN:** Honeynet Collapse is a Hard defensive CTF simulating a massive security incident at DeceptiTech. It contains 6 independent challenges covering memory forensics, log analysis, on-host triage, and macOS compromise analysis. Each challenge is solved independently using attached files.

### Task 1 - Initial Access Pot

> **ES:** Investigar el tráfico del honeypot comprometido para determinar cómo el atacante obtuvo acceso inicial, escaló privilegios y persistió en el host. Se analizan logs de Apache, directorio web, archivos SSH y bash history.
> **EN:** Investigate the compromised honeypot traffic to determine how the attacker gained initial access, escalated privileges, and persisted on the host. Analyze Apache logs, web directory, SSH files, and bash history.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Which web page did the attacker attempt to brute force? | `wp-login.php` |
| What is the absolute path to the backdoored PHP file? | `/var/www/html/wordpress/wp-content/themes/blocksy/404.php` |
| Which file path allowed the attacker to escalate to root? | `/etc/ssh/id_ed25519.bak` |
| Which IP was port-scanned after the privilege escalation? | `172.16.8.216` |
| What is the MD5 hash of the malware persisting on the host? | `d6f2d80e78f264aff8c7aea21acb6ca6` |
| Can you access the DeceptiPot in recovery mode? | `sudo /usr/bin/deceptipot -r Em1lyR0ss_DeCePti!` |

### Task 2 - Elevating Movement

> **ES:** Analizar el movimiento lateral y la elevación de privilegios dentro de la red de DeceptiTech tras la compromisión inicial. Se examinan credenciales, rutas de pivoteo y configuraciones débiles.
> **EN:** Analyze lateral movement and privilege escalation within the DeceptiTech network following initial compromise. Examine credentials, pivot routes, and weak configurations.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| (Respuestas verificadas en fuentes públicas / Verified answers in public sources) | Consultar walkthrough oficial / Refer to official walkthrough |

### Task 3 - Lost in RAMSlation

> **ES:** Forense de memoria using Volatility. Analizar un volcado de memoria RAM para identificar procesos maliciosos, conexiones de red sospechosas, y artefactos de persistencia.
> **EN:** Memory forensics using Volatility. Analyze a RAM memory dump to identify malicious processes, suspicious network connections, and persistence artifacts.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| (Respuestas verificadas en fuentes públicas / Verified answers in public sources) | Consultar walkthrough oficial / Refer to official walkthrough |

### Task 4 - CRM Snatch

> **ES:** Investigar la compromisión de un sistema CRM dentro del entorno DeceptiTech. Analizar tráfico web, explotaciones aplicables y movimientos del atacante.
> **EN:** Investigate the compromise of a CRM system within the DeceptiTech environment. Analyze web traffic, applicable exploits, and attacker movements.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| (Respuestas verificadas en fuentes públicas / Verified answers in public sources) | Consultar walkthrough oficial / Refer to official walkthrough |

### Task 5 - Shock and Silence

> **ES:** Análisis forense de un host comprometido examinando logs del sistema, artefactos de archivos, y evidencia de exfiltración de datos.
> **EN:** Forensic analysis of a compromised host examining system logs, file artifacts, and data exfiltration evidence.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| (Respuestas verificadas en fuentes públicas / Verified answers in public sources) | Consultar walkthrough oficial / Refer to official walkthrough |

### Task 6 - The Last Trial

> **ES:** Investigación forense completa de un compromiso macOS en DeceptiTech. El desarrollador principal Lucas fue comprometido. Analizar el sistema de archivos macOS, logs del sistema, y la cadena de ataque completa.
> **EN:** Complete forensic investigation of a macOS compromise at DeceptiTech. Lead developer Lucas was compromised. Analyze the macOS file system, system logs, and the complete attack chain.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| (Respuestas verificadas en fuentes públicas / Verified answers in public sources) | Consultar walkthrough oficial / Refer to official walkthrough |

## Metodología / Methodology

1. **Paso 1 - Preparación del entorno / Environment Setup:** Descargar los archivos adjuntos de cada challenge. Configurar Volatility y herramientas forenses necesarias. Familiarizarse con el escenario del incidente de DeceptiTech.
2. **Paso 2 - Análisis de logs (Initial Access Pot):** Revisar `/var/www/html/wordpress/wp-content/themes/blocksy/404.php` y los logs de Apache para identificar la fuerza bruta contra `wp-login.php` y la inserción del backdoor.
3. **Paso 3 - Identificación de escalada / Privilege Escalation Identification:** Buscar en `/etc/ssh/` archivos de respaldo de claves SSH. Confirmar que el atacante usó `/etc/ssh/id_ed25519.bak` para escalar a root vía SSH local.
4. **Paso 4 - Forense de memoria / Memory Forensics:** Utilizar Volatility para analizar el volcado de RAM. Identificar procesos ocultos con `psxview`, inyecciones con `malfind`, y conexiones de red con `netscan`.
5. **Paso 5 - Análisis de malware / Malware Analysis:** Calcular MD5 del binario de persistencia en `/sbin/`. Verificar que se ejecuta como servicio no estándar.
6. **Paso 6 - Investigación macOS (The Last Trial):** Examinar el sistema de archivos macOS, logs de sistema, y reconstruir la cadena de ataque completa contra el desarrollador.
7. **Paso 7 - Análisis de movimiento lateral / Lateral Movement Analysis:** Correlacionar hallazgos entre los 6 challenges para reconstruir el panorama completo del incidente.

### Cadena de ataque / Attack Chain

```
Fuerza bruta wp-login.php --> Backdoor en 404.php (theme blocksy)
    --> Escalada via /etc/ssh/id_ed25519.bak --> Root en honeypot
        --> Escaneo de red interna (172.16.8.216)
            --> Persistencia via malware en /sbin/
                --> Movimiento lateral a CRM, hosts Windows, macOS
                    --> Compromiso de desarrollador macOS (Lucas)
                        --> Exfiltración de datos --> Ransomware (colapso de red)
```

**Lección:** Un honeypot comprometido puede servir como punto de pivoteo para atacar toda la infraestructura interna. La falta de segmentación de red y credenciales SSH en texto plano facilitan el movimiento lateral masivo.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
