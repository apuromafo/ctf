# Ninja Skills

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `ninjaskills` | https://tryhackme.com/room/ninjaskills | 01 Level Easy | TryHackMe | find, cat, Linux CLI, archivos ocultos | Formativo — localización y lectura de archivos ocultos con comandos básicos de Linux |

---

**Contexto:** Sala de práctica de comandos de Linux: localizar dentro del sistema los archivos ocultos con los nombres indicados y leer su contenido. Las respuestas son los nombres de los archivos ocultos distribuidos por el sistema de laboratorio: `D8B3 v2Vb`, `oiMO`, `c4ZX`, `bny0`, `X1Uy` y `8V2L`, obtenidos mediante comandos como `find`, `cat` y otros del shell.

> **ES:** Localización de archivos ocultos con find, cat y comandos de Linux: los seis nombres de archivo distribuidos por el sistema se listan como respuestas del reto.
> **EN:** Locating hidden files with find, cat and Linux commands: the six file names distributed across the system are listed as the challenge answers.

## Solucionario

### Task 1: Localización de Archivos / Locating Files

**Explicación:** Aplicando los comandos de Linux (`find`, `cat` y utilidades del shell) se localizan los archivos ocultos distribuidos por el sistema de laboratorio y se leen sus nombres como respuestas del reto. Las seis líneas corresponden a seis archivos ocultos encontrados.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el primer nombre de archivo oculto encontrado? | `D8B3 v2Vb` |
| 2 | ¿Cuál es el segundo nombre de archivo oculto encontrado? | `oiMO` |
| 3 | ¿Cuál es el tercer nombre de archivo oculto encontrado? | `c4ZX` |
| 4 | ¿Cuál es el cuarto nombre de archivo oculto encontrado? | `bny0` |
| 5 | ¿Cuál es el quinto nombre de archivo oculto encontrado? | `X1Uy` |
| 6 | ¿Cuál es el sexto nombre de archivo oculto encontrado? | `8V2L` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el primer nombre de archivo oculto encontrado? | `D8B3 v2Vb` |
| 2 | ¿Cuál es el segundo nombre de archivo oculto encontrado? | `oiMO` |
| 3 | ¿Cuál es el tercer nombre de archivo oculto encontrado? | `c4ZX` |
| 4 | ¿Cuál es el cuarto nombre de archivo oculto encontrado? | `bny0` |
| 5 | ¿Cuál es el quinto nombre de archivo oculto encontrado? | `X1Uy` |
| 6 | ¿Cuál es el sexto nombre de archivo oculto encontrado? | `8V2L` |

---

**Metodología:** Se recorre el sistema de laboratorio combinando los comandos `find`, `cat` y otras utilidades del shell para descubrir los archivos ocultos con los nombres dados y listarlos como respuesta del reto.

### Cadena de ataque / Attack Chain

```text
Exploración del sistema -> find/glob de nombres ocultos -> cat de su contenido -> listado de nombres como respuestas del reto -> verificación
```

**Learning chain:** exploración del sistema de ficheros → localización de archivos ocultos → lectura con cat → listado de respuestas.

**Lección:** *Los archivos ocultos y las rutas inusuales son el escondite clásico de los datos sensibles; la búsqueda sistemática con `find` y `cat` es la técnica base para descubrirlos.*

**MITRE ATT&CK:** T1083 (File and Directory Discovery), T1005 (Data from Local System)

**Fuente:** [TryHackMe - Ninja Skills](https://tryhackme.com/room/ninjaskills)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.