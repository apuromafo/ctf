# Ignite

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `ignite` | [TryHackMe](https://tryhackme.com/room/ignite) | 01 Level Easy | THM | Fuel CMS 1.4.1, RCE, CVE-2018-16763, reverse shell | Ejecución remota de código sobre Fuel CMS y captura de credenciales y bandera |

> **Objeto:** Explotar Fuel CMS 1.4.1 mediante su vulnerabilidad de ejecución remota de código (CVE-2018-16763) para obtener una reverse shell, recuperar el hash de acceso y la bandera.

---

**Contexto:** Sala de TryHackMe donde se compromete una instancia de Fuel CMS 1.4.1 explotando su vulnerabilidad RCE (CVE-2018-16763). Tras subir una reverse shell se obtiene acceso al sistema, se recupera un hash de contraseña y se localiza la bandera.

> **ES:** Una sala práctica de explotación web: se abusa de la inyección evaluada en Fuel CMS 1.4.1 (CVE-2018-16763) para obtener una shell inversa, extraer un hash de acceso y leer la bandera.
> **EN:** A hands-on web exploitation room: it abuses the evaluated injection in Fuel CMS 1.4.1 (CVE-2018-16763) to get a reverse shell, extract an access hash, and read the flag.

## Solucionario

### Task 1: Acceso inicial y explotación / Initial Access & Exploitation

**Explicación:** La aplicación Fuel CMS 1.4.1 evalúa código PHP contenido en un parámetro controlado por el usuario, permitiendo ejecutar comandos remotos. Con una reverse shell se accede al servidor y se recupera el hash de la cuenta y la bandera.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Después de obtener acceso a Fuel CMS, ¿cuál es el contenido del hash de contraseña? / After gaining access to Fuel CMS, what is the contents of the password hash? | `6470e394cbf6dab6a91682cc8585059b` |
| 2 | ¿Cuál es el contenido de la bandera? / What is the contents of the flag? | `b9bbcb33e11b80be759c4e844862482d` |

---

**Metodología:** Se identificó el CMS (Fuel CMS 1.4.1) y su vulnerabilidad RCE CVE-2018-16763, que evalúa el parámetro PHP inyectado por el usuario. Se envió un payload para ejecutar comandos y establecer una reverse shell hacia la máquina atacante. Con acceso al sistema se extrajeron las credenciales del hash `6470e394cbf6dab6a91682cc8585059b` y se leyó la bandera `b9bbcb33e11b80be759c4e844862482d`.

### Cadena de ataque / Attack Chain

Reconocimiento del CMS → identificación de Fuel CMS 1.4.1 → detección de la inyección evaluada (CVE-2018-16763) → envío del payload RCE → reverse shell → obtención de credenciales (hash) → lectura de la bandera.

**Learning chain:** Reconocimiento web → fingerprinting Fuel CMS → CVE-2018-16763 RCE → payload eval() → reverse shell → extracción de hash → bandera.

**Lección:** *Los CMS antiguos con funciones `eval()` sobre entrada de usuario permiten pasar de una llamada HTTP a una shell con pocos pasos; actualizar y parchear el software es el control principal frente a ejecución remota de código.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1003 (OS Credential Dumping), T1083 (File and Directory Discovery).

**Fuente:** [TryHackMe - Ignite](https://tryhackme.com/room/ignite)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.