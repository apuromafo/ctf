# Custom Tooling using Burp

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Hard | Walkthrough | `customtoolingviaburp` | https://tryhackme.com/room/customtoolingviaburp | 03 Level Hard | TryHackMe | Burp Suite / extensiones personalizadas / proxies interceptores (Fiddler, Caido) / fuerza bruta / tráfico HTTPS | Desarrollo de tooling propio para Burp Suite: identificar los proxies interceptores del mercado, construir una extensión personalizada que escucha en un puerto y automatiza una fuerza bruta (startBruteForce), y recuperar las flags escondidas en el tráfico y en el código. |

---

**Contexto:** Sala práctica del catálogo de TryHackMe centrada en el desarrollo de tooling personalizado para Burp Suite. El recorrido arranca identificando los proxies HTTP interceptores (Fiddler, Caido, Burp), continúa con la construcción de una extensión propia de Burp (puerto de escucha `0007` y método `startBruteForce`) y termina recolectando las flags escondidas en el tráfico cifrado y en el código fuente de la sala. Cierra con una conclusión sin respuesta.

> **ES:** "Desarrolla tu propio tooling para Burp Suite: reconoce los proxies interceptores, crea una extensión personalizada (puerto `0007` y método `startBruteForce`) y recoge las flags de la sala."
> **EN:** "Build your own tooling for Burp Suite: recognize the intercepting proxies, create a custom extension (port `0007` and `startBruteForce` method) and collect the room flags."

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Tarea de presentación de la sala sobre tooling con Burp Suite. No requiere respuesta. Contenido original de la tarea:

```text
1. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la introducción de la sala y preparar el entorno. | `No answer needed` |

### Task 2: Proxies interceptores / Intercepting proxies

**Explicación:** La sala pide identificar los proxies HTTP capaces de interceptar tráfico entre el navegador y el servidor. La lista de selección múltiple contempla Fiddler, Caido y Burp. Contenido original de la tarea:

```text
2. 1. Fiddler
   2. Caido
   3. Burp
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Proxies HTTP que interceptan el tráfico (opción 1). | `Fiddler` |
| 2 | Proxies HTTP que interceptan el tráfico (opción 2). | `Caido` |
| 3 | Proxies HTTP que interceptan el tráfico (opción 3). | `Burp` |

### Task 3: Flag de la extensión / Extension flag

**Explicación:** En esta tarea se valida la extensión personalizada cargada en Burp Suite. La primera respuesta es la flag de la propia extensión; la segunda es una respuesta literal adicional que se debe introducir tal cual. Contenido original de la tarea:

```text
3. 1. THM{101Burp}
   2. nay
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de la extensión cargada en Burp Suite. | `THM{101Burp}` |
| 2 | Respuesta literal adicional de la tarea. | `nay` |

### Task 4: Extensión personalizada / Custom extension

**Explicación:** Al implementar la extensión personalizada se configuran dos valores literales: el puerto de escucha de la extensión y el nombre del método que ejecuta la fuerza bruta. Contenido original de la tarea:

```text
4. 1. 0007
   2. startBruteForce
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Puerto de escucha configurado en la extensión. | `0007` |
| 2 | Nombre del método de la extensión que lanza la fuerza bruta. | `startBruteForce` |

### Task 5: Flag del código fuente / Source code flag

**Explicación:** La flag de esta tarea está escondida en el código fuente de la aplicación y se obtiene al inspeccionar los recursos servidos. Contenido original de la tarea:

```text
5. THM{You.Will.Never.Guess.This.Super.Secure.Secret}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag encontrada en el código fuente. | `THM{You.Will.Never.Guess.This.Super.Secure.Secret}` |

### Task 6: Flag del cifrado de extremo a extremo / End-to-end encryption flag

**Explicación:** Al examinar el tráfico cifrado de extremo a extremo del entorno se encuentra esta flag. Contenido original de la tarea:

```text
6. THM{end_2_end_encryption!}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag asociada al cifrado de extremo a extremo. | `THM{end_2_end_encryption!}` |

### Task 7: Conclusión / Conclusion

**Explicación:** Tarea de cierre de la sala; no requiere respuesta. Contenido original de la tarea:

```text
7. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Cierre de la sala y repaso del tooling desarrollado. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la introducción de la sala y preparar el entorno. | `No answer needed` |
| 2 | Proxies HTTP que interceptan el tráfico (opción 1). | `Fiddler` |
| 3 | Proxies HTTP que interceptan el tráfico (opción 2). | `Caido` |
| 4 | Proxies HTTP que interceptan el tráfico (opción 3). | `Burp` |
| 5 | Flag de la extensión cargada en Burp Suite. | `THM{101Burp}` |
| 6 | Respuesta literal adicional de la tarea. | `nay` |
| 7 | Puerto de escucha configurado en la extensión. | `0007` |
| 8 | Nombre del método de la extensión que lanza la fuerza bruta. | `startBruteForce` |
| 9 | Flag encontrada en el código fuente. | `THM{You.Will.Never.Guess.This.Super.Secure.Secret}` |
| 10 | Flag asociada al cifrado de extremo a extremo. | `THM{end_2_end_encryption!}` |
| 11 | Cierre de la sala y repaso del tooling desarrollado. | `No answer needed` |

---

**Metodología:**
1. Identificar los proxies HTTP interceptores: Fiddler, Caido y Burp (selección múltiple).
2. Cargar una extensión personalizada en Burp Suite y validar su funcionamiento (flag `THM{101Burp}`).
3. Configurar la extensión con el puerto de escucha `0007` y el método `startBruteForce`.
4. Inspeccionar el código fuente de la aplicación para recuperar la flag escondida.
5. Analizar el tráfico cifrado de extremo a extremo para recuperar la última flag.

### Cadena de ataque / Attack Chain

```text
Setup -> Identificar proxies interceptores (Fiddler / Caido / Burp) -> Cargar extensión personalizada -> Puerto 0007 -> startBruteForce -> flag THM{101Burp} -> código fuente -> flag THM{You.Will.Never.Guess.This.Super.Secure.Secret} -> tráfico cifrado E2E -> flag THM{end_2_end_encryption!}
```

**Learning chain:** `Identificar proxies interceptores -> extender Burp Suite -> puerto de escucha -> método startBruteForce -> fuerza bruta -> flags del entorno`

**Lección:** *Construir tooling propio sobre las API de Burp Suite (extensiones con puerto de escucha y métodos reutilizables como `startBruteForce`) permite automatizar flujos repetitivos y explorar el tráfico cifrado para extraer información sensible.*

**MITRE ATT&CK:** T1071.001 (Application Layer Protocol: Web Protocols), T1059 (Command and Scripting Interpreter), T1105 (Ingress Tool Transfer), T1005 (Data from Local System)

**Fuente:** [TryHackMe - Custom Tooling using Burp](https://tryhackme.com/room/customtoolingviaburp)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.