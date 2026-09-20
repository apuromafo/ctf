# Intro to Cold System Forensics

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `introtocoldsystemforensics` | https://tryhackme.com/room/introtocoldsystemforensics | 01 Level Easy | TryHackMe | cold boot attack / order of volatility / disk imaging / hash (integridad) / chain of custody / hibernación | Aplicar forensia sobre sistemas en estado dormido o apagado: adquisición bit a bit, jerarquía de volatilidad de las evidencias y documentación de la cadena de custodia. |

---

**Contexto:** La room aborda la forensia digital en sistemas "fríos" (en reposo o apagados). Se explica en qué estados se aplica (Dormant/Powered-off), la base investigadora del *cold boot attack*, la adquisición bit a bit (**disk imaging**), las medidas de preservación (control de acceso, integridad con hashes) y el orden de volatilidad de las fuentes de evidencia. Se cierra con dos retos prácticos: Order of Volatility y Chain of Custody.

> **ES:** Forensia en sistemas apagados: cold boot attack, adquisición bit a bit de disco, integridad mediante hashes, control de acceso, orden de volatilidad y cadena de custodia, con dos retos prácticos de flags.
> **EN:** Forensics on powered-off systems: cold boot attack, bit-by-bit disk imaging, hash-based integrity, access control, order of volatility and chain of custody, with two practical flag challenges.

## Solucionario

### Task 1: Introduction / Introducción

**Explicación:** Se presenta la disciplina de la cold system forensics (forensia en sistemas fríos), orientada a recuperar y preservar evidencia de equipos dormidos o apagados. Sirve de marco para las tareas siguientes. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Deploy the machine and read the introduction. / Despliega la máquina y lee la introducción. | `No answer needed` |

### Task 2: Cold Boot Attack / Ataque de arranque en frío

**Explicación:** La forensia en frío se aplica principalmente bajo dos estados del sistema: **Dormant o Powered-off** (dormido o apagado). La base investigadora de esta disciplina es el **cold boot attack** (ataque de arranque en frío), que demostró que la memoria RAM conserva datos residuales unos segundos tras cortar la alimentación y permite recuperarlos congelando/preparando los módulos de memoria.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Under what two system states are cold system forensics mainly applied? / ¿Bajo qué dos estados del sistema se aplica principalmente la forensia en frío? | `Dormant or Powered-off` |
| 2 | What type of attack provided a research basis for cold system forensics? / ¿Qué tipo de ataque sirvió de base de investigación para la forensia en frío? | `cold boot attack` |

### Task 3: Data Acquisition and Preservation / Adquisición y preservación de datos

**Explicación:** La adquisición forense consiste en hacer una copia **bit a bit** del medio: es el **disk imaging** (imageado de disco). Para restringir el acceso a datos sensibles se usan medidas de **Access control** (control de acceso). Además, la evidencia debe priorizarse por volatilidad: las fuentes más volátiles de un host son los **CPU registers and cache** (registros y caché de la CPU), que se pierden en milisegundos al apagar el equipo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | The making of a bit-by-bit copy of forensic data is known as? / ¿Cómo se llama la realización de una copia bit a bit de los datos forenses? | `Disk imaging` |
| 2 | What restricts access to sensitive data? / ¿Qué restringe el acceso a los datos sensibles? | `Access control` |
| 3 | Which sources of evidence are part of the most volatile on a host? / ¿Qué fuentes de evidencia son las más volátiles de un host? | `CPU registers and cache` |

### Task 4: Forensic Tools / Herramientas forenses

**Explicación:** Las funciones hash (SHA-256, MD5...) se usan para garantizar la **data integrity** (integridad de los datos): cualquier alteración de la imagen modifica el hash y delata la manipulación. La documentación que registra cada pieza de evidencia y quién/es se responsabilizan de ella es la **chain of custody** (cadena de custodia), imprescindible para que la prueba sea admisible en juicio.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Using hash functions seeks to minimise risks associated with what element? / ¿Con qué elemento busca minimizar riesgos el uso de funciones hash? | `data integrity` |
| 2 | What is the name of the documentation responsible for listing the forensic evidence and its accompanying responsibilities? / ¿Cómo se llama la documentación encargada de listar la evidencia forense y sus responsabilidades? | `chain of custody` |

### Task 5: Practical: Order of Volatility and Chain of Custody / Práctica: Orden de volatilidad y cadena de custodia

**Explicación:** Dos retos prácticos: en *Order of Volatility* se ordenan las fuentes de evidencia de más a menos volátiles; en *Chain of Custody* se documenta el recorrido de cada evidencia. Completar cada reto entrega una flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What flag do you receive after completing the Order of Volatility challenge? / ¿Qué flag recibes al completar el reto Order of Volatility? | `THM{729a68a1253a5f4c7126110c0c600740}` |
| 2 | What flag do you receive after completing the Chain of Custody challenge? / ¿Qué flag recibes al completar el reto Chain of Custody? | `THM{4de91692a4057c140d5a09875aba0431}` |

### Task 6: Conclusion / Conclusión

**Explicación:** Recapitulación: en sistemas fríos la adquisición debe ser rápida y ordenada (de lo más volátil a lo persistente), documentando cada paso. Enlaza con recursos para profundizar. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the conclusion. / Lee la conclusión de la room. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Under what two system states are cold system forensics mainly applied? | `Dormant or Powered-off` |
| 2 | What type of attack provided a research basis for cold system forensics? | `cold boot attack` |
| 3 | The making of a bit-by-bit copy of forensic data is known as? | `Disk imaging` |
| 4 | What restricts access to sensitive data? | `Access control` |
| 5 | Which sources of evidence are part of the most volatile on a host? | `CPU registers and cache` |
| 6 | Using hash functions seeks to minimise risks associated with what element? | `data integrity` |
| 7 | What is the name of the documentation responsible for listing the forensic evidence and its accompanying responsibilities? | `chain of custody` |
| 8 | What flag do you receive after completing the Order of Volatility challenge? | `THM{729a68a1253a5f4c7126110c0c600740}` |
| 9 | What flag do you receive after completing the Chain of Custody challenge? | `THM{4de91692a4057c140d5a09875aba0431}` |

---

**Metodología:** Enfoque de preservación por volatilidad: (1) identificar los estados aplicables (dormido/apagado) y la base investigadora (cold boot attack); (2) adquirir copias bit a bit (disk imaging) con control de acceso; (3) priorizar las fuentes de evidencia de mayor a menor volatilidad (registros y caché de CPU primero); (4) garantizar la integridad con hashes; (5) documentar cada pieza en la cadena de custodia; (6) validar el proceso en los retos prácticos Order of Volatility y Chain of Custody.

### Cadena de ataque / Attack Chain

```text
Sistema Dormant/Powered-off -> identificación de evidencia -> disk imaging bit a bit -> acceso controlado -> orden de volatilidad (CPU registers & cache) -> hash de integridad -> chain of custody -> retos prácticos (flags)
```

**Learning chain:** Estados (dormido/apagado) -> cold boot attack -> adquisición bit a bit -> volatilidad -> integridad (hash) -> cadena de custodia -> práctica.

**Lección:** *En forensia la velocidad está ordenada por la volatilidad: los registros y la caché de la CPU viven milisegundos, así que se capturan primero; la integridad (hashes) y la cadena de custodia son las que hacen que la evidencia sobreviva al juzgado.*

**MITRE ATT&CK:** T1005 (Data from Local System), T1560 (Archive Collected Data), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - Intro to Cold System Forensics](https://tryhackme.com/room/introtocoldsystemforensics)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.