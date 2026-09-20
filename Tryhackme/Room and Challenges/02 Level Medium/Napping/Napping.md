# Napping

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
| Medium | Reto / Máquina | napping | https://tryhackme.com/room/napping | Web Security / Client-Side Attacks | TryHackMe | Máquina objetivo, navegador víctima, recurso web | High |

> **Objeto:** Explotar el ataque de *tab nabbing* (secuestro de pestañas) para robar credenciales de la víctima y demostrar el Principio del Mínimo Privilegio (*Principle of Least Privilege*).

---

**Contexto:**

El *tab nabbing* (o *tabnabbing*) es una técnica de ingeniería social y ataque en la que una página maliciosa reemplaza el contenido de una pestaña abierta en el navegador de la víctima mientras esta trabaja en otra pestaña, mostrando una réplica falsa de la página legítima para capturar las credenciales. En este reto se explota esta técnica contra un patrón "admin" que navega con un usuario con privilegios, y finalmente se abusa del Principio del Mínimo Privilegio para elevar privilegios y hacerse con la segunda flag.

> **ES:** La máquina presenta una aplicación web vulnerable a *tab nabbing*. Al crear un HTML malicioso que detecta la pérdida de foco de la pestaña, se sustituye la página por un *phishing* que captura las credenciales del administrador. Después, con las credenciales obtenidas se accede al sistema y, abusando de un servicio que corre con altos privilegios (violando el Principio del Mínimo Privilegio), se obtiene la flag final.

> **EN:** The machine presents a web application vulnerable to tab nabbing. By crafting malicious HTML that detects when the tab loses focus, the page is replaced with a phishing clone that captures the administrator's credentials. Then, with the obtained credentials we access the system and, abusing a service running with high privileges (violating the Principle of Least Privilege), the final flag is obtained.

## Solucionario

### Task 1: Tab Nabbing / Tab Nabbing
**Explicación:**

Se crea una página HTML maliciosa (archivo `.html`) que contiene un enlace a la aplicación víctima. Usando JavaScript con el evento de pérdida de foco de la pestaña (cuando la víctima cambia a otra pestaña), se sustituye el `window.location` de la pestaña por una página de *phishing* clonada. Al volver la víctima a la pestaña, cree estar en la web legítima e introduce sus credenciales, que son capturadas por el atacante. Con las credenciales del administrador se autentica en la aplicación y se obtiene la primera flag.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1 | `THM{Wh@T_1S_Tab_NAbbiN6_&_PrinCIPl3_of_L3A$t_PriViL36E}` |

### Task 2: Principio del Mínimo Privilegio / Principle of Least Privilege
**Explicación:**

Con las credenciales del administrador se accede al sistema. Se enumera el sistema y se comprueba que un servicio/proceso corre con privilegios elevados sin necesidad, violando el Principio del Mínimo Privilegio. Se abusa de esa configuración (por ejemplo, correr código a través de un binario ejecutable por el usuario con permisos elevados) para elevar privilegios y leer la flag de la cuenta privilegiada.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 2 | `THM{Adm1n$_jU$t_c@n'T_stAy_Aw@k3_T$k_tsk_tSK}` |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Flag del ataque de tab nabbing | `THM{Wh@T_1S_Tab_NAbbiN6_&_PrinCIPl3_of_L3A$t_PriViL36E}` |
| 2 | Flag del Principio del Mínimo Privilegio | `THM{Adm1n$_jU$t_c@n'T_stAy_Aw@k3_T$k_tsk_tSK}` |

---

**Metodología:**

1. Análisis de la aplicación web y detección del vector de *tab nabbing*.
2. Creación de un HTML/JavaScript malicioso que clona la página legítima al perder el foco la pestaña.
3. Entrega del enlace a la víctima y captura de las credenciales del administrador.
4. Acceso a la aplicación con las credenciales robadas y obtención de la primera flag.
5. Enumeración del sistema, detección del servicio con privilegios excesivos y elevación mediante el abuso del Principio del Mínimo Privilegio.
6. Obtención de la flag final.

### Cadena de ataque / Attack Chain

```
Crear HTML con tab nabbing (onblur cambia location a login falso)
        |
        v
Víctima (admin) visita la pestaña, cree que es la web legítima e inicia sesión
        |
        v
Captura de credenciales (admin)
        |
        v
Autenticación en la aplicación  -->  Flag 1
        |
        v
Abuso de servicio con privilegios elevados (Least Privilege violado)
        |
        v
Flag 2 (root/admin)
```

**Learning chain:**

- ¿Qué es el *tab nabbing* y por qué funciona contra usuarios desprevenidos?
- ¿Cómo se puede detectar la pérdida de foco de una pestaña con JavaScript (`blur`, `visibilitychange`)?
- ¿Por qué el Principio del Mínimo Privilegio evita que un compromiso parcial se convierta en un compromiso total?
- ¿Qué comprobaciones de localización/seguridad evitarían el ataque (comprobar `window.opener`, URLs de origen, etc.)?

**Lección:**

*Un solo clic en una pestaña abandonada por unos segundos puede robar una sesión completa; y un servicio que corre con más privilegios de los necesarios convierte una credencial robada en la llave del sistema.*

**MITRE ATT&CK:**

- T1189 (Drive-by Compromise)
- T1566.002 (Phishing: Spearphishing Link)
- T1204.001 (User Execution: Malicious Link)
- T1068 (Exploitation for Privilege Escalation)
- T1548 (Abuse Elevation Control Mechanism)

**Fuente:** [TryHackMe - Napping](https://tryhackme.com/room/napping)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.