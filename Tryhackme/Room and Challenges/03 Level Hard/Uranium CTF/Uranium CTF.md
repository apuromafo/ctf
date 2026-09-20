# Uranium CTF

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Reto • CTF | uranium | https://tryhackme.com/room/uranium | 03 Level Hard | TryHackMe | CTF, Criptografía, Ingeniería inversa, Credenciales | Alto |

---

**Contexto:**
> **ES:** Reto CTF de dificultad moderada que combina recuperación de credenciales, descifrado de contenido y análisis de material cifrado, con respuestas en formato de flag hasheado (thm{...}).
> **EN:** Moderate CTF challenge combining credential recovery, content decryption and analysis of encrypted material, with answers in hashed flag format (thm{...}).

## Solucionario

### Task 1: Uranium
**Explicación:**
1. MBMD1vdpjg3kGv6SsIz56VNG
2. Mys3cr3tp4sw0rD
3. thm{2aa50e58fa82244213d5438187c0da7c}
4. thm{804d12e6d16189075db2d45449aeda5f}
5. thm{019d332a6a223a98b955c160b3e6750a}
6. thm{81498047439cc0426bafa1db5da699cd}

### Preguntas y Respuestas / Questions and Answers

| Task | Respuesta / Answer |
|---|---|
| 1.1 | `MBMD1vdpjg3kGv6SsIz56VNG` |
| 1.2 | `Mys3cr3tp4sw0rD` |
| 1.3 | `thm{2aa50e58fa82244213d5438187c0da7c}` |
| 1.4 | `thm{804d12e6d16189075db2d45449aeda5f}` |
| 1.5 | `thm{019d332a6a223a98b955c160b3e6750a}` |
| 1.6 | `thm{81498047439cc0426bafa1db5da699cd}` |

---

**Metodología:**
Análisis del material proporcionado para localizar las primeras piezas (identificador y credenciales), empleo de esas credenciales para acceder al contenido cifrado y recopilación de las flags finales.

### Cadena de ataque / Attack Chain
1. Inspección del material inicial y localización de la primera pieza.
2. Extracción de las credenciales explotables.
3. Uso de las credenciales para acceder al contenido cifrado.
4. Recopilación de las flags completas.

**Learning chain:**
Pieza inicial → Credenciales → Contenido cifrado → Flags.

**Lección:** *En un CTF, cada pieza descubierta (identificador, contraseña, flag intermedia) es la llave para la siguiente prueba.*

**MITRE ATT&CK:**
- No aplica (reto CTF criptográfico — CWE-327).

**Fuente:** [TryHackMe - Uranium CTF](https://tryhackme.com/room/uranium)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.