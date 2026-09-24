# Defy

> **ES:** Arena Battlegrounds de HackTheBox. Servicio web BigTree CMS 4.4.10 con RCE público.
> **EN:** HackTheBox Battlegrounds arena. BigTree CMS 4.4.10 web service with public RCE.

## Web Service Port 8000

```plaintext
BigTree 4.4.10
```

## 🎯 Objetivo / Objective

> **ES:** Explotar el RCE de BigTree CMS 4.4.10 para acceso inicial, luego escalar a user y root.
> **EN:** Exploit BigTree CMS 4.4.10 RCE for initial access, then escalate to user and root.

## 🛠️ Herramientas / Tools

- `nmap`
- Exploit público (ver Fuentes / see Sources)

## 📝 Pasos / Steps

### 1. Reconocimiento / Recon

```bash
nmap -sC -sV <IP>
```

**Resultado / Result:** Puerto 8000 con BigTree 4.4.10.

### 2. Acceso inicial / Foothold

> **ES:** Usar el exploit público de Exploit-DB (abajo en Fuentes).
> **EN:** Use the public Exploit-DB exploit (below in Sources).

**Resultado / Result:** Shell inicial — pendiente de detallar comandos exactos.

### 3. Usuario y Root / User & Root — pendiente de documentar / pending documentation

## 📚 Fuentes / Sources

- [BigTree CMS 4.4.10 - Remote Code Execution](https://www.exploit-db.com/exploits/48831) — Exploit-DB — fecha de acceso: 2026-09-24
- HTB Battlegrounds: Defy — fecha de acceso: 2026-09-24
- Autor notas: Apuromafo

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de contenido activo.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish active content flags.

_Fecha de edición: 2026-09-24_
