# Expediting Registry Analysis

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Forense / Registro de Windows | expeditingregistryanalysis | https://tryhackme.com/room/expeditingregistryanalysis | 02 Level Medium | TryHackMe | FTK Imager, KAPE, Registry Explorer, hives | Adquisición y análisis forense de hives del registro de Windows |

---

**Contexto:** **Expediting Registry Analysis** (room `expregistryforensics`) enseña a adquirir hives del registro en vivo (live) y en frío (cold), y a analizarlos con herramientas como FTK Imager, KAPE (target `RegistryHives`) y Registry Explorer. Se responde información de sistema (Computer Name, TimeZoneKeyName, LastKnownGood), cuentas de usuario (RID, fecha de reseteo de password, grupos Administrators), redes (gateway MAC, timestamps de conexión) y datos de un segundo sistema (nombre, VPN ProtonVPN, organización registrada).

## Solucionario

### Task 1: Introduction
**Explicación:**

Introducción a los objetivos de la sala: cómo adquirir hives del registro en vivo y frío, qué herramientas usar y qué preguntas pueden responderse analizando el registro. No requiere respuesta escrita.

**Respuesta:** `No answer needed`

### Task 2: Live vs Cold Acquisition
**Explicación:**

Cuando la recolección forense se hace sobre la imagen de disco de un sistema, se llama **cold acquisition**. Además, la velocidad no es una de las ventajas de recolectar datos del registro con FTK Imager, por lo que la respuesta es **N**.

Respuestas del lab (contenido original):

```
1. No answer needed
2. cold acquisition
3. N
```

### Task 3: KAPE / Data Acquisition
**Explicación:**

Para recolectar datos de la unidad C: y guardarlos en la unidad D: usando el target `RegistryHives`, el contenido del archivo `_kape.cli` debe ser `--tsource C: --tdest D:\ --target RegistryHives`.

Respuestas del lab (contenido original):

```
1. No answer needed
2. --tsource C: --tdest D:\ --target RegistryHives
```

### Task 4: Registry Analysis Using EZTools (Sistema 4N6)
**Explicación:**

Se analizan los hives con las herramientas de Eric Zimmerman. Del sistema en cuestión se extrae el Computer Name (**4N6**), el TimeZoneKeyName (**UTC**) y el LastKnownGood control set (**2**).

Respuestas del lab (contenido original):

```
1. 4N6
2. UTC
3. 2
```

### Task 5: System Information and Accounts (4N6)
**Explicación:**

La cuenta creada en último lugar es **suspicious**, con fecha de reseteo de password `2024-03-03 11:51:04Z`. La cuenta `4n6lab` tiene RID **1008**, y los tres miembros del grupo Administrators en orden ascendente de RID son **administrator, 4n6lab, suspicious**.

Respuestas del lab (contenido original):

```
1. suspicious
2. 2024-03-03 11:51:04Z
3. 1008
4. administrator, 4n6lab, suspicious
```

### Task 6: Network Information (4N6)
**Explicación:**

Del historial de redes (NetworkList/Profiles) se obtiene el MAC del gateway que estuvo conectado por última vez en 2021: **0A-41-2A-ED-DB-34**, con última conexión el **3/17/2021 14:59**. La red "Network 2" se conectó por primera vez el **3/17/2021 15:08**.

Respuestas del lab (contenido original):

```
1. 0A-41-2A-ED-DB-34
2. 3/17/2021 14:59
3. 3/17/2021 15:08
```

### Task 7: Segundo sistema (JAMES)
**Explicación:**

Sobre el segundo sistema analizado: el nombre del equipo es **JAMES**; además del administrador, el usuario **art-test** forma parte del grupo Administrators. La red que se conectó a una VPN fue **ProtonVPN**, y la organización registrada en el sistema operativo es **Amazon.com**.

Respuestas del lab (contenido original):

```
1. JAMES
2. art-test
3. ProtonVPN
4. Amazon.com
```

### Task 8: Conclusion
**Explicación:**

Cierre de la sala. No requiere respuesta escrita.

**Respuesta:** `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Task 1 (Introduction) | `No answer needed` |
| 2 | ¿Cómo se llama la adquisición forense hecha sobre la imagen de disco? | `cold acquisition` |
| 3 | ¿Es la velocidad una ventaja de FTK Imager para el registro? (Y/N) | `N` |
| 4 | ¿Qué contiene el `_kape.cli` para recolectar C: a D: con RegistryHives? | `--tsource C: --tdest D:\ --target RegistryHives` |
| 5 | ¿Cuál es el Computer Name del sistema analizado? | `4N6` |
| 6 | ¿Cuál es el TimeZoneKeyName? | `UTC` |
| 7 | ¿Cuál es el control set LastKnownGood? | `2` |
| 8 | ¿Qué cuenta fue creada al final? | `suspicious` |
| 9 | ¿Cuál es la fecha de reset de password de esa cuenta? | `2024-03-03 11:51:04Z` |
| 10 | ¿Cuál es el RID de la cuenta 4n6lab? | `1008` |
| 11 | ¿Qué 3 cuentas están en Administrators? (orden ascendente de RID) | `administrator, 4n6lab, suspicious` |
| 12 | ¿Cuál es la MAC del gateway conectado por última vez en 2021? | `0A-41-2A-ED-DB-34` |
| 13 | ¿Cuándo se conectó por última vez esa red? | `3/17/2021 14:59` |
| 14 | ¿Cuándo se conectó por primera vez "Network 2"? | `3/17/2021 15:08` |
| 15 | ¿Cuál es el nombre del segundo sistema? | `JAMES` |
| 16 | ¿Qué otro usuario (no administrator) está en Administrators? | `art-test` |
| 17 | ¿Cómo se llama la red que se conectó a una VPN? | `ProtonVPN` |
| 18 | ¿A qué organización está registrado el sistema operativo? | `Amazon.com` |
| 19 | Conclusion | `No answer needed` |

---

**Metodología:** Adquisición de hives en vivo y en frío, utilización de KAPE con el target `RegistryHives`, y análisis con Registry Explorer/EZTools para extraer información de sistema, cuentas, redes y configuración (usando las claves SYSTEM, SAM y NetworkList).

**Learning chain:** Introducción → Adquisición live/cold → KAPE y siril/`_kape.cli` → Análisis con EZTools → Información de sistema y cuentas → Historial de redes → Segundo sistema → Conclusion.

**Lección:** *Los hives del registro contienen una mina de información persistente (nombres, RIDs, redes, VPNs): combinando FTK Imager/KAPE para la adquisición y Registry Explorer para el parsing se acelera enormemente el análisis forense.*

**MITRE ATT&CK:** T1005 Data from Local System · T1012 Query Registry · T1070.001 Indicator Removal on Host: Clear Windows Event Logs · T1546.001 Event Triggered Execution: Change Default File Association.

**Fuente:** [TryHackMe - Expediting Registry Analysis](https://tryhackme.com/room/expeditingregistryanalysis)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.