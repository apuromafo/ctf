# Team

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | CTF / Máquina Linux | `team` | https://tryhackme.com/room/team | 01 Level Easy | TryHackMe | FTP / LFI / SSH / id_rsa / sshd_config / sudo / admin_checks / command injection / crontab / main_backup.sh / escalada de privilegios | Compromiso total de una máquina Linux: credenciales FTP filtradas en `script.old`, LFI en `dev.team.thm` para leer la `id_rsa` de Dale (desde sshd_config), shell SSH, inyección de comandos en `admin_checks` vía sudo para pasar a gyles, y abuso de un cron raíz (`main_backup.sh`) para escalar a root y leer ambas flags. |

---

**Contexto:** Máquina Linux fácil del autor dalemazza que combina enumeración web, filtrado de credenciales, LFI y escalada de privilegios. En `team.thm` se halla `robots.txt` (dale) y `/scripts/script.txt` que apunta a `script.old`, con credenciales FTP de Dale. En el FTP, `New_site.txt` revela el subdominio `dev.team.thm` y la política de copiar la `id_rsa` en un fichero de configuración. En `dev.team.thm` hay un LFI vía el parámetro `page` de `script.php`; leyendo `/etc/ssh/sshd_config` se recupera la `id_rsa` de Dale. Con ella se entra por SSH, y tras `sudo -l` se ejecuta `/home/gyles/admin_checks` como gyles inyectando `/bin/bash` en el `read`. Gyles pertenece al grupo admin que puede escribir `/usr/local/bin/main_backup.sh`, script ejecutado por root cada minuto vía cron; modificándolo se recibe una shell root y la flag.

> **ES:** Máquina Linux: credenciales en `script.old` -> FTP -> `dev.team.thm` -> LFI en `script.php?page=` -> `id_rsa` de Dale desde `sshd_config` -> SSH -> `sudo -u gyles admin_checks` + `/bin/bash` -> shell gyles -> cron root reescribe `main_backup.sh` -> root -> flags `THM{6Y0TXHz7c2d}` y `THM{fhqbznavfonq}`.
> **EN:** Linux box: credentials in `script.old` -> FTP -> `dev.team.thm` -> LFI in `script.php?page=` -> Dale's `id_rsa` from `sshd_config` -> SSH -> `sudo -u gyles admin_checks` + `/bin/bash` -> gyles shell -> root cron rewrites `main_backup.sh` -> root -> flags `THM{6Y0TXHz7c2d}` and `THM{fhqbznavfonq}`.

## Solucionario

### Task 1: Desplegar la máquina / Deploy the machine

**Explicación:** Se despliega el entorno del laboratorio y se comprueba el alcance de la máquina a través de la VPN o AttackBox. No requiere respuesta más allá del despliegue.

**Respuesta original verbatim:**
```text
1. No answer needed
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Despliega la máquina del laboratorio. / Deploy the lab machine. | `No answer needed` |

### Task 2: Captura las flags / Capture the flags

**Explicación:** Recorriendo la cadena completa (FTP -> LFI -> SSH -> escalada vía sudo y cron) se obtienen las dos flags del sistema: la flag de usuario y la flag de root.

**Respuestas originales verbatim:**
```text
2. 1. THM{6Y0TXHz7c2d}
   2. THM{fhqbznavfonq}
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Cuál es la flag de usuario? / What is the user flag? | `THM{6Y0TXHz7c2d}` |
| 2 | ¿Cuál es la flag de root? / What is the root flag? | `THM{fhqbznavfonq}` |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Despliega la máquina del laboratorio. / Deploy the lab machine. | `No answer needed` |
| 2 | ¿Cuál es la flag de usuario? / What is the user flag? | `THM{6Y0TXHz7c2d}` |
| 3 | ¿Cuál es la flag de root? / What is the root flag? | `THM{fhqbznavfonq}` |

---

**Metodología:** Nmap (21 FTP, 22 SSH, 80 HTTP) -> enumeración web (robots.txt -> dale; /scripts/script.txt -> script.old) -> wfuzz sobre /scripts/ para encontrar `script.old` -> credenciales FTP -> login FTP -> `New_site.txt` -> `dev.team.thm` + pista de id_rsa en config -> LFI en `script.php?page=`/add dev.team.thm a /etc/hosts -> leer `/etc/ssh/sshd_config` -> extraer `/etc/passwd`, user.txt y la id_rsa de Dale -> `chmod 600 id_rsa` -> `ssh -i id_rsa dale@team.thm` -> `sudo -l` (`(gyles) NOPASSWD: /home/gyles/admin_checks`) -> injectar `/bin/bash` en el `read -p "Enter name..."` -> shell gyles -> enumerar grupo admin -> `main_backup.sh` writable por grupo admin y ejecutado por cron root -> inyectar reverse shell -> `nc -lvnp` -> root -> flags.

### Cadena de ataque / Attack Chain

```text
Nmap -> 21/22/80 -> robots.txt (dale) -> /scripts/script.txt -> wfuzz -> script.old -> credenciales FTP -> New_site.txt -> dev.team.thm -> LFI (script.php?page=) -> /etc/ssh/sshd_config -> id_rsa (Dale) -> SSH -> sudo -u gyles /home/gyles/admin_checks -> /bin/bash -> gyles -> cron root -> /usr/local/bin/main_backup.sh -> reverse shell -> root -> THM{6Y0TXHz7c2d} + THM{fhqbznavfonq}
```

**Learning chain:** Enumeración web -> fuzzing de extensiones -> credenciales filtradas -> FTP -> subdominio -> LFI -> fuga de clave privada -> SSH -> sudo misconfig add -> command injection -> pivote de usuario -> grupo admin -> cron abusable -> root.

**Lección:** *Las pistas se suceden: un `script.old` con credenciales, un subdominio en un nota de FTP, y una clave id_rsa comentada en `sshd_config` leíble por LFI; luego `read` que ejecuta input y un cron raíz editable por el grupo admin son los escalones hasta root.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1005 (Data from Local System), T1552.004 (Unsecured Credentials: Private Keys), T1059.004 (Unix Shell), T1543 (Create or Modify System Process) / T1053.003 (Scheduled Task/Job: Cron).

**Fuente:** [TryHackMe - Team](https://tryhackme.com/room/team)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.