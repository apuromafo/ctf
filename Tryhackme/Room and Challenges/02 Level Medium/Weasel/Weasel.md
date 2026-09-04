# Weasel [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** CTF (Free)
* **Slug:** `weasel`
* **Link:** https://tryhackme.com/room/weasel
* **Sección / Section:** Linux / CTF
* **Fuente / Source:** (thmrevenant)

---

## Solucionario de Tareas / Task Solutions

> **ES:** CTF de Linux que combina la explotación inicial de una aplicación web y el abuso de procesos de Python para comprometer la máquina, obtener las flags de usuario y escalar privilegios hasta root.
> **EN:** Linux CTF that combines initial exploitation of a web application and abuse of Python processes to compromise the machine, obtain the user flags and escalate privileges to root.

---

### Task 1 — Flags de Usuario y Root / User and Root Flags

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the user.txt flag? | `THM{w3as3ls_@nd_pyth0ns}` |
| What is the root.txt flag? | `THM{evelated_w3as3l_l0ngest_boi}` |

---

## Metodología / Methodology

1. **Paso / Step:** Enumerar el objetivo y explotar la aplicación web para obtener una shell inicial en la máquina. / Enumerate the target and exploit the web application to obtain an initial shell on the machine.
2. **Paso / Step:** Identificar procesos o scripts de Python con permisos elevados y aprovecharlos (writers/ejecución de código) para escalar privilegios dentro del sistema. / Identify Python processes or scripts with elevated permissions and abuse them (writers/code execution) to escalate privileges within the system.
3. **Paso / Step:** Leer `user.txt` y, tras la escalada, `root.txt`. / Read `user.txt` and, after escalation, `root.txt`.

### Cadena de ataque / Attack Chain

```
Enumeración -> Webapp explotada -> shell (www-data/user)
  -> abuso de procesos Python en ejecución
  -> user.txt = THM{w3as3ls_@nd_pyth0ns}
  -> privesc (elevated Python) -> root.txt = THM{evelated_w3as3l_l0ngest_boi}
```

**Lección:** Los procesos de Python que corren con permisos elevados son objetivos valiosos para la escalada de privilegios; una librería o script modificable puede convertirse en una puerta directa a root.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.