# Overpass 3 - Hosting

| **Dificultad** | MEDIUM | **Tipo** | CTF (Free) | **Slug** | `overpass3hosting` |
| **Link** | [TryHackMe](https://tryhackme.com/room/overpass3hosting) | **Sección** | Linux / CTF | **Fuente** | Writeup de thmrevenant (GitHub) |
| **Componentes** | Web exploitation, upload/injection, privilege escalation, hosting infrastructure | **Impacto** | Compromiso total del servidor de hosting: acceso inicial web, escalada de privilegios de usuario y de root, capturando las tres flags del sistema |

---

**Contexto:** Esta sala es un CTF de una empresa de hosting que ha sido comprometida. El objetivo es explotar una vulnerabilidad en la aplicación web de hosting para obtener acceso inicial, escalar privilegios dentro del sistema y conseguir control total, capturando de manera secuencial tres flags: la web flag, el user flag y el root flag. Requiere combinar reconocimiento web, explotación y múltiples vectores de escalada de privilegios.

> **ES:** CTF de una empresa de hosting comprometida donde se debe explotar una vulnerabilidad web, escalar privilegios y obtener control total del sistema a través de tres flags (web, usuario y root).
> **EN:** CTF of a compromised hosting company where you must exploit a web vulnerability, escalate privileges, and gain full control of the system through three flags (web, user, and root).

## Solucionario

### Task 1: Captura de Flags / Flags Capture

**Explicación:** Se realiza el reconocimiento de la aplicación web de hosting para identificar la vulnerabilidad explotable (probablemente subida de archivos o inyección), obteniendo así acceso inicial y la web flag. Posteriormente se escalan privilegios para acceder al usuario comprometido y capturar el user flag en su directorio, y finalmente se escala a root mediante vectores de privilegios para capturar el root flag.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Web Flag | `thm{0ae72f7870c3687129f7a824194be09d}` |
| User Flag | `thm{3693fc86661faa21f16ac9508a43e1ae}` |
| Root flag | `thm{a4f6adb70371a4bceb32988417456c44}` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Web Flag | `thm{0ae72f7870c3687129f7a824194be09d}` |
| 1.2 | User Flag | `thm{3693fc86661faa21f16ac9508a43e1ae}` |
| 1.3 | Root flag | `thm{a4f6adb70371a4bceb32988417456c44}` |

---

**Metodología:**

1. **Paso / Step:** Realizar reconocimiento de la aplicación web de hosting para identificar vulnerabilidades / Perform reconnaissance of the hosting web application to identify vulnerabilities.
2. **Paso / Step:** Explotar la vulnerabilidad web para obtener acceso inicial al servidor / Exploit the web vulnerability to gain initial access to the server.
3. **Paso / Step:** Localizar y capturar la web flag en el contenido de la aplicación o del servidor / Locate and capture the web flag in the application content or on the server.
4. **Paso / Step:** Escalar privilegios en el sistema para obtener acceso al usuario / Escalate privileges on the system to gain access to the user.
5. **Paso / Step:** Capturar el user flag en el directorio del usuario comprometido / Capture the user flag in the compromised user's directory.
6. **Paso / Step:** Escalar a root mediante vectores de privilegios y capturar el root flag / Escalate to root through privilege vectors and capture the root flag.

### Cadena de ataque / Attack Chain

```
Reconocimiento de la aplicación de hosting
  -> Explotación de vulnerabilidad web (probablemente subida de archivos o inyección)
    -> Web flag obtenida
      -> Escalada de privilegios de usuario
        -> User flag obtenida
          -> Escalada a root
            -> Root flag obtenida: thm{a4f6adb70371a4bceb32988417456c44}
```

**Learning chain:** Reconocimiento de la aplicación de hosting → Explotación de la vulnerabilidad web (subida de archivos/inyección) → Web flag → Escalada de privilegios de usuario → User flag → Escalada a root → Root flag.

**Lección:** *En un CTF de hosting es fundamental combinar el reconocimiento de la aplicación web con múltiples vectores de escalada de privilegios. La captura secuencial de flags (web, user, root) requiere entender completamente la infraestructura del servidor y sus permisos.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1083 (File and Directory Discovery), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Overpass 3 - Hosting](https://tryhackme.com/room/overpass3hosting)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.