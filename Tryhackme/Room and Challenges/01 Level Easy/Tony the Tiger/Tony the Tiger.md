# Tony the Tiger

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `tonythetiger` | [TryHackMe - Tony the Tiger](https://tryhackme.com/room/tonythetiger) | 01 Level Easy | THM | Apache Tomcat, JBoss, hash cracking, FTP | Pentest de servicios Java web y descifrado de credenciales |

---

**Contexto:** El reto explota servicios Java web (Apache Tomcat y JBoss) expuestos, incluyendo la subida de un payload para obtener una shell, el descifrado de un hash y el acceso a una cuenta privilegiada.

> **ES:** Pentest de una máquina con Tomcat y JBoss: se despliega un payload en el servidor para obtener una shell, se descifra un hash y se accede como usuario privilegiado para capturar la flag.
> **EN:** Pentest of a box running Tomcat and JBoss: a payload is deployed to get a shell, a hash is cracked and a privileged account grants the final flag.

## Solucionario

### Task 1: Respuestas / Answers

**Explicación:** Solución de las preguntas de la máquina Tony the Tiger: reconocimiento inicial, servidores web, flags, hash y credenciales.

1. No answer needed
2. 1. lamp
   2. dos
   3. byte streams
3. 1. Apache Tomcat/Coyote JSP engine 1.1
   2. JBoss
4. THM{Tony_Sure_Loves_Frosted_Flakes}
5. No answer needed
6. THM{50c10ad46b5793704601ecdad865eb06}
7. zxcvbnm123456789
8. No answer needed

### Tabla unificada de preguntas / Unified Q&A

| # | Respuesta / Answer |
|---|---|
| 1 | `No answer needed` |
| 2 | `lamp` / `dos` / `byte streams` |
| 3 | `Apache Tomcat/Coyote JSP engine 1.1` / `JBoss` |
| 4 | `THM{Tony_Sure_Loves_Frosted_Flakes}` |
| 5 | `No answer needed` |
| 6 | `THM{50c10ad46b5793704601ecdad865eb06}` |
| 7 | `zxcvbnm123456789` |
| 8 | `No answer needed` |

---

**Metodología:** Se realizó el reconocimiento de la máquina identificando Apache Tomcat/Coyote JSP engine 1.1 y JBoss. Se subió un payload al servidor web para obtener una reverse shell, se localizaron las flags de usuario y root y se descifró el hash (zxcvbnm123456789) que permitía acceder a la cuenta privilegiada.

### Cadena de ataque / Attack Chain

1. Enumeración de servicios web (Tomcat/Coyote 1.1 y JBoss).
2. Despliegue de un payload en la aplicación Java.
3. Obtención de una reverse shell.
4. Captura de la flag de usuario (`THM{Tony_Sure_Loves_Frosted_Flakes}`).
5. Descifrado del hash y acceso a la cuenta privilegiada.
6. Captura de la flag de root.

**Learning chain:** Enumeration → Tomcat & JBoss → payload deploy → reverse shell → hash cracking → privilege escalation

**Lección:** *Los paneles de administración de aplicaciones Java (Tomcat/JBoss) desprotegidos permiten desplegar artefactos arbitrarios que otorgan una shell; los hashes débiles se descifran con diccionarios comunes.*

**MITRE ATT&CK:** T1190 - Exploit Public-Facing Application, T1110 - Brute Force, T1569.002 - System Services: Service Execution

**Fuente:** [TryHackMe - Tony the Tiger](https://tryhackme.com/room/tonythetiger)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.