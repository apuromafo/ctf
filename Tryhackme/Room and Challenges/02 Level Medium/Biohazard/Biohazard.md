# Biohazard
| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `biohazard` |
| **Link** | [TryHackMe](https://tryhackme.com/room/biohazard) |
| **Sección** | 02 Level Medium |
| **Fuente** | TryHackMe |
| **Componentes** | Nmap, enumeración web, FTP, base64, base32, base58, ROT13, Vigenère, binario, hex, esteganografía, GPG, SSH, sudo, salas ocultas de una web temática de Resident Evil |
| **Impacto** | Resuelve un CTF puzle tipo survival horror de Resident Evil: recoger 6 objetos (flags), descifrar multiples capas de criptografía, entrar por FTP y SSH, y escalar hasta root. |
---
**Contexto:** CTF en el que la víctima es una web-mansión temática de Resident Evil (STARS). El flujo es: reconocimiento (3 puertos y el equipo en operación STARS alpha team), paseo por la mansión recogiendo objetos con sus flags, decodificación de mensajes (base64/base32/ROT13/Vigenère), pista de Barry hacia el armario oculto, descifrado de un archivo GPG, acceso SSH (umbrella_guest), descifrado de un disco (Vigenère), y escalada a root vía sudo.
## Solucionario
### Task 1: Introduction
**Explicación:** Escaneo inicial de la máquina: hay **3 puertos abiertos** (web, FTP y SSH). En el footer de la página principal se revela el nombre del equipo en operación: **STARS alpha team**.
```bash
nmap -sV <ip>
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Despliega la máquina y comienza la pesadilla. | `No answer needed` |
| 2 | ¿Cuántos puertos abiertos hay? | `3` |
| 3 | ¿Cuál es el nombre del equipo en operación? | `STARS alpha team` |
### Task 2: The Mansion (item flags)
**Explicación:** La mansión MansionMap.html enumera las salas (`/diningRoom/`, `/teaRoom/`, `/artRoom/`, `/barRoom/`, `/diningRoom2F/`, `/tigerStatusRoom/`, `/galleryRoom/`, `/studyRoom/`, `/armorRoom/`, `/attic/`). En cada sala se encuentra un objeto con su flag (formato `item{32 chars}`):
- Comedor: `/diningRoom/emblem.php` → flag del emblema.
- Sala del té: `master_of_unlock.html` → flag de la ganzúa (lock pick).
- Bar (URL con hash): `musicNote.html` decodifica en base32 → partitura; `gold_emblem.php` → emblema dorado.
- Comedor 2F: pista ROT13 → `diningRoom/sapphire.html` → joya azul.
- Combine las pistas de los emblemas para llegar al `shield_key` (clave de escudo) en `diningRoom/the_great_shield_key.html`.

En el FTP los mensajes codificados revelan las credenciales FTP:
```bash
echo 'RlRQIHVzZXI6IGh1bnRlciwgRlRQIHBhc3M6IHlvdV9jYW50X2hpZGVfZm9yZXZlcg==' | base64 -d
# FTP user: hunter, FTP pass: you_cant_hide_forever
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag del emblema? | `emblem{fec832623ea498e20bf4fe1821d58727}` |
| 2 | ¿Cuál es la flag de la ganzúa? | `lock_pick{037b35e2ff90916a9abf99129c8e1837}` |
| 3 | ¿Cuál es la flag de la partitura? | `music_sheet{362d72deaf65f5bdc63daece6a1f676e}` |
| 4 | ¿Cuál es la flag del emblema dorado? | `gold_emblem{58a8c41a9d08b8a4e38d02a4d7ff4843}` |
| 5 | ¿Cuál es la flag de la llave de escudo? | `shield_key{48a7a9227cd7eb89f0a062590798cbac}` |
| 6 | ¿Cuál es la flag de la joya azul? | `blue_jewel{e1d457e96cac640f863ec7bc475d48aa}` |
| 7 | ¿Cuál es el usuario FTP? | `hunter` |
| 8 | ¿Cuál es la contraseña FTP? | `you_cant_hide_forever` |
### Task 3: The hidden closet
**Explicación:** La nota de Barry en el FTP indica el directorio oculto (`/hidden_closet/`). Dentro se encuentra un archivo cifrado, cuya contraseña es **plant42_can_be_destroy_with_vjolt** (pista del juego). Al descifrarlo se obtiene la contraseña para la sala donde está la llave-casco y con ello la flag `helmet_key`.
```bash
gpg -d <archivo>.gpg
# contraseña: plant42_can_be_destroy_with_vjolt
cat /hidden_closet/helmet_key.txt
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué directorio oculto menciona Barry? | `/hidden_closet/` |
| 2 | ¿Cuál es la contraseña del archivo cifrado? | `plant42_can_be_destroy_with_vjolt` |
| 3 | ¿Cuál es la flag de la llave-casco? | `helmet_key{458493193501d2b94bbab2e727f8db4b}` |
### Task 4: SSH (umbrella_guest)
**Explicación:** Extrayendo datos de la mansión (archivos y esteganografía) se obtienen las credenciales SSH: usuario **umbrella_guest** y contraseña **T_virus_rules**. El lider del equipo STARS Bravo es **Enrico**.
```bash
ssh umbrella_guest@<ip>
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el usuario de acceso SSH? | `umbrella_guest` |
| 2 | ¿Cuál es la contraseña de acceso SSH? | `T_virus_rules` |
| 3 | ¿Quién es el líder del equipo STARS Bravo? | `Enrico` |
### Task 5: Final (privilege escalation / root)
**Explicación:** Dentro de la máquina, el camino final lleva a una celda de la mansión (**jailcell**). Descifrando el disco `MO_DISK1` (cifrado Vigenère con la clave `rebecca`) se obtienen las credenciales de **weasker**: `weasker:stars_members_are_my_guinea_pig`. Con **sudo** ese usuario puede ejecutar todo (`sudo su`) obteniendo root y la flag final. El jefe/enemigo final del juego es **Tyrant**.
```bash
su weasker
# contraseña: stars_members_are_my_guinea_pig
sudo -l   # (ALL : ALL) ALL
sudo su
cat /root/flag.txt
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el nombre de la sala/celda en la que se desarrolla la siguiente fase? | `jailcell` |
| 2 | ¿Qué usuario se obtiene al descifrar MO_DISK1? | `weasker` |
| 3 | ¿Cuál es la contraseña de ese usuario? | `stars_members_are_my_guinea_pig` |
| 4 | ¿Cuál es el nombre del jefe/enemigo final? | `Tyrant` |
| 5 | ¿Cuál es la flag de root? | `3c5794a00dc56c35f2bf096571edf3bf` |
---
**Metodología:** CTF tipo puzle: reconocimiento → enumeración web/FTP → criptografía multicapa → descifrado de archivos → SSH → escalada de privilegios.
**Learning chain:** escaneo → enumeración de la "mansión" (web poking) → base64/base32/ROT13/Vigenère → FTP/gpg → acceso SSH → Vigenère/esteganografía para credenciales → sudo → root flag.
**MITRE ATT&CK:** T1595 (Active Scanning), T1083 (File and Directory Discovery), T1552.001 (Credentials In Files), T1078 (Valid Accounts), T1548.003 (Sudo).
**Fuente:** [TryHackMe - Biohazard](https://tryhackme.com/room/biohazard)