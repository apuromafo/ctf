# Cat Pictures

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | ctf | `catpictures` | [TryHackMe](https://tryhackme.com/room/catpictures) | 01 Level Easy | THM | phpBB, port knocking, FTP anónimo, shell limitada, binario runme, Docker, cron | Medio |

---

**Contexto:** Máquina CTF basada en un foro phpBB de fotos de gatos cuyos posts dejan entrever unos "números mágicos" (1111, 2222, 3333, 4444) para abrir un puerto filtrado mediante port knocking. Al hacerlo se revela un servicio FTP anónimo con una nota que apunta a un shell limitado en el puerto 4420. Desde ese shell se obtiene una shell real, se extrae el binario protegido runme, se recupera su contraseña con strings y se genera una id_rsa, se entra por SSH como catlover a un contenedor Docker (Flag 1) y se escapa del contenedor inyectando una reverse shell en el script de limpieza ejecutado por cron (Root Flag).

> **ES:** Box CTF de nivel fácil: port knocking para abrir un FTP anónimo, un shell interno limitado en el puerto 4420, reverso del binario runme para obtener la clave SSH, acceso SSH a un contenedor Docker como catlover y escape vía cron con una reverse shell para leer la flag de root.

> **EN:** Easy CTF box: port knocking to open an anonymous FTP, a limited internal shell on port 4420, reversing the runme binary to get the SSH key, SSH access into a Docker container as catlover and a cron-based reverse shell to escape the container and read the root flag.

## Solucionario

### Task 1: Deploy the VM / Desplegar la VM

**Explicación:** Iniciar la máquina, permitir que termine de arrancar y conectarse desde la red de atacante. Los posts del foro contienen la pista clave para el resto de la room (los puertos a llamar).

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | I have deployed the VM. | `No answer needed` |

### Task 2: Flags! / Flags

**Explicación:** El foro deja ver los números mágicos para el port knocking: `knock TARGET 1111 2222 3333 4444`. Abierto el puerto 21 (FTP anónimo) se recupera la nota (note.txt) con una pista hacia el servicio interno del puerto 4420, que se degrada a una shell real con un payload mkfifo/nc. El binario /home/catlover/runme exige una contraseña que se encuentra con strings tras transferirlo al equipo atacante; ejecutándolo en la máquina genera id_rsa. El SSH con esa clave entra como catlover en un contenedor Docker (Flag 1). Por último se añade una reverse shell a /opt/clean/clean.sh (cron del host) para escapar del contenedor y obtener la Root Flag.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | What is Flag 1? | `7cf90a0e7c5d25f1a827d3efe6fe4d0edd63cca9` |
| 2 | What is the Root Flag? | `4a98e43d78bab283938a06f38d2ca3a3c53f0476` |

---

**Metodología:** nmap → lectura del foro (pista de port knocking) → `knock` 1111 2222 3333 4444 → reescaneo → FTP anónimo → note.txt → shell interno 4420 → reverse shell con mkfifo/nc → transferencia del binario runme → strings → ejecución → id_rsa → SSH catlover → Flag 1 en el contenedor → reverse shell en /opt/clean/clean.sh (cron) → escape del contenedor → Root Flag.

### Cadena de ataque / Attack Chain

Enumeración del foro → port knocking → FTP anónimo → nota interna → shell limitado 4420 → reverse shell (mkfifo) → reverso de runme → generación de id_rsa → SSH a Docker como catlover → Flag 1 → inyección en clean.sh (cron) → root del host → Root Flag.

**Learning chain:** Enumeración web → port knocking → FTP anónimo → shells limitadas → ingeniería inversa básica (strings) → claves SSH → Docker → abuso de cron → reverse shell.

**Lección:** *El port knocking, los shells limitados y los contenedores parecen barreras, pero una pista en un foro, una nota en FTP o un cron escribible bastan para convertir cada salto en un eslabón más de la cadena hasta root.*

**MITRE ATT&CK:** T1078 (Valid Accounts), T1059 (Command and Scripting Interpreter), T1083 (File and Directory Discovery), T1543 (Create or Modify System Process — cron).

**Fuente:** [TryHackMe - Cat Pictures](https://tryhackme.com/room/catpictures)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.