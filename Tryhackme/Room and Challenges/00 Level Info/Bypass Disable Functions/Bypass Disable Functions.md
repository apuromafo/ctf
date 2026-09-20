# Bypass Disable Functions

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Info | walkthrough | `bypassdisablefunctions` | [TryHackMe](https://tryhackme.com/room/bypassdisablefunctions) | 00 Level Info | TryHackMe | PHP, php.ini, disable_functions, LD_PRELOAD, RCE | Bypass de la directiva disable_functions de PHP mediante LD_PRELOAD para ejecutar comandos en servidores comprometidos |

---

**Contexto:** Sala centrada en la técnica de evasión de la restricción `disable_functions` de PHP: cuando un servidor web comprometido bloquea funciones de ejecución (system, exec, passthru, etc.), se puede abusar de `LD_PRELOAD` para cargar una biblioteca maliciosa y conseguir ejecución remota de comandos. El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

## Solucionario

### Task 1: Configuración / Setup

**Explicación:** Pregunta de arranque de la sala sobre la configuración del entorno (servidor PHP comprometido), sin respuesta que introducir. Respuesta original: `No answer needed`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |

### Task 2: Bypass de disable_functions / Bypassing disable_functions

**Explicación:** Se aplica el bypass de `disable_functions` mediante `LD_PRELOAD` para ejecutar comandos en el servidor y se captura la flag `thm{bypass_d1sable_functions_1n_php}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `thm{bypass_d1sable_functions_1n_php}` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Task 1, Pregunta 1 no especificada en el original)* | `No answer needed` |
| 2 | *(Task 2, Pregunta 1 no especificada en el original)* | `thm{bypass_d1sable_functions_1n_php}` |

---

**Metodología:** Comprender la restricción `disable_functions` de PHP → compilar una biblioteca compartida con `LD_PRELOAD` → forzar la carga de la biblioteca mediante un binario del sistema → ejecutar comandos en el servidor → capturar la flag.

### Cadena de ataque / Attack Chain

```text
PHP comprometido con disable_functions → biblioteca maliciosa (.so) → LD_PRELOAD → carga con binario del sistema → RCE → flag thm{bypass_d1sable_functions_1n_php}
```

**Learning chain:** Restricción disable_functions → técnica LD_PRELOAD → RCE → captura de la flag

**Lección:** *Bloquear en php.ini las funciones de ejecución no detiene a un atacante decidido: LD_PRELOAD ofrece una vía alternativa de ejecución que debe mitigarse con controles del sistema operativo, no solo de la configuración de PHP.*

**MITRE ATT&CK:** T1059 (Command and Scripting Interpreter), T1574 (Hijack Execution Flow - dynamic link library/dynamic linker hijacking), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Bypass Disable Functions](https://tryhackme.com/room/bypassdisablefunctions)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.