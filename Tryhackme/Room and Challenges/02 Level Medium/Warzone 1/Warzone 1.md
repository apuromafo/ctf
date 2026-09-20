# Warzone 1

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | Análisis de malware / Malware Analysis | warzone1 | https://tryhackme.com/room/warzone1 | 02 Level Medium | TryHackMe | Malspam, MirrorBlast, Commander C2, Suricata | Alta - respuesta a incidentes |

> **Objeto:** Analizar un correo malicioso (malspam) y reconstruir la infección por el malware MirrorBlast del grupo TA505 usando reglas Suricata y artefactos del sistema.

---

**Contexto:** "Warzone 1" es un laboratorio SOC de análisis de malware. Partiendo de un malspam con adjunto, se identifican las alertas Suricata, las IPs de comunicación C2, la cadena de entrega (MSI/REBOL) y los archivos desplegados por la familia MirrorBlast (TA505).

> **ES:** Simula el análisis de una campaña de malspam hasta la infección completa.
> **EN:** Simulates analyzing a malspam campaign through to full infection.

## Solucionario

### Task 1: Alerta del IDS / IDS alert

**Explicación:** Revisar la alerta Suricata disparada por el documento malicioso adjunto al correo.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué regla de Suricata saltó? / Which Suricata rule fired? | ET Malware MirrorBlast CnC Activity M3 |

### Task 2: IP origen / Source IP

**Explicación:** Identificar la IP de origen del tráfico malicioso en el PCAP.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es la IP origen? / What is the source IP? | 172[.]16[.]1[.]102 |

### Task 3: IP destino / Destination IP

**Explicación:** Identificar la IP de destino que recibe la comunicación maliciosa.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es la IP destino? / What is the destination IP? | 169[.]239[.]128[.]11 |

### Task 4: Actor de amenaza / Threat actor

**Explicación:** Relacionar la familia de malware con el grupo de cibercrimen que la opera.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué grupo está detrás? / Which group is behind it? | TA505 |

### Task 5: Nombre del malware / Malware name

**Explicación:** Identificar la familia de malware basada en la cadena `MirrorBlast`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cómo se llama el malware? / What is the malware name? | MirrorBlast |

### Task 6: Tipo de instalador / Installer type

**Explicación:** Determinar qué tipo de instalador contiene el binario que ejecuta la carga.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué tipo de instalador usa? / What installer type is used? | Windows Installer |

### Task 7: Artefacto REBOL / REBOL artifact

**Explicación:** Identificar el componente REBOL que despliega el instalador MSI.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué componente REBOL se instala? / Which REBOL component is installed? | REBOL View 2.7.8.3.1 |

### Task 8: IPs de contacto / Contacted IPs

**Explicación:** Enumerar las IPs adicionales a las que se conecta el malware tras la infección.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿A qué IPs se conecta? / Which IPs does it contact? | 185[.]10[.]68[.]235,192[.]36[.]27[.]92 |

### Task 9: Archivos MSI / MSI files

**Explicación:** Listar los archivos MSI descargados por el malware.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué MSIs se descargan? / Which MSIs are downloaded? | filter.msi,10opd3r_load.msi |

### Task 10: Payload persistente / Stored payload

**Explicación:** Localizar los archivos de payload que el malware persiste en el equipo.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Dónde se guarda el payload? / Where is the payload stored? | C:\ProgramData\001\arab.bin,C:\ProgramData\001\arab.exe |

### Task 11: Archivos finales / Final files

**Explicación:** Identificar los ejecutables finales desplegados en el directorio de Google.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué archivos quedan en el sistema? / Which files remain on the system? | C:\ProgramData\Local\Google\rebol-view-278-3-1.exe,C:\ProgramData\Local\Google\exemple.rb |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Qué regla de Suricata saltó? / Which Suricata rule fired? | `ET Malware MirrorBlast CnC Activity M3` |
| 2 | ¿Cuál es la IP origen? / What is the source IP? | `172[.]16[.]1[.]102` |
| 3 | ¿Cuál es la IP destino? / What is the destination IP? | `169[.]239[.]128[.]11` |
| 4 | ¿Qué grupo está detrás? / Which group is behind it? | `TA505` |
| 5 | ¿Cómo se llama el malware? / What is the malware name? | `MirrorBlast` |
| 6 | ¿Qué tipo de instalador usa? / What installer type is used? | `Windows Installer` |
| 7 | ¿Qué componente REBOL se instala? / Which REBOL component is installed? | `REBOL View 2.7.8.3.1` |
| 8 | ¿A qué IPs se conecta? / Which IPs does it contact? | `185[.]10[.]68[.]235,192[.]36[.]27[.]92` |
| 9 | ¿Qué MSIs se descargan? / Which MSIs are downloaded? | `filter.msi,10opd3r_load.msi` |
| 10 | ¿Dónde se guarda el payload? / Where is the payload stored? | `C:\ProgramData\001\arab.bin,C:\ProgramData\001\arab.exe` |
| 11 | ¿Qué archivos quedan en el sistema? / Which files remain on the system? | `C:\ProgramData\Local\Google\rebol-view-278-3-1.exe,C:\ProgramData\Local\Google\exemple.rb` |

---

**Metodología:**

1. Análisis del malspam y la alerta Suricata disparada.
2. Reconstrucción de la conversación C2 (IPs origen/destino).
3. Atribución: grupo TA505, familia MirrorBlast.
4. Deconstrucción de la cadena de entrega MSI/REBOL.
5. Enumeración de IPs y archivos persistidos.

### Cadena de ataque / Attack Chain

```text
Malspam -> Documento -> MSI (InstallUtil) -> MirrorBlast CnC -> filter.msi / 10opd3r_load.msi -> arab.bin/arab.exe -> REBOL View -> C2 IPs (185.10.68.235, 192.36.27.92)
```

**Learning chain:**

- Las reglas Suricata dan la primera pista del malware (ET Malware MirrorBlast CnC Activity M3).
- La cadena de entrega llega hasta `rebol-view-278-3-1.exe` y `exemple.rb` en `C:\ProgramData\Local\Google\`.
- TA505 opera MirrorBlast mediante MSI y REBOL durante la infección.

**Lección:** *Reconstruir la cadena de infección completa convierte alertas sueltas en una historia de ataque coherente.*

**MITRE ATT&CK:**
- T1204.001 - User Execution: Malicious Link
- T1204.002 - User Execution: Malicious File
- T1555 - Credentials from Password Stores
- T1059 - Command and Scripting Interpreter

**Fuente:** [TryHackMe - Warzone 1](https://tryhackme.com/room/warzone1)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.