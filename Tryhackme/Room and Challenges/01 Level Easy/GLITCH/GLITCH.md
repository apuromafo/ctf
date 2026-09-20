# GLITCH

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `glitch` | [TryHackMe](https://tryhackme.com/room/glitch) | 01 Level Easy | THM | Web app, Privilege Escalation, Flags | Análisis web y escalada de privilegios simple |

> **Objeto:** Challenge showcasing a web app and simple privilege escalation. Can you find the glitch?

---

**Contexto:** Reto web centrado en encontrar el "glitch" de una aplicación web: investigando la app se obtienen valores internos y credenciales parciales que se encadenan hasta las tres banderas finales del reto.

> **ES:** Analizar la web app, encontrar el fallo y encadenar los valores descubiertos hasta obtener las banderas del reto.
> **EN:** Analyse the web app, find the flaw and chain the discovered values to capture the room flags.

## Solucionario

### Task 1: El reto / The Challenge

**Explicación:** Reto de una única tarea. Hay que analizar la aplicación web, descubrir el "glitch" y usarlo para la escalada de privilegios, resolviendo las preguntas del apartado.

1. `No answer needed`
2. `this_is_not_real`
3. `THM{i_don't_know_why}`
4. `THM{diamonds_break_our_aching_minds}`

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1.1 | — | `No answer needed` |
| 1.2 | Valor descubierto en el reto | `this_is_not_real` |
| 1.3 | Bandera del reto | `THM{i_don't_know_why}` |
| 1.4 | Bandera final del reto | `THM{diamonds_break_our_aching_minds}` |

---

**Metodología:** Reconocimiento de la web app, identificación del "glitch" que expone valores internos, uso de ese fallo para la escalada de privilegios y recuperación secuencial de las banderas.

### Cadena de ataque / Attack Chain

```text
Web app recon -> identificar el glitch -> exponer valores internos -> escalada de privilegios -> flags
```

**Learning chain:** Web recon → Glitch discovery → Data exposure → Privilege escalation → Flags

**Lección:** *En los retos web, un "glitch" aparentemente inocuo (comparaciones débiles, fallos de lógica) suele ser la puerta a privilegios y banderas ocultas.*

**MITRE ATT&CK:** N/A (Reto web)

**Fuente:** [TryHackMe - GLITCH](https://tryhackme.com/room/glitch)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.