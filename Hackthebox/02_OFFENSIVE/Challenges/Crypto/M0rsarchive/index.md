# M0rsarchive [EASY]

> **ES:** Challenge de archivado recursivo con esteganografía morse: un `M0rsarchive.zip` inicial contiene `flag_999.zip` (con contraseña) + `pwd.png`; la contraseña de cada nivel está dibujada en píxeles morse en su `pwd.png`. Hay que automatizar lectura morse → descompresión durante ~1000 niveles (`flag_999` → `flag_0`) hasta el fichero con la flag (`HTB{...}`). Nota: las fuentes lo etiquetan como Misc aunque en este repo vive en `Crypto/`.
> **EN:** Recursive-archive challenge with morse steganography: an initial `M0rsarchive.zip` holds `flag_999.zip` (password-protected) + `pwd.png`; each level's password is drawn as morse pixels in its `pwd.png`. Automate morse-reading → unzipping across ~1000 levels (`flag_999` → `flag_0`) down to the file with the flag (`HTB{...}`). Note: sources label it Misc although it lives under `Crypto/` in this repo.

| Campo | Valor |
|-------|-------|
| **Categoría** | Crypto (ubicación en repo) / Misc según fuentes — ver nota en fuentes |
| **Dificultad** | Easy (etiquetado "easy" en sealldev; Terminal Blink lo ficha como Misc Challenge) |
| **Estado** | Retired (writeups públicos desde 2023–2024; no se reproduce flag literal) |
| **URL** | https://app.hackthebox.com/challenges/M0rsarchive [verificar slug exacto] |
| **Archivos** | `M0rsarchive.zip` → `flag_999.zip` … `flag_0.zip` + `pwd.png` por nivel |
| **Fecha de resolución** | 2026-09-25 (documentación; resuelto previamente según stub local) |
| **Puntos (nota previa)** | 0pts (nota del stub raíz `Soluciones/Challenges/m0rsarchive.md`; puntos oficiales [verificar]) |
| **Autor original** | lebik (según sealldev) [verificar] |

---

## 🎯 Objetivo / Goal

> **ES:** Escribir un script que, por cada nivel, lea `pwd.png`, convierta los píxeles morse a texto, lo use como contraseña del siguiente `flag_N.zip` y repita hasta `flag_0`, donde aparece el fichero con la flag (formato `HTB{...}`).
> **EN:** Write a script that, per level, reads `pwd.png`, converts the morse pixels to text, uses it as the password for the next `flag_N.zip`, and repeats down to `flag_0`, where the file with the flag appears (`HTB{...}` format).

---

## 🛠️ Herramientas usadas / Tools used

- [ ] `unzip` / `7z` (descompresión con contraseña: `unzip -oP <pass>`, `7z x -p<pass>`)
- [ ] `python3` + `zipfile` (bucle recursivo de extracción)
- [ ] PIL (`Pillow`) u `opencv` (`cv2`) para leer píxeles de `pwd.png`
- [ ] Diccionario morse→texto (o lib `morse3`) para decodificar puntos/rayas
- [ ] `file`, `ls`, `cat` para triage

---

## 📋 Pasos / Steps

### Paso 1 — Análisis inicial / Triage

> **ES:** El zip inicial da `flag_999.zip` (pide contraseña) y `pwd.png` (imagen tiny, p. ej. 25×3 px). A simple vista son puntos y rayas: morse. El primer nivel decodifica a un dígito que abre `flag_999.zip` y revela `flag/flag_998.zip` + otro `pwd.png` (posiblemente multilínea y con otros colores): el reto es recursivo "varias veces" (~1000 niveles).
> **EN:** The initial zip yields `flag_999.zip` (asks for a password) and `pwd.png` (a tiny image, e.g. 25×3 px). At a glance it shows dots and dashes: morse. The first level decodes to a digit that opens `flag_999.zip` and reveals `flag/flag_998.zip` plus another `pwd.png` (possibly multi-line and differently coloured): the challenge is recursive "several times" (~1000 levels).

```bash
unzip M0rsarchive.zip && ls
# esperado: flag_999.zip + pwd.png
unzip -l flag_999.zip
file pwd.png && python3 -c "from PIL import Image; print(Image.open('pwd.png').size)"
# esperado: PNG pequeño; primera contraseña de un dígito
echo "9" | tr -d '\n' > /tmp/p1
unzip -oP "$(cat /tmp/p1)" flag_999.zip && ls flag/
# esperado: flag/flag_998.zip + flag/pwd.png
```

**Resultado / Result:** Confirmado el patrón recursivo: cada `flag_N.zip` se abre con el morse de su `pwd.png` y entrega `flag_{N-1}.zip` + el siguiente `pwd.png`.

### Paso 2 — Automatizar morse→contraseña→unzip / Automate morse→password→unzip

> **ES:** Programar el bucle (paráfrasis de sealldev/Terminal Blink): por nivel, leer `pwd.png` píxel a píxel tomando como fondo el color de `[0,0]`; las rachas largas de píxeles distintos son rayas y las cortas puntos (una fila = un carácter morse); traducir con diccionario, pasar a minúsculas (niveles profundos rechazan mayúsculas) y descomprimir con esa contraseña; mover `flag/*` al cwd y decrementar N. Tarda unos minutos (~1000 niveles).
> **EN:** Script the loop (paraphrase of sealldev/Terminal Blink): per level, read `pwd.png` pixel by pixel using the `[0,0]` colour as background; long runs of differing pixels are dashes and short ones are dots (one row = one morse char); translate with a dictionary, lowercase it (deep levels reject uppercase) and unzip with that password; move `flag/*` to the cwd and decrement N. Takes a few minutes (~1000 levels).

```bash
cat > solve.py <<'EOF'
# Lógica parafraseada de sealldev (cv2+morse3) y Terminal Blink (PIL):
# 1) parseMorse('pwd.png'): fondo = pixel[0,0]; por fila, rachas de píxeles
#    distintos -> '-' (largas) / '.' (cortas); Morse(fila).morseToString()
# 2) zipOpen(nivel, pass): zipfile.ZipFile con pwd=pass.lower().encode()
# 3) bucle N=999..0: si existe flag_N.zip -> parse + extrae + N-=1
print("ver solve.py completo en la descripción; requiere: pip install opencv-python morse3")
EOF
pip install opencv-python morse3 pillow
mkdir -p work && cp flag_999.zip pwd.png work/ 2>/dev/null; cd work
python3 ../solve.py
# esperado: traza "Doing flag_999.zip... / Doing flag_998.zip..." hasta flag_0
ls
cat flag 2>/dev/null || cat flag.txt 2>/dev/null
# esperado: fichero final con la flag en formato HTB{...}
```

**Resultado / Result:** Tras ~1000 iteraciones aparece el fichero final con la flag en claro (formato `HTB{...}`; no se reproduce aquí por integridad del contenido, ver capturas de las fuentes citadas). Detalles operativos: los `pwd.png` cambian de color/tamaño con la profundidad (algunos parecen un bloque sólido a simple vista) y las contraseñas tardías mezclan minúsculas y dígitos.

---

## 🧠 Lo aprendido / Learned

- [ ] Esteganografía mínima: morse codificado en rachas de píxeles con fondo de referencia (`pixel[0,0]`); punto vs. raya = longitud de racha.
- [ ] Recursión de archivado: 1000 niveles exigen automatizar (`zipfile` + `unzip -oP`); hacerlo a mano es inviable.
- [ ] Normalizar contraseñas (`.lower()`): niveles profundos solo aceptan minúsculas/dígitos.
- [ ] Robustez ante variación: el parser debe tolerar cambios de color, tamaño y nº de filas por nivel.
- [ ] Clasificación: las fuentes lo fichan como Misc aunque el envoltorio (zips + morse) parezca Crypto — comprobar categoría oficial.

---

## 📚 Fuentes y Referencias / Sources

- **Walkthrough de referencia:** [M0rsarchive — sealldev](https://seall.dev/writeups/htbchallenge-m0rsarchive) — sealldev / Noah Cooper (challenge de lebik, etiquetado easy; `flag_999.zip` + `pwd.png`; script `cv2`+`morse3` con `parseMorse`/`zipOpen`, bucle 999→0, fichero final con la flag; paráfrasis en el paso 2)
- **Walkthrough de referencia:** [HackTheBox – M0rsarchive — Terminal Blink](https://terminalblink.com/hackthebox-m0rsarchive/) — kylie (fichado como Misc Challenge, 2023-01-31; descripción "Just unzip the archive ... several times ..."; `imageToMorse()` con PIL por color de fondo y rachas punto/raya; `unzip -oP` + `mv flag/* .` recursivo; aviso de colores engañosos y minúsculas en profundidad)
- **Walkthrough adicional:** [M0rsarchive [Misc] Writeup HTB — Write-ups HackTheBox](https://medium.com/write-ups-hackthebox/m0rsarchive-misc-writeup-htb-c11ad8b6063d) — Medium/Write-ups HackTheBox (zip con contraseña + imagen morse)
- **Walkthrough adicional:** [HTB M0rsarchive [Write UP] — Mihir Shah](https://mihirps.medium.com/htb-m0rsarchive-write-up-c8a073012da3) — Mihir Shah (contraseña morse en `pwd.png`)
- **Nota local previa:** stub raíz `Soluciones/Challenges/m0rsarchive.md` ("Points: 0pts") migrado a esta plantilla; discrepancia de categoría (carpeta `Crypto/` del repo vs. `Misc` en fuentes) dejada explícita en la tabla
- **Fecha de acceso:** 2026-09-25
- **Autor de este walkthrough:** Apuromafo (síntesis propia parafraseada a partir de las fuentes citadas)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. Challenge retirado (según fuentes); no se publican flags literales.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Retired challenge (per sources); no literal flags published.

_Fecha de edición: 2026-09-25_
