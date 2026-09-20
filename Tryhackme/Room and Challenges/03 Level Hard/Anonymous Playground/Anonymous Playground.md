# Anonymous Playground

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Reto CTF | anonymousplayground | https://tryhackme.com/room/anonymousplayground | 03 Level Hard | TryHackMe | Hashing, playground virtual, artefactos del laboratorio | Alto |

---

**Contexto:**
> **ES:** Desafío tipo CTF en un "playground" anónimo: tres valores resumen extraídos de los recursos del laboratorio que deben reconstruirse para completar el reto.
> **EN:** CTF-style challenge in an anonymous playground: three summary values extracted from the lab resources that must be reconstructed to complete the challenge.

## Solucionario

### Task 1: Banderas del playground / Playground flags
**Explicación:**
1. 9184177ecaa83073cbbf36f1414cc029
2. 69ee352fb139c9d0699f6f399b63d9d7
3. bc55a426e98deb673beabda50f24ce66

### Preguntas y Respuestas / Questions and Answers

| Task | Respuesta / Answer |
|---|---|
| 1.1 | `9184177ecaa83073cbbf36f1414cc029` |
| 1.2 | `69ee352fb139c9d0699f6f399b63d9d7` |
| 1.3 | `bc55a426e98deb673beabda50f24ce66` |

---

**Metodología:**
Navegación por el playground anónimo: identificar cada recurso relevante, volcar su contenido y resumirlo (hash) para obtener los tres valores finales.

### Cadena de ataque / Attack Chain
1. Acceso al playground anónimo.
2. Enumeración de recursos y archivos disponibles.
3. Localización de los datos objetivo.
4. Generación de los resúmenes o volcados requeridos.
5. Envío de los tres valores para completar el reto.

**Learning chain:**
Enumeración -> Localización de datos -> Hashing/resumen -> Validación cruzada.

**Lección:** *Un "playground" anónimo es un entorno controlado: la respuesta suele estar en los propios datos, no en la herramienta.*

**MITRE ATT&CK:**
- No aplica (desafío CTF) — recopilación y resumen de datos del laboratorio.

**Fuente:** [TryHackMe - Anonymous Playground](https://tryhackme.com/room/anonymousplayground)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.