# pyLon

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Walkthrough | pylon | https://tryhackme.com/room/pylonzf | 02 Level Medium | TryHackMe | Cifrado, OpenVPN, Shell scripts, Python, Escalada | Compromiso de usuarios y root / flags |

---

**Contexto:** La sala **pyLon** es un reto basado en el pentesting de un sistema en el que conviven un gestor de contraseñas casero, cifrado casero (homebrew) y un perfil de OpenVPN vulnerable. La resolución comienza con un reconocimiento sin respuesta, continúa con la penetración del sistema aprovechando los archivos extraídos y el script de OpenVPN, y culmina con la captura de las flags de usuario y de root.

## Solucionario

### Task 1: Recon / Recon
**Explicación:**

Fase de reconocimiento inicial sobre el objetivo; las respuestas no requieren contestarse.

```
1. No answer needed
2. No answer needed
```

Respuestas: `No answer needed`

### Task 2: pyLon / pyLon
**Explicación:**

Tras extraer los archivos, se intenta penetrar en el sistema: se identifica el gestor de contraseñas casero, se recupera la flag de los dos usuarios y se escala hasta root abusando del script de OpenVPN vulnerable.

You extracted some files, and now you will attempt to penetrate the system.

What is Flag 1?
`THM{homebrew_password_manager}`

What is User1 flag?
`TMM{easy_does_it}`

What is User2 flag?
`THM{homebrew_encryption_lol}`

What is root's flag?
`ThM{OpenVPN_script_pwn}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Tarea de recon (sin respuesta) | `No answer needed` |
| 1.2 | Tarea de recon (sin respuesta) | `No answer needed` |
| 2.1 | What is Flag 1? | `THM{homebrew_password_manager}` |
| 2.2 | What is User1 flag? | `TMM{easy_does_it}` |
| 2.3 | What is User2 flag? | `THM{homebrew_encryption_lol}` |
| 2.4 | What is root's flag? | `ThM{OpenVPN_script_pwn}` |

---

**Metodología:** Reconocimiento del sistema, extracción y análisis de los archivos, revisión del gestor de contraseñas y de la encriptación casera, inspección del perfil OpenVPN y abuso del script para escalar a root.

### Cadena de ataque / Attack Chain

```
Reconocimiento (sin respuesta requerida)
        │
        ▼
Extracción y análisis de archivos
        │
        ▼
Gestor de contraseñas casero → Flag 1
        │
        ▼
Descifrado casero → Flags de User1/User2
        │
        ▼
Abuso del script OpenVPN → Flag root
```

**Learning chain:** Recon → extracción de archivos → password manager → crackeo/descifrado → script OpenVPN → root.

**Lección:** *El cifrado casero (homebrew) y los scripts de OpenVPN sin validar son puntos débiles clásicos: la criptografía se debe delegar en bibliotecas estándar y los scripts de VPN deben sanear cualquier entrada del entorno.*

**MITRE ATT&CK:** T1552 Unsecured Credentials · T1083 File and Directory Discovery · T1068 Exploitation for Privilege Escalation · T1059.004 Command and Scripting Interpreter (Unix Shell).

**Fuente:** [TryHackMe - pyLon](https://tryhackme.com/room/pylonzf)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.