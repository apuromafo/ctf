# Packed Light [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** CTF (Evento "Hacker Holidays 2026: The Byte Lotus Hotel")
* **Slug:** `hh-packedlight-02e5330c`
* **Link:** https://tryhackme.com/room/hh-packedlight-02e5330c
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=hh-packedlight-02e5330c` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de descarga (pcap) de Forensics del evento Hacker Holidays. Se entrega un `traffic.pcapng` de un cliente Windows (192.168.1.141) que ejecuta un keylogger contra el servidor del hotel `byte-lotus-hotel.thm:8080`. El binario descargado (`/temp/updates.py`) es un keylogger `pynput` que cifra cada tecla con un XOR de dos cadenas y exfiltra el resultado en la cabecera cookie `hotel_sess_state` de peticiones HTTP repetidas. Recuperar la flag completa exige correlacionar las 30 peticiones, decodificar cada carácter en base64 y aplicarle el primer byte de la clave XOR.
> **EN:** Download room (pcap) of Forensics from the Hacker Holidays event. A `traffic.pcapng` from a Windows client (192.168.1.141) is provided, one that runs a keylogger against the hotel server `byte-lotus-hotel.thm:8080`. The downloaded binary (`/temp/updates.py`) is a `pynput` keylogger that XOR-encrypts each key with two strings and exfiltrates the result in the `hotel_sess_state` cookie header of repeated HTTP requests. Recovering the full flag requires correlating the 30 requests, base64-decoding each character and applying the first byte of the XOR key.

### Task 1 - Forensics — Hacker Holidays: Day 4

> **ES:** Se abre `traffic.pcapng` en Wireshark y se filtra con `http && tcp.port == 8080`. Un cliente (192.168.1.141) contacta `byte-lotus-hotel.thm:8080` (34.41.103.191): primero descarga `/temp/updates.py` y después realiza GET a `/` cada ~1 segundo con User-Agent `ByteLotusClient/1.1`. El script es un keylogger `pynput` que cifra cada tecla por XOR con las claves `"H0t3lSt@ff0Nly"` y `"K3epS3cr3t!"` y la exfiltra en la cabecera cookie `hotel_sess_state=<base64(XOR(char))>`. La primera tecla (`H`, 0x48) es el primer byte de la clave resultante; extrayendo las 30 peticiones/cookies con `tshark`, uniendo los caracteres y aplicando `base64.b64decode(c)[0] ^ 0x48` por cada uno se reconstruye la flag.
> **EN:** Open `traffic.pcapng` in Wireshark and filter with `http && tcp.port == 8080`. A client (192.168.1.141) contacts `byte-lotus-hotel.thm:8080` (34.41.103.191): first it downloads `/temp/updates.py` and then issues a GET to `/` every ~1 second with User-Agent `ByteLotusClient/1.1`. The script is a `pynput` keylogger that XOR-encrypts each key with the keys `"H0t3lSt@ff0Nly"` and `"K3epS3cr3t!"` and exfiltrates it in the `hotel_sess_state=<base64(XOR(char))>` cookie header. The first key (`H`, 0x48) is the first byte of the resulting key; extracting the 30 requests/cookies with `tshark`, concatenating the characters and applying `base64.b64decode(c)[0] ^ 0x48` to each one reconstructs the flag.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag? | `THM{V3r4_1s_w4tch1ng_0veR_y0u}` |

## Metodología / Methodology

1. **Paso / Step - Análisis del pcap:** Se abre `traffic.pcapng` en Wireshark y se aplica el filtro `http && tcp.port == 8080` para aislar el tráfico HTTP del servidor del hotel.
2. **Paso / Step - Identificación del cliente:** Un cliente Windows (192.168.1.141) contacta `byte-lotus-hotel.thm:8080` (34.41.103.191); descarga `/temp/updates.py` y después realiza GET a `/` cada ~1 segundo con User-Agent `ByteLotusClient/1.1`.
3. **Paso / Step - Análisis del binario:** Se exporta `updates.py`: es un keylogger `pynput` que cifra cada tecla por XOR con las claves `"H0t3lSt@ff0Nly"` y `"K3epS3cr3t!"` y exfiltra el carácter en la cabecera cookie `hotel_sess_state=<base64(XOR(char))>`.
4. **Paso / Step - Recuperación de la flag:** La primera tecla grabada es `key[0]='H'` (0x48), el primer byte de la clave XOR final. Con `tshark` se extraen las 30 peticiones/cookies, se unen los caracteres y se aplica `base64.b64decode(c)[0] ^ 0x48` a cada uno para reconstruir la flag completa.

### Cadena de ataque / Attack Chain

```
pcap -> filtro http && tcp.port==8080 -> GET /temp/updates.py
  -> keylogger pynput (claves XOR "H0t3lSt@ff0Nly" + "K3epS3cr3t!")
  -> exfiltración en cookie hotel_sess_state=<base64(XOR(char))>
  -> tshark extrae 30 cookies -> unir chars -> base64.b64decode(c)[0] ^ 0x48
  -> THM{V3r4_1s_w4tch1ng_0veR_y0u}
```

**Lección:** La exfiltración puede vivir en cabeceras "inofensivas"; revisa siempre el User-Agent y las cookies.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
