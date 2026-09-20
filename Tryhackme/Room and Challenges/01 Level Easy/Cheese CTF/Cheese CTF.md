# Cheese CTF

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | ctf | `cheesectf` | [TryHackMe](https://tryhackme.com/room/cheesectf) | 01 Level Easy | THM | SQLi, LFI, php://filter chain, RCE, authorized_keys, systemd timer, SUID xxd | Medio |

---

**Contexto:** Máquina CTF ambientada en una tienda de quesos. La tienda web tiene un login vulnerable a SQL injection (`' || 1=1;-- -`), y tras fuzzear se descubre `/secret-script.php`, un endpoint con Local File Inclusion (include() sin sanitizar) explotable con `php://filter`. Encadenando filtros PHP se logra RCE y una shell como www-data. Se escribe una clave pública en el authorized_keys del usuario comte para pivotar, y finalmente se abusan los privilegios de systemctl sobre un timer (exploit.timer) que copia /usr/bin/xxd a /opt/xxd con el bit SUID, permitiendo escribir la clave pública de root en /root/.ssh/authorized_keys y obtener root.

> **ES:** Box CTF: SQLi en el login → descubrimiento de /secret-script.php → LFI → encadenado de filtros php://filter para RCE → reverse shell como www-data → pivot a comte vía authorized_keys escribible → abuso de exploit.timer/service con systemctl → binario xxd con SUID (GTFOBins) → escritura del authorized_keys de root → root y flags.

> **EN:** CTF box: SQLi on the login → discovery of /secret-script.php → LFI → php://filter chaining to achieve RCE → reverse shell as www-data → pivot to comte via a writable authorized_keys → abuse of exploit.timer/service with systemctl → SUID xxd (GTFOBins) → writing root's authorized_keys → root and flags.

## Solucionario

### Task 1: Deploy / Despliegue

**Explicación:** Iniciar la máquina y realizar el reconocimiento inicial de servicios (web en el puerto 80, SSH en el 22).

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Deploy the machine / Confirmación | `No answer needed` |

### Task 2: Flags / Flags

**Explicación:** Se empieza fuzzeando la app de la tienda de quesos hasta encontrar messages.html, que enlaza con `/secret-script.php?file=...`, un include sin sanitizar vulnerable a LFI. Un SQLi con `' || 1=1;-- -` salta el login. Leyendo login.php y secret-script.php con `php://filter/convert.base64-encode/resource=` se confirma la inclusión arbitraria; con un generador de cadenas de filtros PHP se consigue RCE (`php://filter` chain) y una reverse shell como www-data. Se observa que /home/comte/.ssh/authorized_keys es escribible, así que se añade la clave pública generada y se entra por SSH como comte. Como comte hay NOPASSWD para `/bin/systemctl daemon-reload | restart | start | enable exploit.timer`; el exploit.service copia /usr/bin/xxd a /opt/xxd con SUID. Tras rellenar `OnBootSec=` del timer y arrancar el servicio, se usa el xxd con SUID (GTFOBins) para escribir la clave pública de root en /root/.ssh/authorized_keys y SSH como root, leyendo root.txt.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | What is the user.txt flag? | `THM{9f2ce3df1beeecaf695b3a8560c682704c31b17a}` |
| 2 | What is the root.txt flag? | `THM{dca75486094810807faf4b7b0a929b11e5e0167c}` |

### Task 3: Conclusión / Conclusion

**Explicación:** Cierre de la room: consolidar la cadena SQLi → LFI → RCE → movimiento lateral → escalada a root. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Repaso de la cadena y medidas correctivas / Review of the chain | `No answer needed` |

---

**Metodología:** Reconocimiento web → SQLi en el login → fuzzing → descubrimiento de /secret-script.php → LFI → cadena de filtros php://filter para RCE → reverse shell como www-data → enumeración (authorized_keys escribible) → pivot a comte → abuso de exploit.timer/exploit.service con systemctl → SUID xxd (GTFOBins) → escritura del authorized_keys de root → SSH como root → flags.

### Cadena de ataque / Attack Chain

SQLi (login) → descubrimiento del endpoint con LFI → LFI → php://filter chain → RCE → reverse shell (www-data) → authorized_keys escribible → SSH comte → systemctl sobre exploit.timer → copia de xxd con SUID → escritura del authorized_keys de root → SSH root → flags.

**Learning chain:** Web fuzzing → SQL injection → Local File Inclusion → php filter chains → Remote Code Execution → authorized_keys abuse → systemd timer/service abuse → SUID exploitation (GTFOBins).

**Lección:** *Una inclusión de archivos sin sanitizar se convierte en ejecución remota con solo encadenar filtros PHP, y un permiso NOPASSWD sobre un servicio heredado permite fabricar el binario con SUID que abre la puerta a root: cada eslabón amplifica el siguiente.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1543 (Create or Modify System Process — systemd timer), T1068 (Exploitation for Privilege Escalation), T1078 (Valid Accounts).

**Fuente:** [TryHackMe - Cheese CTF](https://tryhackme.com/room/cheesectf)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.