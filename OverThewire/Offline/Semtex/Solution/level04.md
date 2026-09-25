# Semtex Nivel 4 - 5

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Semtex (offline) |
| **Nivel / Level** | 4 - 5 |
| **URL** | https://overthewire.org/wargames/semtex/ |

Semtex Level 4 → Level 5
Random Networking
Make 10 connections to port 24027 from different IP’s. On each connection you will receive a string of 10 ASCII characters. XOR this string with the Semtex5 password, character by character. Then send back the 10 characters followed by another string of exactly 10 characters which identifies you (can be anything within A-Z, a-z, 0-9). The first 10 characters that you send, are different on every connection, the last 10 have to be the same. If you do not send the correct string back within 5 seconds you are disconnected. Once connected with at least 10 different IP’s You will receive the password on one connection, chosen randomly.

**Note: Your connections time out in 2 minutes and you cannot connect from an IP that is still connected. May the sockets be with you. **

Reading Material
Socks5 Request For Comment

---

## Fuentes / Sources

- OTW: https://overthewire.org/wargames/semtex/ - fecha de acceso: 2026-09-25.
- Autor notas: Apuromafo.

---

## Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a OverTheWire.
> **EN:** Educational and personal use only. Not affiliated with OverTheWire.

_Fecha de edición: 2026-09-25_
