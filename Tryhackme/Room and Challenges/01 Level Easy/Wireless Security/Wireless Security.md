# Wireless Security [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough (Free)
* **Slug:** `wirelesssecurity`
* **Link:** https://tryhackme.com/room/wirelesssecurity
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Redacción oficial de TryHackMe + static-site con simulación de wireless
* **Componentes:** Wi-Fi fundamentals (association) · WPA2/WPA3 · Evil twin/WPS · Bluetooth (pairing, bluesnarfing) · RFID/NFC (cloning) · Zigbee / Z-Wave (S0/S2)
* **Impacto rol:** Fundamentos de wireless security: Wi-Fi, Bluetooth, RFID/NFC, IoT mesh; entender qué proteger y cómo atacan.

## Solucionario de Tareas / Task Solutions

> **ES:** Fundamentals de redes inalámbricas con un enfoque en tres capas: Wi-Fi (WPA2/WPA3), Bluetooth (pairing/bluesnarfing) y RFID/NFC (cloning). Al conectar un dispositivo a Wi-Fi ocurre el **Association** (handshake). Cuando varias comunican en la misma frecuencia → **Interference**. Riesgos Wi-Fi: **Evil Twin** (mimic SSID), **WPS** (PIN de 8 dígitos vulnerable), WPA3 resistente a offline dictionary attacks. Bluetooth: la verificación de código de 6 dígitos se llama **Pairing**; opera en **2.4 GHz**; descarga de contactos sin permiso = **Bluesnarfing**. RFID/NFC: copiar badge = **Cloning**; badge perdido → **Deactivated** / revocar acceso. IoT: **Zigbee** encaja en sensores mesh de baja potencia; en Z-Wave **S0** es vulnerable a interceptación por clave todo-ceros.
> **EN:** Wireless security fundamentals across three layers: Wi-Fi (WPA2/WPA3), Bluetooth (pairing/bluesnarfing) and RFID/NFC (cloning). When a device joins Wi-Fi, the **Association** process occurs. Multiple devices on the same frequency cause **Interference**. Wi-Fi risks: **Evil Twin** (SSIDs mimicry), **WPS** (8-digit PIN), WPA3 resists offline dictionary attacks. Bluetooth: the 6-digit code confirmation is **Pairing**; operates on **2.4 GHz**; unauthorized contact/message download = **Bluesnarfing**. RFID/NFC: copying a badge = **Cloning**; lost badge → **Deactivated** / revoke access. IoT: **Zigbee** fits low-power mesh sensors; Z-Wave **S0** is vulnerable to key interception due to all-zero key.

### Task 1 — Introducción / Introduction

* **ES/EN:** check sin pregunta.

### Task 2 — Fundamentos de Redes Wi-Fi / Wi-Fi Network Fundamentals

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the **process** that occurs when a device connects to a wireless network? | `Association` |
| What occurs when multiple devices communicate on the same frequency, affecting the wireless signal? | `Interference` |

* **Association:** el handshake/protocolo cuando un cliente conecta a un AP (proceso de asociación).
* **Interference:** cuando muchos dispositivos hablan en la misma banda se solapan → ruido de señal.

### Task 3 — Seguridad Wi-Fi / Wi-Fi Security

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Attacker sets up a rogue AP with the same SSID as a coffee shop's network. What attack is this? | `Evil Twin` |
| Wi-Fi feature allowing connection by entering an **8-digit PIN** instead of a password? | `WPS` |
| Between WPA2 and WPA3, which protocol resists **offline dictionary attacks**? | `WPA3` |

* **Evil Twin / Rogue AP:** AP malicioso que imita el SSID legítimo.
* **WPS (Wi-Fi Protected Setup):** facilita conexión con PIN de 8 dígitos; el PIN es vulnerable a fuerza bruta.
* **WPA3-SAE:** usa un handshake que impide ataques offline de diccionario (fuerza contra el handshake PMKID) — ventaja clave sobre WPA2-PSK.

### Task 4 — Seguridad Bluetooth / Bluetooth Security

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| User confirms a six-digit code displayed on both devices while pairing. What is this step called? | `Pairing` |
| What frequency band does Bluetooth operate on? | `2.4 GHz` |
| Attacker downloads contacts and messages without authorisation. What type of attack is this? | `Bluesnarfing` |

* **Pairing:** el proceso de emparejamiento con código PIN / passkey.
* **Frecuencia / Frequency:** banda de **2.4 GHz** (banda ISM compartida con Wi-Fi y otros).
* **Bluesnarfing:** robo de datos (contactos, mensajes) por Bluetooth. Diferente de **Bluejacking** (solo envío no solicitado de mensajes).

### Task 5 — Seguridad RFID y NFC / RFID and NFC Security

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Attacker reads data from a badge and writes it to a blank card. What technique is this? | `Cloning` |
| Badge lost — to prevent unauthorised access, what should be done to the card's access rights? | `Deactivated` |

* **Cloning:** copia el contenido RFID/NFC de un badge a una tarjeta nueva.
* **Revocación / Deactivated:** dado de baja el badge perdido en el sistema de control de acceso.

### Task 6 — Otras Tecnologías / Other Wireless Technologies

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Smart lights + motion sensors communicating via low-power mesh network → which technology? | `Zigbee` |
| Between S0 and S2, which Z-Wave security framework is vulnerable to key interception due to its use of an **all-zero encryption key**? | `S0` |

* **Zigbee / Z-Wave / EnOcean:** son los candidatos; el escenario de "low-power mesh" con sensores apunta a **Zigbee** (más común en domótica; usan mesh con low-power).
* **Z-Wave S0 vs S2:** S0 usa claves de cifrado iniciales predefinidas (todo-ceros), lo que lo hace vulnerable a interceptación; S2 corrige esto.

### Task 7 — Knowledge Test *(static-site)*

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the **flag**? | `THM{w1r3l3ss_thr34ts_1d3nt1f13d}` |

* **Static site / Simulador:** pulsa el botón de cada escenario dentro del activity del task para ver el flag.

### Task 8 — Conclusión / Conclusion

* **ES/EN:** check sin pregunta.

## Metodología / Methodology

1. **Paso / Step:** Leer secciones del room (T2–T6) para capturar las definiciones clave.
2. **Paso / Step:** Completar el Knowledge Test (static-site) → flag `THM{w1r3l3ss_thr34ts_1d3nt1f13d}`.

### Cadena de aprendizaje / Learning Chain

```
Wi-Fi: Association -> Interference -> Evil Twin / WPS (PIN) / WPA3
  -> Bluetooth: Pairing (2.4 GHz) / Bluesnarfing
  -> RFID/NFC: Cloning / Deactivated
  -> IoT mesh: Zigbee (domótica) / Z-Wave S0 vulnerable
  -> flag: THM{w1r3l3ss_thr34ts_1d3nt1f13d}
```

**Mapeo MITRE ATT&CK:** T1040 (Network Sniffing) / Evil Twin · CWE-319 (Cleartext transmission — WPS) · CWE-310 (Weak Crypto — S0) · CWE-284 (Improper Access Control — cloning).

**Lección:** *La seguridad de un IoT no empieza en el firmware: empieza en el protocolo wireless. WPA3, emparejamiento con código alto y revocación de badges son la primera línea.*

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.