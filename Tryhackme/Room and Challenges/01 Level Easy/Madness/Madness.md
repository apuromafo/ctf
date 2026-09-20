# Madness

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | challenge | `madness` | [TryHackMe](https://tryhackme.com/room/madness) | 01 Level Easy | TryHackMe | web enumeration / steganography / image analysis / hash cracking / privesc | Obtención de accesos mediante steganografía en imágenes y escalada de privilegios en una máquina Linux |

---

**Contexto:** Sala de tipo challenge que combina reconocimiento web, extracción de pistas ocultas en imágenes mediante esteganografía y escalada de privilegios en un sistema Linux. Se requiere observar con detenimiento cada pista visual y de contenido para conseguir el acceso inicial y posteriormente el acceso como root.

## Solucionario

### Task 1

**Explicación:** Se resuelve la cadena completa de la máquina: desde la enumeración inicial y el hallazgo de pistas en imágenes hasta la escalada de privilegios, capturando las flags de usuario y de root.

1. THM{d5781e53b130efe2f94f9b0354a5e4ea}
2. THM{5ecd98aa66a6abb670184d7547c8124a}

---

| # | Task | Respuesta |
|---|------|-----------|
| 1 | Task 1 | `THM{d5781e53b130efe2f94f9b0354a5e4ea}` |
| 2 | Task 1 | `THM{5ecd98aa66a6abb670184d7547c8124a}` |

---

**Metodología:** Se inicia con la enumeración de puertos y servicios de la máquina objetivo. La inspección de los recursos web (imágenes, archivos) revela pistas ocultas que se extraen mediante técnicas de esteganografía. Con las credenciales obtenidas se accede al sistema y se captura el user flag. Finalmente se identifica un vector de escalada de privilegios que otorga acceso root y permite obtener el root flag.

### Cadena de ataque / Attack Chain

```text
nmap -> enumeración web -> análisis de imágenes -> esteganografía -> credenciales ocultas -> acceso al sistema -> user flag -> escalada de privilegios -> root flag
```

**Learning chain:** nmap scanning → web enumeration → image steganography → credential discovery → initial access → user flag → privilege escalation → root flag

**Lección:** *Las imágenes y los archivos compartidos en un sitio web pueden esconder credenciales mediante esteganografía; combinar la enumeración exhaustiva con el análisis de contenido es clave para avanzar en la máquina.*

**MITRE ATT&CK:** T1552.002 (Unsecured Credentials: Credentials in Files), T1204 (User Execution), T1059.004 (Command and Scripting Interpreter: Unix Shell)

**Fuente:** [TryHackMe - Madness](https://tryhackme.com/room/madness)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.