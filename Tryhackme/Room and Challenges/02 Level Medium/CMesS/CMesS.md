# CMesS

| Campo | Valor |
|---|---|
| Dificultad | Medium |
| Tipo | CTF |
| Slug | cmess |
| Link | https://tryhackme.com/room/cmess |
| Sección | 02 Level Medium |
| Fuente | TryHackMe |
| Componentes | Enumeración, explotación web |
| Impacto | Obtención de acceso y escalada de privilegios |

---

**Contexto:** CMesS es una sala de TryHackMe de dificultad media que presenta un desafío de penetración con enumeración de servicios, explotación de vulnerabilidades web y escalada de privilegios. El participante debe encontrar las credenciales ocultas, explotar una aplicación vulnerable y escalar privilegios hasta obtener las flags.

## Solucionario

### Task 1: Resolución del desafío

**Explicación:** Se resolvieron las 2 preguntas/flags de la sala mediante enumeración, explotación de vulnerabilidades y escalada de privilegios.

1. thm{c529b5d5d6ab6b430b7eb1903b2b5e1b}
2. thm{9f85b7fdeb2cf96985bf5761a93546a2}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag 1 | `thm{c529b5d5d6ab6b430b7eb1903b2b5e1b}` |
| 2 | Flag 2 | `thm{9f85b7fdeb2cf96985bf5761a93546a2}` |

---

**Metodología:** Enumeración de servicios, identificación de aplicaciones vulnerables, explotación y escalada de privilegios.

**Learning chain:** Enumeración de hosts → descubrimiento de servicios → análisis de aplicaciones web → explotación → obtención de shell → escalada → flags.

**Lección:** *La enumeración exhaustiva y el análisis cuidadoso de aplicaciones web revelan vectores de ataque que conduzcan a la obtención de acceso y escalada.*

**MITRE ATT&CK:** T1190 - Exploit Public-Facing Application

**Fuente:** [TryHackMe - CMesS](https://tryhackme.com/room/cmess)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.