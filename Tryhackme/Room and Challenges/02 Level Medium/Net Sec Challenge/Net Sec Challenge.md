# Net Sec Challenge

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
| Medium | Challenge | netsecchallenge | https://tryhackme.com/room/netsecchallenge | Red Network Security / Nmap | TryHackMe | Máquina objetivo, nmap, ftp, servidor web | High |

> **Objeto:** Aplicar todo lo aprendido en el módulo *Network Security*: escaneo de red con nmap, descubrimiento del servidor web y del FTP, extracción de las flags alojadas en cada servicio y respuesta a las preguntas de cultura general de seguridad de red.

---

**Contexto:**

El Net Sec Challenge es la prueba final del módulo de seguridad de redes. Se despliega una máquina en la red del laboratorio y se debe descubrir su dirección IP usando la técnica correcta de descubrimiento de hosts. Sobre esa máquina se ejecutan escaneos de puertos, servicios y versiones con nmap, se identifica el banner del servidor web y del FTP (vsftpd), se accede a cada servicio para recuperar las flags y se responde a preguntas teóricas sobre protocolos y herramientas de seguridad de red.

> **ES:** Primero se descubre la IP de la máquina desplegada con nmap, se escanean los puertos abiertos (8080 HTTP, 10021 FTP), se obtienen el banner y la versión (vsftpd 3.0.5) y se recuperan las flags del servidor web y del servicio FTP/SSH. Además se responden preguntas sobre protocolos de red y conceptos del módulo.

> **EN:** First the IP of the deployed machine is discovered with nmap, open ports are scanned (8080 HTTP, 10021 FTP), the banner and version are obtained (vsftpd 3.0.5) and the flags from the web server and the FTP/SSH service are recovered. Additionally, questions about network protocols and module concepts are answered.

## Solucionario

### Task 1: Configuración del laboratorio / Lab Setup
**Explicación:**

Se despliega la máquina y se prepara el entorno. Esta task no requiere respuesta escrita.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1 | `No answer needed` |

### Task 2: Escaneo y flags / Scanning and Flags
**Explicación:**

Se descubre la máquina en la red (p. ej., `nmap -sn` sobre la subred) y se escanean todos los puertos. Se identifican el servidor web (`8080`), el servicio FTP dentro del puerto (`10021`), el número de puertos abiertos (`6`), se navega al servidor web para capturar `THM{web_server_25352}`, se accede al servicio correcto para `THM{946219583339}`, se obtiene la versión del FTP (`vsftpd 3.0.5`), y se recuperan las flags `THM{321452667098}` y `THM{f7443f99}` de los servicios correspondientes.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Puerto del servidor web | `8080` |
| 2. Puerto del FTP | `10021` |
| 3. Total de puertos abiertos | `6` |
| 4. Flag del servidor web | `THM{web_server_25352}` |
| 5. Flag del servicio de red | `THM{946219583339}` |
| 6. Versión del FTP | `vsftpd 3.0.5` |
| 7. Flag del FTP | `THM{321452667098}` |
| 8. Flag del servidor SSH | `THM{f7443f99}` |

### Task 3: Cierre / Wrap-up
**Explicación:**

Se consolidan los resultados del escaneo y se da por concluido el reto.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 3 | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Task 1 | `No answer needed` |
| 2 | 1. Puerto del servidor web | `8080` |
| 2 | 2. Puerto del FTP | `10021` |
| 2 | 3. Total de puertos abiertos | `6` |
| 2 | 4. Flag del servidor web | `THM{web_server_25352}` |
| 2 | 5. Flag del servicio de red | `THM{946219583339}` |
| 2 | 6. Versión del FTP | `vsftpd 3.0.5` |
| 2 | 7. Flag del FTP | `THM{321452667098}` |
| 2 | 8. Flag del servidor SSH | `THM{f7443f99}` |
| 3 | Task 3 | `No answer needed` |

---

**Metodología:**

1. Descubrimiento de la máquina en la subred con nmap (`-sn`, ARP en la red local).
2. Escaneo de puertos completo (`-p-`) y detección de servicios/versiones (`-sV`).
3. Identificación del servidor web en `8080` y del FTP en `10021`.
4. Navegación web y conexión FTP para recuperar las flags.
5. Identificación del banner y versión (`vsftpd 3.0.5`) y acceso SSH.
6. Respuesta a las preguntas teóricas de seguridad de red.

### Cadena de ataque / Attack Chain

```
nmap -sn (descubrir IP del objetivo)
        |
        v
nmap -p- -sV (6 puertos abiertos: 8080 web, 10021 ftp, ...)
        |
        v
Navegar a http://IP:8080  -->  THM{web_server_25352}
        |
        v
FTP (10021, vsftpd 3.0.5)  -->  THM{946219583339} / THM{321452667098}
        |
        v
SSH  -->  THM{f7443f99}
```

**Learning chain:**

- ¿Cuál es la técnica de descubrimiento de hosts correcta según el escenario (ARP frente a ICMP/TCP)?
- ¿Cómo se combinan escaneos TCP conection, SYN y versiones para mapear una máquina?
- ¿Cómo se correlacionan servicios, banners y versiones para identificar qué firma usa cada flag?

**Lección:**

*El escaneo correcto es el 80% del reto: saber qué técnica usar, qué puertos escanear y cómo leer los banners determina dónde está cada flag y cómo obtenerla.*

**MITRE ATT&CK:**

- T1595.001 (Active Scanning: Scanning IP Blocks)
- T1595.002 (Active Scanning: Vulnerability Scanning)
- T1046 (Network Service Discovery)

**Fuente:** [TryHackMe - Net Sec Challenge](https://tryhackme.com/room/netsecchallenge)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.