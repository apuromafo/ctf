# Tooling via Browser Automation [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough (Premium)
* **Slug:** `customtoolingviabrowserautomation`
* **Link:** https://tryhackme.com/room/customtoolingviabrowserautomation
* **Sección / Section:** Custom Tooling / Web
* **Fuente / Source:** Writeup de Chetan Chinchulkar (InfoSec Write-ups)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Creación de tooling personalizado para pruebas de aplicaciones usando Selenium y Playwright. La room cubre cómo automatizar el navegador para bypassear CAPTCHAs, restricciones del lado del cliente y extraer valores dinámicos.
> **EN:** Creating custom tooling for application testing using Selenium and Playwright. The room covers how to automate the browser to bypass CAPTCHAs, client-side restrictions and extract dynamic values.

---

### Task 1 — Why Use Browser Automation?

Cuando automatizas el navegador, ya no tienes que romper manualmente las capas de cifrado. Dejas que el navegador haga el trabajo pesado, tal como lo haría un usuario legítimo. El JavaScript que se ejecuta en la aplicación realiza toda su lógica del lado del cliente, incluyendo cifrado personalizado y manipulaciones del DOM.

La automatización del navegador es útil para:

* **Bypass de CAPTCHAs y restricciones del lado del cliente** — al simular interacciones reales, muchos mecanismos de detección de bots se vuelven menos efectivos.
* **Disparar flujos de trabajo multi-paso** — algunos exploits requieren interactuar con la aplicación a través de varias pantallas o acciones de usuario.
* **Extraer valores renderizados o generados dinámicamente** — a menudo los datos o tokens solo aparecen después de que el JavaScript se ejecuta.

Se usa **Selenium** por su facilidad de uso, soporte de Python y amplia compatibilidad con navegadores.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| (Preguntas de lectura / reading questions) | `No answer needed` |

---

### Task 2 — Essential Concepts

Conceptos esenciales de Selenium:

* **WebDriver:** controla el navegador y permite navegar a páginas, interactuar con elementos y extraer datos.
* **Element Identification:** métodos para localizar e interactuar con elementos usando atributos como ID, Name o XPath.
* **Headless Mode:** ejecutar navegadores sin interfaz gráfica, más rápido y eficiente.
* **CSRF Protection:** con Selenium, al usar un navegador, el token CSRF siempre se genera dinámicamente y se envía con cada petición.
* **Stealth Techniques:** Selenium Stealth previene la detección imitando el comportamiento humano y enmascarando huellas automatizadas.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| (Preguntas de lectura / reading questions) | `No answer needed` |

---

### Task 3 — Performing the Brute-Force Attack

La aplicación web en `http://SECOND_VM_IP/labs/lab1/` valida cada petición de login usando un token CSRF. El objetivo es realizar un ataque de fuerza bruta usando un script basado en Selenium para determinar la contraseña correcta.

**Script Overview:**

```python
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth

import time
import logging
from fake_useragent import UserAgent
```

* **Selenium WebDriver** controla el navegador Chrome para la automatización.
* **selenium_stealth** se usa para prevenir la detección de bots.
* **fake_useragent** genera huellas de navegador realistas para evitar la detección.

**Configuración del navegador:**

```python
options = Options()
ua = UserAgent()
userAgent = ua.random
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument("start-maximized")
options.add_argument(f'user-agent={userAgent}')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-cache')
options.add_argument('--disable-gpu')
```

* `--no-sandbox`: previene que Chrome use el modo sandbox (necesario en Docker o como root).
* `--headless`: ejecuta Chrome sin interfaz gráfica.
* `start-maximized`: asegura que el navegador esté maximizado.
* `user-agent`: genera un user agent aleatorio para evadir la detección.
* `--disable-dev-shm-usage`: previene limitaciones de memoria en contenedores Docker.
* `--disable-cache`: asegura que el navegador obtenga datos frescos en cada intento.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| (Preguntas de lectura / reading questions) | `No answer needed` |

---

### Task 4 — Executing the Script

Ejecutar el script de fuerza bruta contra el lab. El script usa Selenium para intentar logins con una wordlist de contraseñas, manejando automáticamente los tokens CSRF.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| (Preguntas de lectura / reading questions) | `No answer needed` |

---

## Metodología / Methodology

1. **Automatización del navegador:** usar Selenium para interactuar con la aplicación como un usuario real.
2. **Stealth:** usar `selenium_stealth` y `fake_useragent` para evitar la detección de bots.
3. **CSRF handling:** el navegador genera y envía automáticamente los tokens CSRF.
4. **Fuerza bruta:** iterar sobre una wordlist de contraseñas hasta encontrar la correcta.

**Lección:** la automatización del navegador permite abrazar la lógica de la aplicación en lugar de luchar contra ella, bypasseando controles del lado del cliente y extrayendo datos dinámicos.

---

*Documentación para propósitos educativos y registro de CTF.*
