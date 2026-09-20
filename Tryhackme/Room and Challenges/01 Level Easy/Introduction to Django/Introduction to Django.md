# Introduction to Django

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `introductiontodjango` | [TryHackMe](https://tryhackme.com/room/introductiontodjango) | 01 Level Easy | TryHackMe | Django, Python, manage.py, runserver, Git, Admin Panel, CTF | Fundamentos de Django aplicados a un CTF: creación y arranque de proyectos, repositorio Git, panel de administración, SSH y flags |

> **Objeto:** Aprender los fundamentos del framework web Django y aplicarlos en un pequeño CTF: crear aplicaciones con manage.py, arrancar el proyecto en la red local, explorar el repositorio Git, acceder al panel de administración y capturar las flags de administrador, usuario y oculta.

---

**Contexto:** Sala que enseña Django como framework Python: cómo crear una aplicación (startapp Forms) y arrancar el proyecto en la red local (runserver), los conceptos básicos de gestión del proyecto y un CTF final sobre una máquina concreta donde se recuperan las flags: la flag de la página de GitHub, la del panel admin (usuario django-admin), la flag de usuario (SSH, usuario StrangeFox) y la flag oculta en el código de una plantilla.

> **ES:** Sala de introducción a Django: manage.py, servidor de desarrollo, aplicación Forms, repositorio Git, panel admin y flags del CTF final.
> **EN:** Introduction to Django room: manage.py, development server, Forms app, Git repository, admin panel and final CTF flags.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación de la sala y de los objetivos: aprender Django y usarlo en un CTF para obtener todas las flags.

No answer needed

### Task 2: Primeros pasos / Unit 2 - Getting started
**Explicación:** Se aprenden los comandos básicos de Django: crear una aplicación llamada Forms con startapp y arrancar el proyecto en la red local con runserver.

1. python3 manage.py startapp Forms
2. python3 manage.py runserver 0.0.0.0:8000

### Task 3: Creando un sitio web / Unit 3 - Creating a website
**Explicación:** Se crea y configura el sitio web (settings.py, ALLOWED_HOSTS, vistas y plantillas) para dejar la aplicación funcionando.

No answer needed

### Task 4: Repositorio Git / Unit 4 - GitHub
**Explicación:** Se explora el repositorio Git del proyecto en la página de GitHub y se obtiene la flag correspondiente.

THM{g1t_djang0_hUb}

### Task 5: CTF final / Unit 5 - CTF
**Explicación:** CTF final sobre la máquina Django: se arregla el error y se recuperan todas las flags: la del panel de administración, la del usuario SSH (StrangeFox) y la oculta en la plantilla home.html.

1. THM{DjanGO_Adm1n}
2. THM{SSH_gUy_101}
3. THM{django_w1zzard}

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | Introducción a la sala | `No answer needed` |
| 2.1 | ¿Cómo crearíamos una aplicación llamada Forms? | `python3 manage.py startapp Forms` |
| 2.2 | ¿Cómo arrancaríamos nuestro proyecto en la red local? | `python3 manage.py runserver 0.0.0.0:8000` |
| 3 | Creación y configuración del sitio web | `No answer needed` |
| 4 | Flag de la página de GitHub | `THM{g1t_djang0_hUb}` |
| 5.1 | Flag del panel de administración | `THM{DjanGO_Adm1n}` |
| 5.2 | Flag de usuario (SSH) | `THM{SSH_gUy_101}` |
| 5.3 | Flag oculta | `THM{django_w1zzard}` |

---

**Metodología:** Instalación y creación de la aplicación Forms con manage.py, arranque del entorno de desarrollo con runserver, configuración del sitio (settings.py y ALLOWED_HOSTS), revisión del repositorio Git para obtener la primera flag, acceso al panel de administración para la flag admin, conexión por SSH como StrangeFox para la flag de usuario y búsqueda en el código (grep de THM en home.html) para la flag oculta.

### Cadena de ataque / Attack Chain

Django app (startapp Forms) -> runserver (0.0.0.0:8000) -> configurar sitio -> repositorio Git -> flag GitHub -> panel admin (django-admin) -> SSH (StrangeFox) -> user flag -> búsqueda de THM en plantillas -> flag oculta

**Learning chain:** Django -> manage.py -> startapp -> runserver -> website config -> Git -> admin panel -> SSH -> flags

**Lección:** *Django simplifica el desarrollo web, pero una configuración descuidada (ALLOWED_HOSTS, credenciales por defecto, secretos en repositorios o comentarios en plantillas) expone la aplicación a compromiso total.*

**MITRE ATT&CK:** T1078 (Valid Accounts) / T1003 (Credential Dumping).

**Fuente:** [TryHackMe - Introduction to Django](https://tryhackme.com/room/introductiontodjango)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.