# Sustah

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Boot2root | sustah | https://tryhackme.com/room/sustah | 02 Level Medium | TryHackMe | Enumeración web, Puertos altos, Ruta oculta, Escalada, Hash cracking | Compromiso de la máquina y captura de material sensible (hash) |

---

**Contexto:** La sala **Sustah** es una máquina boot2root en la que se enumera un **puerto elevado** (10921) con un servicio web cuya aplicación se entra por una **ruta oculta** (`/YouGotTh3P@th/`). A partir de ahí se identifica el usuario del servicio (`Mara`) y la versión de la librería/componente vulnerable (`7.5`), que permite explotar la máquina y obtener dos valores sensibles en forma de hash MD5 que cierran el reto.

## Solucionario

### Task 1: Resolución de la máquina
**Explicación:**

La fase inicial es una enumeración de puertos que descubre el servicio en el puerto **10921**. Se accede a su contenido a través de la ruta oculta encontrada, dando con la aplicación gestionada por el usuario **Mara**. Con la versión del componente (7.5) se identifica la vía de ataque y, al comprometer la máquina, se extraen los dos resúmenes (hashes MD5) que completan la respuesta.

1. `10921`
2. `/YouGotTh3P@th/`
3. `Mara`
4. `7.5`
5. `6b18f161b4de63b5f72577c737b7ebc8`
6. `afbb1696a893f35984163021d03f6095`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Puerto del servicio web | `10921` |
| 1.2 | Ruta oculta de la aplicación | `/YouGotTh3P@th/` |
| 1.3 | Usuario del servicio | `Mara` |
| 1.4 | Versión del componente | `7.5` |
| 1.5 | Primer valor sensible (hash) | `6b18f161b4de63b5f72577c737b7ebc8` |
| 1.6 | Segundo valor sensible (hash) | `afbb1696a893f35984163021d03f6095` |

---

**Metodología:** Escaneo de puertos, localización del servicio en puerto alto, fuzzing de rutas, descubrimiento de la ruta oculta, fingerprinting del usuario y versión, explotación del componente vulnerable y recolección de los hashes del sistema.

**Learning chain:** Reconocimiento → puerto elevado → ruta oculta → identificación de usuario/versión → explotación → extracción de datos (hashes).

**Lección:** *Los servicios en puertos no estándar y las rutas ocultas solo retrasan, no detienen, a quien hace fuzzing sistemático; la versión de cada componente es la llave del compromiso.*

**MITRE ATT&CK:** T1046 Network Service Discovery · T1190 Exploit Public-Facing Application · T1005 Data from Local System · T1078 Valid Accounts.

**Fuente:** [TryHackMe - Sustah](https://tryhackme.com/room/sustah)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.