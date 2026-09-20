# Skynet

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | CTF challenge / box | `skynet` | https://tryhackme.com/room/skynet | 01 Level Easy | TryHackMe | Nmap / SMB (Samba) / curl / enumeración de comparticiones (cifs) / LFI->RFI / credenciales en archivo / SSH / explotación y banderas | Caja CTF: enumerar servicios (web y SMB), conseguir credenciales, abusar de un LFI/RFI para ejecutar comandos y subir privilegios hasta leer la flag. |

---

**Contexto:** Room de tipo caja en el nivel Easy. Se parte únicamente con la IP de la máquina y hay que enumerar los servicios expuestos (HTTP y Samba/SMB). En SMB hay una compartición con credenciales, el servicio web es vulnerable a inclusión de archivos (LFI abusado como RFI) que permite ejecutar comandos, y con ello se obtiene acceso y la flag del reto.

> **ES:** Enumera la caja, saca las credenciales de SMB, explota el LFI/RFI del servicio web y consigue la flag.
> **EN:** Enumerate the box, grab the credentials from SMB, exploit the LFI/RFI on the web service and get the flag.

## Solucionario

### Task 1: Explota Skynet / Exploit Skynet

**Explicación:** Las respuestas de la room se corresponden con las credenciales encontradas (usuario y contraseña en la compartición SMB), el tipo de vulnerabilidad que permite tomar control del servicio web (inclusión remota de archivo, explotada como RFI) y las dos flags del reto. Se conserva el contenido original completo, incluida la frase suelta:

1. 1. cyborg007haloterminator
   2. /45kra24zxs28v3yd
   3. remote file inclusion 
   4. 7ce5c2109a40f958099283600a9ae807
   5. 3f0372db24753accc7179a282cd6a949

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Pregunta 1 / Question 1 | `cyborg007haloterminator` |
| 2 | Pregunta 2 / Question 2 | `/45kra24zxs28v3yd` |
| 3 | Pregunta 3 / Question 3 | `remote file inclusion ` |
| 4 | Pregunta 4 / Question 4 | `7ce5c2109a40f958099283600a9ae807` |
| 5 | Pregunta 5 / Question 5 | `3f0372db24753accc7179a282cd6a949` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Pregunta 1 / Question 1 | `cyborg007haloterminator` |
| 2 | Pregunta 2 / Question 2 | `/45kra24zxs28v3yd` |
| 3 | Pregunta 3 / Question 3 | `remote file inclusion ` |
| 4 | Pregunta 4 / Question 4 | `7ce5c2109a40f958099283600a9ae807` |
| 5 | Pregunta 5 / Question 5 | `3f0372db24753accc7179a282cd6a949` |

---

**Metodología:** Enumeración de puertos con Nmap para localizar HTTP y SMB. Se enumeran las comparticiones Samba con credenciales anónimas para encontrar el archivo que revela usuario y contraseña. Con esas credenciales se explota el LFI del sitio web convirtiéndolo en RFI para ejecutar comandos arbitrarios, y de ahí obtener el shell y las flags del reto.

### Cadena de ataque / Attack Chain

```text
Nmap -> HTTP + SMB -> smbclient (enumeración anónima) -> credenciales en compartición -> LFI/RFI en web -> RCE (ejecución de comandos) -> flag
```

**Learning chain:** Port discovery -> service identification (HTTP/SMB) -> SMB anonymous share enumeration -> credentials -> LFI->RFI -> code/command execution -> flag.

**Lección:** *Una compartición SMB accesible de forma anónima puede filtrar credenciales, y un LFI mal gestionado se convierte en un RFI/RCE cuando admite cabeceras o parámetros que apunten a un recurso controlado por el atacante.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1083 (File and Directory Discovery), T1190 (Exploit Public-Facing Application), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Skynet](https://tryhackme.com/room/skynet)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
