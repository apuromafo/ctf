# Packed Light

| **Dificultad** | Easy |
| **Tipo** | CTF |
| **Slug** | `hh-packedlight-02e5330c` |
| **Link** | [TryHackMe](https://tryhackme.com/room/hh-packedlight-02e5330c) |
| **Sección** | 01 Level Easy |
| **Fuente** | Web (API THM `api/v2/rooms/tasks?roomCode=hh-packedlight-02e5330c` + websearch de walkthroughs) |
| **Componentes** | Wireshark / tshark / base64 / XOR / pcap |
| **Impacto** | Forensics de pcap: correlacionar 30 peticiones HTTP para decodificar un keylogger exfiltrado por cookie y recuperar la flag |

---

**Contexto:** Sala de Forensics del evento Hacker Holidays (Byte Lotus Hotel). Se entrega un `traffic.pcapng` de un cliente Windows (192.168.1.141) que ejecuta un keylogger contra el servidor del hotel `byte-lotus-hotel.thm:8080`. El binario descargado (`/temp/updates.py`) es un keylogger `pynput` que cifra cada tecla con un XOR de dos cadenas y exfiltra el resultado en la cabecera cookie `hotel_sess_state` de peticiones HTTP repetidas. Recuperar la flag completa exige correlacionar las 30 peticiones, decodificar cada carácter en base64 y aplicarle el primer byte de la clave XOR.

## Solucionario

### Task 1: Forensics — Hacker Holidays: Day 4

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{V3r4_1s_w4tch1ng_0veR_y0u}` |

---

**Metodología:**
1. **Análisis del pcap:** abrir `traffic.pcapng` en Wireshark y filtrar con `http && tcp.port == 8080` para aislar el tráfico HTTP del hotel.
2. **Identificación del cliente:** un Windows (192.168.1.141) contacta `byte-lotus-hotel.thm:8080` (34.41.103.191); primero descarga `/temp/updates.py` y después hace GET a `/` cada ~1 segundo con User-Agent `ByteLotusClient/1.1`.
3. **Análisis del binario:** exportar `updates.py`: es un keylogger `pynput` que cifra cada tecla por XOR con `"H0t3lSt@ff0Nly"` y `"K3epS3cr3t!"` y exfiltra el carácter en `hotel_sess_state=<base64(XOR(char))>`.
4. **Recuperación de la flag:** la primera tecla es `key[0]='H'` (0x48), primer byte de la clave XOR final. Extraer las 30 cookies con `tshark`, unir los caracteres y aplicar `base64.b64decode(c)[0] ^ 0x48` a cada uno → `THM{V3r4_1s_w4tch1ng_0veR_y0u}`.

**Learning chain:** pcap → filtro `http && tcp.port==8080` → GET /temp/updates.py → keylogger pynput (claves XOR) → exfiltración en cookie hotel_sess_state → tshark extrae 30 cookies → base64.b64decode(c)[0] ^ 0x48 → THM{V3r4_1s_w4tch1ng_0veR_y0u}

**MITRE ATT&CK:** T1056.001 (Input Capture: Keylogging), T1105 (Ingress Tool Transfer), T1041 (Exfiltration Over C2 Channel)

**Fuente:** [TryHackMe - Packed Light](https://tryhackme.com/room/hh-packedlight-02e5330c)