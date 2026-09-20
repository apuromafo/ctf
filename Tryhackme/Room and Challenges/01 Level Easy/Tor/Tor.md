# Tor

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `tor` | [TryHackMe](https://tryhackme.com/room/tor) | 01 Level Easy | THM | Tor Browser, circuitos Tor, navegación anónima, buscador DuckDuckGo | Uso de Tor Browser para navegar de forma anónima y evadir el rastreo en la web |

---

**Contexto:**

> **ES:** La sala introduce Tor Browser como herramienta de anonimato en la navegación web: se instala el navegador, se comparan sus diferencias frente a los navegadores convencionales y se completan ejercicios prácticos que culminan con el buscador por defecto de Tor, DuckDuckGo, como mecanismo de búsqueda privada.

> **EN:** This room introduces Tor Browser as an anonymisation tool for web browsing: you install the browser, compare it against conventional browsers, and complete hands-on exercises that end with the default Tor search engine, DuckDuckGo, as a privacy-preserving search mechanism.

## Solucionario

### Task 1: Instalación de Tor Browser / Installing Tor Browser

**Explicación:**

1. 1. No answer needed
   2. No answer needed
   3. No answer needed
   4. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Download and install the Tor Browser. | `No answer needed` |
| 2 | Verify the installation and launch the browser. | `No answer needed` |
| 3 | Review the available security levels. | `No answer needed` |
| 4 | Confirm the traffic is routed through the Tor network. | `No answer needed` |

### Task 2: Diferentes Navegadores / Different Browsers

**Explicación:**

2. 1. No answer needed
   2. No answer needed
   3. No answer needed
   4. No answer needed
   5. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Compare the Tor Browser with your regular browser. | `No answer needed` |
| 2 | Identify the visual and fingerprinting differences. | `No answer needed` |
| 3 | Review the extensions and options exclusive to Tor. | `No answer needed` |
| 4 | Evaluate the Tor circuit of a visited page. | `No answer needed` |
| 5 | Continue with the guided exercises. | `No answer needed` |

### Task 3: Ejercicios con Tor Browser / Tor Browser Exercises

**Explicación:**

3. 1. No answer needed
   2. No answer needed
   3. DuckDuckGo

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Complete the first guided browsing exercise. | `No answer needed` |
| 2 | Complete the second guided browsing exercise. | `No answer needed` |
| 3 | What search engine does the Tor Browser use by default? | `DuckDuckGo` |

---

**Metodología:** Se instala Tor Browser, se revisan sus diferencias frente a los navegadores convencionales y se ejecutan los ejercicios guiados de navegación para validar el anonimato, finalizando con la identificación del buscador por defecto del navegador Tor.

### Cadena de ataque / Attack Chain

Instalación del navegador → comparación con navegadores convencionales → navegación anónima por circuitos Tor → identificación del buscador privado DuckDuckGo.

**Learning chain:** Tor Browser installation → browser comparison → anonymized navigation → default search engine identification

**Lección:** *El anonimato no es una herramienta, sino un hábito: los navegadores especializados ayudan, pero la operativa segura se construye con práctica.*

**MITRE ATT&CK:** T1071.001 (Application Layer Protocol: Web Protocols), T1090 (Proxy), T1573 (Encrypted Channel)

**Fuente:** [TryHackMe - Tor](https://tryhackme.com/room/tor)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.