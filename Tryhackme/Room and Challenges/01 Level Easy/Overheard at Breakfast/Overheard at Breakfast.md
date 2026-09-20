# Overheard at Breakfast

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | challenge | `hh-overheardatbreakfast-6f01793c` | https://tryhackme.com/room/hh-overheardatbreakfast-6f01793c | Hunt & Hack House | TryHackMe | OSINT/social media | Identificación de perfiles ocultos en redes sociales mediante inteligencia de fuentes abiertas |

---

**Contexto:** En un desayuno aparentemente inofensivo, conversaciones filtradas revelan la existencia de perfiles secretos en redes sociales. La técnica OSINT permite rastrear huellas digitales dispersas en múltiples plataformas para identificar identidades ocultas y capturar la flag oculta.

> **ES:** Investiga la conversación filtrada durante el desayuno del hotel Byte Lotus: las menciones apuntan a perfiles en redes sociales y, siguiendo el rastro con OSINT, se localiza la identidad oculta y la flag.
> **EN:** Investigate the leaked breakfast conversation at the Byte Lotus hotel, follow the social media mentions using OSINT, and uncover the hidden identity along with the flag.

## Solucionario

### Task 1: Flag

**Explicación:** El reto entrega el fragmento de una conversación entre dos huéspedes del hotel donde se citan nombres de usuario y plataformas de redes sociales. Con búsquedas OSINT en esas plataformas y la correlación cruzada de pistas (nicknames, fotos, publicaciones) se identifica el perfil que el usuario intentaba ocultar. Dentro de ese perfil se encuentra la flag. Es un ejercicio práctico de inteligencia de fuentes abiertas: comparar nombres de usuario, menciones y metadatos públicos entre plataformas para de-anonimizar una identidad.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{S3creT_Pr0fil3_H4s_b33n_Ident1fi3d}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{S3creT_Pr0fil3_H4s_b33n_Ident1fi3d}` |

---

**Metodología:** Se emplea inteligencia de fuentes abiertas (OSINT) para rastrear menciones y huellas digitales en plataformas de redes sociales. A partir de pistas contextuales proporcionadas en el room, se identifican perfiles ocultos de usuarios que intentan ocultar su identidad digital. La correlación de datos entre plataformas permite reconstruir la identidad completa y localizar la flag oculta asociada al perfil secreto.

### Cadena de ataque / Attack Chain

```text
Conversación filtrada -> menciones/usernames -> búsqueda OSINT en redes sociales -> correlación cruzada de perfiles -> identidad oculta -> flag
```

**Learning chain:** OSINT fundamentals → social media profiling → digital footprint analysis → cross-platform correlation → hidden profile identification → flag extraction

**Lección:** *Los perfiles "ocultos" en redes sociales siguen dejando huellas digitales públicas; correlacionar nombres de usuario, imágenes y menciones entre plataformas permite de-anonimizar identidades que se creían invisibles.*

**MITRE ATT&CK:** N/A (defensive/OSINT room)

**Fuente:** [TryHackMe - Overheard at Breakfast](https://tryhackme.com/r/room/hh-overheardatbreakfast-6f01793c)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.