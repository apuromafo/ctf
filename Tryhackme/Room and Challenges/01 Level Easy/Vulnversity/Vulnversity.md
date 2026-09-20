# Vulnversity

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `vulnversity` | https://tryhackme.com/room/vulnversity | 01 Level Easy | TryHackMe | Nmap, gobuster, subida de archivos (.php/.phtml), reverse shell, escalada con systemctl | Compromiso total del servidor web mediante una subida de archivos mal filtrada y escalada de privilegios con systemctl |

---

**Contexto:** Sala guiada que recorre el ciclo completo de un pentest web: reconocimiento con Nmap, enumeración de directorios, explotación de una subida de archivos vulnerable (extensión `.php` bloqueada pero `.phtml` permitida), consecución de una reverse shell y escalada de privilegios explotando un binario SUID (`/bin/systemctl`). El resumen original conserva únicamente las respuestas posicionales, sin los enunciados de las preguntas.

> **ES:** Reconoce la máquina con Nmap, enumera directorios, sube una reverse shell con una extensión permitida y escala a root con el binario SUID `/bin/systemctl`.
> **EN:** Scan the machine with Nmap, enumerate directories, upload a reverse shell with an allowed extension, and escalate to root using the SUID binary `/bin/systemctl`.

## Solucionario

### Task 1: Despliegue / Deployment

**Explicación:** Tarea de preparación: se despliega la máquina y se conecta a la red de TryHackMe (VPN o AttackBox). No requiere respuesta más allá de tener la caja en línea.

```
1. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |

### Task 2: Escaneo con Nmap / Nmap Scanning

**Explicación:** Con Nmap se escanean los puertos y versiones del objetivo. Se identifican `6` puertos abiertos, la versión `4.10` de Apache, `400` como tamaño de la página, el sistema operativo `Ubuntu`, el puerto del servidor web (`3333`) y la flag de escaneo `-v`.

```
2. 1. No answer needed
   2. 6
   3. 4.10
   4. 400
   5. Ubuntu
   6. 3333
   7. No answer needed
   8. -v
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |
| 2 | *(Pregunta 2 no especificada en el original)* | `6` |
| 3 | *(Pregunta 3 no especificada en el original)* | `4.10` |
| 4 | *(Pregunta 4 no especificada en el original)* | `400` |
| 5 | *(Pregunta 5 no especificada en el original)* | `Ubuntu` |
| 6 | *(Pregunta 6 no especificada en el original)* | `3333` |
| 7 | *(Pregunta 7 no especificada en el original)* | `No answer needed` |
| 8 | *(Pregunta 8 no especificada en el original)* | `-v` |

### Task 3: Enumeración web / Web Enumeration

**Explicación:** Se enumera el servidor web (puerto `3333`) y se descubre el directorio `/internal/`, que aloja el endpoint vulnerable de subida de archivos.

```
3. 1. No answer needed
   2. /internal/
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |
| 2 | *(Pregunta 2 no especificada en el original)* | `/internal/` |

### Task 4: Explotación web / Web Exploitation

**Explicación:** El endpoint de subida filtra por extensión: `.php` está bloqueado pero `.phtml` pasa el filtro. Se sube una reverse shell con esa extensión (`-v` como flag de enumeración previa) y se obtiene una shell como el usuario `bill`; la flag de usuario es `8bd7992fbe8a6ad22a63361004cfcedb`.

```
4. 1. .php
   2. No answer needed
   3. .phtml
   4. No answer needed
   5. bill
   6. 8bd7992fbe8a6ad22a63361004cfcedb
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `.php` |
| 2 | *(Pregunta 2 no especificada en el original)* | `No answer needed` |
| 3 | *(Pregunta 3 no especificada en el original)* | `.phtml` |
| 4 | *(Pregunta 4 no especificada en el original)* | `No answer needed` |
| 5 | *(Pregunta 5 no especificada en el original)* | `bill` |
| 6 | *(Pregunta 6 no especificada en el original)* | `8bd7992fbe8a6ad22a63361004cfcedb` |

### Task 5: Escalada de privilegios / Privilege Escalation

**Explicación:** Una vez con shell, se enumera el sistema en busca de binarios SUID. `/bin/systemctl` permite arrancar un servicio como root, otorgando una shell con privilegios de root; la flag de root es `a58ff8579f0a9270368d33a9966c7fd5`.

```
5. 1. /bin/systemctl
   2. a58ff8579f0a9270368d33a9966c7fd5
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `/bin/systemctl` |
| 2 | *(Pregunta 2 no especificada en el original)* | `a58ff8579f0a9270368d33a9966c7fd5` |

---

**Metodología:** Reconocimiento con Nmap → enumeración de directorios → descubrimiento del endpoint `/internal/` → prueba de extensiones permitidas en la subida de archivos → subida de reverse shell `.phtml` → obtención de shell como `bill` → enumeración de binarios SUID → explotación de `/bin/systemctl` para ejecutar comandos como root → lectura de las flags.

### Cadena de ataque / Attack Chain

```text
Nmap (Ubuntu, puertos abiertos, web en 3333) -> enumeración descubre /internal/ -> la subida bloquea .php pero permite .phtml -> reverse shell .phtml -> shell como bill -> find -perm -4000 descubre /bin/systemctl -> systemctl activa servicio malicioso como root -> flag de root
```

**Learning chain:** Enumeración de servicios → descubrimiento web → filtro de extensiones → reverse shell → binario SUID systemctl → escalada a root

**Lección:** *Un filtro de extensiones incompleto (que bloquea `.php` pero permite `.phtml`) y un binario SUID como `/bin/systemctl` son suficientes para pasar de una web pública a una shell de root.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1595.002 (Vulnerability Scanning), T1083 (File and Directory Discovery), T1190 (Exploit Public-Facing Application), T1505.003 (Web Shell), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Vulnversity](https://tryhackme.com/room/vulnversity)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.