# Tooling via Browser Automation

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `customtoolingviabrowserautomation` |
| **Link** | [TryHackMe](https://tryhackme.com/room/customtoolingviabrowserautomation) |
| **Sección** | 01 Level Easy |
| **Fuente** | Writeup de Chetan Chinchulkar (InfoSec Write-ups) |
| **Componentes** | Selenium / Playwright / selenium_stealth / fake_useragent / WebDriver / CSRF / brute force |
| **Impacto** | Creación de tooling personalizado con automatización de navegador para bypassear CAPTCHAs, restricciones del cliente y extraer valores dinámicos |

---

**Contexto:** Creación de tooling personalizado para pruebas de aplicaciones usando Selenium y Playwright. La room cubre cómo automatizar el navegador para bypassear CAPTCHAs, restricciones del lado del cliente y extraer valores dinámicos, hasta ejecutar un ataque de fuerza bruta contra un login protegido con token CSRF.

## Solucionario

### Task 1: Why Use Browser Automation?

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Preguntas de lectura / reading questions) | `No answer needed` |

**Explicación:** Cuando automatizas el navegador, ya no tienes que romper manualmente las capas de cifrado. Dejas que el navegador haga el trabajo pesado, tal como lo haría un usuario legítimo. El JavaScript que se ejecuta en la aplicación realiza toda su lógica del lado del cliente, incluyendo cifrado personalizado y manipulaciones del DOM. La automatización del navegador es útil para: **bypass de CAPTCHAs y restricciones del lado del cliente** (al simular interacciones reales, muchos mecanismos de detección de bots se vuelven menos efectivos), disparar flujos de trabajo multi-paso (algunos exploits requieren interactuar con la aplicación a través de varias pantallas o acciones de usuario) y extraer valores renderizados o generados dinámicamente (a menudo los datos o tokens solo aparecen después de que el JavaScript se ejecuta). Se usa **Selenium** por su facilidad de uso, soporte de Python y amplia compatibilidad con navegadores.

### Task 2: Essential Concepts

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Preguntas de lectura / reading questions) | `No answer needed` |

**Explicación:** Conceptos esenciales de Selenium: **WebDriver** controla el navegador y permite navegar a páginas, interactuar con elementos y extraer datos; **Element Identification** son métodos para localizar e interactuar con elementos usando atributos como ID, Name o XPath; **Headless Mode** ejecuta navegadores sin interfaz gráfica (más rápido y eficiente); **CSRF Protection** — con Selenium, al usar un navegador, el token CSRF siempre se genera dinámicamente y se envía con cada petición; y **Stealth Techniques** — Selenium Stealth previene la detección imitando el comportamiento humano y enmascarando huellas automatizadas.

### Task 3: Performing the Brute-Force Attack

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Preguntas de lectura / reading questions) | `No answer needed` |

**Explicación:** La aplicación web en `http://SECOND_VM_IP/labs/lab1/` valida cada petición de login usando un token CSRF. El objetivo es realizar un ataque de fuerza bruta usando un script basado en Selenium para determinar la contraseña correcta. El script importa `By`, `webdriver`, `Options`, `Service` de Selenium, `selenium_stealth` (**stealth**) y `fake_useragent` (**UserAgent**). La configuración del navegador usa `--no-sandbox` (previene que Chrome use el modo sandbox; necesario en Docker o como root), `--headless` (Chrome sin interfaz gráfica), `start-maximized` (asegura que el navegador esté maximizado), `user-agent={userAgent}` (user agent aleatorio para evadir la detección), `--disable-dev-shm-usage` (previene limitaciones de memoria en contenedores Docker) y `--disable-cache` (asegura que el navegador obtenga datos frescos en cada intento).

### Task 4: Executing the Script

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Preguntas de lectura / reading questions) | `No answer needed` |

**Explicación:** Se ejecuta el script de fuerza bruta contra el lab. El script usa Selenium para intentar logins con una wordlist de contraseñas, manejando automáticamente los tokens CSRF. El navegador genera y envía los tokens CSRF automáticamente en cada petición, y se itera sobre la wordlist hasta encontrar la credencial correcta.

---

**Metodología:**
1. **Automatización del navegador:** usar **Selenium** para interactuar con la aplicación como un usuario real. Al automatizar el navegador dejas que haga el trabajo pesado (como un usuario legítimo): el JavaScript de la aplicación ejecuta su lógica del lado del cliente, incluyendo cifrado personalizado y manipulaciones del DOM. Utilidades: **bypass de CAPTCHAs y restricciones del cliente** (simular interacciones reales reduce la efectividad de los detectores de bots), **disparar flujos multi-paso** (exploits que requieren atravesar varias pantallas) y **extraer valores renderizados o generados dinámicamente** (datos o tokens que solo aparecen tras ejecutar el JS). Se elige Selenium por su facilidad de uso, soporte de Python y amplia compatibilidad con navegadores.
2. **Conceptos esenciales de Selenium:** **WebDriver** controla el navegador (navegar a páginas, interactuar con elementos, extraer datos); **Element Identification** localiza elementos con atributos como ID, Name o XPath; **Headless Mode** ejecuta navegadores sin interfaz gráfica (más rápido y eficiente); con Selenium el **token CSRF** siempre se genera dinámicamente y se envía con cada petición; **Stealth Techniques** (Selenium Stealth) previenen la detección imitando el comportamiento humano y enmascarando huellas automatizadas.
3. **Configuración del navegador para el ataque:** la app en `http://SECOND_VM_IP/labs/lab1/` valida cada login con token CSRF. El script importa `webdriver`, `Options`, `Service`, `stealth` (de selenium_stealth), `logging` y `UserAgent` (fake_useragent). Opciones: `--no-sandbox` (previene el modo sandbox de Chrome, necesario en Docker/root), `--headless` (sin interfaz), `start-maximized`, `user-agent` aleatorio (evadir detección), `--disable-dev-shm-usage` (limitaciones de memoria en Docker) y `--disable-cache` (datos frescos en cada intento), `--disable-gpu`.
4. **Fuerza bruta:** iterar sobre una wordlist de contraseñas hasta encontrar la correcta; el navegador maneja automáticamente los tokens CSRF generados en cada petición. La ejecución del script contra el lab completa la tarea.

**Learning chain:** browser automation (Selenium) → bypass CAPTCHA / client-side restrictions → valores dinámicos (tokens) → stealth (selenium_stealth + fake_useragent) → WebDriver headless → CSRF handling automático → brute-force wordlist sobre /labs/lab1/

**MITRE ATT&CK:** T1110 (Brute Force), T1110.001 (Brute Force: Password Guessing), T1053 (Scheduled Task/Job)

**Fuente:** [TryHackMe - Tooling via Browser Automation](https://tryhackme.com/room/customtoolingviabrowserautomation)