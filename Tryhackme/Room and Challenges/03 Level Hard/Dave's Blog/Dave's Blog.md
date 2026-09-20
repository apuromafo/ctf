# Dave's Blog

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Hard | Reversing | `davesblog` | https://tryhackme.com/room/davesblog | 03 Level Hard | TryHackMe | Ingeniería inversa / strings / Go / gi / análisis de binarios / contraseñas de admin | Sala de ingeniería inversa sobre un blog: recuperar cinco flags avanzando desde la enumeración del sitio, la contraseña del administrador, credenciales o hashes intermedios hasta la flag que se obtiene ejecutando strings contra un binario (RE básica). |

---

**Contexto:** Reto de la categoría Hard enfocado en ingeniería inversa alrededor del blog de "Dave". El progreso se mide con cinco flags HTML-encoded obtenidas paso a paso: una contraseña de administrador con etiqueta THM, dos hashes/cadena de credenciales enmarcados como flags, la flag que aparece al ejecutar `strings` contra un binario (donde se recuerda que "strings es básicamente RE") y una última bandera tras explotar o desensamblar el siguiente paso del reto.

> **ES:** "Recupera las cinco flags del blog de Dave: desde la contraseña del admin hasta la flag escondida tras ejecutar strings sobre un binario."
> **EN:** "Retrieve Dave's blog five flags: from the admin password up to the flag hidden behind running strings over a binary."

## Solucionario

### Task 1: Flags del blog / Blog flags

**Explicación:** Tarea única del reto con cinco respuestas literales que corresponden a las cinco flags HTML-encoded del blog. Se conservan tal cual, incluyendo mayúsculas y formato. Contenido original de la tarea:

```text
1. 1. THM{SuperSecureAdminPassword123}
   2. THM{5fa1f779d1835367fdcfa4741bebb88a}
   3. THM{993e107fc66844482bb5dd0e4c485d5b}
   4. THM{runn1ng_str1ngs_1s_b4sic4lly_RE}
   5. THM{a0a9c4f6809c84e212ac889d39b9cb48}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag 1 del blog. | `THM{SuperSecureAdminPassword123}` |
| 2 | Flag 2 del blog. | `THM{5fa1f779d1835367fdcfa4741bebb88a}` |
| 3 | Flag 3 del blog. | `THM{993e107fc66844482bb5dd0e4c485d5b}` |
| 4 | Flag 4 del blog (binario / strings). | `THM{runn1ng_str1ngs_1s_b4sic4lly_RE}` |
| 5 | Flag 5 del blog. | `THM{a0a9c4f6809c84e212ac889d39b9cb48}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag 1 del blog. | `THM{SuperSecureAdminPassword123}` |
| 2 | Flag 2 del blog. | `THM{5fa1f779d1835367fdcfa4741bebb88a}` |
| 3 | Flag 3 del blog. | `THM{993e107fc66844482bb5dd0e4c485d5b}` |
| 4 | Flag 4 del blog (binario / strings). | `THM{runn1ng_str1ngs_1s_b4sic4lly_RE}` |
| 5 | Flag 5 del blog. | `THM{a0a9c4f6809c84e212ac889d39b9cb48}` |

---

**Metodología:**
1. Enumerar el blog (salas de un CMS/plataforma de blogs) y localizar los puntos de entrada del reto.
2. Recuperar la contraseña del administrador: `THM{SuperSecureAdminPassword123}`.
3. Continuar con el flujo del reto para obtener los hashes/credenciales intermedios.
4. Obtener el binario y ejecutar `strings` sobre él para revelar su flag de ingeniería inversa.
5. Completar el último paso del reto y recoger la quinta flag.

### Cadena de ataque / Attack Chain

```text
Enumeración del blog -> contraseña admin -> THM{SuperSecureAdminPassword123} -> hashes intermedios -> binario -> strings -> THM{runn1ng_str1ngs_1s_b4sic4lly_RE} -> flag final -> THM{a0a9c4f6809c84e212ac889d39b9cb48}
```

**Learning chain:** `Recon -> admin password -> credenciales/hashes -> binario del reto -> strings -> ingeniería inversa -> flags`

**Lección:** *La enumeración junto con la inspección estática de binarios (strings, entre otros) basta para resolver retos de ingeniería inversa sencillos: la flag suele estar literalmente en el binario.*

**MITRE ATT&CK:** T1083 (File and Directory Discovery), T1005 (Data from Local System), T1106 (Native API), T1059 (Command and Scripting Interpreter)

**Fuente:** [TryHackMe - Dave's Blog](https://tryhackme.com/room/davesblog)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.