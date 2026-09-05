# Undiscovered [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Walkthrough
* **Slug:** `undiscoveredup`
* **Link:** https://tryhackme.com/room/undiscoveredup
* **Sección / Section:** 02 Level Medium
* **Fuente / Source:** Writeups públicos de siunam, bvr0n, 5h3ph3rd (josephmtakai), m3n0sd0n4ld y thmrevenant.

## Solucionario de Tareas / Task Solutions

> **ES:** Undiscovered (room creada por ch4rm) combina enumeración de subdominios con un vhost oculto (`deliver.undiscovered.thm`) que ejecuta un RiteCMS 2.2.1 vulnerable. Tras bruteforcear el login admin con Hydra, se sube una webshell (CVE-2020-23934) para conseguir una shell como `www-data`. Una montura NFS de `/home/william` con `root_squash` deshabilitado permite hacerse pasar por `william` (UID 3003) y leer `user.txt`; un binario SUID da acceso a la clave SSH de `leonard`, y sus capacidades `cap_setuid+ep` en `/usr/bin/vim.basic` permiten ejecutar Python como root.
> **EN:** Undiscovered (room created by ch4rm) combines subdomain enumeration with a hidden vhost (`deliver.undiscovered.thm`) running a vulnerable RiteCMS 2.2.1. After brute-forcing the admin login with Hydra, a web shell is uploaded (CVE-2020-23934) to obtain a shell as `www-data`. An NFS share of `/home/william` with `root_squash` disabled allows impersonating `william` (UID 3003) and reading `user.txt`; a SUID binary gives access to `leonard`'s SSH key, and the `cap_setuid+ep` capability on `/usr/bin/vim.basic` allows running Python as root.

### Task 1 - Enumeración de subdominios / Subdomain Enumeration

> **ES:** En la página principal no hay nada útil. Un fuzzing de vhosts con `gobuster vhost` sobre `undiscovered.thm` descubre el subdominio `deliver.undiscovered.thm`, que se añade al `/etc/hosts` y sirve el CMS RiteCMS 2.2.1.
> **EN:** The main page holds nothing useful. Vhost fuzzing with `gobuster vhost` against `undiscovered.thm` discovers the `deliver.undiscovered.thm` subdomain, which is added to `/etc/hosts` and serves the RiteCMS 2.2.1 CMS.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| (Tarea práctica / Practical task) | `No answer needed` |

### Task 2 - Foothold en RiteCMS y pivote por NFS / RiteCMS Foothold and NFS Pivot

> **ES:** RiteCMS 2.2.1 es vulnerable a RCE autenticado (CVE-2020-23934); el panel requiere login en `/cms/`, así que `hydra` hace bruteforce del usuario `admin` contra la wordlist rockyou. Dentro del File Manager se sube una webshell PHP que da una reverse shell como `www-data`. `/etc/exports` muestra `/home/william *(rw,root_squash)`: montando el share NFS y creando un usuario local con el mismo UID (3003) se accede a `user.txt`.
> **EN:** RiteCMS 2.2.1 is vulnerable to authenticated RCE (CVE-2020-23934); the panel requires a login at `/cms/`, so `hydra` brute-forces the `admin` user against the rockyou wordlist. Inside the File Manager a PHP web shell is uploaded, yielding a reverse shell as `www-data`. `/etc/exports` shows `/home/william *(rw,root_squash)`: by mounting the NFS share and creating a local user with the same UID (3003) access to `user.txt` is gained.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| user.txt | `THM{8d7b7299cccd1796a61915901d0e091c}` |

### Task 3 - Escalada a root con vim.basic / Root Escalation with vim.basic

> **ES:** Sobre el share NFS aparecen `admin.sh` y un binario `script` con setuid: con un parámetro ejecuta `/bin/cat /home/leonard/<param>`, por lo que permite leer la clave privada SSH de `leonard` e iniciar sesión SSH como ese usuario. En `leonard`, `.viminfo` revela comandos de escalada con Python y `getcap` confirma `cap_setuid+ep` en `/usr/bin/vim.basic`. `vim.basic -c ':py3 import os; os.setuid(0); os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'` entrega una shell de root.
> **EN:** On the NFS share, `admin.sh` and a setuid binary `script` appear: with a parameter it runs `/bin/cat /home/leonard/<param>`, so it can read `leonard`'s private SSH key and log in over SSH as that user. As `leonard`, `.viminfo` reveals privilege-escalation commands using Python and `getcap` confirms `cap_setuid+ep` on `/usr/bin/vim.basic`. `vim.basic -c ':py3 import os; os.setuid(0); os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'` yields a root shell.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What's the root user's password hash? | `$6$1VMGCoHv$L3nX729XRbQB7u3rndC.8wljXP4eVYM/SbdOzT1IET54w2QVsVxHSH.ghRVRxz5Na5UyjhCfY6iv/koGQQPUB0` |

## Metodología / Methodology

1. **Paso / Step - Reconocimiento:** Nmap encuentra SSH, HTTP y NFS (2049); `gobuster vhost` sobre `undiscovered.thm` localiza `deliver.undiscovered.thm` con RiteCMS 2.2.1.
2. **Paso / Step - Búsqueda de exploits:** `searchsploit RiteCMS` lista el exploit "RiteCMS 2.2.1 - Authenticated Remote Code Execution" (CVE-2020-23934), que requiere autenticación.
3. **Paso / Step - Bruteforce del login:** `hydra -l admin -P rockyou.txt deliver.undiscovered.thm http-post-form "/cms/index.php:username=^USER^&userpw=^PASS^:User unknown or password wrong"` descubre la contraseña de `admin`.
4. **Paso / Step - Shell como www-data:** en `Administration > File Manager > Upload File` se sube una webshell PHP, se ejecuta y se recibe una reverse shell como `www-data`.
5. **Paso / Step - Pivote NFS:** con `/home/william *(rw,root_squash)` se monta el share; `useradd -u 3003 william` replica el UID y permite leer `user.txt`. Se inyecta una clave pública en `.ssh/authorized_keys` para entrar por SSH como `william`.
6. **Paso / Step - Pivote a leonard:** el binario `script` (SUID) ejecuta `cat /home/leonard/<param>`, exponiendo `id_rsa`; con esa clave se hace SSH como `leonard`.
7. **Paso / Step - Root:** `getcap` muestra `cap_setuid+ep` en `/usr/bin/vim.basic`; `:py3 import os; os.setuid(0); os.execl("/bin/sh", ...)` produce una shell de root y el volcado de `/etc/shadow`.

### Cadena de ataque / Attack Chain

```
undiscovered.thm
      |
  gobuster vhost -> deliver.undiscovered.thm (RiteCMS 2.2.1)
      |
  hydra admin + rockyou -> login en /cms/
      |
  File Manager -> webshell.php -> reverse shell (www-data)
      |
  NFS /home/william (rw, root_squash) -> useradd UID 3003
      |
  mount -> user.txt  +  inyectar authorized_keys
      |
  SSH william -> binario SUID "script"
      |
  cat /home/leonard/id_rsa -> SSH leonard
      |
  vim.basic cap_setuid+ep -> :py3 setuid(0)
      |
  root shell -> /etc/shadow (hash de root)
```

**Lección:** Los montajes NFS mal configurados (UID replicable, `root_squash` deshabilitado) rompen la frontera de privilegios, y una capability como `cap_setuid+ep` en un binario con intérprete (vim + Python) equivale a una shell de root. La enumeración de vhosts y de capabilities es tan importante como la de puertos.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.