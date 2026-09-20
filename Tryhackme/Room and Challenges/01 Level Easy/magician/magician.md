# magician

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | challenge | `magician` | [TryHackMe](https://tryhackme.com/room/magician) | 01 Level Easy | TryHackMe | web hacking / parametre manipulation / steganography / LFI / hex decoding | Manipulación de parámetros, esteganografía y codificación hexadecimal para obtener flags en una máquina web |

---

**Contexto:** Sala de tipo challenge de temática mágica. El flujo se centra en la manipulación de parámetros de la aplicación web, la descarga y comparación de archivos de imagen, y la aplicación de técnicas de esteganografía y decodificación hexadecimal para revelar mensajes ocultos y obtener las flags.

## Solucionario

### Task 1

**Explicación:** Se resuelve la primera parte del reto: la manipulación de datos de la aplicación web y la utilización de técnicas de codificación hexadecimal permiten extraer las dos primeras flags.

1. THM{simsalabim_hex_hex}
2. THM{magic_may_make_many_men_mad}

### Task 2

**Explicación:** Tarea de conclusión del reto, no requiere respuesta escrita.

1. No answer needed

---

| # | Task | Respuesta |
|---|------|-----------|
| 1 | Task 1 | `THM{simsalabim_hex_hex}` |
| 2 | Task 1 | `THM{magic_may_make_many_men_mad}` |
| 3 | Task 2 | No answer needed |

---

**Metodología:** Se interactúa con la aplicación web analizando sus parámetros y funcionalidades. Se descargan los archivos de imagen ofrecidos y se comparan entre sí; las diferencias revelan contenido oculto. El mensaje extraído requiere aplicar esteganografía además de decodificación hexadecimal para obtener el texto en claro y las flags.

### Cadena de ataque / Attack Chain

```text
enumeración web -> manipulación de parámetros -> descarga de imágenes -> comparación de archivos -> esteganografía -> decodificación hexadecimal -> flag 1 -> flag 2
```

**Learning chain:** web enumeration → parameter manipulation → image download → file comparison → steganography → hex decoding → flag extraction

**Lección:** *Técnicas combinadas como la esteganografía y la codificación hexadecimal suelen esconder mensajes en recursos aparentemente inofensivos (imágenes, parámetros); comparar versiones de un mismo archivo revela las diferencias ocultas.*

**MITRE ATT&CK:** T1552.002 (Unsecured Credentials: Credentials in Files), T1059.001 (Command and Scripting Interpreter: PowerShell), T1140 (Deobfuscate/Decode Files or Information)

**Fuente:** [TryHackMe - magician](https://tryhackme.com/room/magician)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.