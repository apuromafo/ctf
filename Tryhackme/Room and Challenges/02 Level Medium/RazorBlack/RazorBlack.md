# RazorBlack

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `raz0rblack` |
| **Link** | [TryHackMe](https://tryhackme.com/room/raz0rblack) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Active Directory / enumeration / exploitation / flags |
| **Impacto** | Pongas a prueba el conocimiento de enumeración y explotación de Active Directory |

---

**Contexto:** Room de Active Directory de dificultad media. Testea tus conocimientos de enumeración y explotación de Active Directory. Tiene ICMP habilitado; mira el ping antes de empezar el recon y evita usar `-Pn` en nmap. Creada por Xyan1d3.

## Solucionario

### Task 1: Deploy the box

**Explicación:**

Lanza algo como una roca sobre la gran cosa verde de la derecha para desplegar tu máquina (deploy your box).

`Throw something like a rock on the big green thingy on the right side here to deploy your box.`

La caja tiene ICMP habilitado. Así que, mira el ping primero antes de empezar el recon y deja de poner `-Pn` en nmap.

`The box has ICMP enabled. So, look at ping first before starting recon and stop slapping -Pn on nmap.`

Esta room está hecha con orgullo por: Xyan1d3.

Cada solucionador de esta caja recibirá una galleta gratis al completar la caja.

Si te gusta esta room, por favor házmelo saber etiquetándome en Twitter. También puedes contactarme en caso de rutas no intencionadas o bugs, y estaré encantado de resolverlos. Además, házmelo saber qué parte disfrutaste y qué parte te costó.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Deploy the box) | `No answer needed` |

### Task 2: Flag Submission Panel

**Explicación:**

Esto probará tu conocimiento de enumeración y explotación de Active Directory.

`This will test your Active Directory enumeration and exploitation knowledge.`

Envía tus flags y respuestas para probar tu progreso.

`Submit your flags and answers to prove your progression.`

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Flag/answer) | `raz0rblack.thm` |
| 2 | (Flag) | `THM{ab53e05c9a98def00314a14ccbfa8104}` |
| 3 | (Flag) | `electromagnetismo` |
| 4 | (Flag) | `f220d3988deb3f516c73f40ee16c431d` |
| 5 | (Flag) | `THM{694362e877adef0d85a92e6d17551fe4}` |
| 6 | (Flag) | `cyanide9amine5628` |
| 7 | (Flag) | `THM{62ca7e0b901aa8f0b233cade0839b5bb}` |
| 8 | (Flag) | `THM{1b4f46cc4fba46348273d18dc91da20d}` |
| 9 | (Flag) | `THM{5144f2c4107b7cab04916724e3749fb0}` |
| 10 | (Flag) | `:wq` |
| 11 | (Flag) | `Yes` |

---

**Metodología:**

1. Desplegar la máquina y hacer ping para confirmar conectividad (ICMP habilitado).
2. Enumerar y explotar Active Directory.
3. Enviar cada flag en el panel de envío para probar el progreso.

**Learning chain:** deploy -> ping -> AD enumeration -> AD exploitation -> flag submission

**Lección:** *En las cajas de Active Directory, el ping inicial y la enumeración correcta evitan trabajo innecesario (como `-Pn`) y marcan la diferencia en el avance.*

**MITRE ATT&CK:** T1087 (Account Discovery) · T1482 (Domain Trust Discovery) · técnicas de enumeración y explotación de AD

**Fuente:** [TryHackMe - RazorBlack](https://tryhackme.com/room/raz0rblack)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
