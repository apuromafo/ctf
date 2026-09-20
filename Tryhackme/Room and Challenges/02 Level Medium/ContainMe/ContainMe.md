# ContainMe

| Campo | Valor |
|---|---|
| Dificultad | Medium |
| Tipo | CTF |
| Slug | containme |
| Link | https://tryhackme.com/room/containme |
| Sección | 02 Level Medium |
| Fuente | TryHackMe |
| Componentes | Contenedores, Docker, enumeración |
| Impacto | Escape de contenedor y obtención de flags |

---

**Contexto:** ContainMe es una sala de TryHackMe de dificultad media centrada en contenedores Docker. El participante debe enumerar contenedores en ejecución, identificar servicios internos y encontrar la flag oculta. Se enfoca en habilidades de enumeración de contenedores y comprensión de su arquitectura.

## Solucionario

### Task 1: Fundamentos de contenedores

**Explicación:** Se completó la tarea introductoria sobre fundamentos de contenedores.

No answer needed

### Task 2: Obtención de la flag

**Explicación:** Se enumeraron los contenedores en ejecución, se accedió al contenedor objetivo y se obtuvo la flag.

THM{_Y0U_F0UND_TH3_C0NTA1N3RS_}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tarea introductoria | `No answer needed` |
| 2 | Flag | `THM{_Y0U_F0UND_TH3_C0NTA1N3RS_}` |

---

**Metodología:** Enumeración de contenedores Docker, inspección de servicios internos, navegación entre namespaces y obtención de la flag.

**Learning chain:** Enumeración de contenedores → identificación de servicios → acceso al contenedor → obtención de la flag.

**Lección:** *Los contenedores Docker mal configurados pueden exponer servicios internos y permitir la obtención de credenciales o flags.*

**MITRE ATT&CK:** T1610 - Deploy Container, T1082 - System Information Discovery

**Fuente:** [TryHackMe - ContainMe](https://tryhackme.com/room/containme)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.