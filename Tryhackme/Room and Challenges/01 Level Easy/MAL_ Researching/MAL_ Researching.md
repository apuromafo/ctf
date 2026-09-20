# MAL_ Researching

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `malresearching` | [TryHackMe](https://tryhackme.com/room/malresearching) | 01 Level Easy | TryHackMe | malware research / hash functions / HxD / CertUtil / osint / sample analysis | Investigación de malware: funciones hash, búsqueda OSINT de muestras y análisis de binarios |

---

**Contexto:** Sala centrada en la investigación de malware. Se exploran los conceptos de las funciones hash (MD5, SHA-1, SHA-512), las propiedades y longitudes de los resúmenes, y se practica la búsqueda de información OSINT sobre muestras de malware conocidas, además del uso de herramientas como HxD y CertUtil para el análisis de binarios.

## Solucionario

### Task 1

**Explicación:** Presentación de la sala, no requiere respuesta escrita.

1. No answer needed

### Task 2

**Explicación:** Tarea introductoria, no requiere respuesta escrita.

1. No answer needed

### Task 3

**Explicación:** Se responden preguntas conceptuales sobre las funciones hash: su unidad de medida, la longitud de sus resúmenes y los autores de los algoritmos.

1. Bit
2. Hashes
3. SHA-512
4. 100 Years
5. Ronald Rivest

### Task 4

**Explicación:** Se realiza la investigación OSINT de una muestra concreta: tipo de malware, vector de distribución, fecha del incidente, archivo ejecutable, número de infecciones y dominio malicioso asociado.

1. Trojan
2. spam emails
3. 9/16/2019, 13:54:48
4. easywindow.exe
5. 2748
6. blockchainjoblist.com

### Task 5

**Explicación:** Se calculan los hashes de la muestra con MD5 y SHA-256, y se identifica el comando de Windows para generar el hash SHA256 de un ejecutable.

1. FF395A6D528DC5724BCDE9C844A0EE89
2. 6F870C80361062E8631282D31A16872835F7962222457730BC55676A61AD1EE0
3. CertUtil -hashfile TryHackMe.exe SHA256

### Task 6

**Explicación:** Se edita el binario con un editor hexadecimal, se determina la fecha de creación del archivo y se recupera el flag oculto.

1. HxD.exe
2. 2020-02-28 11:16:36
3. THM{TryHackMe_Malware_Series_Research_Flag}

### Task 7

**Explicación:** Conclusión de la sala, no requiere respuesta escrita.

1. No answer needed

---

| # | Task | Respuesta |
|---|------|-----------|
| 1 | Task 1 | No answer needed |
| 2 | Task 2 | No answer needed |
| 3 | Task 3 | `Bit` |
| 4 | Task 3 | `Hashes` |
| 5 | Task 3 | `SHA-512` |
| 6 | Task 3 | `100 Years` |
| 7 | Task 3 | `Ronald Rivest` |
| 8 | Task 4 | `Trojan` |
| 9 | Task 4 | `spam emails` |
| 10 | Task 4 | `9/16/2019, 13:54:48` |
| 11 | Task 4 | `easywindow.exe` |
| 12 | Task 4 | `2748` |
| 13 | Task 4 | `blockchainjoblist.com` |
| 14 | Task 5 | `FF395A6D528DC5724BCDE9C844A0EE89` |
| 15 | Task 5 | `6F870C80361062E8631282D31A16872835F7962222457730BC55676A61AD1EE0` |
| 16 | Task 5 | `CertUtil -hashfile TryHackMe.exe SHA256` |
| 17 | Task 6 | `HxD.exe` |
| 18 | Task 6 | `2020-02-28 11:16:36` |
| 19 | Task 6 | `THM{TryHackMe_Malware_Series_Research_Flag}` |
| 20 | Task 7 | No answer needed |

---

**Metodología:** Se combina teoría de funciones hash con investigación OSINT: primero se responden los conceptos de hashing, luego se investiga una muestra real de malware en bases de datos públicas para obtener sus características y dominio, se calculan los hashes MD5 y SHA-256 del binario (incluyendo el comando `CertUtil -hashfile`), y finalmente se edita el ejecutable con HxD para localizar el flag en el interior del archivo.

### Cadena de ataque / Attack Chain

```text
teoría de hash -> investigación OSINT de la muestra -> identificación del trojan y del dominio -> cálculo de hashes MD5/SHA-256 -> uso de CertUtil -> edición con HxD -> recuperación del flag
```

**Learning chain:** hash functions → MD5/SHA-1/SHA-512 → OSINT research → sample identification → CertUtil hashing → HxD hex editing → flag recovery

**Lección:** *Los resúmenes hash permiten identificar muestras de malware de forma inequívoca y buscar contexto OSINT; la combinación de hashing, investigación pública y edición hexadecimal es fundamental en el análisis de binarios.*

**MITRE ATT&CK:** T1595.002 (Active Scanning: Vulnerability Scanning), T1105 (Ingress Tool Transfer), T1140 (Deobfuscate/Decode Files or Information)

**Fuente:** [TryHackMe - MAL_ Researching](https://tryhackme.com/room/malresearching)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.