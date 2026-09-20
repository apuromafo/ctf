# TShark Challenge II_ Directory

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `tsharkchallengeiidirectory` | [TryHackMe](https://tryhackme.com/room/tsharkchallengeiidirectory) | 01 Level Easy | THM | tshark, análisis de tráfico, pcap, malware, trojan, RFI | Análisis de una pcap maliciosa con tshark y detección de un trojan descargado por RFI |

---

**Contexto:**

> **ES:** La sala propone un análisis forense de una captura pcap relacionada con un sitio comprometido. Con tshark se identifica el dominio malicioso (`jx2-bavuong[.]com`), los parámetros de la comunicación o la inclusión remota de `123[.]php`, la descarga de `vlauto[.]exe`, su hash SHA-256 y el veredicto del análisis del malware (un trojan .NET).

> **EN:** This room proposes a forensic analysis of a pcap capture linked to a compromised site. With tshark you identify the malicious domain (`jx2-bavuong[.]com`), the communication parameters or the remote inclusion of `123[.]php`, the download of `vlauto[.]exe`, its SHA-256 hash, and the malware analysis verdict (a .NET trojan).

## Solucionario

### Task 1: Configuración / Setup

**Explicación:**

1. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Guided setup of the room and its files. | `No answer needed` |

### Task 2: Análisis del tráfico / Traffic Analysis

**Explicación:**

2. 1. jx2-bavuong[.]com
   2. 14
   3. 141[.]164[.]41[.]174
   4. Apache/2.2.11 (Win32) DAV/2 mod_ssl/2.2.11 OpenSSL/0.9.8i PHP/5.2.9
   5. 3
   6. 123[.]php
   7. vlauto[.]exe
   8. b4851333efaf399889456f78eac0fd532e9d8791b23a86a19402c1164aed20de
   9. .NET executable
   10. MALWARE TROJAN

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which domain serves the malicious payload? | `jx2-bavuong[.]com` |
| 2 | How many requests are sent to the malicious host? | `14` |
| 3 | What is the IP address of the malicious host? | `141[.]164[.]41[.]174` |
| 4 | What is the server banner? | `Apache/2.2.11 (Win32) DAV/2 mod_ssl/2.2.11 OpenSSL/0.9.8i PHP/5.2.9` |
| 5 | How many files are exchanged in the session? | `3` |
| 6 | Which PHP file is used for the remote file inclusion? | `123[.]php` |
| 7 | Which executable is downloaded? | `vlauto[.]exe` |
| 8 | What is the SHA-256 hash of the downloaded file? | `b4851333efaf399889456f78eac0fd532e9d8791b23a86a19402c1164aed20de` |
| 9 | What file type does the analysis report? | `.NET executable` |
| 10 | What is the malware detection verdict? | `MALWARE TROJAN` |

---

**Metodología:** Se abre la captura pcap y con tshark se filtra el tráfico hacia el sitio comprometido: se extrae el dominio y la IP del host, el banner del servidor web y el número de peticiones y archivos intercambiados. Se reproduce la cadena de inclusión remota del `123[.]php`, se recupera el binario `vlauto[.]exe` descargado, se calcula su hash SHA-256 y se somete a análisis de malware, que lo clasifica como un ejecutable .NET y lo detecta como MALWARE TROJAN.

### Cadena de ataque / Attack Chain

pcap analysis → malicious domain → server banner → remote file inclusion → executable download → hash extraction → malware triage → trojan verdict.

**Learning chain:** pcap analysis → malicious domain identification → communication metrics → remote file inclusion → malware download → SHA-256 hash → trojan classification

**Lección:** *Una pcap bien filtrada con tshark convierte un flujo de bytes en una historia completa de infección, desde el dominio inicial hasta el veredicto del malware.*

**MITRE ATT&CK:** T1105 (Ingress Tool Transfer), T1059 (Command and Scripting Interpreter), T1071.001 (Application Layer Protocol: Web Protocols)

**Fuente:** [TryHackMe - TShark Challenge II_ Directory](https://tryhackme.com/room/tsharkchallengeiidirectory)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.