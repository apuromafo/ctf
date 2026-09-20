# VulnNet dotpy

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | Reto / Challenge (Python) | vulnnetdotpy | https://tryhackme.com/room/vulnnetdotpy | 02 Level Medium | TryHackMe | Python (Flask/RoR), Web exploitation, Privesc | Alta - máquina de práctica |

> **Objeto:** Explotar la aplicación Python de la saga VulnNet y escalar privilegios para leer las dos flags.

---

**Contexto:** "VulnNet dotpy" es el hermano Python de la saga VulnNet. La aplicación está escrita en Python (framework estilo Flask/RoR) y junto con el clásico `.jar` de la saga se explota para lograr ejecución de comandos y escalada de privilegios hasta root.

> **ES:** Reto de explotación de una aplicación web Python con root de máquina.
> **EN:** Python web application exploitation challenge with full machine root.

## Solucionario

### Task 1: Flag de usuario / User flag

**Explicación:** Enumerar la web Python, abusar de la funcionalidad vulnerable para ejecutar comandos y leer la flag de usuario.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es la flag de usuario? / What is the user flag? | THM{91c7547864fa1314a306f82a14cd7fb4} |

### Task 2: Flag de root / Root flag

**Explicación:** Escalar privilegios en el sistema para conseguir root y leer la última flag.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es la flag de root? / What is the root flag? | THM{734c7c2f0a23a4f590aa8600676021fb} |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Cuál es la flag de usuario? / What is the user flag? | `THM{91c7547864fa1314a306f82a14cd7fb4}` |
| 1 | ¿Cuál es la flag de root? / What is the root flag? | `THM{734c7c2f0a23a4f590aa8600676021fb}` |

---

**Metodología:**

1. Enumeración de la aplicación web en Python.
2. Abuso de la funcionalidad vulnerable para RCE.
3. Obtención de acceso a la máquina.
4. Escalada de privilegios a root.
5. Captura de las flags.

### Cadena de ataque / Attack Chain

```text
Enumeración web -> RCE (Python) -> Shell -> Privesc -> Root -> Flags
```

**Learning chain:**

- Los retos de la saga VulnNet encadenan web + RCE + escalada.
- La flag de usuario valida la entrada; la de root valida el escalado.
- Mantener el mismo método de la saga permite avanzar rápido.

**Lección:** *El lenguaje de la aplicación cambia, pero la cadena de compromiso es la misma.*

**MITRE ATT&CK:**
- T1190 - Exploit Public-Facing Application
- T1059 - Command and Scripting Interpreter
- T1068 - Exploitation for Privilege Escalation

**Fuente:** [TryHackMe - VulnNet dotpy](https://tryhackme.com/room/vulnnetdotpy)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.