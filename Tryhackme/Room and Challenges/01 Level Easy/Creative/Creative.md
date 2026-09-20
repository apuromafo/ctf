# Creative

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | CTF / Linux challenge | `creative` | https://tryhackme.com/room/creative | 01 Level Easy | TryHackMe | Reconocimiento web / subdomain enumeration / SSRF / servicios internos / disclosure de ficheros / SSH / escalada de privilegios | Explotar una aplicación web vulnerable y una serie de misconfiguraciones para obtener acceso como usuario y escalar a root, encadenando SSRF y divulgación de ficheros. |

---

**Contexto:** Sala challenge de nivel fácil sobre Linux donde varias vulnerabilidades de impacto aparentemente bajo se encadenan hasta comprometer totalmente la máquina: enumeración de subdominios, explotación de un SSRF en la aplicación web, acceso a un servicio interno, divulgación de credenciales (ficheros sensibles como la clave SSH) y una escalada de privilegios final hasta root.

> **ES:** "Comienza con enumeración web y descubrimiento de subdominios, explota un SSRF para alcanzar servicios internos, recupera las credenciales SSH y escala privilegios hasta root."
> **EN:** "Exploit a vulnerable web application and some misconfigurations to gain root privileges."

## Solucionario

### Task 1: Obtén la bandera de usuario y root / Get user and root flags

**Explicación:** El reto se resuelve encadenando varios pasos: descubrir subdominios de la aplicación, explotar el SSRF de la web para alcanzar un servicio interno que no debería estar expuesto, leer ficheros sensibles (como la clave privada SSH) y usarla para conectarse como usuario. Finalmente se enumera el sistema y se encuentra el vector de escalada a root, capturando las dos banderas.

```bash
# 1) Enumeración web y de subdominios
nmap -sV -sC <IP>
ffuf -u http://<IP> -H "Host: FUZZ.<dominio>" -w subdomain_wordlist.txt
# 2) Explotar el SSRF para alcanzar el servicio interno y leer ficheros
# 3) Recuperar la clave privada SSH y conectarse
ssh -i id_rsa saul@<IP>
# 4) Escalar a root y leer la bandera
sudo -l
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la bandera de usuario? / What is the user flag? | `9a1ce90a7653d74ab98630b47b8b4a84` |
| 2 | ¿Cuál es la bandera de root? / What is the root flag? | `992bfd94b90da48634aed182aae7b99f` |

---

| # | Task | Pregunta | Respuesta |
|---|------|----------|-----------|
| 1 | Task 1 | ¿Cuál es la bandera de usuario? / What is the user flag? | `9a1ce90a7653d74ab98630b47b8b4a84` |
| 2 | Task 1 | ¿Cuál es la bandera de root? / What is the root flag? | `992bfd94b90da48634aed182aae7b99f` |

---

**Metodología:** Nmap -> fuzzing de subdominios (ffuf/vhosts) -> análisis de la web -> explotación del SSRF para alcanzar el servicio interno -> divulgación de ficheros sensibles/clave SSH -> acceso como usuario -> enumeración local -> escalada de privilegios -> lectura de banderas.

### Cadena de ataque / Attack Chain

```text
nmap -> vhost fuzzing -> subdominio encontrado -> SSRF -> servicio interno -> file disclosure -> id_rsa -> ssh usuario -> sudo -l -> privesc -> root flag
```

**Learning chain:** nmap -> ffuf (subdomain/vhost) -> SSRF -> internal service -> key disclosure -> SSH -> privesc -> root.

**Lección:** *Un SSRF bien explotado convierte una web aparentemente inofensiva en una puerta a servicios internos y, combinado con la divulgación de ficheros, puede entregar el acceso completo al sistema.*

**MITRE ATT&CK:** T1595 (Active Scanning), T1190 (Exploit Public-Facing Application / SSRF), T1005 (Data from Local System), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Creative](https://tryhackme.com/room/creative)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.