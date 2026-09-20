# NerdHerd

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
| Medium | Máquina (CTF) | nerdherd | https://tryhackme.com/room/nerdherd | Explotación / Web | TryHackMe | Servidor web, panel de control, flags progresivas | High |

> **Objeto:** Explorar un panel web tras la flag inicial, enumerar y explotar las funcionalidades expuestas y avanzar hasta obtener las tres flags de la máquina NerdHerd.

---

**Contexto:**

NerdHerd es un reto en el que se parte de una página web que enmascara el acceso real. Tras localizar el endpoint o panel correcto, se navega por sus funcionalidades (parámetros, cargas o rutas ocultas) y se van obteniendo las tres flags de nivel creciente, cada una en un punto distinto del compromiso: desde la entrada hasta el control final del sistema.

> **ES:** Se obtiene la primera flag al encontrar el panel real de la aplicación. Enumerando parámetros, rutas y funcionalidades del panel se descubre el vector que permite ejecutar acciones no autorizadas y se consiguen la segunda y la tercera flag, completando así el compromiso de NerdHerd.

> **EN:** The first flag is obtained by finding the real panel of the application. By enumerating parameters, routes and panel features, the vector that allows unauthorized actions is discovered, obtaining the second and third flags and completing the compromise of NerdHerd.

## Solucionario

### Task 1: Flag 1 / Flag 1
**Explicación:**

Tras el reconocimiento inicial se localiza el panel o directorio real de la aplicación (el contenido de la web pública enmascara el acceso). Al acceder correctamente se obtiene la primera flag.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Flag 1 | `THM{7fc91d70e22e9b70f98aaf19f9a1c3ca710661be}` |

### Task 2: Flag 2 / Flag 2
**Explicación:**

Se enumeran los parámetros y funcionalidades del panel. Manipulando la petición que la aplicación realiza (parámetro controlado por el usuario) se logra una acción no prevista y se obtiene la segunda flag.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 2. Flag 2 | `THM{5c5b7f0a81ac1c00732803adcee4a473cf1be693}` |

### Task 3: Flag 3 / Flag 3
**Explicación:**

Continuando con la explotación de la funcionalidad vulnerable o tras ganar acceso al entorno interno, se alcanza el último punto del reto y se captura la tercera flag, cerrando el compromiso de la máquina.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 3. Flag 3 | `THM{a975c295ddeab5b1a5323df92f61c4cc9fc88207}` |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Flag 1 | `THM{7fc91d70e22e9b70f98aaf19f9a1c3ca710661be}` |
| 2 | Flag 2 | `THM{5c5b7f0a81ac1c00732803adcee4a473cf1be693}` |
| 3 | Flag 3 | `THM{a975c295ddeab5b1a5323df92f61c4cc9fc88207}` |

---

**Metodología:**

1. Reconocimiento web y descubrimiento del panel real de la aplicación.
2. Obtención de la primera flag.
3. Enumeración de parámetros y funcionalidades del panel.
4. Manipulación de la petición vulnerable para ejecutar acciones no autorizadas.
5. Obtención de la segunda y tercera flag.

### Cadena de ataque / Attack Chain

```
Recon web --> Localizar panel real
        |
        v
Flag 1
        |
        v
Enumeración de parámetros / funcionalidades
        |
        v
Abuso de la funcionalidad vulnerable
        |
        v
Flag 2
        |
        v
Avance hasta el entorno de destino --> Flag 3
```

**Learning chain:**

- ¿Cómo se oculta un panel accesible detrás de un contenido web aparentemente inerte?
- ¿Qué papel juega la enumeración de parámetros en el descubrimiento de vulnerabilidades?
- ¿Cómo un solo parámetro manipulable puede dar acceso a funciones internas del panel?

**Lección:**

*Lo que la web muestra y lo que la aplicación realmente acepta suelen ser cosas distintas: la enumeración paciente de parámetros y rutas es la que convierte una flag inicial en un compromiso completo.*

**MITRE ATT&CK:**

- T1595 (Active Scanning)
- T1190 (Exploit Public-Facing Application)
- T1059 (Command and Scripting Interpreter)

**Fuente:** [TryHackMe - NerdHerd](https://tryhackme.com/room/nerdherd)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.