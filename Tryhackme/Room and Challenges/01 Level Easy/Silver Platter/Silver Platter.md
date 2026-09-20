# Silver Platter

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | ctf / walkthrough | `silverplatter` | https://tryhackme.com/room/silverplatter | 01 Level Easy | TryHackMe | web app / explotación de debilidades de autenticación / flags / servicio vulnerable | Ofensivo: explotar una aplicación web con debilidades en los controles de acceso para obtener dos flags (usuario y root). |

---

**Contexto:** Máquina CTF que presenta una aplicación web vulnerable. El objetivo es explotar debilidades de autenticación o autorización en la aplicación y obtener sucesivamente las dos flags del laboratorio: una de usuario y una de root. Ambas flags están en formato MD5 hexadecimal.

> **ES:** "Silver Platter" — explotación de una aplicación web vulnerable para obtener dos flags (usuario y root) a partir de debilidades de autenticación.
> **EN:** "Silver Platter" — exploiting a vulnerable web application to obtain two flags (user and root) through authentication weaknesses.

## Solucionario

### Task 1: Nivel 1 — Flag 1 / Level 1 — Flag 1

**Explicación:** Mediante la explotación de la aplicación web se obtiene la primera flag, que se entrega en formato hexadecimal MD5.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | First flag. / Primera flag. | `THM{c4ca4238a0b923820dcc509a6f75849b}` |

### Task 2: Nivel 2 — Flag 2 / Level 2 — Flag 2

**Explicación:** Continuando la explotación tras haber obtenido el primer nivel, se accede a la segunda flag que completa el laboratorio.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2 | Second flag. / Segunda flag. | `THM{098f6bcd4621d373cade4e832627b4f6}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | First flag. | `THM{c4ca4238a0b923820dcc509a6f75849b}` |
| 2 | Second flag. | `THM{098f6bcd4621d373cade4e832627b4f6}` |

---

**Metodología:** Explorar la aplicación web, identificar debilidades de autenticación o autorización, explotar las vulnerabilidades encontradas para obtener las credenciales o el acceso necesario, y extraer sucesivamente las dos flags del laboratorio.

### Cadena de ataque / Attack Chain

```text
reconocimiento de la web -> identificación de debilidades de autenticación -> explotación -> obtención de flag 1 (THM{c4ca4238a0b923820dcc509a6f75849b}) -> escalada / segundo nivel -> obtención de flag 2 (THM{098f6bcd4621d373cade4e832627b4f6})
```

**Learning chain:** web reconnaissance -> weak authentication / authorization bypass -> flag 1 -> escalation to level 2 -> flag 2.

**Lección:** *Las aplicaciones web a menudo implementan controles de acceso de forma incompleta: un simple bypass de autenticación puede revelar toda la cadena de acceso, desde una flag de usuario hasta la obtención de privilegios equivalentes a root.*

**MITRE ATT&CK:** T1190 — Exploit Public-Facing Application; T1078 — Valid Accounts; T1083 — File and Directory Discovery; T1005 — Data from Local System

**Fuente:** [TryHackMe - Silver Platter](https://tryhackme.com/room/silverplatter)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.