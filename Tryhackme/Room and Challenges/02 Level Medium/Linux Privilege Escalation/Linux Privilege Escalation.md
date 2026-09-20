# Linux Privilege Escalation

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough | linuxprivilegeescalation | https://tryhackme.com/room/linuxprivilegeescalation | Linux / Privilege Escalation | TryHackMe | kernel (CVE-2015-1328), sudo (nmap --interactive, menos), SUID, vi/view, bash, hashes /etc/shadow, crontab | Escalada de privilegios a root |

---

**Contexto:** La sala **Linux Privilege Escalation** es un reto completo de escalada de privilegios en Linux ("Privilege Escalation" de MuirlandOracle): se parte del usuario `user` y se combinan diferentes técnicas — explotación del kernel (CVE-2015-1328), abuso de sudo en binarios como `nmap --interactive`, `vi`/`view` y `less`, búsqueda de hashes y credenciales en archivos, binarios SUID, tareas cron y el archivo `/etc/passwd` — para conseguir una shell como root y recolectar las flags THM de cada task.

## Solucionario

### Task 1
**Explicación:**

Acceso inicial a la máquina con las credenciales del laboratorio (usuario `user`).

`No answer needed`

### Task 2
**Explicación:**

Enumeración de los servicios de escucha de la máquina.

`No answer needed`

### Task 3
**Explicación:**

Se enumera el sistema: nombre de usuario, versión y release del kernel, sistema operativo y versiones de python/pip, para identificar el exploit de kernel a usar.

1. `wade7363`
2. `3.13.0-24-generic`
3. `Ubuntu 14.04 LTS`
4. `2.7.6`
5. `CVE-2015-1328`

### Task 4
**Explicación:**

Lanzamiento del exploit de kernel (overlayfs) para conseguir acceso root.

`No answer needed`

### Task 5
**Explicación:**

Una vez con root, se inspecciona el sistema y se establece una shell interactiva.

1. `No answer needed`
2. `THM-28392872729920`

### Task 6
**Explicación:**

Abuso de `sudo` sobre el binario `nmap` (modo interactivo) para escalar a root; se recogen respuestas sobre el proceso, el CLUE del exploit y el hash de la cuenta root.

1. `3`
2. `THM-402028394`
3. `sudo nmap --interactive`
4. `$6$2.sUUDsOLIpXKxcr$eImtgFExyr2ls4jsghdD3DHLHHP9X50Iv.jNmwo/BJpphrPRJWjelWEz2HH.joV14aDEwW1c3CahzB1uaqeLR1`

### Task 7
**Explicación:**

Se explotan los binarios SUID del sistema; se identifica el binario vulnerable y se extraen credenciales del archivo de configuración.

1. `gerryconway`
2. `Password1`
3. `THM-3847834`

### Task 8
**Explicación:**

Abuso de sudo sobre `vi`/`view` para lanzar comandos con privilegios elevados y obtener la flag.

1. `No answer needed`
2. `6`
3. `view`
4. `THM-9349843`

### Task 9
**Explicación:**

Explotación del binario sudo `less` para escapar a una shell con privilegios.

1. `4`
2. `THM-383000283`
3. `123456`

### Task 10
**Explicación:**

Se examinan los cron jobs del sistema y se manipulan los scripts ejecutados por root para lanzar una reverse shell.

1. `/home/murdoch`
2. `No answer needed`
3. `THM-736628929`

### Task 11
**Explicación:**

Manipulación del PATH: se crea un binario malicioso cuyo nombre coincide con el invocado por un cron job en ejecución.

1. `3`
2. `3`
3. `No answer needed`
4. `THM-89384012`

### Task 12
**Explicación:**

Con la shell root se verifican los vectores aprendidos y se leen las flags finales de la sala.

1. `THM-42828719920544`
2. `THM-168824782390238`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Task 1 - Respuesta | `No answer needed` |
| 2 | Task 2 - Respuesta | `No answer needed` |
| 3.1 | Task 3 - Respuesta 1 | `wade7363` |
| 3.2 | Task 3 - Respuesta 2 | `3.13.0-24-generic` |
| 3.3 | Task 3 - Respuesta 3 | `Ubuntu 14.04 LTS` |
| 3.4 | Task 3 - Respuesta 4 | `2.7.6` |
| 3.5 | Task 3 - Respuesta 5 | `CVE-2015-1328` |
| 4 | Task 4 - Respuesta | `No answer needed` |
| 5.1 | Task 5 - Respuesta 1 | `No answer needed` |
| 5.2 | Task 5 - Respuesta 2 | `THM-28392872729920` |
| 6.1 | Task 6 - Respuesta 1 | `3` |
| 6.2 | Task 6 - Respuesta 2 | `THM-402028394` |
| 6.3 | Task 6 - Respuesta 3 | `sudo nmap --interactive` |
| 6.4 | Task 6 - Respuesta 4 | `$6$2.sUUDsOLIpXKxcr$eImtgFExyr2ls4jsghdD3DHLHHP9X50Iv.jNmwo/BJpphrPRJWjelWEz2HH.joV14aDEwW1c3CahzB1uaqeLR1` |
| 7.1 | Task 7 - Respuesta 1 | `gerryconway` |
| 7.2 | Task 7 - Respuesta 2 | `Password1` |
| 7.3 | Task 7 - Respuesta 3 | `THM-3847834` |
| 8.1 | Task 8 - Respuesta 1 | `No answer needed` |
| 8.2 | Task 8 - Respuesta 2 | `6` |
| 8.3 | Task 8 - Respuesta 3 | `view` |
| 8.4 | Task 8 - Respuesta 4 | `THM-9349843` |
| 9.1 | Task 9 - Respuesta 1 | `4` |
| 9.2 | Task 9 - Respuesta 2 | `THM-383000283` |
| 9.3 | Task 9 - Respuesta 3 | `123456` |
| 10.1 | Task 10 - Respuesta 1 | `/home/murdoch` |
| 10.2 | Task 10 - Respuesta 2 | `No answer needed` |
| 10.3 | Task 10 - Respuesta 3 | `THM-736628929` |
| 11.1 | Task 11 - Respuesta 1 | `3` |
| 11.2 | Task 11 - Respuesta 2 | `3` |
| 11.3 | Task 11 - Respuesta 3 | `No answer needed` |
| 11.4 | Task 11 - Respuesta 4 | `THM-89384012` |
| 12.1 | Task 12 - Respuesta 1 | `THM-42828719920544` |
| 12.2 | Task 12 - Respuesta 2 | `THM-168824782390238` |

---

**Metodología:** Enumeración del sistema (usuario, kernel, OS, python) → exploit de kernel CVE-2015-1328 → abuso de sudo (nmap --interactive, vi/view, less) → explotación de binarios SUID → modificación de cron jobs y manipulación del PATH → recolección de flags root.

**Learning chain:** Enumeración → kernel exploit → sudo en nmap/vi/less → SUID → cron jobs → PATH hijacking → root + flags.

**Lección:** *Un sistema Linux se escala a root combinando vectores aparentemente inofensivos: un kernel viejo, un binario con sudo interactivo, un editor con permisos y un cron job manipulable. La enumeración paciente y el abuso de las herramientas que ya viven en la máquina (living off the land) son la clave.*

**MITRE ATT&CK:** T1068 Exploitation for Privilege Escalation · T1203 Exploitation for Client Execution · T1548.002 Abuse Elevation Control Mechanism: Sudo and Sudo Caching · T1548.001 Setuid and Setgid · T1053.003 Scheduled Task/Job: Cron · T1574.007 Hijack Execution Flow: Path Interception by PATH Environment Variable · T1003.008 OS Credential Dumping: /etc/passwd and /etc/shadow.

**Fuente:** [TryHackMe - Linux Privilege Escalation](https://tryhackme.com/room/linuxprivilegeescalation)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.