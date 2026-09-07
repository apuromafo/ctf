# Honeynet Collapse

| **Dificultad** | Hard |
| **Tipo** | CTF |
| **Slug** | `honeynet-collapse` |
| **Link** | [TryHackMe](https://tryhackme.com/room/honeynet-collapse) |
| **Sección** | 03 Level Hard |
| **Fuente** | TryHackMe official room, GitHub repos (ramongitau/thhm_writeups_publish), YouTube walkthroughs by Djalil Ayed, Medium writeups by Fuad Khan |
| **Componentes** | Volatility / forense de memoria / Apache / WordPress / SSH / malware / macOS / análisis de logs |
| **Impacto** | CTF defensivo de forense: un honeypot comprometido sirve de pivote para atacar la red de DeceptiTech, con análisis de logs, memoria, host y macOS hasta el colapso por ransomware. |

---

**Contexto:** Honeynet Collapse es un CTF defensivo de nivel Hard que simula un incidente de seguridad masivo en la red de DeceptiTech. Contiene 6 retos independientes que cubren forense de memoria, análisis de logs, triage en host y análisis de macOS comprometido. Cada reto se resuelve de forma independiente con archivos adjuntos.

## Solucionario

### Task 1: Initial Access Pot

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which web page did the attacker attempt to brute force? | `wp-login.php` |
| 2 | What is the absolute path to the backdoored PHP file? | `/var/www/html/wordpress/wp-content/themes/blocksy/404.php` |
| 3 | Which file path allowed the attacker to escalate to root? | `/etc/ssh/id_ed25519.bak` |
| 4 | Which IP was port-scanned after the privilege escalation? | `172.16.8.216` |
| 5 | What is the MD5 hash of the malware persisting on the host? | `d6f2d80e78f264aff8c7aea21acb6ca6` |
| 6 | Can you access the DeceptiPot in recovery mode? | `sudo /usr/bin/deceptipot -r Em1lyR0ss_DeCePti!` |

### Task 2: Elevating Movement

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Respuestas verificadas en fuentes públicas / Verified answers in public sources) | `Consultar walkthrough oficial / Refer to official walkthrough` |

### Task 3: Lost in RAMSlation

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Respuestas verificadas en fuentes públicas / Verified answers in public sources) | `Consultar walkthrough oficial / Refer to official walkthrough` |

### Task 4: CRM Snatch

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Respuestas verificadas en fuentes públicas / Verified answers in public sources) | `Consultar walkthrough oficial / Refer to official walkthrough` |

### Task 5: Shock and Silence

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Respuestas verificadas en fuentes públicas / Verified answers in public sources) | `Consultar walkthrough oficial / Refer to official walkthrough` |

### Task 6: The Last Trial

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Respuestas verificadas en fuentes públicas / Verified answers in public sources) | `Consultar walkthrough oficial / Refer to official walkthrough` |

---

**Metodología:**
1. **Preparación del entorno:** descargar los archivos adjuntos de cada challenge, configurar Volatility y las herramientas forenses necesarias y familiarizarse con el escenario del incidente de DeceptiTech.
2. **Análisis de logs (Initial Access Pot):** revisar `/var/www/html/wordpress/wp-content/themes/blocksy/404.php` y los logs de Apache para identificar la fuerza bruta contra `wp-login.php` y la inserción del backdoor.
3. **Identificación de escalada:** buscar en `/etc/ssh/` archivos de respaldo de claves SSH; confirmar que el atacante usó `/etc/ssh/id_ed25519.bak` para escalar a root vía SSH local.
4. **Forense de memoria:** utilizar Volatility sobre el volcado de RAM; identificar procesos ocultos con `psxview`, inyecciones con `malfind` y conexiones de red con `netscan`.
5. **Análisis de malware:** calcular el MD5 del binario de persistencia en `/sbin/` y verificar que se ejecuta como servicio no estándar.
6. **Investigación macOS (The Last Trial):** examinar el sistema de archivos macOS, los logs de sistema y reconstruir la cadena de ataque completa contra el desarrollador Lucas.
7. **Análisis de movimiento lateral:** correlacionar hallazgos entre los 6 challenges para reconstruir el panorama completo del incidente (honeypot → CRM → hosts Windows → macOS → exfiltración → ransomware).

**Learning chain:** `Fuerza bruta wp-login.php → backdoor en 404.php (theme blocksy) → escalada via /etc/ssh/id_ed25519.bak → root en honeypot → escaneo 172.16.8.216 → persistencia malware en /sbin/ → movimiento lateral a CRM/Windows/macOS → compromiso del desarrollador macOS (Lucas) → exfiltración → ransomware (colapso de red)`

**MITRE ATT&CK:** T1110 (Brute Force), T1505.003 (Web Shell), T1552.004 (Unsecured Credentials: Private Keys), T1046 (Network Service Discovery), T1021 (Remote Services), T1486 (Data Encrypted for Impact)

**Fuente:** [TryHackMe - Honeynet Collapse](https://tryhackme.com/room/honeynet-collapse)