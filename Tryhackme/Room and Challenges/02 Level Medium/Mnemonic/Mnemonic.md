# Mnemonic

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF | mnemonic | https://tryhackme.com/room/mnemonic | 02 Level Medium | TryHackMe | FTP, esteganografía, backups, credenciales | Compromiso total (credenciales + 2 flags) |

---

**Contexto:** La sala **Mnemonic** es un CTF que combina enumeración de servicios, **FTP**, **esteganografía** y la recuperación de un **backup** para obtener credenciales. Una vez dentro del sistema se escala y se recuperan las dos flags. La resolución exige exprimir el `backups.zip`, deducir contraseñas de los pistas de la sala y encadenar las credenciales para llegar al usuario y a root.

## Solucionario

### Task 1: Presentación
**Explicación:**

Introducción al reto y despliegue de la máquina del laboratorio.

Respuesta: `No answer needed`

### Task 2: Enumeración
**Explicación:**

Enumerando el host se descubren los **puertos/servicios relevantes** (`3` y `1337`) y el archivo `backups.zip` que contiene los datos clave del reto.

1. `3`
2. `1337`
3. `backups.zip`

### Task 3: Credenciales
**Explicación:**

Analizando el backup y las pistas de la sala se recuperan las credenciales del servicio **FTP** y los usuarios del sistema.

1. `ftpuser`
2. `love4ever`
3. `james`
4. `bluelove`
5. `pasificbell1981`

### Task 4: Flags
**Explicación:**

Con acceso al sistema se obtienen las flags de usuario y de root.

1. `THM{a5f82a00e2feee3465249b855be71c01}`
2. `THM{2a4825f50b0c16636984b448669b0586}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Presentación del reto | `No answer needed` |
| 2.1 | Primer servicio/puerto relevante | `3` |
| 2.2 | Segundo servicio/puerto relevante | `1337` |
| 2.3 | Archivo de backup clave | `backups.zip` |
| 3.1 | Credencial del servicio FTP | `ftpuser` |
| 3.2 | Primera contraseña | `love4ever` |
| 3.3 | Usuario del sistema | `james` |
| 3.4 | Segunda contraseña | `bluelove` |
| 3.5 | Tercera contraseña | `pasificbell1981` |
| 4.1 | Flag de usuario | `THM{a5f82a00e2feee3465249b855be71c01}` |
| 4.2 | Flag de root | `THM{2a4825f50b0c16636984b448669b0586}` |

---

**Metodología:** Enumeración de puertos y servicios → recuperación de `backups.zip` → esteganografía/análisis del backup → descifrado de credenciales FTP y de usuario → acceso al sistema → captura de flags de usuario y root.

**Learning chain:** Reconocimiento → puertos 3/1337 → backup → credenciales → FTP/usuario → shell → flags.

**Lección:** *Un backup aparentemente inocuo guarda las credenciales; combinar enumeración, estego y reutilización de contraseñas desbloquea la máquina por completo.*

**MITRE ATT&CK:** T1505.001 Server Software Component: SQL Stored Procedures (pista del backup) · T1110 Brute Force.

**Fuente:** [TryHackMe - Mnemonic](https://tryhackme.com/room/mnemonic)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.