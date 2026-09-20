# Slingshot

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | Boot2Root | slingshot | https://tryhackme.com/room/slingshot | 01 Level Easy | TryHackMe | Nmap, NSE, Gobuster, Hydra, phpMyAdmin, MySQL | Crítico |

---

**Contexto:**
> **ES:** Máquina Boot2Root de nivel Easy. La resolución comienza con un escaneo completo de red con Nmap, continúa con el fuzzing de directorios con Gobuster, la fuerza bruta del panel de administración con Hydra y finaliza con el acceso a phpMyAdmin y la exfiltración de credenciales desde el fichero de configuración de MySQL.
> **EN:** An Easy Boot2Root machine. The walkthrough starts with a full network scan with Nmap, continues with directory fuzzing with Gobuster and brute-forcing the admin panel with Hydra, and ends by accessing phpMyAdmin and pulling credentials from the MySQL configuration file.

## Solucionario

### Task 1: Reconocimiento y explotación / Recon & Exploitation
**Explicación:**
La primera tarea recorre la cadena completa de explotación: escaneo de puertos, enumeración web, fuerza bruta de credenciales, ejecución de comandos remota y acceso a la base de datos.

```
1. 10.0.2.15
2. Nmap Scripting Engine
3. Mozilla/5.0 (Gobuster)
4. 1867
5. a76637b62ea99acda12f5859313f539a
6. /admin-login.php
7. Mozilla/4.0 (Hydra)
8. admin:thx1138
9. THM{ecb012e53a58818cbd17a924769ec447}
10. whoami
11. /etc/phpmyadmin/config-db.php
12. /phpmyadmin
13. customer_credit_cards
14. c6aa3215a7d519eeb40a660f3b76e64c
```

### Task 2: Cierre / Final
**Explicación:**
La tarea final no requiere respuesta.

```
No answer needed
```

### Tabla unificada de preguntas/respuestas

| # | Respuesta |
|---|---|
| 1.1 | `10.0.2.15` |
| 1.2 | `Nmap Scripting Engine` |
| 1.3 | `Mozilla/5.0 (Gobuster)` |
| 1.4 | `1867` |
| 1.5 | `a76637b62ea99acda12f5859313f539a` |
| 1.6 | `/admin-login.php` |
| 1.7 | `Mozilla/4.0 (Hydra)` |
| 1.8 | `admin:thx1138` |
| 1.9 | `THM{ecb012e53a58818cbd17a924769ec447}` |
| 1.10 | `whoami` |
| 1.11 | `/etc/phpmyadmin/config-db.php` |
| 1.12 | `/phpmyadmin` |
| 1.13 | `customer_credit_cards` |
| 1.14 | `c6aa3215a7d519eeb40a660f3b76e64c` |
| 2 | `No answer needed` |

---

**Metodología:**
1. Enumeración de puertos y servicios con Nmap y su NSE.
2. Fuzzing de directorios con Gobuster.
3. Detección del panel de administración en el puerto 1867.
4. Fuerza bruta de credenciales con Hydra sobre el login.
5. Autenticación como admin y ejecución de comandos.
6. Recuperación de credenciales MySQL en `/etc/phpmyadmin/config-db.php`.
7. Acceso a phpMyAdmin y consulta de la tabla `customer_credit_cards`.

### Cadena de ataque / Attack Chain
Nmap (escaneo de servicios) → Gobuster (fuzzing de rutas) → Hydra (fuerza bruta) → `/admin-login.php` (acceso) → `whoami` (validación RCE) → `/etc/phpmyadmin/config-db.php` (credenciales MySQL) → phpMyAdmin → `customer_credit_cards` → Flag.

**Learning chain:**
Nmap NSE → Gobuster → Hydra → autenticación web → configuración insegura de credenciales → MySQL → datos sensibles.

**Lección:** *La exposición de credenciales en ficheros de configuración junto con paneles de administración sin protección hace trivial el compromiso total del sistema.*

**MITRE ATT&CK:**
| Técnica | ID |
|---|---|
| Network Service Discovery | T1046 |
| Exploit Public-Facing Application | T1190 |
| Brute Force | T1110 |
| Unsecured Credentials | T1552 |
| Data from Local System | T1005 |

**Fuente:** [TryHackMe - Slingshot](https://tryhackme.com/room/slingshot)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.