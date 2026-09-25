# Cat [EASY]

> **ES:** Challenge Mobile Easy: un backup de Android (`cat.ab`) sin protección que hay que desempaquetar (a `.tar`) e inspeccionar para encontrar la flag (`HTB{...}`) escondida entre los datos restaurados (una imagen con documento "TOP SECRET").
> **EN:** Easy Mobile challenge: an unprotected Android backup (`cat.ab`) to unpack (to `.tar`) and inspect in order to find the flag (`HTB{...}`) hidden among the restored data (an image showing a "TOP SECRET" document).

| Campo | Valor |
|-------|-------|
| **Categoría** | Mobile |
| **Dificultad** | Easy (10 puntos según Esther7171; nota previa del stub raíz decía 1pts — ver nota en fuentes) |
| **Estado** | Retired (writeups públicos desde 2021; no se reproduce flag literal) |
| **URL** | https://app.hackthebox.com/challenges/Cat |
| **Archivos** | `cat.zip` → `cat.ab` (Android Backup, sin contraseña) |
| **Fecha de resolución** | 2026-09-25 (documentación; resuelto previamente según stub local) |

---

## 🎯 Objetivo / Goal

> **ES:** Extraer el contenido del backup `cat.ab`, recorrer el árbol restaurado y localizar la flag en claro (formato `HTB{...}`) visible en una imagen con documentación "TOP SECRET".
> **EN:** Extract the contents of the `cat.ab` backup, walk the restored tree and locate the plaintext flag (`HTB{...}` format) visible in an image showing a "TOP SECRET" document.

---

## 🛠️ Herramientas usadas / Tools used

- [ ] `unzip`, `file`, `tar` (triage y extracción)
- [ ] `abe.jar` ([nelenkov/android-backup-extractor](https://github.com/nelenkov/android-backup-extractor)) — vía `java -jar abe.jar unpack cat.ab cat.tar`
- [ ] Alternativa sin Java: cabecera zlib + `tail` para tratar el `.ab` como `.tar.gz` (ver paso 1, opción B)
- [ ] Visor de imágenes / explorador de archivos para revisar el árbol extraído

---

## 📋 Pasos / Steps

### Paso 1 — Análisis inicial / Triage

> **ES:** El descargable es un `.zip` con un único `cat.ab`: backup de Android SDK sin cifrar. Se confirma el tipo con `file` y se desempaqueta a `.tar` (dos vías equivalentes).
> **EN:** The download is a `.zip` holding a single `cat.ab`: an unencrypted Android SDK backup. Confirm the type with `file` and unpack it to `.tar` (two equivalent ways).

```bash
unzip cat.zip && file cat.*
# esperado: cat.ab: Android Backup (sin contraseña)

# Opción A — extractor oficial (paráfrasis de NB Studio / Danish Zia):
java -jar abe.jar unpack cat.ab cat.tar
tar -xf cat.tar && ls

# Opción B — sin Java, como .tar.gz con cabecera (paráfrasis de w4dd325):
( printf "\x1f\x8b\x08\x00\x00\x00\x00\x00" ; tail -c +25 cat.ab ) | tar xfvz -
```

**Resultado / Result:** Árbol de backup restaurado en disco (carpetas de app + ficheros multimedia); sin contraseña porque el backup está desprotegido — de ahí el título/lección del reto.

### Paso 2 — Inspeccionar el contenido y leer la flag / Inspect contents and read flag

> **ES:** Recorrer las carpetas restauradas: la mayoría de imágenes son de gatos, pero una muestra papeleo "TOP SECRET"; ampliando su parte inferior se lee la flag en claro (formato `HTB{...}`).
> **EN:** Walk the restored folders: most images are cats, but one shows "TOP SECRET" paperwork; zooming into its lower part reveals the plaintext flag (`HTB{...}` format).

```bash
find . -type f | head -40
find . -type f \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.txt" \) | sort
grep -ri "HTB{" . 2>/dev/null | head
# esperado: la flag aparece en imagen (no necesariamente en texto plano grepeable)
```

**Resultado / Result:** Flag localizada visualmente en la imagen del documento (no se reproduce aquí por integridad del contenido; challenge retirado, ver capturas de las fuentes citadas).

---

## 🧠 Lo aprendido / Learned

- [ ] Los backups de Android (`.ab`) pueden generarse sin contraseña: cualquiera con el archivo restaura los datos de la app.
- [ ] `abe.jar unpack <backup.ab> <backup.tar>` convierte el backup en un `.tar` inspeccionable; alternativamente el payload tras el offset 25 es un stream zlib válido con cabecera estándar.
- [ ] Triage forense básico: `unzip` → `file` → `tar -xf` → `find` por extensiones → revisión manual de imágenes.
- [ ] Lección de higiene: no respaldar ni exponer datos sensibles (documentos, fotos con texto legible) sin cifrado.
- [ ] No confundir con la máquina retirada "Cat" (Medium, Linux): este es el challenge Mobile del mismo nombre.

---

## 📚 Fuentes y Referencias / Sources

- **Walkthrough de referencia:** [Cat — w4dd325](https://w4dd325.wordpress.com/2021/05/20/672/) — w4dd325 (descarga, `.ab` como backup de Android SDK, truco `printf`+`tail -c +25` a `.tar.gz`, carpetas con imágenes de gatos, imagen "TOP SECRET" con la flag abajo)
- **Walkthrough de referencia:** [Cat HTB Challenge - Flag Writeup — Esther7171](https://github.com/Esther7171/HackTheBox-Writeups-Walkthroughs/blob/main/Write-ups/Challanges/Cat/readme.md) — Esther7171 (Category: Mobile, Difficulty: Easy, 10 Points; objetivo: backups desprotegidos)
- **Ficha técnica:** [Cat | NB Studio — Nicolas BENY](https://nbeny.fr/hackthebox/Challenges/Mobile/Cat) — Nicolas BENY (Category: Mobile Android, Difficulty: Easy; `java -jar abe.jar unpack cat.ab cat.tar` + `tar -xf cat.tar`)
- **Herramienta citada (no copiada):** [android-backup-extractor — nelenkov](https://github.com/nelenkov/android-backup-extractor) — nelenkov (`abe unpack <backup.ab> <backup.tar> [password]`)
- **Nota local previa:** stub raíz `Soluciones/Challenges/cat.md` ("Points: 1pts") migrado a esta plantilla; la cifra oficial en la fuente citada es 10 puntos (posible confusión con nº de solves en la nota previa)
- **Fecha de acceso:** 2026-09-25
- **Autor de este walkthrough:** Apuromafo (síntesis propia parafraseada a partir de las fuentes citadas)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. Challenge retirado; no se publican flags literales.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Retired challenge; no literal flags published.

_Fecha de edición: 2026-09-25_
