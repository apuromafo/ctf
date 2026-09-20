# One Piece

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF | ctfonepiece65 | https://tryhackme.com/room/ctfonepiece65 | 02 Level Medium | TryHackMe | Web enumeration, navegación/servidores de la app (Apache Sea), "enigmas" y puzles, credenciales y resolución de laberintos | Un reto tipo juego/puzle con temática de One Piece: resolver los "enigmas" que esconden las pistas, navegar por las rutas de la maqueta web y descubrir el One Piece final. |

---

**Contexto:** La sala **One Piece** es un reto CTF tipo "juego y puzle" ambientado en el anime/manga One Piece. El objetivo del reto es encontrar el One Piece y convertirse en el Rey de los Piratas. La mecánica es especial: **no hay exploits complejos** (las habilidades necesarias son básicas), pero **resolver los "enigmas"** para saber qué hacer es la parte complicada, y el autor advierte de que es fácil caer en conejeras (rabbit holes). Se navega por rutas temáticas (el "Apache Sea") siguiendo pistas de la historia, hasta llegar a Laugh Tale. La sala está pensada para quienes hayan seguido la serie (spoilers a partir del arco de Zou).

> **ES:** Un juego-puzle CTF donde no importan los exploits sino resolver los enigmas: navegar el "Apache Sea", descifrar los Road Poneglyphs y llegar a Laugh Tale para encontrar el One Piece.
> **EN:** A CTF game-puzzle where the challenge is solving the enigmas, not running exploits: sail the "Apache Sea", decode the Road Poneglyphs, and reach Laugh Tale to find the One Piece.

> **Introducción original / Original room introduction:**
> Welcome to the One Piece room.
> Your dream is to find the One Piece and hence to become the Pirate King.
> Once the VM is deployed, you will be able to enter a World full of Pirates.
> Please notice that pirates do not play fair. They can create rabbit holes to trap you.
> This room may be a bit different to what you are used to:
>     - Required skills to perform the intended exploits are pretty basic.
>     - However, solving the (let's say) "enigmas" to know what you need to do may be trickier.
> This room is some sort of game, some sort of puzzle.
> Please note that if you are currently reading/watching One Piece and if you did not finish Zou arc, you will get spoiled during this room.

## Solucionario

### Task 1: Set Sail / Set Sail
**Explicación:** Tarea de presentación del reto y de la advertencia de la sala: los piratas no juegan limpio y pueden crear conejeras (rabbit holes). No requiere respuesta: solo confirmar que se ha leído la introducción y que se está preparado para zarpar.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Confirm you are ready to set sail (no answer required). / Confirma que estás listo para zarpar. | `No answer needed` |

### Task 2: Road Poneglyphs / Road Poneglyphs
**Explicación:** El jugador debe explorar la web para localizar las pistas y responder preguntas del lore de One Piece. El camino por el "Apache Sea" sigue el orden de la historia: el árbol que guarda el **1er Road Poneglyph** es *The Whale*; el primer pirata al que se encuentra navegando es **Donquixote Doflamingo**; la **2ª isla** es **Whole Cake**; el amigo que encontró es **Buggy the Clown**; el **2º Emperador** es **Kaido of the Beasts**; y el mensaje oculto de los 4 Road Poneglyphs es la credencial codificada `M0nk3y_D_7uffy:1_w1ll_b3_th3_p1r@t3_k1ng!`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the tree that contains the 1st Road Poneglyph? | `The Whale` |
| 2 | What is the name of the 1st pirate you meet navigating the Apache Sea? | `Donquixote Doflamingo` |
| 3 | What is the name of the 2nd island you reach navigating the Apache Sea? | `Whole Cake` |
| 4 | What is the name of the friend you meet navigating the Apache Sea? | `Buggy the Clown` |
| 5 | What is the name of the 2nd Emperor you meet navigating the Apache Sea? | `Kaido of the Beasts` |
| 6 | What is the hidden message of the 4 Road Poneglyphs? | `M0nk3y_D_7uffy:1_w1ll_b3_th3_p1r@t3_k1ng!` |

### Task 3: Laugh Tale / Laugh Tale
**Explicación:** Con las pistas y credenciales recogidas se llega a Laugh Tale, donde se enfrentan los dos piratas y se descubre el One Piece. En Laugh Tale, al mismo tiempo que Luffy, se encuentra **Marshall D Teach**; lo que permitió a Luffy ganar la pelea fue **Willpower** (la voluntad); y el One Piece es `S3cr3ts_0f_tH3_W0rlD_&_0f_Th3_P@st$`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Who is on Laugh Tale at the same time as Luffy? | `Marshall D Teach` |
| 2 | What allowed Luffy to win the fight? | `Willpower` |
| 3 | What is the One Piece? | `S3cr3ts_0f_tH3_W0rlD_&_0f_Th3_P@st$` |

### Tabla unificada de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Task 1) Set Sail - confirmación. | `No answer needed` |
| 2 | (Task 2) What is the name of the tree that contains the 1st Road Poneglyph? | `The Whale` |
| 3 | (Task 2) What is the name of the 1st pirate you meet navigating the Apache Sea? | `Donquixote Doflamingo` |
| 4 | (Task 2) What is the name of the 2nd island you reach navigating the Apache Sea? | `Whole Cake` |
| 5 | (Task 2) What is the name of the friend you meet navigating the Apache Sea? | `Buggy the Clown` |
| 6 | (Task 2) What is the name of the 2nd Emperor you meet navigating the Apache Sea? | `Kaido of the Beasts` |
| 7 | (Task 2) What is the hidden message of the 4 Road Poneglyphs? | `M0nk3y_D_7uffy:1_w1ll_b3_th3_p1r@t3_k1ng!` |
| 8 | (Task 3) Who is on Laugh Tale at the same time as Luffy? | `Marshall D Teach` |
| 9 | (Task 3) What allowed Luffy to win the fight? | `Willpower` |
| 10 | (Task 3) What is the One Piece? | `S3cr3ts_0f_tH3_W0rlD_&_0f_Th3_P@st$` |

---

**Metodología:** Leer atentamente la introducción y sus advertencias → explorar la maquetación web del reto buscando las pistas y rutas del "Apache Sea" → seguir el orden de la historia para responder las preguntas de lore → descifrar el mensaje oculto de los Road Poneglyphs (credencial) → emplear la credencial para alcanzar Laugh Tale → resolver la pregunta final del One Piece en Laugh Tale.

**Learning chain:** lectura del briefing y detección de conejeras → exploración de rutas web (Apache Sea) → correlación con el lore de One Piece → decodificación del mensaje de los Poneglyphs → desenlace en Laugh Tale.

**Lección:** *En un CTF de puzles, la lectura cuidadosa vale más que el exploit: las pistas y credenciales están integradas en la narrativa, y saltarse detalles (o caer en conejeras) es el mayor obstáculo.*

**MITRE ATT&CK:** T1595 (Active Scanning) · T1083 (File and Directory Discovery) · T1078 (Valid Accounts) · T1539 (Steal Web Session Cookie).

**Fuente:** [TryHackMe - One Piece](https://tryhackme.com/room/ctfonepiece65)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.