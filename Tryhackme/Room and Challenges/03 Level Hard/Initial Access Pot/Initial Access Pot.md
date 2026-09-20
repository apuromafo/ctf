# Initial Access Pot

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Pentesting | initialaccesspot | [Initial Access Pot](https://tryhackme.com/room/initialaccesspot) | 03 Level Hard | TryHackMe | Rutas, IP, Hash, Flag | Alto |

---

**Contexto:**

> **ES:** Room de pentesting centrada en la obtención de acceso inicial sobre una máquina con WordPress: ruta de login, webshell en el tema `blocksy`, clave SSH filtrada, IP interna, hash MD5 y la flag de acceso concedido.
> **EN:** Pentesting room focused on gaining initial access to a WordPress machine: login path, webshell in the `blocksy` theme, leaked SSH key, internal IP, MD5 hash and the access-granted flag.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:**

El contenido original de la tarea es el siguiente:

1. No answer needed

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 1 | ¿Hay respuesta para esta tarea? / Is there an answer for this task? | `No answer needed` |

### Task 2: Acceso inicial / Initial access

**Explicación:**

El contenido original de la tarea es el siguiente:

2. 1. /wp-login.php
   2. /var/www/html/wordpress/wp-content/themes/blocksy/404.php
   3. /etc/ssh/id_ed25519.bak
   4. 172.16.8.216
   5. d6f2d80e78f264aff8c7aea21acb6ca6
   6. THM{acc3ss_gr4nt3d!}

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 2 | ¿Cuál es la ruta de acceso al login? / What is the login access path? | `/wp-login.php` |
| 2 | ¿Cuál es la ruta del webshell en el tema? / What is the theme webshell path? | `/var/www/html/wordpress/wp-content/themes/blocksy/404.php` |
| 2 | ¿Cuál es la ruta de la clave SSH filtrada? / What is the leaked SSH key path? | `/etc/ssh/id_ed25519.bak` |
| 2 | ¿Cuál es la IP interna del sistema? / What is the internal system IP? | `172.16.8.216` |
| 2 | ¿Cuál es el hash MD5 encontrado? / What is the MD5 hash found? | `d6f2d80e78f264aff8c7aea21acb6ca6` |
| 2 | ¿Cuál es la flag de acceso? / What is the access flag? | `THM{acc3ss_gr4nt3d!}` |

---

**Metodología:**

Enumeración de WordPress, localización de rutas de login y webshells en temas, detección de claves SSH expuestas, identificación de la IP interna y recolección de hashes y flags tras conseguir el acceso inicial.

### Cadena de ataque / Attack Chain

1. Enumeración del sitio WordPress.
2. Acceso al panel de login (`/wp-login.php`).
3. Abuso del tema `blocksy` con webshell (`404.php`).
4. Lectura de la clave SSH filtrada y de la IP interna.
5. Obtención del hash y de la flag de acceso concedido.

**Learning chain:**

`WordPress` → `/wp-login.php` → tema `blocksy` → webshell `404.php` → `id_ed25519.bak` → `172.16.8.216` → MD5 → `THM{acc3ss_gr4nt3d!}`.

**Lección:** *El acceso inicial casi nunca es un hito único: una webshell oculta en un tema legítimo, una clave SSH respaldada y un hash revelan cuán cerca del control total queda la máquina una vez roto el primer perímetro.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application, T1078 Valid Accounts, T1505.003 Web Shell, T1021.001 Remote Services: SSH.

**Fuente:** [TryHackMe - Initial Access Pot](https://tryhackme.com/room/initialaccesspot)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.