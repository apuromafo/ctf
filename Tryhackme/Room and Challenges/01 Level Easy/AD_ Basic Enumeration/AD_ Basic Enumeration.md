# AD: Basic Enumeration

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `adbasicenumeration` | https://tryhackme.com/room/adbasicenumeration | 01 Level Easy | TryHackMe | Nmap / smbclient / ldapsearch / enum4linux-ng / kerbrute / rpcclient / CrackMapExec (crackmapexec) / password spraying | Enumeración básica de Active Directory sin credenciales: descubrir el dominio, versiones, shares SMB, usuarios/grupos vía LDAP y políticas de contraseña, para terminar con un password spraying con CrackMapExec. |

---

**Contexto:** Room de la ruta Jr. Penetration Tester centrada en enumerar un entorno AD al que se accede por VPN sin credenciales previas. Se parte de un escaneo de red para identificar el Domain Controller y su sistema `za.tryhackme.loc`, con Windows Server 2019 Datacenter. Después se enumeran shares SMB (flag en uno de ellos), usuarios y grupos vía LDAP (grupo de rduke, nombre completo, RID mapping) y la política de contraseñas, para cerrar con un ataque de password spraying que recupera unas credenciales válidas. Todo es enumeration previa al acceso autenticado.

> **ES:** Enumerar el dominio `tryhackme.loc`, sus shares, usuarios y políticas antes de conseguir credenciales; el paso final es un password spraying con CrackMapExec.
> **EN:** Enumerating the `tryhackme.loc` domain, its shares, users and password policy before having valid credentials; the final step is a CrackMapExec password spraying.

## Solucionario

### Task 1: Desplegar la máquina / Deploy the machine

**Explicación:** Se despliega el entorno del laboratorio (máquinas THMWRK1/THMDC y el jump host) y se comprueba la conectividad por VPN o AttackBox. La máquina atacante es la única forma de interactuar con el dominio en esta fase. No requiere respuesta más allá del despliegue.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Despliega la máquina del laboratorio. | `No answer needed` |

### Task 2: Enumeración de red / Network Enumeration

**Explicación:** Con un escaneo de puertos dirigido (SMB 445, LDAP 389, RPC 135, Kerberos 88) se identifica el Domain Controller. Sobre él, consultando DNS/LDAP y el hostname se obtiene el dominio: `tryhackme.loc`, corriendo sobre Windows Server 2019 Datacenter.

```bash
nmap -p 88,135,139,389,445 -sV -sC <DC_IP>
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the domain name of our target? / ¿Cuál es el nombre de dominio del objetivo? | `tryhackme.loc` |
| 2 | What version of Windows Server is running on the DC? / ¿Qué versión de Windows Server corre en el DC? | `Windows Server 2019 Datacenter` |

### Task 3: Enumeración de shares SMB / Enumerating Shares

**Explicación:** Se listan los recursos compartidos SMB del dominio. Entre los shares accesibles sin credenciales hay uno de lectura abierta que contiene un archivo con la flag.

```bash
smbclient -L //<DC_IP> -N
smbclient //<DC_IP>/<share> -N
get <archivo>
cat <archivo>
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag hidden in one of the shares? / ¿Cuál es la flag oculta en uno de los shares? | `THM{88_SMB_88}` |

### Task 4: Enumeración de usuarios y grupos / Enumerating Users and Groups

**Explicación:** Mediante consultas LDAP sin credenciales (`ldapsearch -x -H ldap://<DC_IP> -b "dc=tryhackme,dc=loc" "(objectClass=person)"`) se listan los usuarios del dominio. Para el usuario `rduke` se identifica su grupo (Domain Users), su nombre completo (Raoul Duke), y mapeando objectSID a RID con un pequeño script se asocia el RID 1634 al usuario `katie.thomas`.

```bash
ldapsearch -x -H ldap://<DC_IP> -b "dc=tryhackme,dc=loc" "(objectClass=person)"
# decode_object_sid.py para mapear objectSid -> RID (1634 -> katie.thomas)
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What group is the user rduke part of? / ¿De qué grupo forma parte el usuario rduke? | `Domain Users` |
| 2 | What is this user's full name? / ¿Cuál es el nombre completo de este usuario? | `Raoul Duke` |
| 3 | Which username is associated with RID 1634? / ¿Qué nombre de usuario está asociado al RID 1634? | `katie.thomas` |

### Task 5: Política de contraseñas y password spraying / Password Policies and Spraying

**Explicación:** Se lee la política de contraseñas del dominio (mínimo 7 caracteres y bloqueo de 2 minutos tras fallos), datos necesarios para diseñar el spraying sin bloquear cuentas. Con una lista de usuarios enumerada y una lista pequeña de contraseñas probables se lanza CrackMapExec contra el equipo de trabajo: la única combinación válida es `rduke:Password1!`.

```bash
rpcclient -U "" -N <DC_IP>
# > getdompwinfo -> mínimo 7 caracteres, lockout 2 minutos
crackmapexec smb <WRK_IP> -u users.txt -p passwords.txt
# [+] smb://<WRK_IP> rduke:Password1!
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the minimum password length? / ¿Cuál es la longitud mínima de contraseña? | `7` |
| 2 | What is the locked account duration? / ¿Cuál es la duración del bloqueo de cuenta? | `2 minutes` |
| 3 | Perform password spraying using CrackMapExec. What valid credentials did you find? (format: username:password) / Haz password spraying con CrackMapExec. ¿Qué credenciales válidas encontraste? (formato: usuario:contraseña) | `rduke:Password1!` |

### Task 6: Conclusión / Conclusion

**Explicación:** Cierre de la room: la enumeración sin credenciales permitió mapear el dominio, sus shares, usuarios, políticas y recuperar credenciales válidas, preparando el acceso autenticado para la siguiente fase. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la conclusión de la room. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the domain name of our target? | `tryhackme.loc` |
| 2 | What version of Windows Server is running on the DC? | `Windows Server 2019 Datacenter` |
| 3 | What is the flag hidden in one of the shares? | `THM{88_SMB_88}` |
| 4 | What group is the user rduke part of? | `Domain Users` |
| 5 | What is this user's full name? | `Raoul Duke` |
| 6 | Which username is associated with RID 1634? | `katie.thomas` |
| 7 | What is the minimum password length? | `7` |
| 8 | What is the locked account duration? | `2 minutes` |
| 9 | Perform password spraying using CrackMapExec. What valid credentials did you find? (format: username:password) | `rduke:Password1!` |

---

**Metodología:** Host discovery y escaneo de puertos para localizar el DC y el equipo de trabajo; extraer el dominio y la versión del servidor; enumerar shares SMB abiertos (flag); listar usuarios/grupos con LDAP y resolver RIDs; obtener la política de contraseñas para calibrar el ataque; y lanzar un password spraying con CrackMapExec contra la lista de usuarios para obtener `rduke:Password1!`.

### Cadena de ataque / Attack Chain

```text
Nmap -> identificar DC (tryhackme.loc, WS2019) -> smbclient (shares, flag) -> ldapsearch (usuarios/grupos/RID) -> rpcclient (política de contraseñas) -> crackmapexec (password spraying) -> credenciales válidas
```

**Learning chain:** Host discovery -> SMB enumeration -> LDAP enumeration -> RID mapping -> password policy -> password spraying -> credenciales.

**Lección:** *La enumeración sin credenciales puede revelar todo un dominio: shares abiertos, usuarios, políticas y, con password spraying calibrado, las primeras credenciales válidas.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1087 (Account Discovery), T1069 (Permission Groups Discovery), T1110 (Brute Force / Password Spraying)

**Fuente:** [TryHackMe - AD: Basic Enumeration](https://tryhackme.com/room/adbasicenumeration)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.