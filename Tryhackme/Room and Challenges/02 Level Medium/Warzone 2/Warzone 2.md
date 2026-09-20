# Warzone 2

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | Análisis de malware / Malware Analysis | warzone2 | https://tryhackme.com/room/warzone2 | 02 Level Medium | TryHackMe | Banking malware, Phishing, C2, Suricata | Alta - respuesta a incidentes |

> **Objeto:** Analizar la campaña de phishing bancario (banking trojan) a partir de las reglas Suricata, fuentes de descarga de la DLL maliciosa y dominios C2 implicados.

---

**Contexto:** "Warzone 2" continúa la saga Warzone con un objetivo bancario. Se identifican las reglas Suricata que detectan la descarga de `draw.dll`, la IP y URI de descarga, el user-agent, y se enumeran los dominios e IPs de C2 y los dominios falsos de banca.

> **ES:** Investigación de una campaña bancaria maliciosa completa (dropper + ladrón de credenciales).
> **EN:** Investigation of a full malicious banking campaign (dropper + credential stealer).

## Solucionario

### Task 1: Regla de alerta 1 / Alert rule 1

**Explicación:** Revisar la primera regla Suricata relacionada con la descarga del ejecutable malicioso desde MSXMLHTTP.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué regla Salta primero? / Which rule fires first? | ET MALWARE Likely Evil EXE download from MSXMLHTTP non-exe extension M2 |

### Task 2: Regla de alerta 2 / Alert rule 2

**Explicación:** Identificar la segunda regla Suricata de descarga de binarios PE.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué segunda regla salta? / Which second rule fires? | ET POLICY PE EXE or DLL Windows file download HTTP |

### Task 3: IP de descarga / Download IP

**Explicación:** Determinar la IP desde la que se descarga el binario malicioso.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es la IP de descarga? / What is the download IP? | 185[.]118[.]164[.]8 |

### Task 4: Solicitud maliciosa / Malicious request

**Explicación:** Localizar la URI completa de la petición HTTP que entrega la carga.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es la URI de la petición? / What is the request URI? | awh93dhkylps5ulnq-be[.]com/czwih/fxla[.]php?l=gap1[.]cab |

### Task 5: DLL descargada / Downloaded DLL

**Explicación:** Nombrar la DLL que se descarga e inyecta en el proceso bancario.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué DLL se descarga? / Which DLL is downloaded? | draw.dll |

### Task 6: User-Agent / User-Agent

**Explicación:** Anotar el User-Agent con el que el malware solicita los recursos.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué User-Agent usa el malware? / Which User-Agent does the malware use? | Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/8.0; .NET4.0C; .NET4.0E) |

### Task 7: Dominios C2 / C2 domains

**Explicación:** Enumerar los dominios de C2 utilizados por la familia.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué dominios C2 usa? / Which C2 domains are used? | a-zcorner[.]com,knockoutlights[.]com |

### Task 8: IPs C2 / C2 IPs

**Explicación:** Resolver las IPs de infraestructura de mando y control.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué IPs C2 existen? / Which C2 IPs exist? | 64[.]225[.]65[.]166,142[.]93[.]211[.]176 |

### Task 9: Dominios falsos / Fake bank domains

**Explicación:** Identificar los dominios falsos creados para suplantar la banca legítima.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué dominios bancarios falsos hay? / Which fake bank domains exist? | safebanktest[.]top, tocsicambar[.]xyz, ulcertification[.]xyz |

### Task 10: Dominio de caída / Drop domain

**Explicación:** Señalar el dominio desde el que se sirve la carga final.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Desde qué dominio se cae la carga? / From which domain is the payload dropped? | 2partscow[.]top |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Qué regla Salta primero? / Which rule fires first? | `ET MALWARE Likely Evil EXE download from MSXMLHTTP non-exe extension M2` |
| 2 | ¿Qué segunda regla salta? / Which second rule fires? | `ET POLICY PE EXE or DLL Windows file download HTTP` |
| 3 | ¿Cuál es la IP de descarga? / What is the download IP? | `185[.]118[.]164[.]8` |
| 4 | ¿Cuál es la URI de la petición? / What is the request URI? | `awh93dhkylps5ulnq-be[.]com/czwih/fxla[.]php?l=gap1[.]cab` |
| 5 | ¿Qué DLL se descarga? / Which DLL is downloaded? | `draw.dll` |
| 6 | ¿Qué User-Agent usa el malware? / Which User-Agent does the malware use? | `Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/8.0; .NET4.0C; .NET4.0E)` |
| 7 | ¿Qué dominios C2 usa? / Which C2 domains are used? | `a-zcorner[.]com,knockoutlights[.]com` |
| 8 | ¿Qué IPs C2 existen? / Which C2 IPs exist? | `64[.]225[.]65[.]166,142[.]93[.]211[.]176` |
| 9 | ¿Qué dominios bancarios falsos hay? / Which fake bank domains exist? | `safebanktest[.]top, tocsicambar[.]xyz, ulcertification[.]xyz` |
| 10 | ¿Desde qué dominio se cae la carga? / From which domain is the payload dropped? | `2partscow[.]top` |

---

**Metodología:**

1. Análisis de las reglas Suricata (descarga MSXMLHTTP / PE download).
2. Trazado de la petición HTTP completa (IP, URI, User-Agent).
3. Identificación de la DLL inyectada (`draw.dll`).
4. Enumeración de infraestructura C2 (dominios e IPs) y dominios bancarios falsos.
5. Correlación del dominio de entrega final.

### Cadena de ataque / Attack Chain

```text
Descarga EXE/DLL -> ET MALWARE signaturas -> draw.dll (185.118.164.8) -> gap1.cab -> C2 a-zcorner.com / knockoutlights.com -> 64.225.65.166 / 142.93.211.176 -> phishing bancario
```

**Learning chain:**

- Las firmas ET MALWARE identifican la exfiltración vía MSXMLHTTP con extensiones no ejecutables.
- `draw.dll` es la DLL bancaria inyectada; su descarga pasa por dominios similares al objetivo.
- Los dominios falsos (`safebanktest[.]top`, `tocsicambar[.]xyz`, `ulcertification[.]xyz`) imitan a la banca real.

**Lección:** *La infraestructura C2 (dominios, IPs, UA) es la identidad operativa del actor; cartografíarla permite bloquear la campaña.*

**MITRE ATT&CK:**
- T1105 - Ingress Tool Transfer
- T1555 - Credentials from Password Stores
- T1071 - Application Layer Protocol
- T1059 - Command and Scripting Interpreter

**Fuente:** [TryHackMe - Warzone 2](https://tryhackme.com/room/warzone2)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.