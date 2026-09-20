# Year of the Pig

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Reto • CTF | yearofthepig | https://tryhackme.com/room/yearofthepig | 03 Level Hard | TryHackMe | CTF, Codificación, Criptografía | Medio |

---

**Contexto:**
> **ES:** Reto de la serie Year of the ... : resolviendo el enigma se obtiene la pieza del año, un fragmento en Base64 que codifica la flag correspondiente al Cerdo.
> **EN:** Challenge from the Year of the ... series: solving the riddle yields the piece of the year, a Base64 fragment encoding the flag corresponding to the Pig.

## Solucionario

### Task 1: La pieza del año / The piece of the year
**Explicación:**
1. THM{MDg0MGVjYzFjY2ZkZGMzMWY1NGZiNjhl}
2. THM{Y2Q2N2M1NzNmYTQzYTI4ODliYzkzMmZh}
3. THM{MjcxNmVmYjNhYzdkZDc0M2RkNTZhNDA0}

### Preguntas y Respuestas / Questions and Answers

| Task | Respuesta / Answer |
|---|---|
| 1.1 | `THM{MDg0MGVjYzFjY2ZkZGMzMWY1NGZiNjhl}` |
| 1.2 | `THM{Y2Q2N2M1NzNmYTQzYTI4ODliYzkzMmZh}` |
| 1.3 | `THM{MjcxNmVmYjNhYzdkZDc0M2RkNTZhNDA0}` |

---

**Metodología:**
Resolución del enigma del reto, identificación del esquema de codificación (Base64) y decodificación del fragmento para componer la flag completa del año.

### Cadena de ataque / Attack Chain
1. Lectura del enigma planteado en el reto.
2. Identificación del esquema de codificación (Base64).
3. Decodificación del fragmento.
4. Composición de la flag completa.

**Learning chain:**
Enigma → Pieza del año → Flag completa del Cerdo.

**Lección:** *Cada desafío de la serie 'Year of the ...' entrega una pieza codificada que debe descifrarse para llegar a la flag del año.*

**MITRE ATT&CK:**
- No aplica (reto CTF de codificación).

**Fuente:** [TryHackMe - Year of the Pig](https://tryhackme.com/room/yearofthepig)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.