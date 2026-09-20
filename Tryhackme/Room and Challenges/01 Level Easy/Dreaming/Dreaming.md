# Dreaming

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | challenge | `dreaming` | [TryHackMe](https://tryhackme.com/room/dreaming) | 01 Level Easy | TryHackMe | Pluck CMS / CVE-2019-10690 / RCE / MySQL / SQL injection / credential stuffing / Python library hijacking / sudo | Explotar un CMS vulnerable, abusar de una biblioteca Python ejecutada con privilegios y escalar hasta root. |

> **Objeto:** Comprometer la máquina Dreaming mediante RCE en un Pluck CMS desactualizado (CVE-2019-10690), reutilizar credenciales contra una web basada en PHP/MySQL, pivotar a otro usuario y abusar de una biblioteca Python ejecutada por sudo (library hijacking) para obtener una shell como root y capturar las tres flags (Lucien, Death y Morpheus).

---

**Contexto:** La máquina ejecuta un Pluck CMS que permite cargar archivos de tema y ejecutar código arbitrario, obteniendo así una shell como el usuario Lucien. De una base de datos MySQL se recupera la credencial del usuario Death, que reutiliza contraseña en una web de otro usuario con la que se obtiene una shell como ese usuario (Lucien está en el grupo de otro usuario y la contraseña se recupera de su directorio). Finalmente, un script Python se ejecuta con privilegios elevados pero importa una biblioteca que el usuario puede reemplazar (library hijacking), lo que permite ejecutar comandos como morpheus y escalar a root por sudo NOPASSWD. Los tres usuarios oneiric forman parte del grupo "death" y cada flag corresponde a un nivel de acceso.

> **ES:** Se explota una RCE de Pluck CMS (CVE-2019-10690) subiendo un tema con backdoor para obtener una webshell como Lucien. Se extrae de MySQL la credencial de Death (reutilizada en una web), se encuentra la contraseña de Death en el directorio de Lucien, y se usa el abuso de una biblioteca Python (creando un freewill.py malicioso dentro de /home/death/scripts porque la biblioteca se importa con un import no seguro) que se ejecuta con sudo para obtener una shell como morpheus y después como root. Cada flag (Lucien, Death, Morpheus) se captura en el correspondiente nivel de acceso.
> **EN:** A Pluck CMS RCE (CVE-2019-10690) is exploited by uploading a backdoored theme to get a webshell as Lucien. Death's credential is extracted from MySQL (reused on another web app), password reuse is found in Lucien's home directory, and a Python library hijacking (malicious freewill.py inside /home/death/scripts since the library is imported unsafely) is abused via sudo to get a shell as morpheus and then as root. Each flag (Lucien, Death, Morpheus) is captured at the corresponding access level.

## Solucionario

### Task 1: Flag de Lucien / The Lucien Flag
**Explicación:** Pluck CMS desactualizado es vulnerable a una RCE (CVE-2019-10690) que permite subir archivos en el tema instalado. Se crea un archivo .php con un webshell, se sube vía wpfilemanager del CMS y se ejecuta para obtener una shell como el usuario Lucien (contraseña de SSH encontrada en ficheros: HeyLucien#@1999!). La flag de Lucien está en su directorio personal.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the Lucien Flag? / ¿Cuál es la flag de Lucien? | `THM{TH3_L1BR4R14N}` |

### Task 2: Flag de Death / The Death Flag
**Explicación:** Lucien es miembro del grupo de Death y su directorio tiene archivos con la contraseña de Death. Se usa esa credencial para conectar por SSH o por la web como Death; la flag de Death está en /home/death (archivo user.txt). El usuario Death pertenece al grupo oneiric junto con morpheus.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the Death Flag? / ¿Cuál es la flag de Death? | `THM{1M_TH3R3_4_TH3M}` |

### Task 3: Flag de Morpheus / The Morpheus Flag
**Explicación:** El script /home/death/scripts/freewill.py se ejecuta con privilegios (sudo NOPASSWD) pero importa una biblioteca del directorio de scripts sin import seguro; se reemplaza el archivo (por ejemplo, creando un freewill.py malicioso que recoja las credenciales de morpheus) para que, al ejecutarse con sudo, la biblioteca hijackeada entregue una shell como morpheus. La flag está en /home/morpheus.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the Morpheus Flag? / ¿Cuál es la flag de Morpheus? | `THM{DR34MS_5H4P3_TH3_W0RLD}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the Lucien Flag? / ¿Cuál es la flag de Lucien? | `THM{TH3_L1BR4R14N}` |
| 2 | What is the Death Flag? / ¿Cuál es la flag de Death? | `THM{1M_TH3R3_4_TH3M}` |
| 3 | What is the Morpheus Flag? / ¿Cuál es la flag de Morpheus? | `THM{DR34MS_5H4P3_TH3_W0RLD}` |

---

**Metodología:** Escaneo de puertos (web con Pluck CMS antiguo). Se descarga la versión vulnerable y se sube un tema modificado con backdoor PHP para lograr RCE y una shell como Lucien. Se encuentra la contraseña de Death en el directorio de Lucien y se obtiene una shell como Death (los tres usuarios oneiric pertenecen al grupo "death"). En /home/death/scripts hay un script freewill.py que se ejecuta con sudo sin NOPASSWD padre y que importa bibliotecas del mismo directorio; se sustituye la biblioteca por una maliciosa para ejecutar código como morpheus, cuya cuenta aparece en el script junto con la de root, y se escala a root para capturar todas las flags.

### Cadena de ataque / Attack Chain

```text
nmap -> Pluck CMS 4.7.3 -> CVE-2019-10690 (RCE vía temas) -> webshell -> shell como Lucien -> credencial en su home -> Death (SSH/web) -> /home/death/scripts/freewill.py (sudo) -> python library hijacking -> shell como morpheus -> root -> 3 flags
```

**Learning chain:** port scanning → Pluck CMS identification → CVE-2019-10690 (theme upload RCE) → webshell → Lucien shell → password discovery → Death access → python library hijacking (freewill.py) → Morpheus shell → privilege escalation to root → 3 flags.

**Lección:** *El software CMS desactualizado es una puerta de entrada trivial (RCE por subida de temas); las contraseñas reutilizadas entre usuarios/servicios permiten pivotar, y los imports "inseguros" de bibliotecas Python en scripts ejecutados con sudo son una vía silenciosa de escalada de privilegios.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1592 (Gather Victim Host Information), T1078 (Valid Accounts), T1574.001 (DLL/Path Hijacking - Hijack Execution Flow), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Dreaming](https://tryhackme.com/room/dreaming)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.