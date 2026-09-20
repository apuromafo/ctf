# b3dr0ck

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `b3dr0ck` |
| **Link** | [TryHackMe](https://tryhackme.com/room/b3dr0ck) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | WordPress, wpscan, fuerza bruta, credentials dumping |
| **Impacto** | Compromiso de un sitio WordPress mediante enumeración y fuerza bruta, acceso a credenciales y recuperación de las flags de la máquina. |

---

**Contexto:** La sala es una máquina guiada centrada en el compromiso de un WordPress. Se realiza la enumeración del sitio, se aplican credenciales por defecto y fuerza bruta para obtener acceso administrativo, se recuperan las credenciales de acceso a la base de datos y se consiguen las tres flags de la máquina junto con la contraseña de la base de datos.

## Solucionario

### Task 1: Explotación de WordPress / WordPress Exploitation

**Explicación:** Tarea única en la que se completa la cadena de compromiso del WordPress: se obtiene la primera flag del servidor, se recupera la contraseña de la base de datos (`YabbaDabbaD0000!`) y se accede al entorno para capturar las dos flags restantes de la máquina.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag obtenida en la máquina? | `THM{f05780f08f0eb1de65023069d0e4c90c}` |
| 2 | ¿Cuál es la contraseña de la base de datos recuperada? | `YabbaDabbaD0000!` |
| 3 | ¿Cuál es la segunda flag de la máquina? | `THM{08da34e619da839b154521da7323559d}` |
| 4 | ¿Cuál es la flag final de la máquina? | `THM{de4043c009214b56279982bf10a661b7}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag obtenida en la máquina? | `THM{f05780f08f0eb1de65023069d0e4c90c}` |
| 2 | ¿Cuál es la contraseña de la base de datos recuperada? | `YabbaDabbaD0000!` |
| 3 | ¿Cuál es la segunda flag de la máquina? | `THM{08da34e619da839b154521da7323559d}` |
| 4 | ¿Cuál es la flag final de la máquina? | `THM{de4043c009214b56279982bf10a661b7}` |

---

**Metodología:**

1. Se enumera el sitio WordPress para identificar usuarios, plugins y versiones.
2. Se obtiene acceso al panel/recurso comprometido y se localiza la primera flag: `THM{f05780f08f0eb1de65023069d0e4c90c}`.
3. Se recuperan las credenciales de la base de datos (`YabbaDabbaD0000!`) desde la configuración del sitio.
4. Se explota el acceso para ejecutar comandos/cargar un webshell y se captura la segunda flag: `THM{08da34e619da839b154521da7323559d}`.
5. Se completa la escalada/acceso final y se obtiene la flag `THM{de4043c009214b56279982bf10a661b7}`.

### Cadena de ataque / Attack Chain

```
Enumeración WordPress -> usuarios/plugins
  -> Acceso (credenciales/fuerza bruta)
  -> THM{f05780f08f0eb1de65023069d0e4c90c}
  -> Configuración -> BD -> YabbaDabbaD0000!
  -> Webshell / RCE -> THM{08da34e619da839b154521da7323559d}
  -> Escalada final -> THM{de4043c009214b56279982bf10a661b7}
```

**Learning chain:** Enumeración WordPress → Acceso → Primera flag → Credenciales de BD → RCE/webshell → Segunda flag → Acceso final → Flag final

**Lección:** *Un WordPress mal configurado con credenciales débiles y plugins/versiones desactualizados expone tanto el panel como la propia base de datos; una vez obtenida la configuración, la recuperación de contraseñas y la ejecución de comandos se encadenan para comprometer la máquina por completo.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1110 (Brute Force), T1078 (Valid Accounts), T1059 (Command and Scripting Interpreter)

**Fuente:** [TryHackMe - b3dr0ck](https://tryhackme.com/room/b3dr0ck)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.