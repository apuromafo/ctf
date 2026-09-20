# AttackerKB

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `attackerkb` |
| **Link** | [TryHackMe](https://tryhackme.com/room/attackerkb) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | AttackerKB, Webmin, CVSS, Supply Chain, backdoor |
| **Impacto** | Análisis de vulnerabilidades documentadas en AttackerKB, incluyendo un compromiso tipo Supply Chain sobre Webmin para robar contenido y tomar control del servicio. |

---

**Contexto:** La sala enseña a utilizar **AttackerKB** como plataforma de análisis de vulnerabilidades. Se investiga una entrada correspondiente a **Webmin**, se analiza su puntuación CVSS y el tipo de fallo, y posteriormente se examina un escenario de compromiso tipo **Supply Chain** en el que un paquete/instalador modificado permite inyectar un componente malicioso. Finalmente se confirma el impacto instalando una versión comprometida y extrayendo las flags de la sala.

## Solucionario

### Task 1: Introducción a AttackerKB / Introduction to AttackerKB

**Explicación:** Presentación de la plataforma AttackerKB y de cómo se utiliza para documentar, puntuar y consultar vulnerabilidades reales. Tarea informativa sin respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la introducción de la sala. | `No answer needed` |

### Task 2: Análisis de Webmin / Analyzing Webmin

**Explicación:** Se abre en AttackerKB la entrada correspondiente a Webmin y se recogen los datos básicos de la vulnerabilidad documentada: el producto afectado, su puntuación CVSS en la plataforma y el tipo de fallo/vulnerabilidad publicado.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Completar los pasos de búsqueda en AttackerKB. | `No answer needed` |
| 2 | ¿Qué producto está documentado en la entrada analizada? | `Webmin` |
| 3 | ¿Cuál es la puntuación CVSS indicada para la vulnerabilidad? | `1.890` |
| 4 | ¿Qué tipo de fuente/vulnerabilidad se indica en la entrada? | `source` |
| 5 | Registrar los datos encontrados sobre Webmin. | `No answer needed` |

### Task 3: Análisis profundo / Deep Dive

**Explicación:** Se profundiza en el análisis de la entrada de AttackerKB: se confirma la puntuación CVSS, se identifica el tipo del compromiso como **Supply Chain**, la fecha de publicación del informe y el identificador que referencia el incidente.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Paso práctico de navegación por la entrada. | `No answer needed` |
| 2 | Paso práctico de lectura de la entrada. | `No answer needed` |
| 3 | ¿Cuál es la puntuación CVSS que vuelve a aparecer en el análisis? | `1.890` |
| 4 | ¿Qué tipo de compromiso se describe? | `Supply Chain` |
| 5 | ¿Cuándo se informó/publicó el incidente? | `August 17th 2019` |
| 6 | ¿Cuál es el identificador del incidente documentado? | `12219` |
| 7 | Registrar los hallazgos del análisis profundo. | `No answer needed` |

### Task 4: Banderas / Flags

**Explicación:** Se reproduce el escenario de compromiso: al instalar una versión o componente afectado se evidencia la inyección del código malicioso (método/canal `ssl`) y aparecen dos flags que demuestran tanto el compromiso de la cadena de suministro como la importancia de mantener las instalaciones actualizadas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Paso práctico de instalación del componente afectado. | `No answer needed` |
| 2 | Paso práctico de reproducción del backdoor. | `No answer needed` |
| 3 | ¿Por qué canal/método se inyecta el componente malicioso? | `ssl` |
| 4 | ¿Cuál es la flag del compromiso de la cadena de suministro? | `THM{SUPPLY_CHAIN_COMPROMISE}` |
| 5 | ¿Cuál es la flag que recuerda la importancia de actualizar? | `THM{UPDATE_YOUR_INSTALL}` |
| 6 | Registrar el resultado del ejercicio. | `No answer needed` |

### Task 5: Conclusión / Conclusion

**Explicación:** Recapitulación de la utilidad de AttackerKB para el análisis en profundidad de vulnerabilidades y del caso de Supply Chain estudiado. No hay respuesta que enviar.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la conclusión de la sala. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la introducción de la sala. | `No answer needed` |
| 2 | Completar los pasos de búsqueda en AttackerKB. | `No answer needed` |
| 3 | ¿Qué producto está documentado en la entrada analizada? | `Webmin` |
| 4 | ¿Cuál es la puntuación CVSS indicada para la vulnerabilidad? | `1.890` |
| 5 | ¿Qué tipo de fuente/vulnerabilidad se indica en la entrada? | `source` |
| 6 | Registrar los datos encontrados sobre Webmin. | `No answer needed` |
| 7 | Paso práctico de navegación por la entrada. | `No answer needed` |
| 8 | Paso práctico de lectura de la entrada. | `No answer needed` |
| 9 | ¿Cuál es la puntuación CVSS que vuelve a aparecer en el análisis? | `1.890` |
| 10 | ¿Qué tipo de compromiso se describe? | `Supply Chain` |
| 11 | ¿Cuándo se informó/publicó el incidente? | `August 17th 2019` |
| 12 | ¿Cuál es el identificador del incidente documentado? | `12219` |
| 13 | Registrar los hallazgos del análisis profundo. | `No answer needed` |
| 14 | Paso práctico de instalación del componente afectado. | `No answer needed` |
| 15 | Paso práctico de reproducción del backdoor. | `No answer needed` |
| 16 | ¿Por qué canal/método se inyecta el componente malicioso? | `ssl` |
| 17 | ¿Cuál es la flag del compromiso de la cadena de suministro? | `THM{SUPPLY_CHAIN_COMPROMISE}` |
| 18 | ¿Cuál es la flag que recuerda la importancia de actualizar? | `THM{UPDATE_YOUR_INSTALL}` |
| 19 | Registrar el resultado del ejercicio. | `No answer needed` |
| 20 | Leer la conclusión de la sala. | `No answer needed` |

---

**Metodología:**

1. Se accede a **AttackerKB** y se localiza la entrada dedicada al producto analizado (Webmin).
2. Se recogen los datos básicos de la vulnerabilidad: producto afectado, puntuación CVSS (`1.890`) y tipo de fallo (`source`).
3. Se profundiza en el análisis de la entrada, confirmando el tipo de compromiso **Supply Chain**, la fecha del informe (`August 17th 2019`) y el identificador del incidente (`12219`).
4. Se reproduce el escenario instalando la versión/componente comprometido, confirmando la inyección maliciosa por `ssl`.
5. Se extraen las flags `THM{SUPPLY_CHAIN_COMPROMISE}` y `THM{UPDATE_YOUR_INSTALL}`.

### Cadena de ataque / Attack Chain

```
AttackerKB -> entrada Webmin (CVSS 1.890, source)
  -> Análisis profundo -> Supply Chain + fecha 2019-08-17
  -> Identificador del incidente 12219
  -> Instalar componente comprometido -> backdoor vía ssl
  -> Flags THM{SUPPLY_CHAIN_COMPROMISE} / THM{UPDATE_YOUR_INSTALL}
```

**Learning chain:** AttackerKB → Análisis de Webmin → CVSS y tipo de fallo → Supply Chain → Reproducción del backdoor → Flags

**Lección:** *El análisis estructurado de vulnerabilidades con AttackerKB permite comprender el impacto real (CVSS, tipo de fallo y origen) y evidencia cómo un compromiso de la cadena de suministro se convierte en la puerta de entrada a un sistema.*

**MITRE ATT&CK:** T1195 (Supply Chain Compromise), T1195.001 (Compromise Software Supply Chain), T1190 (Exploit Public-Facing Application)

**Fuente:** [TryHackMe - AttackerKB](https://tryhackme.com/room/attackerkb)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.