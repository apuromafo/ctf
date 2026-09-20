# Pickle Rick

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | ctf | `picklerick` | [TryHackMe](https://tryhackme.com/room/picklerick) | 01 Level Easy | THM | OWASP Top 10, RCE, Linux, Escalada de privilegios, SUID, PATH hijacking | CTF Linux de explotación web y post-explotación |

---

**Contexto:** CTF inspirado en la serie Rick y Morty: se compromete un servidor web vulnerable (OWASP Top 10), se obtiene una reverse shell en Linux y se escala privilegios hasta root para recuperar los tres ingredientes que necesita Rick. El acceso se consigue explotando una vulnerabilidad del sitio y la escalada se realiza abusando de binarios con permisos SUID y de variables de entorno.

> **ES:** Máquina CTF de nivel fácil: explota un sitio web vulnerable para conseguir una reverse shell y escala privilegios a root para robar los tres ingredientes de la receta de Rick.
> **EN:** Easy CTF machine: exploit a vulnerable website to get a reverse shell and escalate privileges to root to steal the three ingredients for Rick's recipe.

## Solucionario

### Task 1: Los tres ingredientes / The Three Ingredients

**Explicación:** Resuelve la máquina completa: enumeración del sitio web vulnerable, explotación que permite ejecución de comandos y obtención de una shell en la máquina. Con la shell se localiza el primer ingrediente (mr. meeseek hair), se escala privilegios (abusando de binarios SUID y de la configuración del PATH) para obtener el segundo (1 jerry tear) y el tercero (fleeb juice) como root.

1. 1. mr. meeseek hair
   2. 1 jerry tear
   3. fleeb juice

| Pregunta | Respuesta |
|---|---|
| ¿Cuál es el primer ingrediente que Rick necesita? | `mr. meeseek hair` |
| ¿Cuál es el segundo ingrediente que Rick necesita? | `1 jerry tear` |
| ¿Cuál es el último ingrediente que Rick necesita? | `fleeb juice` |

---

**Metodología:** Enumeración web y de puertos, identificación de la vulnerabilidad de ejecución de comandos (RCE) en el panel del sitio, obtención de una reverse shell, enumeración de binarios SUID y manipulación del PATH para ejecutar comandos como root.

### Cadena de ataque / Attack Chain
Escaneo de puertos y servicios -> Enumeración del sitio web -> Explotación del RCE para obtener una shell -> Localización del primer ingrediente -> Enumeración de binarios con SUID -> Abuso del PATH hijacking para realizar una escalada de privilegios -> Obtención del segundo y tercer ingrediente como root.

**Learning chain:** XSS/RCE por comandos en aplicaciones web, reverse shells, binarios SUID, path hijacking y enumeración básica de sistemas Linux.

**Lección:** *Los binarios SUID mal configurados y los directorios del PATH modificables convierten una shell limitada en acceso root: la enumeración local es clave tras obtener una foothold.*

**MITRE ATT&CK:** T1059 Command and Scripting Interpreter, T1059.004 Unix Shell, T1505.003 Web Shell, T1548.001 Abuse Elevation Control Mechanism (Setuid and Setgid), T1574.007 Hijack Execution Flow (PATH hijacking), T1068 Exploitation for Privilege Escalation.

**Fuente:** [TryHackMe - Pickle Rick](https://tryhackme.com/room/picklerick)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.