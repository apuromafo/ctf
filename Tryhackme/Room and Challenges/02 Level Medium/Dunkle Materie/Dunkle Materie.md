# Dunkle Materie

| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `dunklematerie` |
| **Link** | [TryHackMe](https://tryhackme.com/room/dunklematerie) |
| **Sección** | 02 Level Medium |
| **Fuente** | thmrevenant (GitHub) |
| **Componentes** | PCAP / Wireshark / análisis de malware / ransomware / BlackMatter / DNS / registro de Windows |
| **Impacto** | Análisis de tráfico de red y artefactos de un host comprometido para reconstruir y atribuir una infección por el ransomware BlackMatter |

---

**Contexto:** Dunkle Materie (Dark Matter) es un reto de análisis de malware/DFIR en el que se entrega un PCAP y los artefactos de un host Windows comprometido por el ransomware BlackMatter. Se correlaciona el tráfico de red (puertos 8644/7128, dominios mojobiden.com y paymenthacks.com, IPs 146.112.61.108 y 206.188.197.206, User-Agent Firefox/89.0 y resolución DNS de Cisco Umbrella) con el ejecutable malicioso (c:\users\sales\appdata\local\temp\exploreer.exe), la nota de rescate (ley9kpi9r.bmp), el PID 4892 y la unidad montada HKLM\SYSTEM\MountedDevices\DosDevices\Z: para concluir la familia de malware.

## Solucionario

### Task 1: Preguntas del reto

**Explicación:** Combinando el análisis del PCAP con la inspección del host se responden las cuestiones del reto. El tráfico usa los puertos **8644,7128**; el ejecutable malicioso es **c:\users\sales\appdata\local\temp\exploreer.exe**; los dominios C2 son **mojobiden.com,paymenthacks.com**; las IPs son **146.112.61.108,206.188.197.206**; el User-Agent es **Firefox/89.0**; la resolución DNS apunta a **Cisco Umbrella**; la nota de rescate es **ley9kpi9r.bmp**; el proceso tiene PID **4892**; el valor de registro de la unidad montada es **HKLM\SYSTEM\MountedDevices\DosDevices\Z:**; y la familia de malware identificada es **Blackmatter Ransomware**.

1. 8644,7128
2. c:\users\sales\appdata\local\temp\exploreer.exe
3. mojobiden.com,paymenthacks.com
4. 146.112.61.108,206.188.197.206
5. Firefox/89.0
6. Cisco Umbrella
7. ley9kpi9r.bmp
8. 4892
9. HKLM\SYSTEM\MountedDevices\DosDevices\Z:
10. Blackmatter Ransomware

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué puertos se observan en el tráfico malicioso? | `8644,7128` |
| 2 | ¿Cuál es la ruta del ejecutable malicioso? | `c:\users\sales\appdata\local\temp\exploreer.exe` |
| 3 | ¿Qué dominios se observan en el tráfico? | `mojobiden.com,paymenthacks.com` |
| 4 | ¿Qué direcciones IP aparecen? | `146.112.61.108,206.188.197.206` |
| 5 | ¿Qué User-Agent usa el tráfico? | `Firefox/89.0` |
| 6 | ¿Qué servicio/proveedor DNS responde? | `Cisco Umbrella` |
| 7 | ¿Cuál es la nota de rescate? | `ley9kpi9r.bmp` |
| 8 | ¿Qué PID tiene el proceso malicioso? | `4892` |
| 9 | ¿Qué valor de registro indica la unidad montada? | `HKLM\SYSTEM\MountedDevices\DosDevices\Z:` |
| 10 | ¿Qué familia de malware es? | `Blackmatter Ransomware` |

---

**Metodología:**

1. Abrir el PCAP con Wireshark y filtrar las conversaciones de red (puertos 8644/7128, dominios e IPs).
2. Revisar headers HTTP/HTTPS y el User-Agent (Firefox/89.0) para caracterizar el tráfico.
3. Correlacionar con el host: localizar el ejecutable malicioso (exploreer.exe en temp de sales), su PID y la nota de rescate.
4. Revisar el registro de Windows (MountedDevices, unidad Z:) y la configuración DNS (Cisco Umbrella).
5. Concluir la atribución: BlackMatter ransomware.

**Learning chain:** PCAP -> Wireshark -> Tráfico 8644/7128 -> Dominios mojobiden/paymenthacks -> IPs -> User-Agent Firefox/89.0 -> Cisco Umbrella -> exploreer.exe -> Nota ley9kpi9r.bmp -> PID 4892 -> MountedDevices Z: -> BlackMatter

**Lección:** *Correlacionar el tráfico de red con los artefactos del host permite reconstruir una infección de ransomware y atribuirla a una familia concreta.*

**MITRE ATT&CK:** T1486 (Data Encrypted for Impact), T1071.001 (Web Protocols), T1105 (Ingress Tool Transfer), T1027.002 (Software Packing)

**Fuente:** [TryHackMe - Dunkle Materie](https://tryhackme.com/room/dunklematerie)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.