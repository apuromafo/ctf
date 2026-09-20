# Plotted-TMS

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | ctf | `plottedtms` | [TryHackMe](https://tryhackme.com/room/plottedtms) | 01 Level Easy | THM | Reconocimiento web, Enumeración de puertos, Aplicaciones web internas, Explotación, Flags | CTF de explotación web y máquina Linux |

---

**Contexto:** CTF de nivel fácil donde el compromiso comienza con la enumeración de un sitio web y el descubrimiento de una aplicación interna accesible en un puerto alternativo. A través de la manipulación de la aplicación y del servicio de fondo se consigue la ejecución de comandos y el acceso a la máquina para recuperar las dos flags del desafío.

> **ES:** Máquina CTF donde el reconocimiento de una aplicación web lleva a un servicio interno vulnerable; explotándolo se obtiene una shell y las dos flags del desafío.
> **EN:** CTF machine where web application recon leads to a vulnerable internal service; exploiting it grants a shell and both flags.

## Solucionario

### Task 1: Flags / Flags

**Explicación:** Completa la máquina: se enumeran los puertos y servicios, se descubre la aplicación, se explota la funcionalidad vulnerable para conseguir una shell y se recuperan las dos flags del desafío.

1. 1. 77927510d5edacea1f9e86602f1fbadb
   2. 53f85e2da3e874426fa059040a9bdcab

| Pregunta | Respuesta |
|---|---|
| ¿Cuál es la primera flag del desafío? | `77927510d5edacea1f9e86602f1fbadb` |
| ¿Cuál es la segunda flag del desafío? | `53f85e2da3e874426fa059040a9bdcab` |

---

**Metodología:** Enumeración de puertos abiertos, tratamiento de la aplicación web descubierta (virtual host o puerto interno), análisis del código/funcionalidad de la aplicación y explotación de la vulnerabilidad para obtener una shell en la máquina.

### Cadena de ataque / Attack Chain
Escaneo de puertos y servicios -> Descubrimiento del sitio web y de la aplicación interna -> Análisis de la aplicación y de su comportamiento -> Explotación de la funcionalidad vulnerable -> Obtención de una shell -> Recuperación de las dos flags.

**Learning chain:** Enumeración web y de servicios, análisis de aplicaciones web, identificación de vector de ejecución y compromiso inicial de una máquina Linux.

**Lección:** *Las aplicaciones y servicios ocultos en puertos alternativos suelen ser el vector real de entrada: la enumeración exhaustiva vale más que el ataque directo a la superficie visible.*

**MITRE ATT&CK:** T1595 Active Scanning, T1190 Exploit Public-Facing Application, T1059 Command and Scripting Interpreter, T1059.004 Unix Shell.

**Fuente:** [TryHackMe - Plotted-TMS](https://tryhackme.com/room/plottedtms)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.