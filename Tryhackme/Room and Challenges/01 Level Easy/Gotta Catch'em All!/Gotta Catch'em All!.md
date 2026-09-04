# Gotta Catch'em All! [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** CTF (Free)
* **Slug:** `pokemon`
* **Link:** https://tryhackme.com/room/pokemon
* **Sección / Section:** CTF / Máquinas
* **Fuente / Source:** Writeup de Hassan Sheikh (InfoSec Write-ups) + 0xnirvana (GitBook) + AfvanMoopen (GitHub)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Room basada en la serie original de Pokemon. El objetivo es encontrar todos los pokemons (flags) escondidos en la máquina, usando enumeración web, criptografía (hex, ROT, base64) y escalada de privilegios.
> **EN:** Room based on the original Pokemon series. The goal is to find all the pokemons (flags) hidden on the machine, using web enumeration, cryptography (hex, ROT, base64) and privilege escalation.

---

### Escaneo / Scanning

```
nmap -sC -sV -p- -oN nmap/pokemon MACHINE_IP
```

```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Can You Find Them All?
```

---

### Enumeración web / Web Enumeration

En la página web (Apache por defecto), en el código fuente hay un comentario y credenciales:

```html
<pokemon>:<hack_the_pokemon>
  <!--(Check console for extra surprise!)-->
</pokemon>
```

En la consola del navegador hay un array con pokemons: Bulbasaur, Charmander, Squirtle, Snorlax, Zapdos, Mew, Charizard, Grimer, Metapod, Magikarp.

Las credenciales son `pokemon:hack_the_pokemon`. Conectarse por SSH:

```
ssh pokemon@MACHINE_IP
```

---

### 1. Find the Grass-Type Pokemon

En el Desktop hay un archivo `P0kEmOn.zip`. Descomprimirlo:

```
unzip P0kEmOn.zip
cat P0kEmOn/grass-type.txt
```

```
50 6f 4b 65 4d 6f 4e 7b 42 75 6c 62 61 73 61 75 72 7d
```

Es hex. Decodificar (CyberChef):

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Find the Grass-Type Pokemon | `PoKeMoN{Bulbasaur}` |

---

### 2. Find the Water-Type Pokemon

Buscar archivos de agua:

```
find / -name water* 2>/dev/null
cat /var/www/html/water-type.txt
```

```
Ecgudfxq_EcGmP{Ecgudfxq}
```

Es ROT13 con rotación 14. Decodificar:

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Find the Water-Type Pokemon | `Squirtle_SqUaD{Squirtle}` |

---

### 3. Find the Fire-Type Pokemon

Buscar archivos de fuego:

```
find / -name '*fire-type*' -type f 2>/dev/null | grep -ivE "(firefox|firewall)"
cat /etc/why_am_i_here?/fire-type.txt
```

```
UDBrM20wbntDaGFybWFuZGVyfQ==
```

Es base64. Decodificar:

```
echo 'UDBrM20wbntDaGFybWFuZGVyfQ==' | base64 -d
```

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Find the Fire-Type Pokemon | `P0k3m0n{Charmander}` |

---

### 4. Who is Root's Favorite Pokemon?

En `/home` hay un archivo `roots-pokemon.txt` accesible solo por root. `sudo -l` no permite sudo. Enumerar carpetas: en `~/Videos/Gotta/Catch/Them/ALL!/` hay un archivo `Could_this_be_what_Im_looking_for?.cplusplus`:

```
strings Could_this_be_what_Im_looking_for?.cplusplus
```

```
# include <iostream>
int main() {
        std::cout << "ash : pikapika"
        return 0;
```

Credenciales `ash:pikapika`. Cambiar de usuario (escalada horizontal):

```
su ash
cat /home/roots-pokemon.txt
```

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Who is Root's Favorite Pokemon? | `Pikachu!` |

---

## Metodología / Methodology

1. **Recon:** nmap revela SSH (22) y Apache (80).
2. **Web:** credenciales en el código fuente (`pokemon:hack_the_pokemon`) y array de pokemons en la consola.
3. **Foothold:** SSH con las credenciales.
4. **Flags:** hex (Bulbasaur), ROT14 (Squirtle), base64 (Charmander) en archivos del sistema.
5. **Privesc:** escalada horizontal a `ash` con credenciales encontradas en un archivo `.cplusplus` → `Pikachu!`.

**Lección:** enumerar siempre (find), revisar carpetas inusuales, y si la escalada vertical no es posible, probar escalada horizontal.

---

*Documentación para propósitos educativos y registro de CTF.*
