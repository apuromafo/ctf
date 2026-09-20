# Kenobi

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `kenobi` | https://tryhackme.com/room/kenobi | 01 Level Easy | TryHackMe | Nmap / SMB (enum4linux/smbclient) / FTP / ProFTPD 1.3.5 (mod_copy) / PATH hijack / SUID / ssh2john | Máquina Linux del catálogo: explotar Samba y ProFTPD (mod_copy), usar el path hijack del binario menu y las capacidades SUID para obtener las flags user y root. |

---

**Contexto:** Máquina clásica de TryHackMe (Kenobi). El recorrido pasa por enumerar SMB y FTP, explotar la vulnerabilidad de ProFTPD 1.3.5 (`mod_copy`, copia remota de archivos), recuperar una clave SSH, aprovechar un binario SUID con PATH hijack (`/usr/bin/menu`) y abusar de las capacidades de `setuid`/Python para escalar a root y leer ambas flags.

> **ES:** Máquina de explotación Linux: enumeración SMB/FTP, explotación de ProFTPD mod_copy, path hijack y capacidades SUID para escalar privilegios.
> **EN:** Linux exploitation box: SMB/FTP enumeration, ProFTPD mod_copy exploit, path hijack and SUID capabilities for privilege escalation.

## Solucionario

### Task 1: Reconocimiento / Recon

**Explicación:** Se lanza el reconocimiento con Nmap. La primera pregunta no requiere respuesta y el escaneo revela que la máquina tiene `7` puertos abiertos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Paso previo del reconocimiento. / Previous recon step. | `No answer needed` |
| 2 | ¿Cuántos puertos están abiertos? / How many ports are open? | `7` |

### Task 2: Enumeración SMB / SMB Enumeration

**Explicación:** Se enumeran los recursos Samba: se descubren `3` shares, el archivo de log `log.txt`, el puerto `21` como servicio FTP y la ruta `/var` donde se encuentra la flag/archivo de interés.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos recursos compartidos (shares) hay? / How many shares are there? | `3` |
| 2 | ¿Cómo se llama el archivo de log encontrado? / What is the name of the log file found? | `log.txt` |
| 3 | ¿En qué puerto corre FTP? / On which port does FTP run? | `21` |
| 4 | ¿Dónde se encuentra la flag? / Where is the flag located? | `/var` |

### Task 3: Explotación / Exploitation

**Explicación:** Se explota el servicio FTP: la versión de ProFTPD es `1.3.5` y el archivo enumerado contiene `4` líneas. Tras obtener acceso se recupera la user flag `d0b0f3f53b6caa532a83915e19224899`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué versión de ProFTPD se está ejecutando? / What version of ProFTPD is running? | `1.3.5` |
| 2 | ¿Cuántas líneas tiene el archivo? / How many lines does the file have? | `4` |
| 3 | Paso previo de la explotación. / Previous exploitation step. | `No answer needed` |
| 4 | Paso previo de la explotación. / Previous exploitation step. | `No answer needed` |
| 5 | ¿Cuál es la user flag? / What is the user flag? | `d0b0f3f53b6caa532a83915e19224899` |

### Task 4: Escalada de privilegios / Privilege Escalation

**Explicación:** Se identifica el binario SUID `/usr/bin/menu` con `3` opciones. Aprovechando su ejecución sin rutas absolutas (PATH hijack) se consigue una shell como root y se lee la root flag `177b3cd8562289f37382721c28381f02`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la ruta absoluta del binario? / What is the absolute path of the binary? | `/usr/bin/menu` |
| 2 | ¿Cuántas opciones tiene el menú? / How many options does the menu have? | `3` |
| 3 | Paso previo de la escalada. / Previous privesc step. | `No answer needed` |
| 4 | ¿Cuál es la root flag? / What is the root flag? | `177b3cd8562289f37382721c28381f02` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Paso previo del reconocimiento. | `No answer needed` |
| 2 | ¿Cuántos puertos están abiertos? | `7` |
| 3 | ¿Cuántos recursos compartidos (shares) hay? | `3` |
| 4 | ¿Cómo se llama el archivo de log encontrado? | `log.txt` |
| 5 | ¿En qué puerto corre FTP? | `21` |
| 6 | ¿Dónde se encuentra la flag? | `/var` |
| 7 | ¿Qué versión de ProFTPD se está ejecutando? | `1.3.5` |
| 8 | ¿Cuántas líneas tiene el archivo? | `4` |
| 9 | ¿Cuál es la user flag? | `d0b0f3f53b6caa532a83915e19224899` |
| 10 | ¿Cuál es la ruta absoluta del binario? | `/usr/bin/menu` |
| 11 | ¿Cuántas opciones tiene el menú? | `3` |
| 12 | ¿Cuál es la root flag? | `177b3cd8562289f37382721c28381f02` |

---

**Metodología:** Enumeración inicial con Nmap; enumeración de recursos Samba para descubrir las shares, el log y el servicio FTP; explotación del mod_copy de ProFTPD 1.3.5 para copiar archivos (claves/SSH) y obtener la primera shell; y escalada aprovechando el SUID `/usr/bin/menu` con PATH hijack, terminando con el abuso de capacidades para leer la root flag.

### Cadena de ataque / Attack Chain

```text
nmap -> enumeración SMB (shares/log) -> FTP 21 -> ProFTPD 1.3.5 mod_copy -> obtener clave/archivo -> user flag -> binario SUID /usr/bin/menu -> PATH hijack -> root -> root flag
```

**Learning chain:** nmap -> SMB -> FTP -> ProFTPD mod_copy -> shell -> SUID menu -> PATH hijack -> root.

**Lección:** *La combinación de servicios legados (Samba, ProFTPD) y binarios SUID mal escritos (sin rutas absolutas) permite encadenar acceso inicial y escalada de privilegios hasta root.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1547.009 (SUID), T1574.007 (PATH Hijacking), T1082 (System Information Discovery)

**Fuente:** [TryHackMe - Kenobi](https://tryhackme.com/room/kenobi)
---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.