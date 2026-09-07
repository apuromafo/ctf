# Git Happens

| **Dificultad** | Easy |
| **Tipo** | CTF |
| **Slug** | `githappens` |
| **Link** | [TryHackMe](https://tryhackme.com/room/githappens) |
| **Sección** | 01 Level Easy |
| **Fuente** | Writeup de Kiran Dawadi (CyberSec Nerds) + AfvanMoopen (GitHub) |
| **Componentes** | nmap / .git expuesto / git-dumper / wget / git log / git show / nginx |
| **Impacto** | Aprovecha un repositorio `.git` expuesto públicamente para filtrar credenciales de un commit anterior no ofuscado. |

---

**Contexto:** Room de nivel principiante que enseña sobre malas configuraciones de control de versiones (git) y errores de desarrolladores que llevan a problemas de seguridad. Un repositorio `.git` expuesto públicamente filtra credenciales en un commit anterior.

## Solucionario

### Task 1: Find the Super Secret Password

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Find the Super Secret Password | `Th1s_1s_4_L0ng_4nd_S3cur3_P4ssw0rd!` |

---

**Metodología:**
1. **Recon:** `nmap -sC -sV MACHINE_IP` descubre el servicio http nginx 1.14.0 (Ubuntu) en el puerto 80 y, vía el script `http-git`, un repositorio git expuesto en `/.git/`.
2. **Descarga:** descargar el repositorio `.git` completo con git-dumper (`/opt/git-dumper/git-dumper.py http://MACHINE_IP:80/.git/ ./git_files`) o con wget recursivo (`wget http://MACHINE_IP/.git/ --recursive --no-parent`).
3. **Análisis:** `git log` revela dos commits: `d0b3578a` ("Update .gitlab-ci.yml", HEAD) y `395e087` ("Made the login page, boss!"); el commit `395e087` contiene el código de la página de login **antes** de que se ofuscara.
4. **Foothold:** `git show 395e087334d613d5e423cdf8f7be27196a360459` muestra el `index.html` con las credenciales en texto claro: `username === "admin"` y `password === "Th1s_1s_4_L0ng_4nd_S3cur3_P4ssw0rd!"`; la contraseña se puede usar como flag o para autenticarse (cookie `login=1`).

**Learning chain:** nmap (http-git) → repositorio .git expuesto → git-dumper/wget descarga → git log → commit "Made the login page, boss!" → git show → credenciales en texto claro en el diff → flag.

**MITRE ATT&CK:** T1005 (Data from Local System), T1552.001 (Unsecured Credentials: Credentials in Files).

**Fuente:** [TryHackMe - Git Happens](https://tryhackme.com/room/githappens)