# Hacking Hadoop

| **Dificultad** | Hard |
| **Tipo** | Walkthrough |
| **Slug** | `hackinghadoop` |
| **Link** | [TryHackMe](https://tryhackme.com/room/hackinghadoop) |
| **Sección** | 03 Level Hard |
| **Fuente** | TryHackMe |
| **Componentes** | Apache Zeppelin / shiro.ini / Python / Kerberos (keytab, kinit) / HDFS / Hadoop / YARN / Ranger / klist |
| **Impacto** | Compromiso completo de un datalake Hadoop Kerberizado: RCE vía Apache Zeppelin, abuso del keytab para acceso a HDFS y escalada por suplantación del servicio YARN y a root hasta dominar todos los nodos del clúster. |

---

**Contexto:** El room despliega un datalake Hadoop con autenticación Kerberos (Kerberised) y varios de sus componentes: NameNode, Edge Node, YARN para el scheduling y Ranger para el control de acceso granular. El ataque comienza por el notebook de Apache Zeppelin del edge node, donde se explota la autenticación (shiro.ini) y el interpreter de Python para ejecutar comandos como el usuario OS `zp`. Con esa base se roba el keytab `zp.service.keytab`, se autentica con `kinit` y se leen los flags dispersos por HDFS, para después suplantar al servicio `yarn`, alcanzar las cuentas del NodeManager y, finalmente, escalar a root y comprometer el nodo secundario del clúster.

## Solucionario

### Task 1: Introduction

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed | `No answer needed` |

### Task 2: Hadoop Basics

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which node is responsible for actively keeping the directory tree structure of the datalake? | `Primary NameNode` |
| 2 | What type of node provides applications for users? | `Edge Node` |
| 3 | What Hadoop service is responsible for scheduling jobs? | `YARN` |
| 4 | What Hadoop service provides granular access control to resources? | `Ranger` |
| 5 | What is the term provided to a datalake that makes use of Kerberos for security? | `Kerberised` |
| 6 | Who owns the largest Hadoop cluster in the world? | `Facebook` |

### Task 3: Initial Access via Apache Zeppelin

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What edge node service is running on this host? | `Zeppelin` |
| 2 | What file is responsible for the authentication configuration for this service? | `shiro.ini` |
| 3 | What is the username and password combination that gives you your initial entry? (Format: <username>:<password>) | `user1:password2` |
| 4 | Once authenticated, submit the flag that is hiding nicely in one of the notebooks. | `THM{Whats.That.Smell.On.The.Hindenburg?}` |

### Task 4: Code Execution via the Interpreters

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the password of the user allowed to interface with the interpreters and provided notebook? | `p@ssw0rd12345` |
| 2 | Which active interpreter can be used to execute code? | `python` |
| 3 | What OS user does the application run as? | `zp` |
| 4 | What is the value of the flag found in the user's home directory (flag2.txt)? | `THM{It.Was.Hydrogen!}` |

### Task 5: Kerberos Keytab and HDFS

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which directory stores the keytabs for the Hadoop services? | `/etc/security/keytabs/` |
| 2 | What is the keytab file's name associated with the compromised user? | `zp.service.keytab` |
| 3 | What is the first principal stored in this keytab file? | `zp/hadoop.docker.com@EXAMPLE.COM` |
| 4 | What is the full verbose command to authenticate with this keytab using the full file path? | `kinit zp/hadoop.docker.com@EXAMPLE.COM -k -V -t /etc/security/keytabs/zp.service.keytab` |
| 5 | What is the value of the flag stored in the compromised user's HDFS home directory (flag3.txt)? | `THM{Now.We.Are.Talking.About.Distributed.Storage}` |

### Task 6: YARN Impersonation

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the service we will attempt to impersonate for privilege escalation? | `yarn` |
| 2 | What is the value of the flag in the impersonated user's HDFS home directory (flag4.txt)? | `THM{Little.Kitty.Goes.Meow}` |
| 3 | What is the value of the flag in the impersonated user's OS home directory (flag5.txt)? | `THM{Little.Kitty.Got.Its.Ball.Of.Yarn}` |

### Task 7: NodeManager Flags

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the value of the flag associated with the NodeManager's HDFS home directory (flag6.txt)? | `THM{Regional.Assistant.Manager}` |
| 2 | What is the value of the flag associated with the NodeManager's OS home directory (flag7.txt)? | `THM{Assistance.To.The.Regional.Manager}` |

### Task 8: Root Privilege Escalation

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the value of the flag in the root user's home directory (flag8.txt)? | `THM{This.Has.Got.To.Be.The.Saddest.Root.Privesc.Ever}` |
| 2 | What is the value of the flag in the root user's HDFS home directory (flag9.txt)? | `THM{Nothing.Can.Stop.You.Now!}` |

### Task 9: Secondary Cluster Node

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the value of the flag in the root user's directory on the secondary cluster node (flag10.txt)? | `THM{This.Just.Keeps.Getting.Sadder.And.Sadder}` |

### Task 10: Conclusion

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed | `No answer needed` |

---

**Metodología:**
1. Reconocer el datalake (arquitectura Hadoop/edge node, YARN, Ranger y Kerberos) y localizar el notebook Apache Zeppelin corriendo en el edge node.
2. Autenticarse en Zeppelin con `user1:password2` (configurado en `shiro.ini`) y buscar en los notebooks el flag oculto.
3. Recuperar la contraseña del usuario que puede hablar con los interpreters (`p@ssw0rd12345`) y ejecutar código con el interpreter `python` como el usuario OS `zp` para leer `flag2.txt`.
4. Con acceso a `zp`, extraer el keytab `/etc/security/keytabs/zp.service.keytab`, autenticarse con `kinit` (modo verbose) usando el principal `zp/hadoop.docker.com@EXAMPLE.COM` y acceder a HDFS para leer `flag3.txt`.
5. Suplantar el servicio `yarn` para escalar: leer sus flags en HDFS (`flag4.txt`) y en su home de SO (`flag5.txt`).
6. Avanzar hacia el NodeManager (`flag6.txt` y `flag7.txt`), escalar a root (`flag8.txt` y `flag9.txt`) y comprometer el nodo secundario del clúster (`flag10.txt`).

**Learning chain:** `Zeppelin (RCE) → interpreter python → usuario zp → keytab → Kerberos (kinit) → HDFS → impersonación YARN → NodeManager → root → clúster completo`

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1078 (Valid Accounts), T1005 (Data from Local System), T1068 (Exploitation for Privilege Escalation), T1083 (File and Directory Discovery)

**Fuente:** [TryHackMe - Hacking Hadoop](https://tryhackme.com/room/hackinghadoop)