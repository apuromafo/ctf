# TShark

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Forense / Análisis de tráfico | tshark | https://tryhackme.com/room/tshark | 02 Level Medium | TryHackMe | TShark, PCAP, DNS, display filters, Base32, CyberChef | Detección y extracción de exfiltración de datos por DNS |

---

**Contexto:** La sala **TShark** enseña a usar la versión CLI de Wireshark para acelerar el análisis de capturas (pcap) cuando la interfaz gráfica no está disponible. Se aprende a leer ficheros `.pcap` (`tshark -r`), aplicar **display filters** (`-Y`), extraer campos concretos (`-T fields -e`) y detectar **exfiltración de datos por DNS**. El reto final consiste en reconstruir una cadena encadenada de consultas DNS sospechosas (ID de transacción `0xbeef`), extraer la subcadena codificada en **Base32** y descodificarla con CyberChef para obtener la flag.

## Solucionario

### Task 1: Pre-Reqs / Requisitos
**Explicación:**

Se instala `tshark` en la máquina de ataque (viene por defecto en Kali; con otras distribuciones se instala con `apt-get`).

```bash
sudo apt-get install tshark
tshark --version
```

| Pregunta | Respuesta |
|----------|-----------|
| Install TShark | `No answer needed` |

### Task 2: Reading PCAP Files / Lectura de PCAP
**Explicación:**

Se descarga/usa la captura `dns.cap` (por ejemplo) y se practica la lectura de paquetes. Para contar paquetes se combina `tshark -r` con `wc -l`; para filtrar registros DNS tipo A se usa el display filter `dns.qry.type==1`, y para extraer solo los nombres de dominio consultados se combina con `-T fields -e dns.qry.name`.

```bash
tshark -r dns.cap | wc -l        # 38
tshark -r dns.cap -Y "dns.qry.type==1"
tshark -r dns.cap -Y "dns.qry.type==1" -T fields -e dns.qry.name
```

**Respuestas de la captura:**

- Paquetes totales: `38`
- Registros A (incluyendo respuestas): `6`
- Registro A más presente: `GRIMM.utelsystems.local`

| Pregunta | Respuesta |
|----------|-----------|
| How many packets are in the dns.cap file? | `38` |
| How many A records are in the capture? (Including responses) | `6` |
| Which A record was present the most? | `GRIMM.utelsystems.local` |

### Task 3: DNS Exfil / Exfiltración DNS
**Explicación:**

Se analiza la captura de exfiltración por DNS. Se cuentan los paquetes totales y, filtrando únicamente las consultas (`dns.flags.response == 0`), el número de queries. Las consultas sospechosas comparten el ID de transacción `0xbeef`. Encadenando los subdominios de las queries de tipo `1` y eliminando los puntos con `tr -d "\n"` se reconstruye la cadena codificada en **Base32**. Descodificándola (con `base32 -d` o CyberChef) se obtiene la flag.

```bash
tshark -r dns_exfil.pcap | wc -l                        # 125
tshark -r dns_exfil.pcap -Y "dns.flags.response==0" | wc -l   # 56
tshark -r dns_exfil.pcap -Y "dns.flags.response==0" -T fields -e dns.id | sort -u
# 0xbeef

tshark -r dns_exfil.pcap -Y "dns.flags.response == 0" -T fields -e dns.qry.name | cut -d "." -f1 | tr -d "\n" | base32 -d && echo
# flag{th1s_is_t0ugh_with0u7_tsh4rk!}
```

La cadena extraída es: `MZWGCZ33ORUDC427NFZV65BQOVTWQX3XNF2GQMDVG5PXI43IGRZGWIL5`

| Pregunta | Respuesta |
|----------|-----------|
| How many packets are in the dns_exfil pcap file? | `125` |
| How many DNS queries are in this pcap? (Not responses!) | `56` |
| What is the DNS transaction ID of the suspicious queries (in hex)? | `0xbeef` |
| What is the string extracted from the DNS queries? | `MZWGCZ33ORUDC427NFZV65BQOVTWQX3XNF2GQMDVG5PXI43IGRZGWIL5` |
| What is the flag? | `flag{th1s_is_t0ugh_with0u7_tsh4rk!}` |

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Install TShark | `No answer needed` |
| 2 | How many packets are in the dns.cap file? | `38` |
| 2 | How many A records are in the capture? (Including responses) | `6` |
| 2 | Which A record was present the most? | `GRIMM.utelsystems.local` |
| 3 | How many packets are in the dns_exfil pcap file? | `125` |
| 3 | How many DNS queries are in this pcap? (Not responses!) | `56` |
| 3 | What is the DNS transaction ID of the suspicious queries (in hex)? | `0xbeef` |
| 3 | What is the string extracted from the DNS queries? | `MZWGCZ33ORUDC427NFZV65BQOVTWQX3XNF2GQMDVG5PXI43IGRZGWIL5` |
| 3 | What is the flag? | `flag{th1s_is_t0ugh_with0u7_tsh4rk!}` |

---

**Metodología:** Conteo de paquetes y filtrado de tráfico DNS con display filters de TShark, extracción de campos concretos (`dns.id`, `dns.qry.name`), concatenación de subdominios exfiltrados y descodificación Base32 (CyberChef / `base32 -d`) para recuperar la flag.

### Cadena de ataque / Attack Chain

```
tshark -r (lectura) → wc -l (conteo) → -Y "dns.flags.response==0" (queries) → dns.id=0xbeef (sospechosas) → -T fields -e dns.qry.name + cut/tr (cadena) → Base32 decode → flag
```

**Learning chain:** Familiarización con la CLI → filtros de visualización → extracción de campos → correlación de queries → decodificación de datos exfiltrados.

**Lección:** *El DNS es un canal habitual de exfiltración: consultas con IDs repetidos y subdominios que concatenados forman una cadena codificada delatan al atacante; TShark permite automatizar su detección y recuperación.*

**MITRE ATT&CK:** T1040 Network Sniffing · T1048.003 Exfiltration Over Alternative Protocol (DNS/Web Service) · T1560.001 Archive Collected Data.

**Fuente:** [TryHackMe - TShark](https://tryhackme.com/room/tshark)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.