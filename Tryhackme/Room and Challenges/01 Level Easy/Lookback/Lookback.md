# Lookback

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | challenge | `lookback` | [TryHackMe](https://tryhackme.com/room/lookback) | 01 Level Easy | TryHackMe | web exploration / source code inspection / flag extraction / browser devtools | Captura de tres flags accediendo a contenido olvidado y oculto en un sitio web |

---

**Contexto:** El room presenta un sitio web con contenido legado y olvidado. La enumeración de rutas históricas y la inspección del código y los recursos del sitio permiten descubrir tres flags escondidas como recompensa por explorar lo que no se ve a simple vista.

## Solucionario

### Task 1

**Explicación:** Se explora el sitio web y se localizan las tres flags ocultas en contenido antiguo o en recursos accesibles del servidor web.

1. THM{Security_Through_Obscurity_Is_Not_A_Defense}
2. THM{Stop_Reading_Start_Doing}
3. THM{Looking_Back_Is_Not_Always_Bad}

---

| # | Task | Respuesta |
|---|------|-----------|
| 1 | Task 1 | `THM{Security_Through_Obscurity_Is_Not_A_Defense}` |
| 2 | Task 1 | `THM{Stop_Reading_Start_Doing}` |
| 3 | Task 1 | `THM{Looking_Back_Is_Not_Always_Bad}` |

---

**Metodología:** Se parte de la página principal y se revisa el historial de cambios del sitio. Se prueba el acceso a rutas antiguas y versiones previas de los recursos, así como la inspección cuidadosa del contenido renderizado. Cada flag aparece al volver a mirar (look back) elementos que parecían irrelevantes o se daban por obsoletos.

### Cadena de ataque / Attack Chain

```text
exploración del sitio -> revisar historial/versiones antiguas -> inspeccionar rutas y recursos olvidados -> extraer flag 1 -> flag 2 -> flag 3
```

**Learning chain:** web exploration → historic content review → hidden resource discovery → flag extraction

**Lección:** *El contenido no siempre se elimina por completo en los sitios web; las rutas y versiones antiguas suelen quedar accesibles y se convierten en una fuente de información sensible.*

**MITRE ATT&CK:** T1083 (File and Directory Discovery), T1106 (Native API)

**Fuente:** [TryHackMe - Lookback](https://tryhackme.com/room/lookback)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.