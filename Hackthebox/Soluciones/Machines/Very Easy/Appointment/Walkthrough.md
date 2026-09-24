# Appointment [VERY EASY]

> **ES:** Máquina Very Easy de HackTheBox. La solución vive en esta misma carpeta en varias opciones (ver abajo).
> **EN:** HackTheBox Very Easy machine. The solution lives in this same folder in several options (see below).

| Campo | Valor |
|-------|-------|
| **Dificultad / Difficulty** | Very Easy |
| **OS** | Linux (verificar en `app.hackthebox.com/machines/Appointment`) |
| **Estado / Status** | Retired |
| **URL** | https://app.hackthebox.com/machines/Appointment |
| **Fecha / Date** | 2026-09-24 |

## 📂 Opciones de solución en esta carpeta / Solution options in this folder

> **ES:** Si hay más de una solución, se muestran todas como opciones. Elige la que prefieras.
> **EN:** When more than one solution exists, all are shown as options. Pick whichever you prefer.

| # | Opción / Option | Archivo / File |
|---|-----------------|----------------|
| 1 | Write-up PDF (principal / main) | `htb_Appointment.pdf` |
| 2 | Write-up PDF (copia en subcarpeta / copy in subfolder) | `Writeup/Appointment Write-up.pdf` |
| 3 | Enlace oficial / Official link | `Readme.md` |

## 🎯 Objetivo / Objective

> **ES:** Obtener `user.txt` y `root.txt` siguiendo los pasos de los write-ups adjuntos.
> **EN:** Obtain `user.txt` and `root.txt` following the steps in the attached write-ups.

## 🛠️ Herramientas / Tools

- `nmap`, `gobuster` / `feroxbuster`
- `Burp Suite`
- Navegador / Browser

## 📝 Pasos / Steps

### 1. Reconocimiento / Recon

```bash
nmap -sC -sV <IP>
```

**Resultado / Result:** Ver detalle en `htb_Appointment.pdf` (opción 1).

### 2. Acceso inicial / Foothold

**Resultado / Result:** Ver detalle en `htb_Appointment.pdf` (opción 1).

### 3. Usuario / User

**Resultado / Result:** `user.txt` — ver detalle en `htb_Appointment.pdf` (opción 1).

### 4. Root

**Resultado / Result:** `root.txt` — ver detalle en `htb_Appointment.pdf` (opción 1).

## 📚 Fuentes / Sources

- Write-up local (opción 1): `htb_Appointment.pdf` — esta carpeta
- Write-up local (opción 2): `Writeup/Appointment Write-up.pdf` — esta carpeta
- HTB oficial: https://app.hackthebox.com/machines/Appointment — fecha de acceso: 2026-09-24
- Autor notas: Apuromafo

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de contenido activo.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish active content flags.

_Fecha de edición: 2026-09-24_
