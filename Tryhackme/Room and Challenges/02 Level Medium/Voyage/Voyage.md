# Voyage

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | Reto / Challenge (Linux) | voyage | https://tryhackme.com/room/voyage | 02 Level Medium | TryHackMe | Enumeración web, explotación, escalada de privilegios | Media - máquina de práctica |

> **Objeto:** Comprometer la máquina objetivo mediante enumeración, explotación de la aplicación web y escalada de privilegios para obtener ambas flags.

---

**Contexto:** "Voyage" es una máquina de dificultad media basada en Linux. El reto combina enumeración de servicios, análisis de la aplicación web, obtención de acceso inicial y posterior escalada de privilegios hasta conseguir las dos flags de la máquina.

> **ES:** Máquina de práctica que guía al usuario desde la fase de reconocimiento hasta el control total del sistema.
> **EN:** Practice machine that walks the user from the recon phase to full system compromise.

## Solucionario

### Task 1: Flag de usuario y root / User & Root flag

**Explicación:** Tras enumerar la máquina, explotar la vulnerabilidad de la aplicación web y escalar privilegios para obtener las dos flags.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es la flag de usuario? / What is the user flag? | THM{ee346612fb944085af0dd2cd677b1902} |
| ¿Cuál es la flag de root? / What is the root flag? | THM{ace91ec899f84498a74629b078bdceff} |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Cuál es la flag de usuario? / What is the user flag? | `THM{ee346612fb944085af0dd2cd677b1902}` |
| 1 | ¿Cuál es la flag de root? / What is the root flag? | `THM{ace91ec899f84498a74629b078bdceff}` |

---

**Metodología:**

1. Enumeración de puertos y servicios (nmap).
2. Descubrimiento de la aplicación web y sus rutas ocultas.
3. Explotación de la vulnerabilidad para obtener una shell inversa.
4. Escalada de privilegios dentro del sistema comprometido.
5. Captura de las flags de usuario y root.

### Cadena de ataque / Attack Chain

```text
Reconocimiento -> Enumeración web -> Acceso inicial (shell) -> Escalada de privilegios -> Flags
```

**Learning chain:**

- La enumeración previa define el vector de acceso.
- Una vez con low shell, buscar binarios SUID, tareas cron o credenciales en config para escalar.
- Las máquinas "walkthrough" suelen tener un único camino claro hasta la flag de root.

**Lección:** *Sigue siempre el principio de enumeración incremental: cada salida de una fase alimenta la siguiente.*

**MITRE ATT&CK:**
- T1046 - Network Service Discovery
- T1190 - Exploit Public-Facing Application
- T1068 - Exploitation for Privilege Escalation

**Fuente:** [TryHackMe - Voyage](https://tryhackme.com/room/voyage)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.