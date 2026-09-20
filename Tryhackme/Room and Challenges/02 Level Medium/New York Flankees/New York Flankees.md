# New York Flankees

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
| Medium | Máquina (CTF) | newyorkflankees | https://tryhackme.com/room/newyorkflankees | Explotación / Web | TryHackMe | Aplicación web, credenciales, escalada, flags | High |

> **Objeto:** Comprometer la aplicación *New York Flankees*: obtener una credencial válida, autenticarse, explotar las funciones internas de la aplicación y escalar para capturar las cuatro flags repartidas por el sistema.

---

**Contexto:**

New York Flankees es un reto sobre una aplicación web de un equipo de béisbol. El camino comienza con la obtención de una credencial filtrada o generada (usuario `stefan1197` con su contraseña), el acceso a la aplicación y la explotación de sus funcionalidades internas. Cada paso del compromiso entrega una flag: desde la autenticación, pasando por el abuso de funciones de la aplicación hasta el control del sistema interno.

> **ES:** Se obtiene la credencial `stefan1197` con su contraseña y se accede a la aplicación. Tras enumerar las funciones ocultas se explota la lógica de la aplicación para obtener la primera y segunda flag, y mediante la escalada de privilegios sobre el sistema se capturan las flags finales (THM...), completando el reto.

> **EN:** The credential `stefan1197` with its password is obtained and the application is accessed. After enumerating hidden features, the application logic is exploited to obtain the first and second flags, and through privilege escalation over the system the final flags (THM...) are captured, completing the challenge.

## Solucionario

### Task 1: Credencial inicial / Initial Credential
**Explicación:**

Se localiza la credencial de acceso a la aplicación, formada por el usuario `stefan1197` y su contraseña.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Credencial | `stefan1197:ebb2B76@62#f??7cA6B76@6!@62#f6dacd2599` |

### Task 2: Flag 1 / Flag 1
**Explicación:**

Tras autenticarse en la aplicación se accede al panel interno y se obtiene la primera flag del reto.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 2. Flag 1 | `THM{a4113536187c6e84637a1ee2ec5359eca17bbbd1b2629b23dbfd3b4ce2f30604}` |

### Task 3: Flag 2 / Flag 2
**Explicación:**

Explotando una funcionalidad de la aplicación (carga o lógica de negocio) se obtiene la segunda flag.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 3. Flag 2 | `THM{342878cd14051bd787352ee73c75381b1803491e4e5ac729a91a03e3c889c2bf}` |

### Task 4: Flag 3 / Flag 3
**Explicación:**

Tras la escalada de privilegios sobre el sistema y el acceso a los archivos internos se captura la flag final.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 4. Flag 3 | `THM{b3653cb04abf4a5b9c7a77ec52f550e73416b6e61015b8014fff9831a7eb61ce}` |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Credencial | `stefan1197:ebb2B76@62#f??7cA6B76@6!@62#f6dacd2599` |
| 2 | Flag 1 | `THM{a4113536187c6e84637a1ee2ec5359eca17bbbd1b2629b23dbfd3b4ce2f30604}` |
| 3 | Flag 2 | `THM{342878cd14051bd787352ee73c75381b1803491e4e5ac729a91a03e3c889c2bf}` |
| 4 | Flag 3 | `THM{b3653cb04abf4a5b9c7a77ec52f550e73416b6e61015b8014fff9831a7eb61ce}` |

---

**Metodología:**

1. Reconocimiento web y descubrimiento de la credencial `stefan1197`.
2. Autenticación en la aplicación y obtención de la primera flag.
3. Enumeración de funciones internas y explotación de la lógica/fallo de la aplicación.
4. Obtención de la segunda flag y escalada de privilegios.
5. Captura de la flag final en el sistema.

### Cadena de ataque / Attack Chain

```
Recon web --> credencial stefan1197:ebb2B76@...
        |
        v
Login en la aplicación --> Flag 1
        |
        v
Explotación de la funcionalidad interna --> Flag 2
        |
        v
Escalada / acceso interno --> Flag 3
```

**Learning chain:**

- ¿Cómo se obtienen credenciales válidas de una aplicación web?
- ¿Qué funciones de negocio suelen ser manipulables y cómo se abusan?
- ¿Cómo se conecta la explotación de la aplicación con la escalada en el sistema?

**Lección:**

*Una aplicación con credenciales recuperable y funciones internas sin validar abre una cadena que va de la puerta de entrada hasta la flag final: cada capa sin control es un eslabón más para el atacante.*

**MITRE ATT&CK:**

- T1595 (Active Scanning)
- T1078 (Valid Accounts)
- T1190 (Exploit Public-Facing Application)
- T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - New York Flankees](https://tryhackme.com/room/newyorkflankees)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.