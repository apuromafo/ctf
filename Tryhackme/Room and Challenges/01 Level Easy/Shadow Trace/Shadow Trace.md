# Shadow Trace

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `shadowtrace` | [TryHackMe](https://tryhackme.com/room/shadowtrace) | `01 Level Easy` | THM | Threat hunting, IOC, malware analysis, network signatures | Resolución completa del reto de threat hunting |

---

**Contexto:** Room de caza de amenazas sobre un binario malicioso: se analiza una muestra para extraer sus IOCs —arquitectura 64-bit, hash SHA-256, URL de descarga, dominios C2, la DLL WS2_32.dll y la flag de IOCs— y se reconstruye el comportamiento observado (descargas posteriores desde otros dominios y el archivo test.txt).

> **ES:** Análisis de una muestra maliciosa para extraer indicadores de compromiso (IOCs): arquitectura, hash, URLs de descarga, dominios de red y DLLs implicadas.
> **EN:** Analysis of a malicious sample to extract indicators of compromise (IOCs): architecture, hash, download URLs, network domains and involved DLLs.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Tarea inicial de la room: se comienza el análisis de la muestra sin necesidad de respuesta.

1. No answer needed

### Task 2: Indicadores de compromiso / Indicators of Compromise

**Explicación:** Se analiza la muestra y se extraen los IOCs: arquitectura 64-bit, el hash SHA-256 b2a88de3e3bcfae4a4b38fa36e884c586b5cb2c2c283e71fba59efdb9ea64bfc, la URL de descarga http://tryhatme.com/update/security-update.exe, el dominio de C2 responses.tryhatme.com, la flag THM{you_g0t_some_IOCs_friend} y la DLL WS2_32.dll.

1. 64-bit
2. b2a88de3e3bcfae4a4b38fa36e884c586b5cb2c2c283e71fba59efdb9ea64bfc
3. http://tryhatme.com/update/security-update.exe
4. responses.tryhatme.com
5. THM{you_g0t_some_IOCs_friend}
6. WS2_32.dll

### Task 3: Comportamiento observado / Observed behavior

**Explicación:** Se registran los elementos observados durante el análisis dinámico: las URLs https://tryhatme.com/dev/main.exe y https://reallysecureupdate.tryhatme.com/update.exe, además del archivo test.txt.

1. https://tryhatme.com/dev/main.exe
2. https://reallysecureupdate.tryhatme.com/update.exe
3. test.txt

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|---|---|---|
| 1.1 | Arranque de la room | `No answer needed` |
| 2.1 | Arquitectura de la muestra | `64-bit` |
| 2.2 | Hash SHA-256 de la muestra | `b2a88de3e3bcfae4a4b38fa36e884c586b5cb2c2c283e71fba59efdb9ea64bfc` |
| 2.3 | URL de descarga original | `http://tryhatme.com/update/security-update.exe` |
| 2.4 | Dominio responsable del C2 | `responses.tryhatme.com` |
| 2.5 | Flag de los IOCs | `THM{you_g0t_some_IOCs_friend}` |
| 2.6 | DLL de red implicada | `WS2_32.dll` |
| 3.1 | URL de la primera descarga posterior | `https://tryhatme.com/dev/main.exe` |
| 3.2 | URL de la segunda descarga posterior | `https://reallysecureupdate.tryhatme.com/update.exe` |
| 3.3 | Archivo creado/observado | `test.txt` |

---

**Metodología:** 1) Desplegar la room y obtener la muestra. 2) Determinar la arquitectura y calcular el hash SHA-256. 3) Extraer las URLs de descarga y los dominios asociados. 4) Identificar las DLLs de red e importar los IOCs. 5) Observar el comportamiento posterior de la muestra para completar la cadena.

### Cadena de ataque / Attack Chain

```text
Muestra 64-bit -> SHA-256 b2a88de3... -> descarga http://tryhatme.com/update/security-update.exe -> C2 responses.tryhatme.com -> THM{you_g0t_some_IOCs_friend} -> WS2_32.dll -> https://tryhatme.com/dev/main.exe -> https://reallysecureupdate.tryhatme.com/update.exe -> test.txt
```

**Learning chain:** Obtención de la muestra -> extracción de IOCs (arquitectura, hash, URLs, dominio, DLL) -> análisis de comportamiento -> reconstrucción de la cadena de descargas

**Lección:** *La caza de amenazas empieza por extraer IOCs sólidos (hash, dominios, DLLs) y termina observando el comportamiento: correlacionar estática y dinámica permite reconstruir la actividad completa de la muestra.*

**MITRE ATT&CK:** T1105 (Ingress Tool Transfer), T1104 (Multi-Stage Channels), T1071 (Application Layer Protocol), T1219 (Remote Access Software)

**Fuente:** [TryHackMe - Shadow Trace](https://tryhackme.com/room/shadowtrace)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.