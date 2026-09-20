# Brains

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | challenge | `brains` | [TryHackMe](https://tryhackme.com/room/brains) | 01 Level Easy | TryHackMe | SSH / enumeration / zip / credenciales | Acceso a la máquina mediante enumeración y credenciales, captura del user flag y localización de un fichero de credenciales comprimido |

---

**Contexto:** Brains es una máquina Linux de práctica que requiere enumeración y explotación para obtener acceso. El objetivo es conseguir el user flag del sistema y, durante la post-explotación, localizar credenciales adicionales como los usuarios `eviluser` y `datacollector`, así como un fichero comprimido `AyzzbuXY.zip` que contiene información sensible.

> **ES:** Máquina Linux vulnerable. Tras la enumeración se obtienen credenciales, se captura el user flag y se encuentran en el sistema los usuarios `eviluser` y `datacollector` y el zip `AyzzbuXY.zip`.
> **EN:** A vulnerable Linux box. After enumeration credentials are recovered, the user flag is captured and users `eviluser` and `datacollector` plus the archive `AyzzbuXY.zip` are found on the system.

## Solucionario

### Task 1: User Flag
**Explicación:** Tras descubrir las credenciales del servicio expuesto y obtener acceso al sistema, se localiza el archivo del user flag.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| ¿Cuál es el user flag? | `THM{faa9bac345709b6620a6200b484c7594}` |

### Task 2: Enumeración post-explotación / Post-exploitation enumeration
**Explicación:** Dentro del sistema se enumeran las cuentas y los archivos relevantes. Se identifican los usuarios `eviluser` y `datacollector`, y se localiza un fichero de credenciales comprimido llamado `AyzzbuXY.zip`.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| ¿Cuál es el nombre del primer usuario encontrado? | `eviluser` |
| ¿Cuál es el nombre del segundo usuario encontrado? | `datacollector` |
| ¿Cuál es el nombre del fichero comprimido localizado? | `AyzzbuXY.zip` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | User flag | `THM{faa9bac345709b6620a6200b484c7594}` |
| 2 | Primer usuario encontrado | `eviluser` |
| 3 | Segundo usuario encontrado | `datacollector` |
| 4 | Fichero comprimido localizado | `AyzzbuXY.zip` |

---

**Metodología:** Se realiza la enumeración inicial de la máquina y se identifican servicios y credenciales que permiten el acceso. Con acceso al sistema se captura el user flag. En la fase de post-explotación se enumeran los usuarios y ficheros relevantes, identificando a `eviluser` y `datacollector` y el comprimido `AyzzbuXY.zip` con credenciales sensibles.

### Cadena de ataque / Attack Chain

```text
nmap -> enumeración -> credenciales -> acceso SSH -> user flag -> enumeración de sistema -> eviluser / datacollector -> AyzzbuXY.zip
```

**Learning chain:** network enumeration --> credential recovery --> remote access --> user flag --> system enumeration --> user discovery --> sensitive zip archive

**Lección:** *La enumeración post-explotación es tan importante como el acceso inicial: cuentas adicionales y ficheros comprimidos suelen esconder credenciales y datos sensibles del sistema.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1078 (Valid Accounts), T1005 (Data from Local System), T1552 (Unsecured Credentials)

**Fuente:** [TryHackMe - Brains](https://tryhackme.com/room/brains)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.