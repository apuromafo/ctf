# Undiscovered

| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `undiscoveredup` |
| **Link** | [TryHackMe](https://tryhackme.com/room/undiscoveredup) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | subdomain enumeration / vhost / RiteCMS / CVE-2020-23934 / NFS / capabilities / vim.basic |
| **Impacto** | Explotar un CMS vulnerable, abusar de un NFS misconfigurado y de capabilities para escalar a root |

---

**Contexto:** Undiscovered combina enumeración de subdominios con un vhost oculto (`deliver.undiscovered.thm`) que ejecuta un RiteCMS 2.2.1 vulnerable. Tras bruteforcear el login admin con Hydra, se sube una webshell (CVE-2020-23934) para conseguir una shell como `www-data`. Una montura NFS de `/home/william` con `root_squash` deshabilitado permite hacerse pasar por `william` (UID 3003) y leer `user.txt`; un binario SUID da acceso a la clave SSH de `leonard`, y sus capacidades `cap_setuid+ep` en `/usr/bin/vim.basic` permiten ejecutar Python como root.

## Solucionario

### Task 1: Enumeración de subdominios / Subdomain Enumeration

**Explicación:**

En la página principal no hay nada útil. Un fuzzing de vhosts con `gobuster vhost` sobre `undiscovered.thm` descubre el subdominio `deliver.undiscovered.thm`, que se añade al `/etc/hosts` y sirve el CMS RiteCMS 2.2.1.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Tarea práctica / Practical task) | `No answer needed` |

### Task 2: Foothold en RiteCMS y pivote por NFS / RiteCMS Foothold and NFS Pivot

**Explicación:**

RiteCMS 2.2.1 es vulnerable a RCE autenticado (CVE-2020-23934); el panel requiere login en `/cms/`, así que `hydra` hace bruteforce del usuario `admin` contra la wordlist rockyou. Dentro del File Manager se sube una webshell PHP que da una reverse shell como `www-data`. `/etc/exports` muestra `/home/william *(rw,root_squash)`: montando el share NFS y creando un usuario local con el mismo UID (3003) se accede a `user.txt`. user.txt: `THM{8d7b7299cccd1796a61915901d0e091c}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | user.txt | `THM{8d7b7299cccd1796a61915901d0e091c}` |

### Task 3: Escalada a root con vim.basic / Root Escalation with vim.basic

**Explicación:**

Sobre el share NFS aparecen `admin.sh` y un binario `script` con setuid: con un parámetro ejecuta `/bin/cat /home/leonard/<param>`, por lo que permite leer la clave privada SSH de `leonard` e iniciar sesión SSH como ese usuario. En `leonard`, `.viminfo` revela comandos de escalada con Python y `getcap` confirma `cap_setuid+ep` en `/usr/bin/vim.basic`. `vim.basic -c ':py3 import os; os.setuid(0); os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'` entrega una shell de root. El hash de contraseña de root es `$6$1VMGCoHv$L3nX729XRbQB7u3rndC.8wljXP4eVYM/SbdOzT1IET54w2QVsVxHSH.ghRVRxz5Na5UyjhCfY6iv/koGQQPUB0`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the root user's password hash? | `$6$1VMGCoHv$L3nX729XRbQB7u3rndC.8wljXP4eVYM/SbdOzT1IET54w2QVsVxHSH.ghRVRxz5Na5UyjhCfY6iv/koGQQPUB0` |

---

**Metodología:**

1. **Reconocimiento:** Nmap encuentra SSH, HTTP y NFS (2049); `gobuster vhost` sobre `undiscovered.thm` localiza `deliver.undiscovered.thm` con RiteCMS 2.2.1.
2. **Búsqueda de exploits:** `searchsploit RiteCMS` lista el exploit "RiteCMS 2.2.1 - Authenticated Remote Code Execution" (CVE-2020-23934), que requiere autenticación.
3. **Bruteforce del login:** `hydra -l admin -P rockyou.txt deliver.undiscovered.thm http-post-form "/cms/index.php:username=^USER^&userpw=^PASS^:User unknown or password wrong"` descubre la contraseña de `admin`.
4. **Shell como www-data:** en `Administration > File Manager > Upload File` se sube una webshell PHP, se ejecuta y se recibe una reverse shell como `www-data`.
5. **Pivote NFS:** con `/home/william *(rw,root_squash)` se monta el share; `useradd -u 3003 william` replica el UID y permite leer `user.txt`. Se inyecta una clave pública en `.ssh/authorized_keys` para entrar por SSH como `william`.
6. **Pivote a leonard:** el binario `script` (SUID) ejecuta `cat /home/leonard/<param>`, exponiendo `id_rsa`; con esa clave se hace SSH como `leonard`.
7. **Root:** `getcap` muestra `cap_setuid+ep` en `/usr/bin/vim.basic`; `:py3 import os; os.setuid(0); os.execl("/bin/sh", ...)` produce una shell de root y el volcado de `/etc/shadow`.

**Learning chain:** undiscovered.thm -> gobuster vhost -> deliver.undiscovered.thm (RiteCMS 2.2.1) -> hydra admin/rockyou -> webshell.php -> reverse shell (www-data) -> NFS /home/william (rw, root_squash) -> useradd UID 3003 -> user.txt + authorized_keys -> binario SUID "script" -> cat /home/leonard/id_rsa -> SSH leonard -> vim.basic cap_setuid+ep -> :py3 setuid(0) -> root shell -> /etc/shadow

**Lección:** *Los montajes NFS mal configurados (UID replicable, `root_squash` deshabilitado) rompen la frontera de privilegios, y una capability como `cap_setuid+ep` en un binario con intérprete (vim + Python) equivale a una shell de root. La enumeración de vhosts y de capabilities es tan importante como la de puertos.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application) · T1135 (Network Share Discovery) · T1548.001 (Setuid and Setgid) · T1068 (Exploitation for Privilege Escalation) · CWE-22 (Path Traversal)

**Fuente:** [TryHackMe - Undiscovered](https://tryhackme.com/room/undiscoveredup)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
