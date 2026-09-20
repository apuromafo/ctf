# Microsoft Windows Hardening

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `microsoftwindowshardening` | [TryHackMe](https://tryhackme.com/room/microsoftwindowshardening) | 01 Level Easy | THM | Windows Defender, UAC, PowerShell, registro, Windows 11 | Endurecimiento y configuración segura de Windows 11 |

> **Objeto:** Aplicar las mejores prácticas de hardening en Microsoft Windows: registro, UAC, firewall, PowerShell, defensa de credenciales y configuraciones de seguridad.

---

**Contexto:** Sala de hardening de Microsoft Windows: se endurecen las configuraciones del sistema (registro, contraseñas, UAC, firewall, PowerShell), se obtienen flags del registro y se comprueban ajustes de seguridad en una máquina Windows.

> **ES:** Sala de hardening de Microsoft Windows: registro, UAC, firewall, PowerShell y defensa de credenciales.
> **EN:** Microsoft Windows hardening room: registry, UAC, firewall, PowerShell and credential protection.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación de la sala y de los objetivos del endurecimiento de Windows.

No answer needed

### Task 2: Registro y credenciales / Registry and credentials
**Explicación:** Se revisan las claves del registro relacionadas con la protección de credenciales y se obtienen las flags del reto.

1. Manual
2. {THM_REG_FLAG}
3. {THM_1000710}
4. No answer needed

### Task 3: Control de cuentas / UAC
**Explicación:** Se configura el Control de Cuentas de Usuario (UAC) y se verifica el nivel de notificación.

1. Harden
2. Always Notify
3. 0

### Task 4: Firewall de Windows / Windows Firewall
**Explicación:** Se revisan los perfiles del firewall y los ajustes de red del equipo.

1. Private
2. 192.168.1.140
3. ff-ff-ff-ff-ff-ff

### Task 5: PowerShell y scripts / PowerShell and scripts
**Explicación:** Se endurece la ejecución de scripts y se comprueban las políticas de PowerShell.

1. .ps
2. nay
3. {THM_1101110}

### Task 6: Configuraciones de seguridad / Security configurations
**Explicación:** Se aplican y verifican más ajustes de seguridad y backups del sistema.

1. 377564
2. 48
3. .bkf

### Task 7: Versión del sistema / System version
**Explicación:** Se confirma la versión del sistema operativo endurecido.

1. 7.8

### Task 8: Conclusión / Conclusion
**Explicación:** Cierre de la sala y repaso de las configuraciones aplicadas.

No answer needed

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | — | `No answer needed` |
| 2.1 | Modo/configuración | `Manual` |
| 2.2 | Flag del registro | `{THM_REG_FLAG}` |
| 2.3 | Flag adicional | `{THM_1000710}` |
| 2.4 | — | `No answer needed` |
| 3.1 | Acción de hardening | `Harden` |
| 3.2 | Nivel de notificación UAC | `Always Notify` |
| 3.3 | Valor/resultado | `0` |
| 4.1 | Perfil de red/firewall | `Private` |
| 4.2 | Dirección de red | `192.168.1.140` |
| 4.3 | Dirección MAC | `ff-ff-ff-ff-ff-ff` |
| 5.1 | Extensión de scripts | `.ps` |
| 5.2 | Respuesta sí/no | `nay` |
| 5.3 | Flag de PowerShell | `{THM_1101110}` |
| 6.1 | Resultado 1 | `377564` |
| 6.2 | Resultado 2 | `48` |
| 6.3 | Extensión de backup | `.bkf` |
| 7.1 | Versión del sistema | `7.8` |
| 8 | — | `No answer needed` |

---

**Metodología:** Revisión de las claves del registro relacionadas con la defensa de credenciales, configuración del Control de Cuentas de Usuario (UAC) y del firewall con su perfil de red, endurecimiento de la ejecución de scripts de PowerShell, y verificación de los ajustes finales de seguridad y backups del sistema.

### Cadena de ataque / Attack Chain

Windows base → registro/credenciales → UAC → firewall → PowerShell → configuraciones de seguridad → verificación final.

**Learning chain:** Hardening → registro → UAC → firewall → PowerShell → versiones/backups

*Lección:* El hardening de Windows es capa por capa: registro, UAC, firewall y PowerShell deben endurecerse juntos para reducir la superficie de ataque.

**MITRE ATT&CK:** T1547 - Boot or Logon Autostart Execution, T1059 - Command and Scripting Interpreter.

**Fuente:** [TryHackMe - Microsoft Windows Hardening](https://tryhackme.com/room/microsoftwindowshardening)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.