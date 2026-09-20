# Nax

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
| Medium | Máquina (CTF) | nax | https://tryhackme.com/room/nax | Explotación / Nagios XI | TryHackMe | Máquina Linux, Nagios XI, Metasploit | High |

> **Objeto:** Comprometer una máquina que ejecuta Nagios XI: enumeración inicial, obtención de credenciales por fuerza bruta, explotación del plugin *check_ping* (CVE-2019-15949) y escalada de privilegios para leer ambas flags.

---

**Contexto:**

NAX es una máquina que presenta un panel de gestión *Nagios XI* accesible. El camino habitual comienza con la descompresión/obtención de un recurso que revela un cuadro estilo *Piet Mondrian* que da entrada al descubrimiento del CMS, seguido de fuerza bruta contra la cuenta de administrador, la explotación de una vulnerabilidad de Nagios XI (inyección de comandos en el plugin `check_ping`, CVE-2019-15949) mediante Metasploit y finalmente la escalada a root.

> **ES:** Se compromete un servidor con Nagios XI. Tras extraer un archivo con una imagen de arte *Piet Mondrian*, se obtiene el nombre del archivo y se identifica el software. Con credenciales obtenidas por fuerza bruta (nagiosadmin) se entra al panel y se lanza el exploit de inyección de comandos en el plugin `check_ping` (CVE-2019-15949). Una shell como el usuario `nagios` permite leer la primera flag y, tras escalar a root, la segunda.

> **EN:** A server running Nagios XI is compromised. After extracting a file containing a *Piet Mondrian* art image, the file name is obtained and the software is identified. With credentials obtained by brute force (nagiosadmin) we log into the panel and launch the command injection exploit in the `check_ping` plugin (CVE-2019-15949). A shell as the `nagios` user allows reading the first flag and, after escalating to root, the second one.

## Solucionario

### Task 1: Reconocimiento inicial / Initial Recon
**Explicación:**

Se explora el servicio web. Se encuentra y descarga un archivo que, al extraerse, expone la imagen `PI3T.Png`, una obra en estilo *Piet Mondrian*. Este detalle identifica el software que genera el archivo y permite continuar con el compromiso.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. ¿Cuál es la extensión del archivo que se puede editar? / What is the file extension of the file that can be edited? | `PI3T.Png` |
| 2. ¿Qué artista pintó este arte? / Which artist painted this art? | `Piet Mondrian` |
| 3. Task subpregunta | `No answer needed` |

### Task 2: Acceso al panel / Panel Access
**Explicación:**

Se identifica la aplicación como **Nagios XI**. Se realiza fuerza bruta / acceso al panel con credenciales por defecto o descubiertas, logrando autenticarse como `nagiosadmin` con la contraseña obtenida durante el proceso de enumeración.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 4. ¿Cuál es el nombre de usuario? / What is the username? | `nagiosadmin` |
| 5. ¿Cuál es la contraseña? / What is the password? | `n3p3UQ&9BjLp4$7uhWdY` |
| 6. ¿Qué CVE corresponde a esta vulnerabilidad? / What CVE is related to this vulnerability? | `CVE-2019-15949` |
| 7. Task subpregunta | `No answer needed` |

### Task 3: Explotación / Exploitation
**Explicación:**

Con el panel autenticado se localiza el módulo de Metasploit que explota la inyección de comandos en el plugin `check_ping` de Nagios XI. Se ejecuta el exploit y se obtiene una sesión de Meterpreter/shell como el usuario `nagios`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 8. ¿Cuál es la ruta del exploit? / What is the path of the exploit? | `exploit/linux/http/nagios_xi_plugins_check_plugin_authenticated_rce` |

### Task 4: Flags / Flags
**Explicación:**

Con la shell obtenida se localiza y lee la flag de usuario y posteriormente la de root tras escalar privilegios.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 9. Flag de usuario / User flag | `THM{84b17add1d72a9f2e99c33bc568ae0f1}` |
| 10. Flag de root / Root flag | `THM{c89b2e39c83067503a6508b21ed6e962}` |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Extensión del archivo editable | `PI3T.Png` |
| 2 | Artista del arte | `Piet Mondrian` |
| 3 | Task 1 subpregunta | `No answer needed` |
| 4 | Usuario del panel Nagios | `nagiosadmin` |
| 5 | Contraseña del panel Nagios | `n3p3UQ&9BjLp4$7uhWdY` |
| 6 | CVE de la vulnerabilidad | `CVE-2019-15949` |
| 7 | Task 2 subpregunta | `No answer needed` |
| 8 | Ruta del exploit de Metasploit | `exploit/linux/http/nagios_xi_plugins_check_plugin_authenticated_rce` |
| 9 | Flag de usuario | `THM{84b17add1d72a9f2e99c33bc568ae0f1}` |
| 10 | Flag de root | `THM{c89b2e39c83067503a6508b21ed6e962}` |

---

**Metodología:**

1. Reconocimiento web y descarga del archivo editable.
2. Extracción e identificación del arte (`Piet Mondrian`) y de la aplicación (Nagios XI).
3. Fuerza bruta de credenciales y acceso como `nagiosadmin`.
4. Selección del exploit `nagios_xi_plugins_check_plugin_authenticated_rce` (CVE-2019-15949).
5. Ejecución del exploit y obtención de shell con la cuenta `nagios`.
6. Lectura de la flag de usuario y escalada a root para la flag final.

### Cadena de ataque / Attack Chain

```
Web recon --> Descarga y extracción de PI3T.Png
        |
        v
Identificación: Nagios XI
        |
        v
Fuerza bruta: nagiosadmin : n3p3UQ&9BjLp4$7uhWdY
        |
        v
Metasploit: nagios_xi_plugins_check_plugin_authenticated_rce (CVE-2019-15949)
        |
        v
Shell como nagios --> Flag de usuario
        |
        v
Escalada a root --> Flag de root
```

**Learning chain:**

- ¿Cómo una imagen incrustada en un archivo revela el software que la generó?
- ¿Por qué las credenciales débiles o predecibles en paneles de gestión exponen todo el sistema?
- ¿Qué es CVE-2019-15949 y por qué la inyección de comandos en `check_ping` es crítica en Nagios XI?
- ¿Cómo una vulnerabilidad autenticada en un panel de monitoreo conduce a un RCE completo?

**Lección:**

*Un panel de administración no parcheado, con credenciales débiles y un plugin con inyección de comandos, convierte una simple página web en una puerta directa al control total del servidor.*

**MITRE ATT&CK:**

- T1595 (Active Scanning)
- T1110 (Brute Force)
- T1585 (Establish Accounts)
- T1210 (Exploitation of Remote Services)
- T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Nax](https://tryhackme.com/room/nax)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.