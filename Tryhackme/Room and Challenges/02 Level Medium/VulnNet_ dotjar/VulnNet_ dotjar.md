# VulnNet dotjar

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | Reto / Challenge (Java) | vulnnetdotjar | https://tryhackme.com/room/vulnnetdotjar | 02 Level Medium | TryHackMe | Java, Deserialización/RCE, Web exploitation | Alta - máquina de práctica |

> **Objeto:** Explotar la aplicación Java de la familia VulnNet y escalar privilegios para obtener las dos flags.

---

**Contexto:** "VulnNet dotjar" es un reto de la saga VulnNet centrado en aplicaciones Java (JAR/PHP). Se parte del clásico `.jar` vulnerable de la saga para conseguir una shell y escalar posteriormente hasta root.

> **ES:** Reto de explotación de una aplicación Java con escalada de privilegios incluida.
> **EN:** Java application exploitation challenge with privilege escalation included.

## Solucionario

### Task 1: Flag de usuario / User flag

**Explicación:** Analizar la aplicación Java, abusar de la ejecución remota de código y leer la flag de usuario.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es la flag de usuario? / What is the user flag? | THM{1ae87fa6ec2cd9f840c68cbad78e9351} |

### Task 2: Flag de root / Root flag

**Explicación:** Escalar privilegios en el sistema comprometido para obtener acceso de root y leer la última flag.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es la flag de root? / What is the root flag? | THM{464c29e3ffae05c2e67e6f0c5064759c} |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Cuál es la flag de usuario? / What is the user flag? | `THM{1ae87fa6ec2cd9f840c68cbad78e9351}` |
| 1 | ¿Cuál es la flag de root? / What is the root flag? | `THM{464c29e3ffae05c2e67e6f0c5064759c}` |

---

**Metodología:**

1. Enumeración de la aplicación web Java.
2. Abuso de la deserialización / RCE del `.jar`.
3. Obtención de una shell en la máquina.
4. Escalada de privilegios a root.
5. Captura de las flags.

### Cadena de ataque / Attack Chain

```text
Enumeración web -> Explotación Java (.jar) -> RCE -> Shell -> Privesc -> Root -> Flags
```

**Learning chain:**

- Las aplicaciones Java conservan la misma técnica nuclear de la saga (.jar malicioso).
- La flag de usuario se obtiene tras el RCE; la de root tras la escalada.
- Los retos "walkthrough" validan cada fase con una flag.

**Lección:** *La ejecución remota de código es solo el principio; la escalada de privilegios completa el compromiso.*

**MITRE ATT&CK:**
- T1190 - Exploit Public-Facing Application
- T1203 - Exploitation for Client Execution
- T1068 - Exploitation for Privilege Escalation

**Fuente:** [TryHackMe - VulnNet dotjar](https://tryhackme.com/room/vulnnetdotjar)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.