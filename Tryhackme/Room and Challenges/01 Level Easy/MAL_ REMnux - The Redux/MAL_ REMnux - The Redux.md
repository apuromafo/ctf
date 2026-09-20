# MAL_ REMnux - The Redux

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `malremnuxtheredux` | [TryHackMe](https://tryhackme.com/room/malremnuxtheredux) | 01 Level Easy | TryHackMe | REMnux / malware analysis / strings / upx / FLOSS / C2 | Uso de REMnux para analizar malware: extracción de cadenas, detección de packers y malwares ocultos |

---

**Contexto:** Sala práctica centrada en el uso de REMnux, la distribución Linux especializada en análisis de malware. Se trabaja con muestras reales para extraer cadenas útiles, identificar contenido malicioso, detectar packers y analizar la comunicación con servidores de comando y control (C2).

## Solucionario

### Task 1

**Explicación:** Presentación de la sala, no requiere respuesta escrita.

1. No answer needed

### Task 2

**Explicación:** Tarea introductoria con preguntas conceptuales, no requiere respuesta escrita.

1. No answer needed

### Task 3

**Explicación:** Se analiza una muestra con REMnux: cantidad de cadenas extraídas, contenido del mensaje oculto, número de archivos y el nombre del ejecutable no sospechoso.

1. 3
2. THM{Luckily_This_Isn't_Harmful}
3. 6
4. notsuspicious

### Task 4

**Explicación:** Se identifica el nombre del ejecutable con apariencia legítima y la URL de comunicación con el servidor de comando y control.

1. DefoLegit
2. http://tryhackme.com/notac2cserver.sh

### Task 5

**Explicación:** Se extraen datos del binario: número de secciones, valor del checksum y la herramienta de empaquetado detectada.

1. 8
2. 0
3. UPX

### Task 6

**Explicación:** Tarea de análisis, no requiere respuesta escrita.

1. No answer needed

### Task 7

**Explicación:** Tarea de análisis, no requiere respuesta escrita.

1. No answer needed

### Task 8

**Explicación:** Conclusión de la sala, no requiere respuesta escrita.

1. No answer needed

---

| # | Task | Respuesta |
|---|------|-----------|
| 1 | Task 1 | No answer needed |
| 2 | Task 2 | No answer needed |
| 3 | Task 3 | `3` |
| 4 | Task 3 | `THM{Luckily_This_Isn't_Harmful}` |
| 5 | Task 3 | `6` |
| 6 | Task 3 | `notsuspicious` |
| 7 | Task 4 | `DefoLegit` |
| 8 | Task 4 | `http://tryhackme.com/notac2cserver.sh` |
| 9 | Task 5 | `8` |
| 10 | Task 5 | `0` |
| 11 | Task 5 | `UPX` |
| 12 | Task 6 | No answer needed |
| 13 | Task 7 | No answer needed |
| 14 | Task 8 | No answer needed |

---

**Metodología:** Se utilizan las herramientas de REMnux para inspeccionar las muestras proporcionadas: extracción de strings con herramientas como `strings` y `FLOSS`, análisis de ejecutables para detectar el empaquetado (UPX), cálculo de secciones y checksums, y búsqueda de indicadores de comando y control (URLs de C2) dentro de los binarios.

### Cadena de ataque / Attack Chain

```text
revisión de la muestra -> extracción de strings -> identificación del flag oculto -> detección de packer (UPX) -> análisis de secciones -> localización del C2 (notac2cserver.sh)
```

**Learning chain:** REMnux setup → strings extraction → FLOSS → UPX packing detection → section analysis → C2 identification

**Lección:** *REMnux concentra todas las herramientas necesarias para el análisis estático de malware; extraer cadenas y reconocer packers como UPX revela el comportamiento y las comunicaciones del binario.*

**MITRE ATT&CK:** T1027 (Obfuscated Files or Information), T1140 (Deobfuscate/Decode Files or Information), T1071.001 (Application Layer Protocol: Web Protocols)

**Fuente:** [TryHackMe - MAL_ REMnux - The Redux](https://tryhackme.com/room/malremnuxtheredux)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.