# Extracted

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | DFIR / Análisis de tráfico y KeePass | extracted | https://tryhackme.com/room/extracted | 02 Level Medium | TryHackMe | TShark, base64, XOR, keepass_dump, John the Ripper | Extracción de credenciales de KeePass desde un volcado de memoria exfiltrado |

---

**Contexto:** **Extracted** es una sala DFIR en la que se analiza una captura `traffic.pcapng` con tráfico HTTP sospechoso por el puerto 1337. Se extrae un payload codificado con `tshark`, se invierte una doble capa de codificación (base64 + XOR) con un script Python propio, se recupera una base de datos **KeePass** (.kdbx), se obtiene su hash con `keepass2john` y se crackea con John the Ripper usando una wordlist generada por fuerza bruta (prefijo + `NoWaYIcanF0rGetThis123`). Finalmente se abre la base con `kpcli` y se recupera la flag final.

## Solucionario

### Task 1: Análisis de la exfiltración de KeePass
**Explicación:**

Se examina el pcap en Wireshark/TShark filtrando por `tcp.dstport == 1337`, se extrae el payload (`xxd -ps -r`), se decodifica base64 y se aplica XOR con clave `'B'` (`get_kdbx.py`) para reconstruir `Database1337.kdbx`. Con `keepass_dump` se lee el volcado y con un script de fuerza bruta se genera la wordlist (carácter especial + `NoWaYIcanF0rGetThis123`). `keepass2john` + `john` recupera la contraseña, que permite abrir la base con `kpcli` y leer la flag `THM{B3tt3r_Upd4t3_Y0ur_K33p455}`.

Respuestas del lab (contenido original):

```
1. NoWaYIcanF0rGetThis123
2. No answer needed
3. THM{B3tt3r_Upd4t3_Y0ur_K33p455}
```

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la parte inicial de la contraseña de KeePass? | `NoWaYIcanF0rGetThis123` |
| 2 | ¿Escuentas la base de datos KeePass y la abres? | `No answer needed` |
| 3 | ¿Cuál es la flag? | `THM{B3tt3r_Upd4t3_Y0ur_K33p455}` |

---

**Metodología:** Análisis de pcap con TShark, extracción del payload binario (port 1337), decodificación base64 + XOR con scripting en Python, reconstrucción de la base KeePass, dumping con `keepass_dump`, crackeo con `keepass2john` + `john` y apertura final con `kpcli`.

**Learning chain:** Captura de tráfico → Extracción de payload → Decodificación en capas (base64 + XOR) → Análisis de la base KeePass → Fuerza bruta de la passphrase → Recuperación de la flag.

**Lección:** *Los volcados de memoria de gestores de contraseñas pueden ser robados por scripts maliciosos y exfiltrados encadenando codificaciones; ante capas de base64/XOR o un Kdbx con frase débil, la combinación de scripting y John the Ripper recupera las credenciales.*

**MITRE ATT&CK:** T1005 Data from Local System · T1560.002 Archive Collected Data: Archive via Library · T1555.004 Credentials from Password Stores: Windows Credential Manager/KeePass · T1059.001 Command and Scripting Interpreter: PowerShell.

**Fuente:** [TryHackMe - Extracted](https://tryhackme.com/room/extracted)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.