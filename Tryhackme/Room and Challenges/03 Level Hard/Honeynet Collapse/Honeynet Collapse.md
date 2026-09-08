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

**Explicación:** Se analiza el tráfico del honeypot comprometido: los logs de Apache muestran una fuerza bruta contra **`wp-login.php`** y, tras la intrusión, el tema `blocksy` de WordPress tiene su `404.php` backdooreado (**`/var/www/html/wordpress/wp-content/themes/blocksy/404.php`**). La escalada a root se hizo reutilizando la copia de seguridad de la clave SSH del host (**`/etc/ssh/id_ed25519.bak`**) vía SSH local. Ya como root, el atacante escaneó la IP interna **`172.16.8.216`**, y el binario de persistencia en `/sbin/` tiene el hash MD5 **`d6f2d80e78f264aff8c7aea21acb6ca6`**. El "DeceptiPot" puede abrirse en modo recovery con `deceptipot -r` y la contraseña `Em1lyR0ss_DeCePti!`.

```bash
# exclusión de logs a revisar
grep wp-login /var/log/apache2/access.log | tail -n 20
# persistencia
find /sbin -newer /etc/hostname 2>/dev/null ; md5sum /sbin/<malware>
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which web page did the attacker attempt to brute force? | `wp-login.php` |
| 2 | What is the absolute path to the backdoored PHP file? | `/var/www/html/wordpress/wp-content/themes/blocksy/404.php` |
| 3 | Which file path allowed the attacker to escalate to root? | `/etc/ssh/id_ed25519.bak` |
| 4 | Which IP was port-scanned after the privilege escalation? | `172.16.8.216` |
| 5 | What is the MD5 hash of the malware persisting on the host? | `d6f2d80e78f264aff8c7aea21acb6ca6` |
| 6 | Can you access the DeceptiPot in recovery mode? | `sudo /usr/bin/deceptipot -r Em1lyR0ss_DeCePti!` |

### Task 2: Elevating Movement

**Explicación:** Task sin respuestas transcritas en las fuentes públicas (solo se remite al walkthrough oficial). Temáticamente cubre el movimiento lateral y la elevación de privilegios dentro de la red de DeceptiTech tras la compromisión inicial: mirado desde credenciales encontradas, rutas de pivoteo y configuraciones débiles.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Respuestas verificadas en fuentes públicas / Verified answers in public sources) | `Consultar walkthrough oficial / Refer to official walkthrough` |

### Task 3: Lost in RAMSlation

**Explicación:** Forense de memoria con **Volatility** sobre un volcado de RAM: procesos maliciosos con `psxview`/`pslist`, inyecciones con `malfind` y conexiones de red sospechosas con `netscan`, además de artefactos de persistencia. Las respuestas concretas solo están en el walkthrough oficial.

```bash
volatility -f dump.raw imageinfo
volatility -f dump.raw --profile=Win7SP1x64 psxview
volatility -f dump.raw --profile=Win7SP1x64 malfind --dump-dir=out
volatility -f dump.raw --profile=Win7SP1x64 netscan
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Respuestas verificadas en fuentes públicas / Verified answers in public sources) | `Consultar walkthrough oficial / Refer to official walkthrough` |

### Task 4: CRM Snatch

**Explicación:** Investigar la compromisión de un sistema CRM dentro de DeceptiTech: análisis de tráfico web, explotaciones aplicables y los movimientos del atacante sobre el servicio. Las respuestas específicas no están transcritas en las fuentes públicas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Respuestas verificadas en fuentes públicas / Verified answers in public sources) | `Consultar walkthrough oficial / Refer to official walkthrough` |

### Task 5: Shock and Silence

**Explicación:** Análisis forense de un host comprometido: logs del sistema, artefactos de archivos y evidencia de exfiltración de datos. Al igual que en los retos 2-4 y 6, los literales exactos se remiten al walkthrough oficial.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Respuestas verificadas en fuentes públicas / Verified answers in public sources) | `Consultar walkthrough oficial / Refer to official walkthrough` |

### Task 6: The Last Trial

**Explicación:** Investigación forense completa de un compromiso macOS: el desarrollador principal **Lucas** fue comprometido. Se examinan el sistema de archivos macOS (apps, launch agents/daemons), los logs del sistema (`/Library/Logs`, `~/.zsh_history`) y se reconstruye la cadena de ataque completa hasta la exfiltración/ransomware.

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

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
