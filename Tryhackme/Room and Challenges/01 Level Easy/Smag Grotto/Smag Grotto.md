# Smag Grotto

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | Boot2Root | smaggrotto | https://tryhackme.com/room/smaggrotto | 01 Level Easy | TryHackMe | Enumeración, Explotación web, Escalada de privilegios | Crítico |

---

**Contexto:**
> **ES:** Máquina Boot2Root de nivel Easy. La resolución consiste en enumerar el sistema, explotar la aplicación web y escalar privilegios para obtener las dos flags del laboratorio.
> **EN:** An Easy Boot2Root machine. The walkthrough consists of enumerating the system, exploiting the web application, and escalating privileges to obtain the two flags of the lab.

## Solucionario

### Task 1: Obtención de flags / Capturing the Flags
**Explicación:**
La única tarea del laboratorio entrega dos flags (usuario y root) tras la explotación y la escalada de privilegios.

```
1. 1. iusGorV7EbmxM5AuIe2w499msaSuqU3j
   2. uJr6zRgetaniyHVRqqL58uRasybBKz2T
```

### Tabla unificada de preguntas/respuestas

| # | Respuesta |
|---|---|
| 1.1 | `iusGorV7EbmxM5AuIe2w499msaSuqU3j` |
| 1.2 | `uJr6zRgetaniyHVRqqL58uRasybBKz2T` |

---

**Metodología:**
1. Enumeración de puertos y servicios.
2. Análisis y explotación de la aplicación web.
3. Escalada de privilegios en el sistema.
4. Captura de las flags de usuario y root.

### Cadena de ataque / Attack Chain
Enumeración → Explotación web → Escalada de privilegios → Flag de usuario → Flag de root.

**Learning chain:**
Reconocimiento → explotación → escalada → flags.

**Lección:** *La persistencia en la enumeración y la correcta explotación de la aplicación web son la clave para conseguir ambas flags.*

**MITRE ATT&CK:**
| Técnica | ID |
|---|---|
| Network Service Discovery | T1046 |
| Exploit Public-Facing Application | T1190 |
| Exploitation for Privilege Escalation | T1068 |
| File and Directory Discovery | T1083 |

**Fuente:** [TryHackMe - Smag Grotto](https://tryhackme.com/room/smaggrotto)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.