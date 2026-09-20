# Linux Agency
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `linuxagency` |
| **Link** | [TryHackMe](https://tryhackme.com/room/linuxagency) |
| **Sección** | 02 Level Medium |
| **Fuente** | Solución de laboratorio (repositorio Apuromafo) |
| **Componentes** | Linux, enumeración, recopilación de flags (misiones 1-30), escalada de privilegios (user → root), temática HITMAN |
| **Impacto** | Afila tus habilidades de Linux y aprende escalada de privilegios básica con una temática HITMAN: completar las misiones, localizar sus flags repartidas por el sistema y ganar acceso root a la máquina. |
---
**Contexto:** Sala de temática HITMAN («Agency») diseñada para afilar habilidades de Linux y practicar escalada básica de privilegios. En el laboratorio se recogen las respuestas finales por tarea: dos introducciones sin respuesta, la secuencia de las 30 misiones con su flag (`missionN{...}`), la flag de viktor que cierra la fase de misiones, y el cierre con los objetivos restantes (dalia, silvio, reza, jordan, ken, sean, penelope y maya), la respuesta final `industryweapon` y las flags `user{...}` y `root{...}`.
> **ES:** Esta sala te ayudará a afilar tus habilidades de Linux y a aprender escalada de privilegios básica con una temática de HITMAN. Así que prepara tu maletín y coge tus SilverBallers, porque va a ser un viaje duro.
> **EN:** This Room will help you to sharpen your Linux Skills and help you to learn basic privilege escalation in a HITMAN theme. So, pack your briefcase and grab your SilverBallers as its gonna be a tough ride.
## Solucionario
### Task 1 — Introducción
**Explicación:** Tarea introductoria de la sala. Presenta la ambientación del agente y el encuadre del reto. No requiere ninguna respuesta.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Respuesta de la tarea 1 (introducción). | `No answer needed` |
### Task 2 — Preparación
**Explicación:** Segunda tarea de ambientación/preparación del laboratorio. No requiere ninguna respuesta.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Respuesta de la tarea 2 (introducción). | `No answer needed` |
### Task 3 — Misiones 1-30 y flag de viktor
**Explicación:** Las 30 misiones de la sala se resuelven recopilando una flag por misión, en formato `missionN{...}`. Cada flag se localiza en el sistema tras ejecutar la tarea correspondiente; no se requieren respuestas intermedias más allá del valor de cada flag. Al completar la secuencia de misiones se obtiene además la flag `viktor{...}`, que cierra esta fase del reto.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de la misión 1. | `mission1{174dc8f191bcbb161fe25f8a5b58d1f0}` |
| 2 | Flag de la misión 2. | `mission2{8a1b68bb11e4a35245061656b5b9fa0d}` |
| 3 | Flag de la misión 3. | `mission3{ab1e1ae5cba688340825103f70b0f976}` |
| 4 | Flag de la misión 4. | `mission4{264a7eeb920f80b3ee9665fafb7ff92d}` |
| 5 | Flag de la misión 5. | `mission5{bc67906710c3a376bcc7bd25978f62c0}` |
| 6 | Flag de la misión 6. | `mission6{1fa67e1adc244b5c6ea711f0c9675fde}` |
| 7 | Flag de la misión 7. | `mission7{53fd6b2bad6e85519c7403267225def5}` |
| 8 | Flag de la misión 8. | `mission8{3bee25ebda7fe7dc0a9d2f481d10577b}` |
| 9 | Flag de la misión 9. | `mission9{ba1069363d182e1c114bef7521c898f5}` |
| 10 | Flag de la misión 10. | `mission10{0c9d1c7c5683a1a29b05bb67856524b6}` |
| 11 | Flag de la misión 11. | `mission11{db074d9b68f06246944b991d433180c0}` |
| 12 | Flag de la misión 12. | `mission12{f449a1d33d6edc327354635967f9a720}` |
| 13 | Flag de la misión 13. | `mission13{076124e360406b4c98ecefddd13ddb1f}` |
| 14 | Flag de la misión 14. | `mission14{d598de95639514b9941507617b9e54d2}` |
| 15 | Flag de la misión 15. | `mission15{fc4915d818bfaeff01185c3547f25596}` |
| 16 | Flag de la misión 16. | `mission16{884417d40033c4c2091b44d7c26a908e}` |
| 17 | Flag de la misión 17. | `mission17{49f8d1348a1053e221dfe7ff99f5cbf4}` |
| 18 | Flag de la misión 18. | `mission18{f09760649986b489cda320ab5f7917e8}` |
| 19 | Flag de la misión 19. | `mission19{a0bf41f56b3ac622d808f7a4385254b7}` |
| 20 | Flag de la misión 20. | `mission20{b0482f9e90c8ad2421bf4353cd8eae1c}` |
| 21 | Flag de la misión 21. | `mission21{7de756aabc528b446f6eb38419318f0c}` |
| 22 | Flag de la misión 22. | `mission22{24caa74eb0889ed6a2e6984b42d49aaf}` |
| 23 | Flag de la misión 23. | `mission23{3710b9cb185282e3f61d2fd8b1b4ffea}` |
| 24 | Flag de la misión 24. | `mission24{dbaeb06591a7fd6230407df3a947b89c}` |
| 25 | Flag de la misión 25. | `mission25{61b93637881c87c71f220033b22a921b}` |
| 26 | Flag de la misión 26. | `mission26{cb6ce977c16c57f509e9f8462a120f00}` |
| 27 | Flag de la misión 27. | `mission27{444d29b932124a48e7dddc0595788f4d}` |
| 28 | Flag de la misión 28. | `mission28{03556f8ca983ef4dc26d2055aef9770f}` |
| 29 | Flag de la misión 29. | `mission29{8192b05d8b12632586e25be74da2fff1}` |
| 30 | Flag de la misión 30. | `mission30{d25b4c9fac38411d2fcb4796171bda6e}` |
| 31 | Flag de viktor. | `viktor{b52c60124c0f8f85fe647021122b3d9a}` |
### Task 4 — Flags finales: objetivos, arma, user y root
**Explicación:** Fase final de la sala. Tras completar las misiones se resuelven los objetivos restantes: las flags de los cómplices/objetivos (dalia, silvio, reza, jordan, ken, sean, penelope y maya), la respuesta del acertijo final que devuelve `industryweapon`, y finalmente las flags de usuario (`user{...}`) y de root (`root{...}`) que confirman la escalada completa.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Respuesta de la tarea 4, pregunta 1. | `No answer needed` |
| 2 | Flag de dalia. | `dalia{4a94a7a7bb4a819a63a33979926c77dc}` |
| 3 | Flag de silvio. | `silvio{657b4d058c03ab9988875bc937f9c2ef}` |
| 4 | Flag de reza. | `reza{2f1901644eda75306f3142d837b80d3e}` |
| 5 | Flag de jordan. | `jordan{fcbc4b3c31c9b58289b3946978f9e3c3}` |
| 6 | Flag de ken. | `ken{4115bf456d1aaf012ed4550c418ba99f}` |
| 7 | Flag de sean. | `sean{4c5685f4db7966a43cf8e95859801281}` |
| 8 | Flag de penelope. | `penelope{2da1c2e9d2bd0004556ae9e107c1d222}` |
| 9 | Flag de maya. | `maya{a66e159374b98f64f89f7c8d458ebb2b}` |
| 10 | Respuesta del acertijo/arma final. | `industryweapon` |
| 11 | Flag de user.txt. | `user{620fb94d32470e1e9dcf8926481efc96}` |
| 12 | Flag de root.txt. | `root{62ca2110ce7df377872dd9f0797f8476}` |
---
**Metodología:** Enumeración del sistema Linux → resolución de las 30 misiones recopilando sus flags (`missionN{...}`) → flag de viktor → fase final: flags de los objetivos (dalia, silvio, reza, jordan, ken, sean, penelope, maya), respuesta `industryweapon` y flags `user{...}` / `root{...}` → escalada de privilegios completa.
### Cadena de ataque / Attack Chain
La sala se resuelve en progresión de misiones: el jugador explora el sistema (enumeración de ficheros, procesos y permisos) para localizar cada flag `missionN{...}`; al completar las 30 misiones obtiene la flag de viktor, y en la fase final recupera las flags de los objetivos (dalia → maya), identifica el arma/objeto `industryweapon` y escala privilegios hasta leer `user{...}` y `root{...}`. No hay código de explotación adicional; la clave es la enumeración sistemática y la recolección de flags.
**Learning chain:** conceptos de Linux → enumeración del sistema → recopilación de las flags de cada misión → escalada de privilegios básica (user → root).
**Lección:** *Completar un reto basado en misiones obliga a dominar la enumeración ordenada del sistema Linux y a encadenar pequeños avances (flags) hasta convertir el acceso de usuario en acceso total, reforzando la escalada de privilegios básica.*
**MITRE ATT&CK:** T1083 (File and Directory Discovery - localización de flags y ficheros), T1068 (Exploitation for Privilege Escalation - escalada a root), T1078 (Valid Accounts - acceso con cuentas legítimas).
**Fuente:** [TryHackMe - Linux Agency](https://tryhackme.com/room/linuxagency)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.