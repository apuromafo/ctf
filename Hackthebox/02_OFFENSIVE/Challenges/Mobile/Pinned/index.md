# Pinned [EASY]

> **ES:** Challenge Mobile Easy: una app Android (`com.example.pinned`) con login automático contra un backend HTTPS con certificate pinning; hay que anular el pinning e interceptar el tráfico para recuperar la contraseña/flag (`HTB{...}`).
> **EN:** Easy Mobile challenge: an Android app (`com.example.pinned`) with auto-login against an HTTPS backend using certificate pinning; bypass the pinning and intercept traffic to recover the password/flag (`HTB{...}`).

| Campo | Valor |
|-------|-------|
| **Categoría** | Mobile (ubicado provisionalmente en `Misc/` hasta mover la carpeta) |
| **Dificultad** | Easy |
| **Estado** | Retired |
| **URL** | https://app.hackthebox.com/challenges/Pinned [verificar slug exacto] |
| **Archivos** | `pinned.apk` + instancia remota (login) [verificar nombre exacto del zip] |
| **Fecha de resolución** | 2026-09-25 (documentación; resuelto previamente según stub local) |
| **Puntos** | [verificar] (rango Easy habitual: 10–30) |

---

## 🎯 Objetivo / Goal

> **ES:** Instalar la APK, anular el certificate pinning con instrumentación dinámica (Frida/objection o script de unpinning) e interceptar el login con Burp/HTTP Toolkit para leer la contraseña/flag en claro (formato `HTB{...}`).
> **EN:** Install the APK, disable certificate pinning via dynamic instrumentation (Frida/objection or an unpinning script) and intercept the login with Burp/HTTP Toolkit to read the password/flag in plaintext (`HTB{...}` format).

---

## 🛠️ Herramientas usadas / Tools used

- [ ] Emulador Android (API ≤ 29 recomendada; p. ej. Android 10 Google APIs) + `adb`
- [ ] `zipalign` + `keytool` + `apksigner` (solo si la APK no instala en Android moderno)
- [ ] Frida (`frida-server` + `frida-tools` / `frida-ps`) u `objection`
- [ ] Script de unpinning (p. ej. `frida-android-unpinning/frida-script.js`) o `android sslpinning disable`
- [ ] Proxy interceptador: Burp Suite o HTTP Toolkit (con su CA instalada en el emulador)

---

## 📋 Pasos / Steps

### Paso 1 — Análisis inicial / Triage

> **ES:** La descripción indica login automático sobre conexión "segura" que no deja interceptar: pista de pinning. Se instala la APK (`com.example.pinned`) y se confirma que el proxy ve conexiones fallidas/bloqueadas.
> **EN:** The description mentions auto-login over a "secure" connection that resists interception: a pinning hint. Install the APK (`com.example.pinned`) and confirm the proxy sees failed/blocked connections.

```bash
adb install pinned.apk
frida-ps -Uia | grep -i pinned
# esperado: com.example.pinned listado como instrumentable
```

**Resultado / Result:** App instalada y proceso `com.example.pinned` visible para Frida; sin bypass, el login no deja ver tráfico en claro (pinning activo).

> **ES:** Nota de compatibilidad: en Android 11+ (API 30+) la APK original puede fallar al instalar (`resources.arsc ... uncompressed and aligned`); se realinea y re-firma.
> **EN:** Compatibility note: on Android 11+ (API 30+) the original APK may fail to install (`resources.arsc ... uncompressed and aligned`); re-align and re-sign it.

```bash
zipalign -p -f -v 4 pinned.apk align-pinned.apk
keytool -genkey -v -keystore research.keystore -alias research_key -keyalg RSA -keysize 2048 -validity 10000
apksigner sign --ks research.keystore align-pinned.apk
adb install align-pinned.apk
```

**Resultado / Result:** APK instalada en el emulador moderno; la pantalla de login carga [verificar captura propia en `img/`].

### Paso 2 — Bypass de certificate pinning / Pinning bypass

> **ES:** Se arranca `frida-server` en el dispositivo y se inyecta el bypass de dos formas equivalentes (elegir una): script genérico de unpinning o `objection`.
> **EN:** Start `frida-server` on the device and inject the bypass via either equivalent method (pick one): a generic unpinning script or `objection`.

```bash
# En el dispositivo/emulador (root):
adb push frida-server /data/local/tmp/frida-server
adb shell "chmod 755 /data/local/tmp/frida-server"
adb shell "/data/local/tmp/frida-server &"

# Desde el host:
frida-ps -U -ai

# Opción A — script genérico (paráfrasis de CSbyGB):
wget https://raw.githubusercontent.com/httptoolkit/frida-android-unpinning/main/frida-script.js
frida -U -l ./frida-script.js -f com.example.pinned

# Opción B — objection (paráfrasis de Gabe Roy):
objection -g com.example.pinned explore
# dentro de objection:
# android sslpinning disable
```

**Resultado / Result:** Agente inyectado (`Agent injected and responds ok!` / proceso spawneado); los `TrustManager` quedan neutralizados y el tráfico ya pasa por el proxy.

### Paso 3 — Interceptar el login y leer la flag / Intercept login and read flag

> **ES:** Con el proxy (Burp/HTTP Toolkit) interceptando y el bypass activo, pulsar login en la app y buscar la petición/respuesta con la contraseña o flag.
> **EN:** With the proxy (Burp/HTTP Toolkit) intercepting and the bypass active, tap login in the app and look for the request/response carrying the password or flag.

```bash
# Sin comando: acción en la app (tap "login") + inspección en Burp/HTTP Toolkit
# (historial HTTP → petición de login → cuerpo en claro con credencial/flag)
```

**Resultado / Result:** Credencial/flag visible en claro en el inspector con formato `HTB{...}` (no se reproduce aquí por integridad del contenido; challenge retirado, ver capturas de las fuentes citadas). [verificar] reproducción propia con captura en `img/`.

---

## 🧠 Lo aprendido / Learned

- [ ] Certificate pinning ≠ TLS normal: la app fija el certificado esperado y rechaza el proxy aunque su CA esté instalada.
- [ ] Frida + `frida-server` permite instrumentación dinámica (`frida-ps -Uia`, spawn/attach a `com.example.pinned`).
- [ ] Dos vías equivalentes de bypass: script universal de unpinning o `objection` → `android sslpinning disable`.
- [ ] Detalle operativo: API ≤ 29 evita fricción de instalación; en API 30+ realinear (`zipalign`) y re-firmar (`apksigner`).
- [ ] Parte de la pista "Intro to Android Exploitation" de HTB (junto a Manager, Anchored, APKrypt) [verificar alcance exacto del track].

---

## 📚 Fuentes y Referencias / Sources

- **Walkthrough de referencia:** [Android CTF - HTB Pinned — Gabe Roy](https://gaberoy.zip/posts/pinned/pinned) — Gabe Roy (descripción del challenge, error de instalación en API 30+, realineado/firmado, `frida-ps`, `objection -g com.example.pinned explore`, `android sslpinning disable`, interceptación del login)
- **Walkthrough de referencia:** [HTB-Intro-to-android-Exploitation-Track — CSbyGB/pentips](https://github.com/CSbyGB/pentips/blob/main/writeups/HTB-Intro-to-android-Exploitation-Track.md) — CSbyGB (setup Frida en venv, `adb push frida-server`, `frida-ps -U -ai`, script `httptoolkit/frida-android-unpinning/frida-script.js`, `frida -U -l ./frida-script.js -f com.example.pinned`, login → flag en Burp)
- **Script citado (no copiado):** [frida-android-unpinning — HTTPCToolkit](https://raw.githubusercontent.com/httptoolkit/frida-android-unpinning/main/frida-script.js) — HTTP Toolkit (script genérico de bypass referenciado por CSbyGB)
- **Nota local previa:** `Soluciones/Challenges/pinned.md` (front-matter `type: Challenge / target: Pinned / status: Solved`) + stub previo de este `index.md` — ubicaba el challenge provisionalmente en `Misc/`; aquí se corrige la categoría a Mobile
- **Fecha de acceso:** 2026-09-25
- **Autor de este walkthrough:** Apuromafo (síntesis propia parafraseada a partir de las fuentes citadas)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. Challenge retirado; no se publican flags literales.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Retired challenge; no literal flags published.

_Fecha de edición: 2026-09-25_
