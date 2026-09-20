# Chrome

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Reto • Forense | chrome | https://tryhackme.com/room/chrome | 03 Level Hard | TryHackMe | Análisis de navegador, credenciales almacenadas, historial | Medio |

---

**Contexto:**
> **ES:** Laboratorio forense sobre el navegador Chrome: análisis de perfiles, historial, marcadores y credenciales almacenadas para reconstruir la actividad del usuario.
> **EN:** Forensics lab on the Chrome browser: analysis of profiles, history, bookmarks and stored credentials to reconstruct user activity.

## Solucionario

### Task 1: Análisis de Chrome / Chrome analysis
**Explicación:**
1. bubbles
2. hxxps[://]mysecuresite[.]thm/
3. Sup3rPaS$w0rd1
4. hxxps[://]worksite[.]thm/
5. Sup3rSecuR3!

### Preguntas y Respuestas / Questions and Answers

| Task | Respuesta / Answer |
|---|---|
| 1.1 | `bubbles` |
| 1.2 | `hxxps[://]mysecuresite[.]thm/` |
| 1.3 | `Sup3rPaS$w0rd1` |
| 1.4 | `hxxps[://]worksite[.]thm/` |
| 1.5 | `Sup3rSecuR3!` |

---

**Metodología:**
Análisis forense del perfil de Chrome: extracción del nombre de usuario, sitios visitados (ofuscados para su neutralización) y credenciales almacenadas por el navegador.

### Cadena de ataque / Attack Chain
1. Identificación del perfil de usuario en los datos del navegador.
2. Inspección de credenciales almacenadas.
3. Reconstrucción de los sitios visitados.
4. Recuperación de las contraseñas guardadas.
5. Correlación de la actividad completa del usuario.

**Learning chain:**
Perfil -> Credenciales -> Historial -> Correlación de actividad.

**Lección:** *El navegador es una mina forense: credenciales y comportamiento del usuario quedan registrados aunque estén ofuscados.*

**MITRE ATT&CK:**
- T1555.003 Credentials from Web Browsers
- T1005 Data from Local System

**Fuente:** [TryHackMe - Chrome](https://tryhackme.com/room/chrome)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.