# Opacity

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `opacity` | [TryHackMe](https://tryhackme.com/room/opacity) | `01 Level Easy` | THM | web, credenciales, explotación | Resolución de los dos apartados del reto |

> **Objeto:** Resolver la sala Opacity explotando la aplicación web y las credenciales descubiertas, hasta extraer los datos (hashes) solicitados en los dos apartados finales del reto.

---

**Contexto:** Walkthrough de la sala Opacity: se documentan las dos respuestas finales del reto, obtenidas tras explotar la aplicación web y acceder a los datos solicitados mediante las credenciales y funcionalidades descubiertas.

> **ES:** Walkthrough de la sala Opacity: se documentan las dos respuestas finales del reto, obtenidas tras explotar la aplicación web y acceder a los datos solicitados mediante las credenciales y funcionalidades descubiertas.

> **EN:** Walkthrough for the Opacity room: the two final answers of the challenge are documented, obtained after exploiting the web application and accessing the requested data through the discovered credentials and functionalities.

## Solucionario

### Task 1: Opacity / Opacity

**Explicación:** La tarea recoge las respuestas finales del reto. El contenido original, conservado íntegramente, es el siguiente:

1. 1. 6661b61b44d234d230d06bf5b3c075e2
   2. ac0d56f93202dd57dcb2498c739fd20e

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Respuesta del apartado 1 del reto | `6661b61b44d234d230d06bf5b3c075e2` |
| 2 | Respuesta del apartado 2 del reto | `ac0d56f93202dd57dcb2498c739fd20e` |

---

**Metodología:** 1) Enumeración inicial de la aplicación web para descubrir el panel de administración. 2) Aprovechamiento de las credenciales y de la funcionalidad vulnerable para acceder a los datos internos. 3) Extracción de las dos respuestas (hashes) finales del reto.

### Cadena de ataque / Attack Chain

1. Enumeración de la aplicación web.
2. Descubrimiento del panel de administración y acceso con las credenciales obtenidas.
3. Abuso de la funcionalidad vulnerable para leer datos internos.
4. Extracción de los dos hashes finales: `6661b61b44d234d230d06bf5b3c075e2` y `ac0d56f93202dd57dcb2498c739fd20e`.

**Learning chain:** web enumeration → descubrimiento del panel de administración → credenciales → abuso de la funcionalidad → extracción de flags/hashes

**Lección:** *Las aplicaciones web suelen esconder paneles y funcionalidades accesibles: una vez dentro, la enumeración cuidadosa de las opciones disponibles es lo que permite leer los datos finales del reto.*

**MITRE ATT&CK:** T1190 - Exploit Public-Facing Application, T1005 - Data from Local System, T1083 - File and Directory Discovery

**Fuente:** [TryHackMe - Opacity](https://tryhackme.com/room/opacity)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.