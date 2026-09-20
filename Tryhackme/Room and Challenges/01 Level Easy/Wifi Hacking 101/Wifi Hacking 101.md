# Wifi Hacking 101

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `wifihacking101` | [TryHackMe](https://tryhackme.com/room/wifihacking101) | 01 Level Easy | TryHackMe | WPA/WPA2-Personal / PSK / airmon-ng / airodump-ng / aircrack-ng / hashcat / wordlists | Ataque a redes WPA(2) personal: modo monitor, captura del 4-way handshake y cracking del PSK mediante diccionarios y aceleración por GPU |

---

**Contexto:** Sala de iniciación al hacking de redes WiFi WPA/WPA2(2). Cubre los fundamentos del protocolo WPA2-Personal, la puesta de la interfaz en modo monitor con la suite Aircrack-ng, la captura dirigida del tráfico y del handshake con airodump-ng, y el volcado offline de la clave PSK mediante aircrack-ng o hashcat (HCCAPX) con aceleración por GPU contra diccionarios como rockyou.

> **ES:** La sala guía el ataque completo a una red WPA2-Personal: explicación del PSK y sus debilidades, activación del modo monitor (airmon-ng), captura del handshake (airodump-ng) y crackeo con aircrack-ng o hashcat usando la GPU.
> **EN:** This room walks you through attacking WPA2-Personal networks: an intro to the PSK and its weaknesses, putting the interface into monitor mode (airmon-ng), capturing the handshake (airodump-ng) and cracking it with aircrack-ng or hashcat using GPU acceleration.

## Solucionario

### Task 1: Introducción a WPA / The basics — An intro to WPA
**Explicación:** Se introducen los conceptos clave del protocolo WPA2-Personal. El ataque offline contra el cifrado se basa en probar contraseñas comunes (brute force); WPA2-EAP no es vulnerable a este método porque utiliza credenciales únicas por usuario. El PSK (Pre-Shared Key) es el término técnico para la "contraseña/código/frase de acceso WiFi" y su longitud mínima es de 8 caracteres. Contenido original de la sala (verbatim): `brute force`, `Nay`, `PSK`, `8`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué tipo de ataque sobre el cifrado se puede realizar contra WPA(2) personal? | `brute force` |
| ¿Puede este método utilizarse para atacar handshakes WPA2-EAP? (Yea/Nay) | `Nay` |
| ¿Qué abreviatura de tres letras es el término técnico para la "contraseña/código/frase de acceso WiFi"? | `PSK` |
| ¿Cuál es la longitud mínima de una contraseña WPA2 Personal? | `8` |

### Task 2: Capturando paquetes / You're being watched — Capturing packets to attack
**Explicación:** Se aprende a preparar el entorno de captura con la suite Aircrack-ng. La interfaz se pone en modo monitor con `airmon-ng start wlan0` (la interfaz pasa a llamarse `wlan0mon`), se eliminan los procesos conflictivos con `airmon-ng check kill` y se captura el tráfico con `airodump-ng` usando los flags `--bssid`, `--channel` y `-w`. Contenido original de la sala (verbatim): `airmon-ng start wlan0`, `wlan0mon`, `airmon-ng check kill`, `airodump-ng`, `--bssid`, `--channel`, `-w`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cómo pones la interfaz "wlan0" en modo monitor con las herramientas Aircrack? (Comando completo) | `airmon-ng start wlan0` |
| ¿Qué nombre es probable que tenga la nueva interfaz después de habilitar el modo monitor? | `wlan0mon` |
| ¿Qué haces si otros procesos están usando actualmente esa tarjeta de red? | `airmon-ng check kill` |
| ¿Qué herramienta de la suite aircrack-ng se usa para crear una captura? | `airodump-ng` |
| ¿Qué flag usas para fijar el BSSID a monitorizar? | `--bssid` |
| ¿Y para fijar el canal? | `--channel` |
| ¿Y cómo le indicas que capture paquetes a un archivo? | `-w` |

### Task 3: Aircrack-ng — A crackear / Aircrack-ng — Let's get cracking
**Explicación:** Se realiza el cracking offline del handshake WPA capturado. Con `aircrack-ng` se especifica el BSSID objetivo con el flag `-b` y el diccionario con el flag `-w`; alternativamente se crea un archivo HCCAPX con el flag `-j` para usar hashcat con aceleración por GPU. El password del capture es `greeneggsandham` y el cracking más rápido se logra con una GPU. Contenido original de la sala (verbatim): `-b`, `-w`, `-j`, `greeneggsandham`, `GPU`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué flag usamos para especificar un BSSID al que atacar? | `-b` |
| ¿Qué flag usamos para especificar un diccionario (wordlist)? | `-w` |
| ¿Cómo creamos un HCCAPX para usar hashcat y crackear el password? | `-j` |
| Usando el diccionario rockyou, crackea el password de la captura adjunta. ¿Cuál es el password? | `greeneggsandham` |
| ¿Dónde es probable que el cracking de passwords sea más rápido, CPU o GPU? | `GPU` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tipo de ataque sobre el cifrado WPA(2) personal | `brute force` |
| 2 | ¿Se puede atacar WPA2-EAP con este método? | `Nay` |
| 3 | Abreviatura de tres letras para la contraseña WiFi | `PSK` |
| 4 | Longitud mínima de una contraseña WPA2 Personal | `8` |
| 5 | Comando para poner wlan0 en modo monitor | `airmon-ng start wlan0` |
| 6 | Nombre de la interfaz tras el modo monitor | `wlan0mon` |
| 7 | Qué hacer si otros procesos usan el adaptador | `airmon-ng check kill` |
| 8 | Herramienta aircrack-ng que crea la captura | `airodump-ng` |
| 9 | Flag para fijar el BSSID a monitorizar | `--bssid` |
| 10 | Flag para fijar el canal | `--channel` |
| 11 | Flag para capturar paquetes a un archivo | `-w` |
| 12 | Flag para especificar un BSSID a atacar | `-b` |
| 13 | Flag para especificar un diccionario | `-w` |
| 14 | Crear HCCAPX para hashcat | `-j` |
| 15 | Password de la captura con rockyou | `greeneggsandham` |
| 16 | ¿CPU o GPU para cracking? | `GPU` |

---

**Metodología:** Se siguen los pasos guiados de la sala: estudio del protocolo WPA2-Personal y su PSK, puesta de la tarjeta en modo monitor con `airmon-ng start wlan0`, eliminación de procesos conflictivos con `airmon-ng check kill`, captura dirigida con `airodump-ng` usando `--bssid`, `--channel` y `-w`, y finalmente el cracking offline con `aircrack-ng -b -w` o la conversión a HCCAPX con el flag `-j` para hashcat con aceleración por GPU contra rockyou.

### Cadena de ataque / Attack Chain

```text
airmon-ng start wlan0 -> modo monitor (wlan0mon) -> airmon-ng check kill -> airodump-ng --bssid --channel -w -> captura del 4-way handshake -> aircrack-ng -b/-w o hashcat -j (HCCAPX) -> wordlist rockyou -> PSK: greeneggsandham -> GPU = máxima velocidad
```

**Learning chain:** WPA2-Personal (PSK) --> weak passphrase --> monitor mode (airmon-ng start wlan0, wlan0mon) --> airmon-ng check kill --> airodump-ng --bssid --channel -w --> WPA handshake capture --> brute force (aircrack-ng -b/-w) --> HCCAPX (-j) --> hashcat + GPU --> rockyou wordlist --> greeneggsandham

**Lección:** *La robustez de WPA2-Personal reside por completo en la fortaleza del PSK: si la clave es corta o aparece en diccionarios públicos como rockyou, capturar el 4-way handshake y crackearla offline es trivial.*

**MITRE ATT&CK:** T1110 (Brute Force)

**Fuente:** [TryHackMe - Wifi Hacking 101](https://tryhackme.com/room/wifihacking101)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.