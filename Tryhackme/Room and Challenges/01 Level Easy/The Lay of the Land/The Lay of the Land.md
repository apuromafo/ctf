# The Lay of the Land

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `thelayoftheland` | https://tryhackme.com/room/thelayoftheland | 01 Level Easy | TryHackMe | Active Directory / Get-ADUser / thmredteam.com / Defender / PowerView.ps1 / firewall (Get-NetFirewallRule) / servicios (netstat) / DNS zone transfer (nslookup) / sysmon | Enumeración inicial de un entorno AD y de una máquina Windows (dominio, usuarios, soluciones de seguridad de host, servicios y DNS) para hacerse con información clave antes de atacar. |

---

**Contexto:** Room de la ruta Red Team que enseña a conocer el terreno ("lay of the land") en un entorno corporativo: tecnologías comunes y productos de seguridad, tanto de host como de red. Sobre la máquina Windows adjunta se identifica si está en un AD y su dominio (`thmredteam.com`), se enumeran usuarios con `Get-ADUser` (6 usuarios, admin `thmadmin@thmredteam.com`), se revisa Windows Defender (alerta por `PowerView.ps1`), el firewall (regla THM-Connection con puerto 17337) y aplicaciones/servicios (THM Service en 13337) y se realiza una transferencia de zona DNS con `nslookup.exe` que entrega las flags.

> **ES:** Enumeración de terreno en AD: dominio thmredteam.com, usuarios (Get-ADUser, 6 usuarios y thmadmin@thmredteam.com), Defender (PowerView.ps1), firewall (THM-Connection -> 17337), servicio THM (13337) y DNS zone transfer (flags).
> **EN:** Ground truth enumeration in an AD environment: thmredteam.com domain, users (Get-ADUser, 6 users and thmadmin@thmredteam.com), Defender (PowerView.ps1), firewall (THM-Connection -> 17337), THM service (13337) and DNS zone transfer (flags).

## Solucionario

### Task 1: Red Team / Red Team

**Explicación:** Contexto de la room: como red teamer hay que conocer el terreno antes de atacar: redes, hosts, dominios y credenciales. Sin respuesta que rellenar en esta tarea.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Lee la introducción de la room. / Read the room introduction. | `No answer needed` |

### Task 2: Despliega la máquina / Deploy the machine

**Explicación:** Se despliega la máquina Windows del laboratorio, accesible vía VPN o AttackBox. No requiere respuesta más allá del despliegue.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Despliega la máquina. / Deploy the machine. | `No answer needed` |

### Task 3: Soluciones de seguridad de host / Host Security Solutions

**Explicación:** Introducción a las soluciones de seguridad de host (AV, EDR, Sysmon, firewall) y cómo enumerarlas en Windows (wmic, Get-CimInstance, Get-Service WinDefend, firewall). Sin respuesta que rellenar en esta tarea.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Lee la tarea de soluciones de seguridad de host. / Read the host security solutions task. | `No answer needed` |

### Task 4: Entorno de Active Directory / Active Directory

**Explicación:** Se comprueba si la máquina forma parte de un entorno AD (con `systeminfo` y dominio) y se identifica el nombre del dominio: `thmredteam.com`.

**Respuestas originales verbatim:**
```text
4. 1. Y
   2. thmredteam.com
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿La máquina adjunta forma parte del entorno AD? (Y/N) / Is the attached machine part of the AD environment? (Y/N) | `Y` |
| 2 | ¿Cuál es el nombre de dominio del AD? / What is the domain name of the AD? | `thmredteam.com` |

### Task 5: Usuarios / Users

**Explicación:** Se enumeran los usuarios del dominio en la OU THM con `Get-ADUser -Filter * -SearchBase "OU=THM,DC=THMREDTEAM,DC=COM"`: hay 6 usuarios disponibles y la cuenta de administración tiene como UserPrincipalName (email) `thmadmin@thmredteam.com`.

**Respuestas originales verbatim:**
```text
5. 1. 6
   2. thmadmin@thmredteam.com
```

```powershell
Get-ADUser -Filter * -SearchBase "OU=THM,DC=THMREDTEAM,DC=COM"
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Cuántos usuarios están disponibles? / How many users are available? | `6` |
| 2 | ¿Cuál es el UserPrincipalName (email) de la cuenta de admin? / What is the UserPrincipalName (email) of the admin account? | `thmadmin@thmredteam.com` |

### Task 6: Ataque a la red / Network attacks

**Explicación:** Se revisan las soluciones de seguridad de la máquina: Windows Defender reporta una alerta cuyo archivo causante es `PowerView.ps1`, el firewall de host está deshabilitado de forma insegura y la regla THM-Connection permite el puerto `17337`.

**Respuestas originales verbatim:**
```text
6. 1. N
   2. PowerView.ps1
   3. 17337
   4. No answer needed
```

```powershell
Get-MpThreat
Get-NetFirewallRule | Select DisplayName, Enabled, Description | findstr "THM-Connection"
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿El firewall de la máquina está habilitado? (Y/N) / Is the host-based firewall enabled? (Y/N) | `N` |
| 2 | ¿Cuál es el nombre del archivo que produce la alerta de Defender? / What is the file name that causes this alert to record? | `PowerView.ps1` |
| 3 | ¿Qué puerto está permitido bajo la regla THM-Connection? / What is the port that is allowed under the THM-Connection rule? | `17337` |
| 4 | Completa la tarea de soluciones de seguridad. / Complete the security solutions task. | `No answer needed` |

### Task 7: Soluciones de seguridad de red / Network Security Solutions

**Explicación:** Se introducen las soluciones de seguridad de red que protegen el tráfico en el entorno corporativo (firewalls de red, segmentación, IPS/IDS). Sin respuesta que rellenar.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Lee la tarea de soluciones de seguridad de red. / Read the network security solutions task. | `No answer needed` |

### Task 8: Aplicaciones y servicios / Applications and Services

**Explicación:** Introducción a la enumeración de aplicaciones y servicios corriendo en el host (wmic, Get-Process, netstat, servicios Windows). Sin respuesta que rellenar en esta tarea.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Lee la tarea de aplicaciones y servicios. / Read the applications and services task. | `No answer needed` |

### Task 9: Enumeración de servicios y DNS / Enumerating Services and DNS

**Explicación:** Se enumeran los servicios en escucha: el THM Service escucha en el puerto `13337`, y al visitar localhost en ese puerto aparece la flag `THM{S3rv1cs_1s_3numerat37ed}`. Finalmente, enumerando el DNS del DC (`nslookup.exe` + `ls -d thmredteam.com` para la transferencia de zona) se obtiene la flag `THM{DNS-15-Enumerated!}` de uno de los registros.

**Respuestas originales verbatim:**
```text
9. 1. 13337
   2. THM{S3rv1cs_1s_3numerat37ed}
   3. THM{DNS-15-Enumerated!}
```

```powershell
netstat -noa | findstr "LISTENING" | findstr "13337"
curl http://127.0.0.1:13337
nslookup.exe
> server <DC_IP>
> ls -d thmredteam.com
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Cuál es el número de puerto del THM Service? / What is the port number? | `13337` |
| 2 | Visita el localhost en el puerto de la pregunta anterior. ¿Cuál es la flag? / Visit the localhost on the port you found in the previous question. What is the flag? | `THM{S3rv1cs_1s_3numerat37ed}` |
| 3 | Enumera el nombre de dominio del DC, thmredteam.com, con nslookup.exe y realiza una transferencia de zona DNS. ¿Cuál es la flag de uno de los registros? / Now enumerate the domain name of the domain controller, thmredteam.com, using the nslookup.exe, and perform a DNS zone transfer. What is the flag for one of the records? | `THM{DNS-15-Enumerated!}` |

### Task 10: Conclusión / Conclusion

**Explicación:** Cierre de la room: se ha obtenido una foto completa del terreno (dominio, usuarios, soluciones de seguridad, servicios y DNS) lista para la siguiente fase ofensiva. Sin respuesta que rellenar.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Completa la conclusión. / Complete the conclusion. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Lee la introducción de la room. / Read the room introduction. | `No answer needed` |
| 2 | Despliega la máquina. / Deploy the machine. | `No answer needed` |
| 3 | Lee la tarea de soluciones de seguridad de host. / Read the host security solutions task. | `No answer needed` |
| 4 | ¿La máquina adjunta forma parte del entorno AD? (Y/N) / Is the attached machine part of the AD environment? (Y/N) | `Y` |
| 5 | ¿Cuál es el nombre de dominio del AD? / What is the domain name of the AD? | `thmredteam.com` |
| 6 | ¿Cuántos usuarios están disponibles? / How many users are available? | `6` |
| 7 | ¿Cuál es el UserPrincipalName (email) de la cuenta de admin? / What is the UserPrincipalName (email) of the admin account? | `thmadmin@thmredteam.com` |
| 8 | ¿El firewall de la máquina está habilitado? (Y/N) / Is the host-based firewall enabled? (Y/N) | `N` |
| 9 | ¿Cuál es el nombre del archivo que produce la alerta de Defender? / What is the file name that causes this alert to record? | `PowerView.ps1` |
| 10 | ¿Qué puerto está permitido bajo la regla THM-Connection? / What is the port that is allowed under the THM-Connection rule? | `17337` |
| 11 | Completa la tarea de soluciones de seguridad. / Complete the security solutions task. | `No answer needed` |
| 12 | Lee la tarea de soluciones de seguridad de red. / Read the network security solutions task. | `No answer needed` |
| 13 | Lee la tarea de aplicaciones y servicios. / Read the applications and services task. | `No answer needed` |
| 14 | ¿Cuál es el número de puerto del THM Service? / What is the port number? | `13337` |
| 15 | Visita el localhost en el puerto de la pregunta anterior. ¿Cuál es la flag? | `THM{S3rv1cs_1s_3numerat37ed}` |
| 16 | Enumera el nombre de dominio del DC con nslookup.exe y haz una transferencia de zona DNS. ¿Cuál es la flag de uno de los registros? | `THM{DNS-15-Enumerated!}` |
| 17 | Completa la conclusión. / Complete the conclusion. | `No answer needed` |

---

**Metodología:** Comprobar el dominio (`systeminfo` -> thmredteam.com) -> enumerar usuarios con `Get-ADUser` (6, thmadmin@thmredteam.com) -> revisar Defender (`Get-MpThreat` -> PowerView.ps1) y firewall (`Get-NetFirewallRule` -> THM-Connection -> 17337) -> enumerar servicios (`netstat` -> 13337) -> leer la flag del servicio -> DNS zone transfer con `nslookup` (`ls -d thmredteam.com` -> THM{DNS-15-Enumerated!}) -> concluir.

### Cadena de ataque / Attack Chain

```text
systeminfo -> dominio thmredteam.com -> Get-ADUser -> 6 usuarios + thmadmin@thmredteam.com -> Defender/Get-MpThreat -> PowerView.ps1 -> Get-NetFirewallRule -> THM-Connection 17337 -> netstat -> THM Service 13337 -> localhost:13337 -> THM{S3rv1cs_1s_3numerat37ed} -> nslookup ls -d thmredteam.com -> DNS zone transfer -> THM{DNS-15-Enumerated!}
```

**Learning chain:** AD environment -> domain discovery -> user enumeration -> host security (Defender/firewall) -> service enumeration -> local flag -> DNS zone transfer -> flag.

**Lección:** *Antes de atacar hay que conocer el terreno: el dominio, los usuarios, las soluciones de seguridad y los servicios de una máquina son enumerables con cmdlets nativos de Windows, y una transferencia de zona DNS deja a la vista los registros del AD.*

**MITRE ATT&CK:** T1087 (Account Discovery), T1046 (Network Service Discovery), T1018 (Remote System Discovery), T1016 (System Network Configuration Discovery), T1007 (System Service Discovery), T1083 (File and Directory Discovery).

**Fuente:** [TryHackMe - The Lay of the Land](https://tryhackme.com/room/thelayoftheland)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.