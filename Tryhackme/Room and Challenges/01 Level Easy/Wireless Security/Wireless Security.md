# Wireless Security

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `wirelesssecurity` |
| **Link** | [TryHackMe](https://tryhackme.com/room/wirelesssecurity) |
| **Sección** | 01 Level Easy |
| **Fuente** | Redacción oficial de TryHackMe + static-site con simulación de wireless |
| **Componentes** | Wi-Fi fundamentals (association) / WPA2 / WPA3 / Evil twin / WPS / Bluetooth (pairing, bluesnarfing) / RFID / NFC (cloning) / Zigbee / Z-Wave (S0/S2) |
| **Impacto** | Fundamentos de wireless security en tres capas (Wi-Fi, Bluetooth, RFID/NFC) más IoT mesh: qué proteger y cómo atacan |

---

**Contexto:** Fundamentals de redes inalámbricas con un enfoque en tres capas: Wi-Fi (WPA2/WPA3), Bluetooth (pairing/bluesnarfing) y RFID/NFC (cloning). Al conectar un dispositivo a Wi-Fi ocurre el **Association** (handshake). Cuando varias comunican en la misma frecuencia → **Interference**. Riesgos Wi-Fi: **Evil Twin** (mimic SSID), **WPS** (PIN de 8 dígitos vulnerable); WPA3 es resistente a offline dictionary attacks. Bluetooth: la verificación de código de 6 dígitos se llama **Pairing**, opera en **2.4 GHz**; la descarga de contactos sin permiso = **Bluesnarfing**. RFID/NFC: copiar badge = **Cloning**; badge perdido → **Deactivated**/revocar acceso. IoT: **Zigbee** encaja en sensores mesh de baja potencia; en Z-Wave **S0** es vulnerable a interceptación por clave todo-ceros.

## Solucionario

### Task 1: Introducción / Introduction

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Check sin pregunta / check, no question) | `No answer needed` |

**Explicación:** Introducción al room de fundamentos de seguridad inalámbrica en tres capas: Wi-Fi (WPA2/WPA3), Bluetooth (pairing/bluesnarfing) y RFID/NFC (cloning), más IoT (Zigbee/Z-Wave). No requiere respuesta.

### Task 2: Fundamentos de Redes Wi-Fi / Wi-Fi Network Fundamentals

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the **process** that occurs when a device connects to a wireless network? | `Association` |
| 2 | What occurs when multiple devices communicate on the same frequency, affecting the wireless signal? | `Interference` |

**Explicación:** **Association** es el handshake/protocolo cuando un cliente conecta a un AP (el proceso de asociación en el que el dispositivo se registra en el punto de acceso). **Interference** ocurre cuando muchos dispositivos hablan en la misma banda y se solapan → ruido de señal.

### Task 3: Seguridad Wi-Fi / Wi-Fi Security

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Attacker sets up a rogue AP with the same SSID as a coffee shop's network. What attack is this? | `Evil Twin` |
| 2 | Wi-Fi feature allowing connection by entering an **8-digit PIN** instead of a password? | `WPS` |
| 3 | Between WPA2 and WPA3, which protocol resists **offline dictionary attacks**? | `WPA3` |

**Explicación:** **Evil Twin / Rogue AP** es un AP malicioso que imita el SSID legítimo para capturar tráfico o credenciales. **WPS (Wi-Fi Protected Setup)** facilita la conexión con un PIN de 8 dígitos, pero el PIN es vulnerable a fuerza bruta. **WPA3-SAE** usa un handshake que impide ataques offline de diccionario contra el PMKID — ventaja clave sobre WPA2-PSK.

### Task 4: Seguridad Bluetooth / Bluetooth Security

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | User confirms a six-digit code displayed on both devices while pairing. What is this step called? | `Pairing` |
| 2 | What frequency band does Bluetooth operate on? | `2.4 GHz` |
| 3 | Attacker downloads contacts and messages without authorisation. What type of attack is this? | `Bluesnarfing` |

**Explicación:** **Pairing** es el proceso de emparejamiento con código PIN/passkey (confirmación del código de 6 dígitos). Bluetooth opera en la banda de **2.4 GHz** (banda ISM compartida con Wi-Fi y otros). **Bluesnarfing** roba datos (contactos, mensajes) por Bluetooth — diferente de **Bluejacking** (solo envío no solicitado de mensajes).

### Task 5: Seguridad RFID y NFC / RFID and NFC Security

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Attacker reads data from a badge and writes it to a blank card. What technique is this? | `Cloning` |
| 2 | Badge lost — to prevent unauthorised access, what should be done to the card's access rights? | `Deactivated` |

**Explicación:** **Cloning** copia el contenido RFID/NFC de un badge a una tarjeta nueva (el atacante lee los datos del badge y los escribe en una tarjeta en blanco). Ante un badge perdido se **Deactivated** (dar de baja) en el sistema de control de acceso para prevenir el acceso no autorizado.

### Task 6: Otras Tecnologías / Other Wireless Technologies

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Smart lights + motion sensors communicating via low-power mesh network → which technology? | `Zigbee` |
| 2 | Between S0 and S2, which Z-Wave security framework is vulnerable to key interception due to its use of an **all-zero encryption key**? | `S0` |

**Explicación:** Entre Zigbee/Z-Wave/EnOcean (candidatos para IoT), el escenario "smart lights + motion sensors via low-power mesh" apunta a **Zigbee** (más común en domótica; usan mesh con low-power). En **Z-Wave**, **S0** usa claves de cifrado iniciales predefinidas (todo-ceros), lo que lo hace vulnerable a interceptación de clave; **S2** corrige esto.

### Task 7: Knowledge Test *(static-site)*

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the **flag**? | `THM{w1r3l3ss_thr34ts_1d3nt1f13d}` |

**Explicación:** El static-site es un simulador: se pulsan los botones de cada escenario dentro del activity del task para ver el flag → `THM{w1r3l3ss_thr34ts_1d3nt1f13d}`.

### Task 8: Conclusión / Conclusion

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Check sin pregunta / check, no question) | `No answer needed` |

**Explicación:** Cierre del room. Lección: la seguridad de un IoT no empieza en el firmware, empieza en el protocolo wireless (WPA3, emparejamiento con código alto y revocación de badges son la primera línea).

---

**Metodología:**
1. **Fundamentos Wi-Fi:** **Association** es el handshake/protocolo cuando un cliente conecta a un AP (proceso de asociación); **Interference** ocurre cuando muchos dispositivos hablan en la misma banda y se solapan → ruido de señal.
2. **Seguridad Wi-Fi:** **Evil Twin/Rogue AP** es un AP malicioso que imita el SSID legítimo; **WPS (Wi-Fi Protected Setup)** facilita la conexión con un PIN de 8 dígitos vulnerable a fuerza bruta; **WPA3-SAE** usa un handshake que impide ataques offline de diccionario contra el PMKID (ventaja clave sobre WPA2-PSK).
3. **Bluetooth:** **Pairing** es el proceso de emparejamiento con código PIN/passkey; la banda es **2.4 GHz** (banda ISM compartida con Wi-Fi); **Bluesnarfing** roba datos (contactos, mensajes) por Bluetooth — distinto de **Bluejacking** (solo envío no solicitado de mensajes).
4. **RFID/NFC:** **Cloning** copia el contenido RFID/NFC de un badge a una tarjeta nueva; ante un badge perdido se **Deactivated** (dar de baja) en el sistema de control de acceso para prevenir acceso no autorizado.
5. **Otras tecnologías:** entre Zigbee/Z-Wave/EnOcean, el escenario "low-power mesh" con sensores apunta a **Zigbee** (común en domótica); en **Z-Wave**, **S0** usa claves de cifrado iniciales predefinidas (todo-ceros), vulnerable a interceptación, y **S2** corrige esto.
6. **Knowledge Test:** completar el simulador (static-site) pulsando el botón de cada escenario en el activity → flag `THM{w1r3l3ss_thr34ts_1d3nt1f13d}`.

**Learning chain:** Wi-Fi: Association → Interference → Evil Twin / WPS (PIN) / WPA3 → Bluetooth: Pairing (2.4 GHz) / Bluesnarfing → RFID/NFC: Cloning / Deactivated → IoT mesh: Zigbee (domótica) / Z-Wave S0 vulnerable → flag: THM{w1r3l3ss_thr34ts_1d3nt1f13d}

**MITRE ATT&CK:** T1040 (Network Sniffing), T1557 (Adversary-in-the-Middle), T1112 (Modify Registry), CWE-319 (Cleartext Transmission — WPS), CWE-310 (Weak Crypto — S0), CWE-284 (Improper Access Control — cloning)

**Fuente:** [TryHackMe - Wireless Security](https://tryhackme.com/room/wirelesssecurity)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
