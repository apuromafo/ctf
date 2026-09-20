# dogcat

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `dogcat` |
| **Link** | [TryHackMe](https://tryhackme.com/room/dogcat) |
| **Sección** | 02 Level Medium |
| **Fuente** | thmrevenant (GitHub) |
| **Componentes** | LFI / php://filter / log poisoning / LFI to RCE / Docker / container escape / escalada de privilegios |
| **Impacto** | Cadena completa: LFI con filtros PHP, envenenamiento de logs para RCE, escape de contenedor Docker y escalada a root con cuatro flags |

---

**Contexto:** dogcat es una sala CTF clásica de PHP que arranca con un LFI (Local File Inclusion) cuyo parámetro filtra las palabras "dog" y "cat". Usando filtros `php://` y, después, el envenenamiento de los logs de Apache, se consigue ejecutar comandos (LFI to RCE). El shell resultante vive dentro de un contenedor Docker; gracias al script de compatibilidad y al directorio de backups del entorno se escapa del contenedor y se escala hasta root, obteniendo en total cuatro flags.

## Solucionario

### Task 1: Flags del reto

**Explicación:** La resolución completa de la sala reporta cuatro flags: la primera **THM{Th1s_1s_N0t_4_Catdog_ab67edfa}** (lectura de archivos vía LFI), la segunda **THM{LF1_t0_RC3_aec3fb}** (LFI convertido en RCE), la tercera **THM{D1ff3r3nt_3nv1ronments_874112}** (escape del contenedor a un entorno distinto) y la cuarta **THM{esc4l4tions_on_esc4l4tions_on_esc4l4tions_7a52b17dba6ebb0dc38bc1049bcba02d}** (root).

1. THM{Th1s_1s_N0t_4_Catdog_ab67edfa}
2. THM{LF1_t0_RC3_aec3fb}
3. THM{D1ff3r3nt_3nv1ronments_874112}
4. THM{esc4l4tions_on_esc4l4tions_on_esc4l4tions_7a52b17dba6ebb0dc38bc1049bcba02d}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag de la fase LFI? | `THM{Th1s_1s_N0t_4_Catdog_ab67edfa}` |
| 2 | ¿Cuál es la flag de la fase LFI a RCE? | `THM{LF1_t0_RC3_aec3fb}` |
| 3 | ¿Cuál es la flag del entorno/contenedor? | `THM{D1ff3r3nt_3nv1ronments_874112}` |
| 4 | ¿Cuál es la flag final (root)? | `THM{esc4l4tions_on_esc4l4tions_on_esc4l4tions_7a52b17dba6ebb0dc38bc1049bcba02d}` |

---

**Metodología:**

1. Enumerar la web y detectar el parámetro vulnerable a LFI que fuerza la inclusión de archivos con "dog" o "cat".
2. Abusar del filtro encadenando los parámetros y usando `php://filter/convert.base64-encode/resource=` para leer el código fuente.
3. Escalar a RCE envenenando los logs de Apache con un payload PHP (User-Agent con `<?php system($_GET['c']); ?>`).
4. Dentro del contenedor, localizar el script de compatibilidad y el directorio de backups (montado en el host) para el escape.
5. Escalar a root aprovechando el cron/script de backup y leer las flags de cada fase.

**Learning chain:** LFI (php://filter) -> Bypass filtro dog/cat -> Log poisoning -> LFI to RCE -> Shell en contenedor -> Docker escape -> Escalada a root -> Flags

**Lección:** *Un LFI aparentemente restringido se convierte en RCE combinando filtros php://, envenenamiento de logs y conocimiento de la arquitectura del contenedor.*

**MITRE ATT&CK:** T1059.004 (Unix Shell), T1083 (File and Directory Discovery), T1610 (Deploy Container), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - dogcat](https://tryhackme.com/room/dogcat)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.