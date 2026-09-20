# CAPTCHApocalypse
| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `captchapocalypse` |
| **Link** | [TryHackMe](https://tryhackme.com/room/captchapocalypse) |
| **Sección** | Web / Custom Tooling |
| **Fuente** | Research de djalilayed (GitHub) y Valikahn (GitHub) |
| **Componentes** | Web, CAPTCHA (captcha.php), criptografía en el cliente (RSA embebido en JavaScript), selenium + chromium/chromedriver, pytesseract (OCR), Pillow, rockyou (100 primeras), brute force de login, CSRF/JS-driven login, dashboard |
| **Impacto** | Sala Medium de "Custom Tooling": construir un script de automatización (Selenium + OCR) que resuelva el CAPTCHA y descifre el flujo de login cifrado en el cliente para hacer fuerza bruta contra el formulario de administración y capturar la flag del dashboard. |
---
**Contexto:** La sala propone automatizar el login de un panel web protegido por CAPTCHA y por criptografía asimétrica en el navegador: el formulario cifra los datos (usuario, contraseña y captcha) con una clave RSA embebida en `script.js` y los envía a `server.php`; la respuesta llega cifrada. La solución es "herramienta sobre medida": Selenium con Chromium replica el flujo real del navegador, Tesseract (OCR) lee cada CAPTCHA, y solo se prueban las 100 primeras contraseñas de `rockyou.txt` hasta detectar la válida y entrar en `dashboard.php`, donde está la flag.
*EN: The room asks you to automate the login of a web panel protected by a CAPTCHA and by client-side asymmetric cryptography: the form encrypts the data (username, password and captcha) with an RSA key embedded in `script.js` and sends it to `server.php`; the reply comes back encrypted. The solution is custom tooling: Selenium with Chromium replicates the real browser flow, Tesseract (OCR) reads each CAPTCHA, and only the first 100 RockYou passwords are tested until the valid one is detected, reaching `dashboard.php`, where the flag lies.*
## Solucionario
### Task 1 — Get the Flag
**Explicación:** Configuración: máquina objetivo (`captcha.thm`), Apache en 80 con el login; `script.js` muestra el flujo (CSRF token + RSA + submit cifrado a `server.php`). Se prepara el entorno (Chromium + chromedriver versiones iguales, Selenium, Pillow, pytesseract, Tesseract) y un wordlist con las 100 primeras líneas de `rockyou.txt`. El script automatiza: abrir login, capturar la imagen `captcha.php`, OCR con `--psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`, rellenar `username=admin`, probar una contraseña, pulsar el botón real (que cifra y envía) y distinguir entre `FAILED`, `MISREAD` (CAPTCHA mal leído, reintentar) y `SUCCESS` (redirección a `dashboard.php`). Con la credencial correcta el dashboard muestra la flag.
*EN: Setup: target machine (`captcha.thm`), Apache on 80 hosting the login; `script.js` shows the flow (CSRF token + RSA + encrypted submit to `server.php`). Environment preparation (matching Chromium + chromedriver versions, Selenium, Pillow, pytesseract, Tesseract) and a wordlist with the first 100 lines of `rockyou.txt`. The script automates: open login, capture the `captcha.php` image, OCR with `--psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`, fill `username=admin`, try one password, click the real button (which encrypts and submits) and distinguish between `FAILED`, `MISREAD` (misread CAPTCHA, retry) and `SUCCESS` (redirect to `dashboard.php`). With the correct credential the dashboard shows the flag.*

```bash
# Preparación del entorno
pip install selenium selenium-stealth fake_useragent pillow pytesseract
wget https://storage.googleapis.com/chrome-for-testing-public/137.0.7151.103/linux64/chromedriver-linux64.zip
# Wordlist limitada (100 primeras de rockyou)
head -n 100 /usr/share/wordlists/rockyou.txt > newrockyou.txt
# Configuración OCR
config="--psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
python3 script.py   # Selenium: captcha -> OCR -> login -> dashboard
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{8938aed9fbf43bddb7c0a98f292dca00}` |
---
**Metodología:** Preparar target y `/etc/hosts` (captcha.thm) → enumerar web y endpoints (server.php, captcha.php, dashboard.php, script.js) → analizar el JS (RSA embebido, submit cifrado) → preparar wordlist (100 primeras de rockyou) → framework Selenium+OCR (pytesseract/Pillow) con selector de CAPTCHA y botón real → distinguir errores de CAPTCHA vs contraseña → detectar la correcta (redirect a dashboard) → leer la flag.
**Learning chain:** client-side crypto review → browser automation (Selenium) → CAPTCHA solving with OCR → constrained brute force (rockyou-100) → logged-in dashboard → flag.
**Lección:** *La criptografía en el navegador no oculta nada: si el flujo completo ocurre en el cliente, automatizar el navegador real (no recrear la API) resuelve CAPTCHA y cifrado de una vez. El CAPTCHA sin rate limiting es solo un retraso, no una defensa.*
**MITRE ATT&CK:** T1110 (Brute Force), T1110.004 (Credential Stuffing), T1059.007/006 (JavaScript/Python), T1071.001 (Web), T1530 (Data from Cloud Storage Object - dashboard), T1078.
**Fuente:** [TryHackMe - CAPTCHApocalypse](https://tryhackme.com/room/captchapocalypse)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.