# Year of the Rabbit

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | CTF | `yearoftherabbit` | https://tryhackme.com/room/yearoftherabbit | 01 Level Easy | TryHackMe | Enumeración · explotación · extracción de flags | Reto CTF con dos banderas THM |

---

**Contexto:** Reto CTF de TryHackMe con dos banderas. La fuente de este catálogo solo conserva las respuestas finales (flag inicial y flag de finalización) sin el detalle paso a paso de la explotación, por lo que el solucionario se limita a reproducir las dos banderas exactas.

> **ES:** Reto CTF con dos banderas finales; la tarea única de la sala entrega la flag inicial y la flag de cierre.
> **EN:** CTF challenge with two final flags; the room's single task yields the initial flag and the closing flag.

## Solucionario

### Task 1: Bandera 1 y Bandera 2 / Flag 1 and Flag 2

**Explicación:**
1. 1. THM{1107174691af9ff3681d2b5bdb5740b1589bae53}
   2. THM{8d6f163a87a1c80de27a4fd61aef0f3a0ecf9161}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Bandera 1 / Flag 1 | `THM{1107174691af9ff3681d2b5bdb5740b1589bae53}` |
| 2 | Bandera 2 / Flag 2 | `THM{8d6f163a87a1c80de27a4fd61aef0f3a0ecf9161}` |

---

**Metodología:** Esta sala se resuelve completando los pasos del reto hasta obtener las dos banderas. Al conservar únicamente las respuestas, la metodología se limita a registrar las dos flags exactas obtenidas durante el reto.

### Cadena de ataque / Attack Chain

```text
enumeración inicial -> explotación del reto -> flag 1 -> escalada/pasos finales -> flag 2
```

**Learning chain:** enumeración -> explotación -> flag inicial -> pasos finales -> flag final.

**Lección:** *Siempre hay que documentar las banderas completas tal y como se entregan, ya que son el artefacto de verificación principal del reto y su valor exacto (mayúsculas, minúsculas y formato) debe preservarse sin alteraciones.*

**MITRE ATT&CK:** N/A (CTF)

**Fuente:** [TryHackMe - Year of the Rabbit](https://tryhackme.com/room/yearoftherabbit)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.