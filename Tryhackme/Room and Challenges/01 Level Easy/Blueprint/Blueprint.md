# Blueprint

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | challenge | `blueprint` | [TryHackMe](https://tryhackme.com/room/blueprint) | 01 Level Easy | TryHackMe | OSCommerce / web exploitation / RCE | Compromiso de una tienda OSCommerce vulnerable mediante una ruta de explotación remota y captura de la flag |

---

**Contexto:** Blueprint es una máquina vulnerable que ejecuta OSCommerce, un sistema de comercio electrónico desactualizado con una conocida vulnerabilidad de ejecución remota de código. La sala guía en la enumeración web, la localización de la ruta de explotación y la obtención de una shell para capturar la flag del sistema.

> **ES:** Tienda OSCommerce vulnerable. Se enumera el servidor web, se encuentra la carpeta oculta `googleplus` y se explota el RCE del CMS para obtener una shell y la flag.
> **EN:** A vulnerable OSCommerce store. After web enumeration, the hidden `googleplus` folder is found and the CMS RCE is exploited to get a shell and the flag.

## Solucionario

### Task 1: Carpeta secreta / Secret folder
**Explicación:** La enumeración de directorios del servidor web revela una carpeta oculta en el sitio de OSCommerce que da acceso a la ruta de explotación.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| ¿Cuál es el nombre de la carpeta secreta/oculta del servidor web? | `googleplus` |

### Task 2: Flag
**Explicación:** Explotando la vulnerabilidad de OSCommerce se obtiene una shell en el sistema y se localiza el archivo con la flag.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| ¿Cuál es la flag del sistema? | `THM{aea1e3ce6fe7f89e10cea833ae009bee}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Carpeta secreta/oculta del servidor web | `googleplus` |
| 2 | Flag del sistema | `THM{aea1e3ce6fe7f89e10cea833ae009bee}` |

---

**Metodología:** Se enumera el servidor web de OSCommerce y se descubre la carpeta oculta `googleplus`. A partir de esa ruta se localiza el exploit disponible para el CMS (ejecución remota de código), se lanza y se obtiene una shell en la máquina. Con acceso al sistema se navega por el filesystem y se captura la flag.

### Cadena de ataque / Attack Chain

```text
nmap -> puerto 80 OSCommerce -> enumeración de directorios -> googleplus -> exploit RCE OSCommerce -> shell -> flag
```

**Learning chain:** service enumeration --> web fingerprint (OSCommerce) --> directory discovery (googleplus) --> RCE exploit --> reverse shell --> flag capture

**Lección:** *Los CMS desactualizados con vulnerabilidades de ejecución remota conocidas representan un riesgo grave; la enumeración de directorios suele destapar la ruta exacta de explotación.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1046 (Network Service Discovery), T1059 (Command and Scripting Interpreter), T1005 (Data from Local System)

**Fuente:** [TryHackMe - Blueprint](https://tryhackme.com/room/blueprint)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.