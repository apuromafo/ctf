# Bolt

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | challenge | `bolt` | [TryHackMe](https://tryhackme.com/room/bolt) | 01 Level Easy | TryHackMe | Bolt CMS / RCE / Metasploit / web exploitation | Compromiso de un servidor con Bolt CMS vulnerable a ejecución remota de código y captura de la flag root |

---

**Contexto:** Bolt es una sala que presenta un servidor web ejecutando Bolt CMS en su versión 3.7.1, accesible por el puerto 8000. La sala muestra cómo autenticarse con unas credenciales por defecto y explotar una vulnerabilidad de ejecución remota de código (RCE) con Metasploit para obtener una shell y capturar la flag de root.

> **ES:** CMS Bolt 3.7.1 en el puerto 8000. Con `bolt:boltadmin123` se entra en el panel y se lanza el módulo `exploit/unix/webapp/bolt_authenticated_rce` para conseguir una shell y el root flag.
> **EN:** Bolt CMS 3.7.1 running on port 8000. Using `bolt:boltadmin123` the admin panel is accessed and `exploit/unix/webapp/bolt_authenticated_rce` is fired to obtain a shell and the root flag.

## Solucionario

### Task 1: Introducción / Intro
**Explicación:** Pregunta introductoria de la sala. No requiere respuesta.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| Pregunta introductoria de la sala | `No answer needed` |

### Task 2: Reconocimiento y explotación / Recon and exploitation
**Explicación:** El escaneo muestra el CMS Bolt 3.7.1 corriendo en el puerto 8000. Se accede al panel con las credenciales `bolt:boltadmin123`. En Metasploit se identifican el módulo `exploit/unix/webapp/bolt_authenticated_rce` y su ID `48296`. Con el exploit se obtiene una shell y se localiza el root flag.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| ¿En qué puerto corre el servidor web? | `8000` |
| ¿Cuál es el nombre de usuario para acceder al panel? | `bolt` |
| ¿Cuál es la contraseña del panel? | `boltadmin123` |
| ¿Qué versión de Bolt CMS se está ejecutando? | `Bolt 3.7.1` |
| ¿Cuál es el ID del módulo de exploit en Metasploit? | `48296` |
| ¿Cuál es la ruta del módulo de exploit en Metasploit? | `exploit/unix/webapp/bolt_authenticated_rce` |
| ¿Qué pregunta de configuración se plantea? | `No answer needed` |
| ¿Cuál es el flag de root? | `THM{wh0_d035nt_l0ve5_b0l7_r1gh7?}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Pregunta introductoria de la sala | `No answer needed` |
| 2 | Puerto del servidor web | `8000` |
| 3 | Usuario del panel | `bolt` |
| 4 | Contraseña del panel | `boltadmin123` |
| 5 | Versión de Bolt CMS | `Bolt 3.7.1` |
| 6 | ID del módulo de exploit | `48296` |
| 7 | Ruta del módulo de exploit | `exploit/unix/webapp/bolt_authenticated_rce` |
| 8 | Pregunta de configuración | `No answer needed` |
| 9 | Flag de root | `THM{wh0_d035nt_l0ve5_b0l7_r1gh7?}` |

---

**Metodología:** Se escanea la máquina y se identifica el CMS Bolt 3.7.1 en el puerto 8000. Con las credenciales `bolt:boltadmin123` se accede al panel de administración. A continuación se selecciona en Metasploit el módulo `exploit/unix/webapp/bolt_authenticated_rce` (ID `48296`), se ejecuta y se obtiene una shell en el sistema. Recorriendo el filesystem se encuentra y se captura el flag de root.

### Cadena de ataque / Attack Chain

```text
nmap -> puerto 8000 -> Bolt 3.7.1 -> bolt:boltadmin123 -> msfconsole -> search 48296 -> exploit/unix/webapp/bolt_authenticated_rce -> shell -> root flag
```

**Learning chain:** port scanning --> web fingerprint (Bolt CMS) --> default credentials --> Metasploit module search --> authenticated RCE --> reverse shell --> flag capture

**Lección:** *El uso de credenciales por defecto junto con un CMS con vulnerabilidades de RCE convierte cualquier panel accesible en el punto de entrada perfecto hacia el sistema.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1078 (Valid Accounts), T1059 (Command and Scripting Interpreter), T1005 (Data from Local System)

**Fuente:** [TryHackMe - Bolt](https://tryhackme.com/room/bolt)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.