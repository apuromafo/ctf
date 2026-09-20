# Metasploit_ Introduction

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `metasploitintroduction` | [TryHackMe](https://tryhackme.com/room/metasploitintroduction) | 01 Level Easy | THM | msfconsole, modules, search, set/setg, exploit | Introducción al uso básico del framework Metasploit |

> **Objeto:** Conocer los módulos del framework Metasploit, su consola msfconsole y los comandos básicos de búsqueda y configuración de exploits y payloads.

---

**Contexto:** Sala introductoria a Metasploit: se explican los tipos de módulos (exploit, payload, auxiliares, encoders/nops y singles), la búsqueda de módulos con `search`, la base de datos `todb`, y la configuración de opciones con `set`/`setg`, hasta lanzar el exploit.

> **ES:** Sala introductoria a Metasploit: módulos, búsqueda, base de datos y configuración de exploits y payloads.
> **EN:** Introductory room to Metasploit: modules, search, database and exploit/payload configuration.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación de la sala y del framework Metasploit.

No answer needed

### Task 2: Módulos de Metasploit / Metasploit modules
**Explicación:** Se identifican los tipos de módulos del framework y sus características.

1. Exploit
2. Payload
3. Singles
4. Singles

### Task 3: Búsqueda de módulos / Module search
**Explicación:** Se utilizan los comandos `search` y la base de datos `todb` para localizar módulos.

1. search apache
2. todb

### Task 4: Configuración y ejecución / Configuration and execution
**Explicación:** Se configura el exploit con las opciones LPORT, RHOSTS y PAYLOAD, y se lanza contra el objetivo.

1. set LPORT 6666
2. setg RHOSTS 10.10.19.23
3. unset PAYLOAD
4. exploit

### Task 5: Conclusión / Conclusion
**Explicación:** Cierre de la sala y repaso de los comandos aprendidos.

No answer needed

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | — | `No answer needed` |
| 2.1 | Módulo 1 | `Exploit` |
| 2.2 | Módulo 2 | `Payload` |
| 2.3 | Módulo 3 | `Singles` |
| 2.4 | Módulo 4 | `Singles` |
| 3.1 | Comando de búsqueda | `search apache` |
| 3.2 | Base de datos del framework | `todb` |
| 4.1 | Configuración del puerto local | `set LPORT 6666` |
| 4.2 | Configuración global del host remoto | `setg RHOSTS 10.10.19.23` |
| 4.3 | Limpieza del payload | `unset PAYLOAD` |
| 4.4 | Lanzamiento del exploit | `exploit` |
| 5 | — | `No answer needed` |

---

**Metodología:** Arranque de msfconsole, identificación de los tipos de módulos del framework, uso de `search` y de la base de datos `todb` para localizar módulos, configuración de opciones con `set`/`setg` y lanzamiento del exploit seleccionado.

### Cadena de ataque / Attack Chain

msfconsole → módulos del framework → búsqueda (search) → base de datos (todb) → configuración (set/setg) → exploit.

**Learning chain:** Metasploit → módulos → search → todb → configuración → exploit

*Lección:* Entender la jerarquía de módulos y los comandos de búsqueda y configuración es el primer paso para usar Metasploit con eficacia.

**MITRE ATT&CK:** T1190 - Exploit Public-Facing Application, T1059 - Command and Scripting Interpreter.

**Fuente:** [TryHackMe - Metasploit_ Introduction](https://tryhackme.com/room/metasploitintroduction)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.