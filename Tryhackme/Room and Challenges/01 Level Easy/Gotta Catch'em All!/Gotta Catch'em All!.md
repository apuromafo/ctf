# Gotta Catch'em All!

| **Dificultad** | Easy |
| **Tipo** | CTF |
| **Slug** | `pokemon` |
| **Link** | [TryHackMe](https://tryhackme.com/room/pokemon) |
| **Sección** | 01 Level Easy |
| **Fuente** | Writeup de Hassan Sheikh (InfoSec Write-ups) + 0xnirvana (GitBook) + AfvanMoopen (GitHub) |
| **Componentes** | nmap / SSH / Apache / hex / ROT13 / base64 / find / escalada horizontal |
| **Impacto** | Encuentra todos los pokemon (flags) escondidos en la máquina usando enumeración web, criptografía (hex, ROT, base64) y escalada de privilegios. |

---

**Contexto:** Room basada en la serie original de Pokemon. El objetivo es encontrar todos los pokemons (flags) escondidos en la máquina, usando enumeración web, criptografía (hex, ROT, base64) y escalada de privilegios.

## Solucionario

### Task 1: Find the Grass-Type Pokemon

**Explicación:** Conectados por SSH como `pokemon:hack_the_pokemon`, en el Desktop hay `P0kEmOn.zip`. Descomprimir y leer el archivo de tipo planta:

```
unzip P0kEmOn.zip
cat P0kEmOn/grass-type.txt
# 50 6f 4b 65 4d 6f 4e 7b 42 75 6c 62 61 73 61 75 72 7d
```

Es **hex**; decodificar con CyberChef → `PoKeMoN{Bulbasaur}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Find the Grass-Type Pokemon | `PoKeMoN{Bulbasaur}` |

### Task 2: Find the Water-Type Pokemon

**Explicación:** Buscar archivos de agua:

```
find / -name water* 2>/dev/null
cat /var/www/html/water-type.txt
# Ecgudfxq_EcGmP{Ecgudfxq}
```

Es **ROT13 con rotación 14**. Decodificar → `Squirtle_SqUaD{Squirtle}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Find the Water-Type Pokemon | `Squirtle_SqUaD{Squirtle}` |

### Task 3: Find the Fire-Type Pokemon

**Explicación:** Buscar archivos de fuego (filtrando firefox/firewall):

```
find / -name '*fire-type*' -type f 2>/dev/null | grep -ivE "(firefox|firewall)"
cat /etc/why_am_i_here?/fire-type.txt
# UDBrM20wbntDaGFybWFuZGVyfQ==
```

Es **base64**. Decodificar:

```
echo 'UDBrM20wbntDaGFybWFuZGVyfQ==' | base64 -d
# P0k3m0n{Charmander}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Find the Fire-Type Pokemon | `P0k3m0n{Charmander}` |

### Task 4: Who is Root's Favorite Pokemon?

**Explicación:** En `/home` hay `roots-pokemon.txt` accesible solo por root. `sudo -l` no permite sudo. Enumerando: en `~/Videos/Gotta/Catch/Them/ALL!/` hay `Could_this_be_what_Im_looking_for?.cplusplus`; `strings` revela las credenciales de otro usuario:

```
strings Could_this_be_what_Im_looking_for?.cplusplus
# # include <iostream>
# int main() {
#         std::cout << "ash : pikapika"
```

Escalada horizontal: `su ash` (credenciales `ash:pikapika`) → `cat /home/roots-pokemon.txt` → `Pikachu!`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Who is Root's Favorite Pokemon? | `Pikachu!` |

---

**Metodología:**
1. **Recon:** `nmap -sC -sV -p-` revela SSH (22, OpenSSH 7.2p2) y Apache (80); el título de la web es "Can You Find Them All?".
2. **Web:** en el código fuente de la página hay un comentario y credenciales (`<pokemon>:<hack_the_pokemon>`), además del aviso "(Check console for extra surprise!)"; en la consola del navegador hay un array con los pokemons: Bulbasaur, Charmander, Squirtle, Snorlax, Zapdos, Mew, Charizard, Grimer, Metapod, Magikarp.
3. **Foothold:** SSH con las credenciales `pokemon:hack_the_pokemon`.
4. **Grass (hex):** en el Desktop hay `P0kEmOn.zip`; descomprimir (`unzip P0kEmOn.zip`) y leer `P0kEmOn/grass-type.txt`, que contiene `50 6f 4b 65 4d 6f 4e 7b 42 75 6c 62 61 73 61 75 72 7d` — hex que decodifica a `PoKeMoN{Bulbasaur}`.
5. **Water (ROT14):** `find / -name water* 2>/dev/null` → `/var/www/html/water-type.txt` con `Ecgudfxq_EcGmP{Ecgudfxq}`, ROT13 con rotación 14 → `Squirtle_SqUaD{Squirtle}`.
6. **Fire (base64):** `find / -name '*fire-type*' -type f` (filtrando firefox/firewall) → `/etc/why_am_i_here?/fire-type.txt` con `UDBrM20wbntDaGFybWFuZGVyfQ==`, base64 → `P0k3m0n{Charmander}`.
7. **Privesc:** `sudo -l` no permite sudo; enumerando `~/Videos/Gotta/Catch/Them/ALL!/` aparece `Could_this_be_what_Im_looking_for?.cplusplus`; `strings` revela `ash : pikapika`; `su ash` (escalada horizontal) permite leer `/home/roots-pokemon.txt` → `Pikachu!`.

**Learning chain:** nmap (22, 80) → código fuente (pokemon:hack_the_pokemon + consola array) → SSH → P0kEmOn.zip → hex → PoKeMoN{Bulbasaur} → find water* → ROT14 → Squirtle_SqUaD{Squirtle} → find fire-type → base64 → P0k3m0n{Charmander} → .cplusplus strings → ash:pikapika → su ash → roots-pokemon.txt → Pikachu!.

**Lección:** enumerar siempre (find), revisar carpetas inusuales, y si la escalada vertical no es posible, probar escalada horizontal.

**MITRE ATT&CK:** T1078.001 (Valid Accounts: Default Accounts), T1005 (Data from Local System), T1021.004 (Remote Services: SSH), T1078 (Valid Accounts).

**Fuente:** [TryHackMe - Gotta Catch'em All!](https://tryhackme.com/room/pokemon)