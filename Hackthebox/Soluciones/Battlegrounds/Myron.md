# Myron

> **ES:** Arena Battlegrounds de HackTheBox. Pista original conservada como cita + paráfrasis ES/EN.
> **EN:** HackTheBox Battlegrounds arena. Original hint kept as quote + ES/EN paraphrase.

## 📝 Nota original / Original note

> [ZH] "mongo-express框架 默认凭据 admin:pass"
> **ES:** Panel mongo-express con credenciales por defecto `admin:pass`.
> **EN:** mongo-express panel with default credentials `admin:pass`.

## 🎯 Objetivo / Objective

> **ES:** Acceso inicial vía credenciales por defecto de mongo-express, luego escalar a user y root.
> **EN:** Initial access via mongo-express default credentials, then escalate to user and root.

## 🛠️ Herramientas / Tools

- `nmap`
- Navegador / Browser (mongo-express web UI)
- `mongo` / `mongosh`

## 📝 Pasos / Steps

### 1. Reconocimiento / Recon

```bash
nmap -sC -sV <IP>
```

**Resultado / Result:** Localizar el puerto del panel mongo-express.

### 2. Acceso inicial / Foothold

> **ES:** Probar `admin:pass` en el login de mongo-express.
> **EN:** Try `admin:pass` at the mongo-express login.

**Resultado / Result:** Acceso al panel → ejecución / exfiltración según versión — pendiente de detallar.

### 3. Usuario y Root / User & Root — pendiente de documentar / pending documentation

## 📚 Fuentes / Sources

- Nota previa local (cita ZH + paráfrasis, esta misma ficha)
- HTB Battlegrounds: Myron — fecha de acceso: 2026-09-24
- Autor notas: Apuromafo

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de contenido activo.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish active content flags.

_Fecha de edición: 2026-09-24_
