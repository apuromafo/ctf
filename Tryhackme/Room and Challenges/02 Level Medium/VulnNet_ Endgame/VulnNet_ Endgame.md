# VulnNet Endgame

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | Reto final / Endgame Challenge | vulnnetendgame | https://tryhackme.com/room/vulnnetendgame | 02 Level Medium | TryHackMe | Web exploitation, CTF endgame, Privesc | Alta - máquina de práctica |

> **Objeto:** Completar el reto final de la saga VulnNet resolviendo las tres subpreguntas del flag final.

---

**Contexto:** "VulnNet Endgame" cierra la saga VulnNet. El reto presenta tres preguntas encadenadas cuya resolución requiere explotar la aplicación web, obtener credenciales y escalar privilegios. El primer valor corresponde a una credencial/clave encontrada en el sitio, seguida de la flag de usuario y la de root.

> **ES:** El desenlace de la saga VulnNet: web, credenciales y escalada.
> **EN:** The finale of the VulnNet saga: web, credentials, and privilege escalation.

## Solucionario

### Task 1: Clave de acceso / Access credential

**Explicación:** Enumerar la aplicación web y localizar la credencial/clave expuesta en el sitio.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es la credencial encontrada? / What is the found credential? | vAxWtmNzeTz |

### Task 2: Flag de usuario / User flag

**Explicación:** Usar la credencial para acceder al sistema y leer la primera flag.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es la primera flag? / What is the first flag? | THM{fb84e79072015186c72ec77ded49a5ff} |

### Task 3: Flag de root / Root flag

**Explicación:** Escalar privilegios en el sistema para obtener la flag final.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es la flag final? / What is the final flag? | THM{1d42edbb03c0b287a8d0d8a265dce012} |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Cuál es la credencial encontrada? / What is the found credential? | `vAxWtmNzeTz` |
| 1 | ¿Cuál es la primera flag? / What is the first flag? | `THM{fb84e79072015186c72ec77ded49a5ff}` |
| 1 | ¿Cuál es la flag final? / What is the final flag? | `THM{1d42edbb03c0b287a8d0d8a265dce012}` |

---

**Metodología:**

1. Enumeración de la aplicación web.
2. Extracción de credenciales expuestas.
3. Acceso inicial al sistema.
4. Escalada de privilegios hasta root.
5. Resolución de las tres preguntas del reto.

### Cadena de ataque / Attack Chain

```text
Recon web -> Credencial vAxWtmNzeTz -> Acceso -> Flag de usuario -> Privesc -> Flag final
```

**Learning chain:**

- Las credenciales en la superficie de la web abren la puerta.
- La flag de usuario confirma el acceso; la final, el escalado completo.
- Endgame combina todas las técnicas vistas en la saga.

**Lección:** *Las buenas credenciales en el sitio correcto son la llave de todo el compromiso.*

**MITRE ATT&CK:**
- T1190 - Exploit Public-Facing Application
- T1078 - Valid Accounts
- T1068 - Exploitation for Privilege Escalation

**Fuente:** [TryHackMe - VulnNet Endgame](https://tryhackme.com/room/vulnnetendgame)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.