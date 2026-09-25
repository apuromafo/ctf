# oBfsC4t10n2 [HARD]

> **ES:** Challenge Forensics Hard: otro documento de phishing (`invoice.xls` en un zip); hay que averiguar qué ejecuta siguiendo sus celdas, fórmulas y saltos ofuscados hasta extraer la flag (`HTB{...}`). El hilo oficial sugiere tres vías: adivinar, ejecutar o analizar (la última es la más instructiva).
> **EN:** Hard Forensics challenge: another phishing document (`invoice.xls` inside a zip); work out what it executes by following its cells, formulas and obfuscated jumps to extract the flag (`HTB{...}`). The official thread suggests three routes: guess, run, or analyze (the last being the most instructive).

| Campo | Valor |
|-------|-------|
| **Categoría** | Forensics |
| **Dificultad** | Hard |
| **Estado** | Retired |
| **URL** | https://app.hackthebox.com/challenges/oBfsC4t10n2 |
| **Archivos** | Zip descargable con `invoice.xls` (phishing maldoc con fórmulas/celdas ofuscadas) [verificar nombre exacto del zip] |
| **Fecha de resolución** | 2026-09-25 (documentación; resuelto previamente según stub local) |
| **Puntos** | 70 (índice público actual; la nota previa local indicaba 7pts — se corrige aquí) |

---

## 🎯 Objetivo / Goal

> **ES:** Analizar estáticamente el `.xls` (fórmulas Excel 4.0/XLM encadenadas entre celdas + posible PowerShell), desenredar la cadena de desofuscado sin ejecutar el payload y recuperar la flag (`HTB{...}`).
> **EN:** Statically analyze the `.xls` (chained Excel 4.0/XLM formulas across cells + possible PowerShell), untangle the deobfuscation chain without running the payload, and recover the flag (`HTB{...}`).

---

## 🛠️ Herramientas usadas / Tools used

- [ ] `unzip` + `file` (triage del adjunto)
- [ ] `olevba` / `oletools` (extracción de macros y cadenas sospechosas)
- [ ] `strings` + `xxd` (inspección rápida del binario)
- [ ] LibreOffice/Excel con macros **desactivadas** (revisar celdas y fórmulas visibles)
- [ ] CyberChef (decodificados intermedios: base64/hex/concatenaciones)

---

## 📋 Pasos / Steps

### Paso 1 — Triage del `.xls` / `.xls` triage

> **ES:** Se descomprime el zip y se confirma el `invoice.xls`; el aviso del creador ("muchas celdas, fórmulas y saltos") anticipa ofuscación por fórmulas encadenadas, no un único macro monolítico.
> **EN:** Unzip the archive and confirm `invoice.xls`; the author's hint ("lots of cells, formulas, and jumping here and there") points to chained-formula obfuscation rather than a single monolithic macro.

```bash
unzip <archivo>.zip && file *
oletools 2>/dev/null; olevba invoice.xls | head -60
strings invoice.xls | grep -iE "powershell|cmd|http|HTB" | head -20
```

**Resultado / Result:** Documento identificado como phishing maldoc con lógica repartida en fórmulas; `olevba`/`strings` exponen fragmentos del flujo (llamadas, URLs o trozos de PowerShell) sin necesidad de ejecutarlo.

### Paso 2 — Seguir la cadena de fórmulas / Follow the formula chain

> **ES:** Se recorren las celdas/fórmulas (saltos entre hojas y celdas ocultas) reconstruyendo cada capa: concatenaciones → decodificados → comando final (estilo `PowerShell -enc …`). Cada salto se resuelve a mano o con decodificados parciales, sin lanzar el documento.
> **EN:** Walk the cells/formulas (jumps across sheets and hidden cells) rebuilding each layer: concatenations → decodings → final command (e.g. `PowerShell -enc …`). Resolve each hop manually or with partial decodings, never launching the document.

```bash
# Enfoque estático (paráfrasis de las fuentes citadas):
# 1) listar fórmulas visibles/ocultas del .xls
# 2) copiar cada capa a CyberChef (From Base64 / Generic Code Beautify / Find & Replace)
# 3) reensamblar el comando PowerShell final y leer sus argumentos en claro
echo '<capa_base64>' | base64 -d | head -c 500
```

**Resultado / Result:** Cadena de ofuscación desenredada hasta el comando que el documento habría ejecutado; sus argumentos contienen la flag en formato `HTB{...}` (no se reproduce aquí por integridad del contenido; challenge retirado, ver capturas de las fuentes citadas). [verificar] reproducción propia con captura en `img/`.

---

## 🧠 Lo aprendido / Learned

- [ ] Los maldocs Excel 4.0/XLM reparten la lógica en celdas y fórmulas: el análisis es seguir saltos, no leer un solo macro.
- [ ] Tres vías del hilo oficial (adivinar / ejecutar / analizar): la estática enseña más y es segura.
- [ ] `olevba` + `strings` bastan para el triage inicial sin detonar el payload.
- [ ] Capas típicas: concatenación de celdas → base64/hex → `PowerShell -enc`.
- [ ] Regla operativa: abrir el `.xls` siempre con macros desactivadas (o no abrirlo y trabajar sobre extracciones).

---

## 📚 Fuentes y Referencias / Sources

- **Walkthrough de referencia:** [oBfsC4t10n2 — vanniichan/HackTheBox](https://github.com/vanniichan/HackTheBox/blob/main/oBfsC4t10n2/WriteUp.md) — vanniichan (descripción "Another Phishing document", zip con `invoice.xls`, análisis con `olevba`)
- **Walkthrough de referencia:** [Hack The Box — oBfsC4t10n2 Writeup — Jason Lionardi](https://medium.com/@lionardijason/hack-the-box-obfsc4t10n2-writeup-a4e4cf656d99) — Jason Lionardi (zip con `.xls` descrito como documento de phishing)
- **Hilo oficial:** [[Forensics] oBfsC4t10n2 — HTB Forums](https://forum.hackthebox.com/t/forensics-obfsc4t10n2/2597) — Hack The Box :: Forums (pista del autor: "lots of cells, formulas, and jumping"; "you can guess, you can run, or you can analyze"; nota de que versiones iniciales se resolvían subiéndolo a sandboxes públicos)
- **Índice público de challenges:** [foobarto.me/htb/challenges](https://foobarto.me/htb/challenges/) — Bartosz Ptaszyński (`oBfsC4t10n2 · Forensics · Hard · 70 pts`, 2020-04-24)
- **Nota local previa:** stub raíz `Soluciones/Challenges/obfsc4t10n2.md` ("Points: 7pts") migrado a esta plantilla; el valor oficial documentado es 70 pts
- **Fecha de acceso:** 2026-09-25
- **Autor de este walkthrough:** Apuromafo (síntesis propia parafraseada a partir de las fuentes citadas)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. Challenge retirado; no se publican flags literales.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Retired challenge; no literal flags published.

_Fecha de edición: 2026-09-25_
