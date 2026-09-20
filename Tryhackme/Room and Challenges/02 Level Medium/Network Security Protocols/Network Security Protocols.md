# Network Security Protocols

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
| Medium | Módulo / Laboratorio | networksecurityprotocols | https://tryhackme.com/room/networksecurityprotocols | Protocolos de Seguridad de Red | TryHackMe | TLS/SSL, FTPS, GPG, Wireshark, IPsec | High |

> **Objeto:** Comprender y ejercitar los protocolos de seguridad de red: identificación del tráfico TLS/SSL en Wireshark, modo PASV de FTPS, uso de GPG para cifrado asimétrico y decodificación de tráfico con SSLKEYLOGFILE, además de clasificar los protocolos IPsec/SLL-TLS.

---

**Contexto:**

Esta sala repasa los protocolos criptográficos que protegen las comunicaciones de red. Se comienza identificando tráfico SSL/TLS en una captura (puerto 443), se analiza el uso de FTPS y su modo PASV, se trabaja con GNU Privacy Guard (GPG) para generar claves (`gpg --gen-key`) y cifrar, y se usa la clave de sesión SSL (SSLKEYLOGFILE) en Wireshark para descifrar tráfico HTTPS y extraer la flag. Finalmente se clasifican protocolos como IPsec (ESP) y SSL/TLS.

> **ES:** Se usa Wireshark para identificar el tráfico seguro: el protocolo SSL/TLS en el puerto 443 y el modo PASV de FTPS. Con GPG se generan claves y se cifra, respondiendo cuántas entradas posee la clave. Con `SSLKEYLOGFILE` se descifra la sesión TLS capturada y se obtiene `THM{GOT_THE_SSLKEY}`. Se relacionan Encapsulating Security Payload con IPsec y SSL/TLS.

> **EN:** Wireshark is used to identify secure traffic: the SSL/TLS protocol on port 443 and the PASV mode of FTPS. With GPG keys are generated and encryption is performed, answering how many entries the key has. With `SSLKEYLOGFILE` the captured TLS session is decrypted and `THM{GOT_THE_SSLKEY}` is obtained. Encapsulating Security Payload is related to IPsec and SSL/TLS.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:**

Se presentan los protocolos de seguridad de red que se van a analizar.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1 | `No answer needed` |

### Task 2: Análisis de tráfico protegido / Protected Traffic Analysis
**Explicación:**

Se abre la captura en Wireshark y se identifica el tráfico SSL/TLS por su puerto (`443`) y el modo de transferencia de FTPS.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Puerto del tráfico SSL/TLS | `443` |
| 2. Modo de transferencia en FTPS | `PASV` |
| 3 | `No answer needed` |
| 4 | `No answer needed` |

### Task 3: Cifrado con GPG / GPG Encryption
**Explicación:**

Se trabaja con GNU Privacy Guard: se identifica el nombre de la herramienta de cifrado, se genera una clave con `gpg --gen-key` y se responde cuántas entradas se observan en la clave generada.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Nombre del estándar de cifrado | `Pretty Good Privacy` |
| 2. Implementación usada | `Gnu Privacy Guard` |
| 3. Comando para generar la clave | `gpg --gen-key` |
| 4. Número de entradas de la clave | `3` |

### Task 4: Descifrado TLS / TLS Decryption
**Explicación:**

Se usa la clave de sesión SSL (SSLKEYLOGFILE) en Wireshark para descifrar el tráfico HTTPS capturado. Se confirma visualmente el descifrado y se responde cuántos datos de la clave se necesitan, extrayendo la flag oculta en la sesión.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. ¿Se descifró correctamente? | `yea` |
| 2. Número de entradas/claves usadas | `5` |
| 3. Flag de la sesión descifrada | `THM{GOT_THE_SSLKEY}` |

### Task 5: Clasificación de protocolos / Protocol Classification
**Explicación:**

Se relacionan las siglas de los protocolos de seguridad con sus nombres completos: el protocolo que encapsula autenticación y cifrado en IPsec es *Encapsulating Security Payload*, y se clasifican IPsec y SSL/TLS según su capa/uso.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Nombre completo de ESP | `Encapsulating Security Payload` |
| 2. Protocolo que usa la suite de seguridad | `IPsec` |
| 3. Protocolo de seguridad en transporte | `SSL/TLS` |

### Task 6: Resumen / Summary
**Explicación:**

Se consolida lo aprendido sobre protocolos de seguridad de red.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 6 | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Task 1 | `No answer needed` |
| 2 | 1. Puerto SSL/TLS | `443` |
| 2 | 2. Modo FTPS | `PASV` |
| 2 | 3 | `No answer needed` |
| 2 | 4 | `No answer needed` |
| 3 | 1. Estándar de cifrado | `Pretty Good Privacy` |
| 3 | 2. Implementación | `Gnu Privacy Guard` |
| 3 | 3. Comando | `gpg --gen-key` |
| 3 | 4. Entradas | `3` |
| 4 | 1. ¿Descifrado? | `yea` |
| 4 | 2. Número de entradas | `5` |
| 4 | 3. Flag | `THM{GOT_THE_SSLKEY}` |
| 5 | 1. ESP completo | `Encapsulating Security Payload` |
| 5 | 2. Protocolo IPsec | `IPsec` |
| 5 | 3. Protocolo de transporte | `SSL/TLS` |
| 6 | Task 6 | `No answer needed` |

---

**Metodología:**

1. Análisis de la captura en Wireshark: localizar SSL/TLS (443) y FTPS (PASV).
2. Ejercicio de cifrado asimétrico con GPG (`gpg --gen-key`) y conteo de entradas.
3. Configuración de la clave de sesión (`SSLKEYLOGFILE`) y descifrado del tráfico HTTPS.
4. Extracción de la flag de la sesión descifrada y clasificación de IPsec vs SSL/TLS.

### Cadena de ataque / Attack Chain

```
Captura: identificar SSL/TLS (443) y FTPS (PASV)
        |
        v
GPG: gpg --gen-key --> clave con 3 entradas
        |
        v
Wireshark + SSLKEYLOGFILE (5 entradas) --> decrypted HTTPS
        |
        v
Flag: THM{GOT_THE_SSLKEY}
        |
        v
Clasificar: ESP = Encapsulating Security Payload (IPsec) / SSL/TLS
```

**Learning chain:**

- ¿Cómo se identifica el tráfico SSL/TLS en una captura y qué puerto usa?
- ¿Qué es el modo PASV en FTPS y por qué importa en el análisis?
- ¿Cómo funciona el cifrado asimétrico con GPG y qué genera `gpg --gen-key`?
- ¿Cómo descifra Wireshark una sesión TLS con la clave de sesión?

**Lección:**

*El cifrado en tránsito no es un muro infranqueable: con la clave de sesión adecuada (SSLKEYLOGFILE) el tráfico "protegido" se vuelve legible, y saber clasificar IPsec frente a SSL/TLS permite elegir bien el mecanismo para cada necesidad.*

**MITRE ATT&CK:**

- T1040 (Network Sniffing)
- T1557.001 (Adversary-in-the-Middle: LLMNR/NBT-NS Poisoning and SMB Relay) — contexto teórico
- T1573.002 (Encrypted Channel: Asymmetric Cryptography) — segmento defensivo

**Fuente:** [TryHackMe - Network Security Protocols](https://tryhackme.com/room/networksecurityprotocols)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.