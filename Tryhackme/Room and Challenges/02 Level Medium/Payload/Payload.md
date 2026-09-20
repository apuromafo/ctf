# Payload

| **Dificultad** | MEDIUM | **Tipo** | Premium (requiere suscripción) | **Slug** | `payload` |
| **Link** | [TryHackMe](https://tryhackme.com/room/payload) | **Sección** | IA / Cadena de Suministro / DFIR | **Fuente** | Answers for the TryHackMe Payload Room — Simon Taplin + Payload - TryHackMe — monasx0 |
| **Componentes** | AI Supply Chain, ML Model Analysis, Pickle/Fickling, Keras/TensorFlow Lambda Layers, Deployment Log Analysis, Beacon Detection | **Impacto** | Compromiso de la cadena de suministro de IA mediante modelos maliciosos (pickle envenenado y capas Lambda) que ejecutan código arbitrario y hacen beaconing C2 |

> **Objeto:** Habilidades prácticas de la cadena de suministro de IA: analizar logs de despliegue, descompilar modelos, rastrear beacons.
> **Objective:** Practical skills from the AI Supply Chain path: analyse deployment logs, decompile models, trace beacons.

---

**Contexto:** Una alerta del SOC se disparó a las 03:14 sin despliegues programados ni cambios registrados; el servidor de inferencia ML hacía conexiones HTTPS salientes a una dirección no reconocida. Se investiga el incidente completo en `/opt/supply-chain/incident/`: primero se construye una línea de tiempo con los logs de despliegue y red (`logs/`), después se descompila el modelo de producción (`models/`) con `fickling`, y finalmente se inspecciona un modelo candidato `.h5` con un script de inspección, recuperando las dos partes de la flag de la campaña.

> **ES:** Una alerta SOC se disparó a las 03:14 sin despliegues programados ni cambios registrados. El servidor de inferencia ML estaba haciendo conexiones HTTPS salientes a una dirección no reconocida. Te han llamado para investigar. Todos los materiales del incidente están en `/opt/supply-chain/incident/`: `logs/` (logs de despliegue y red), `models/` (el modelo de producción en ejecución, un candidato de reemplazo en staging y un modelo baseline limpio). La investigación sigue un orden natural: empieza con los logs, examina el modelo de producción y evalúa el candidato de reemplazo antes de que se despliegue.
> **EN:** A SOC alert fired at 03:14 with no scheduled deployments or recorded changes. The ML inference server was making outbound HTTPS connections to an unrecognized address. You have been called in to investigate. All incident materials are in `/opt/supply-chain/incident/`: `logs/` (deployment and network logs), `models/` (the currently running production model, a replacement candidate in staging, and a clean baseline model). The investigation follows a natural order: start with the logs, then examine the production model, and finally evaluate the replacement candidate before it is deployed.

> **Escenario original / Scenario:**
> Una alerta SOC se disparó a las 03:14 sin despliegues programados ni cambios registrados. El servidor de inferencia ML estaba haciendo conexiones HTTPS salientes a una dirección no reconocida. Te han llamado para investigar.
>
> Todos los materiales del incidente están en `/opt/supply-chain/incident/`. Ese es tu directorio de trabajo para toda la investigación. Contiene:
>
> * `logs/` — logs de despliegue y red
> * `models/` — el modelo de producción actualmente en ejecución y un candidato de reemplazo en staging
> * Un modelo baseline limpio para comparación
>
> La investigación sigue un orden natural: empieza con los logs para construir una línea de tiempo, luego examina el modelo de producción, y después evalúa el candidato de reemplazo antes de que se despliegue.

## Solucionario

### Task 1: Leyendo el Log de Despliegue / Reading the Deployment Log

**Explicación:** Se inspecciona el log de despliegue para construir la línea de tiempo del incidente. El log revela la organización de la que vino el modelo de reemplazo (`trustworthy-ai-lab`) y permite calcular los días transcurridos entre el despliegue y la alerta SOC: el modelo se desplegó el 26 de enero y la alerta se disparó el 16 de febrero, es decir, 5 días restantes de enero más 16 de febrero = 21 días.

```
cat /opt/supply-chain/incident/logs/deployment.log
```

Dos cosas saltan a la vista de la salida.

**Q1 — ¿De qué organización vino el modelo de reemplazo? / What organisation did the replacement model come from?**

El log contiene esta línea:

```
New source organisation detected: trustworthy-ai-lab
```

> **trustworthy-ai-lab**

**Q2 — ¿Cuántos días pasaron entre el despliegue y la alerta SOC? / How many days passed between deployment and the SOC alert?**

Dos timestamps son relevantes:

```
[2024-01-26 14:32:16] INFO  Model deployed to production inference server
[2024-02-16 03:14:00] ALERT SOC automated alert: unusual outbound HTTPS traffic detected
```

El modelo se desplegó el 26 de enero. La alerta se disparó el 16 de febrero. Contando los días: 5 días restantes de enero más 16 días de febrero da:

> **21**

### Task 2: Descompilando el Modelo de Producción / Decompiling the Production Model

**Explicación:** Se navega al directorio de modelos y se ejecuta `fickling` contra el modelo de producción. Fickling analiza archivos pickle de Python, usados para serializar modelos ML pero peligrosos porque pueden ejecutar código arbitrario al cargarse. La salida descompilada revela que el payload usa la función `system` para ejecutar comandos shell, y que el comando que captura la identidad del host es `hostname`.

```
cd /opt/supply-chain/incident/models
fickling production_model.pkl
```

Fickling es una herramienta para analizar archivos pickle de Python. Los archivos pickle se usan comúnmente para serializar modelos ML pero son peligrosos porque pueden ejecutar código arbitrario al cargarse. Esto es exactamente lo que pasó aquí.

**Q3 — ¿Qué función de Python usa el payload para ejecutar el comando shell? / What Python function does the payload use to execute the shell command?**

La salida descompilada muestra claramente la función `system` usada para ejecutar comandos shell.

> **system**

**Q4 — ¿Qué comando shell usa el payload para capturar la identidad del host? / What shell command does the payload use to capture the host's identity?**

Mirando lo que la función `system` está ejecutando realmente, el payload llama a `hostname` para identificar la máquina en la que ha aterrizado.

> **hostname**

### Task 3: Comprobando el Log de Captura de Beacon / Checking the Beacon Capture Log

**Explicación:** Se lee el log de captura de beacon que registró la petición saliente que disparó la alerta SOC, revelando el método HTTP usado en la petición (POST). En este log también es visible la primera parte de la flag de la campaña, necesaria para la pregunta final.

```
cat /opt/supply-chain/incident/logs/beacon_capture.log
```

Este log capturó la petición saliente que disparó la alerta SOC. Leyéndolo se revela el método HTTP usado en la petición.

**Q5 — El log de captura de beacon muestra el método HTTP usado en la petición saliente. ¿Cuál es? / The beacon capture log shows the HTTP method used in the outbound request. What is it?**

> **POST**

Toma nota de la primera parte de la flag visible en este log — la necesitarás para la pregunta final.

### Task 4: Inspeccionando el Modelo Candidato de Reemplazo / Inspecting the Candidate Replacement Model

**Explicación:** El equipo de ingeniería preparó un modelo `.h5` como reemplazo pero aún no lo ha desplegado. Se ejecuta el script de inspección proporcionado contra él y la salida marca una capa que requiere revisión: `lambda (manipulate_output)`. Se trata de una capa Lambda, una capa personalizada en un modelo Keras/TensorFlow que puede ejecutar código Python arbitrario; el nombre por sí solo es una bandera roja, por lo que este modelo candidato también está comprometido y no debería desplegarse. La salida también contiene la segunda parte de la flag.

```
python3 /opt/supply-chain/tools/inspect_h5_model.py candidate_model.h5
```

La salida marca una capa que requiere revisión:

```
lambda (manipulate_output)
```

Esta es una capa Lambda — una capa personalizada en un modelo Keras/TensorFlow que puede ejecutar código Python arbitrario. El nombre por sí solo es una bandera roja. Este modelo candidato también está comprometido y no debería desplegarse.

**Q6 — ¿Qué capa maliciosa contiene el modelo candidato? / What malicious layer does the candidate model contain?**

> **manipulate_output**

La salida también contiene la segunda parte de la flag. Anótala.

### Task 5: Recuperando la Flag Completa de la Campaña / Recovering the Full Campaign Flag

**Explicación:** El atacante dividió el campaign ID en dos artefactos para evitar la exposición completa en una sola captura. La Parte 1 se encontró en `beacon_capture.log` y la Parte 2 en la salida de `inspect_h5_model.py`. Combinándolas en orden se obtiene la flag completa de la campaña.

**Q7 — ¿Cuál es la flag completa de la campaña? / What is the full campaign flag?**

El atacante dividió el campaign ID en dos artefactos para evitar la exposición completa en una sola captura. Ya tienes ambas piezas:

* **Parte 1** — encontrada en `beacon_capture.log`
* **Parte 2** — encontrada en la salida de `inspect_h5_model.py`

Combínalas en orden y envía la flag completa.

> **THM{b4ckd00r_1n_pl41n_s1ght}**

### Qué Enseña Esta Room / What This Room Teaches You

**Explicación:** Los ataques a la cadena de suministro de ML son una amenaza real y creciente: los atacantes no necesitan irrumpir directamente en la infraestructura, pueden comprometer el modelo mismo antes de que llegue. Esta room demuestra dos técnicas comunes: envenenar un archivo pickle con código arbitrario que se ejecuta al cargar, y ocultar lógica maliciosa dentro de una capa Lambda personalizada en una red neuronal. Ambas son lo bastante sutiles como para pasar revisiones que solo comprueban la precisión del modelo y no su integridad. Siempre verifica la fuente de tus modelos e inspecciónalos antes del despliegue.

Los ataques a la cadena de suministro de ML son una amenaza real y creciente. Los atacantes no necesitan irrumpir directamente en tu infraestructura — pueden comprometer el modelo mismo antes de que llegue a ti. Esta room demuestra dos técnicas comunes: envenenar un archivo pickle con código arbitrario que se ejecuta al cargar, y ocultar lógica maliciosa dentro de una capa Lambda personalizada en una red neuronal. Ambas son lo bastante sutiles como para pasar revisiones que solo comprueban la precisión del modelo y no su integridad. Siempre verifica la fuente de tus modelos e inspecciónalos antes del despliegue.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What organisation did the replacement model come from? | `trustworthy-ai-lab` |
| 2 | How many days passed between deployment and the SOC alert? | `21` |
| 3 | What Python function does the payload use to execute the shell command? | `system` |
| 4 | What shell command does the payload use to capture the host's identity? | `hostname` |
| 5 | The beacon capture log shows the HTTP method used in the outbound request. What is it? | `POST` |
| 6 | What malicious layer does the candidate model contain? | `manipulate_output` |
| 7 | What is the full campaign flag? | `THM{b4ckd00r_1n_pl41n_s1ght}` |

---

**Metodología:** Investigación dirigida por el incidente: se construye la línea de tiempo con `deployment.log` (origen del modelo y días hasta la alerta), se descompila el modelo de producción con `fickling` para descubrir la ejecución de `system` con `hostname`, se analiza `beacon_capture.log` para el método HTTP de la petición saliente (POST) y la parte 1 de la flag, se inspecciona el candidato `.h5` con `inspect_h5_model.py` revelando la capa Lambda `manipulate_output` y la parte 2 de la flag, y se ensamblan ambas partes para obtener la flag completa.

### Cadena de ataque / Attack Chain

```
Alerta SOC 03:14 sin despliegue programado
  -> Log de despliegue: fuente "trustworthy-ai-lab", 21 días → alerta
    -> fickling production_model.pkl: ejecuta system("hostname")
      -> beacon_capture.log: método POST (parte 1 de la flag)
        -> inspect_h5_model.py candidate_model.h5: capa Lambda "manipulate_output" (parte 2)
          -> Flag completa: THM{b4ckd00r_1n_pl41n_s1ght}
            -> Conclusión: verificar la fuente e integridad de los modelos ML
```

**Learning chain:** Alerta SOC → Timeline con deployment.log → Descompilación con fickling (pickle envenenado, función system, hostname) → Análisis del beacon (HTTP POST y parte 1 de la flag) → Inspección del modelo .h5 (capa Lambda manipulate_output y parte 2) → Ensamblado de la flag completa → Lección sobre integridad en la cadena de suministro de IA.

**Lección:** *Los modelos de machine learning son superficies de ataque de la cadena de suministro: un pickle puede ejecutar código arbitrario al cargarse y una capa Lambda de Keras puede ocultar lógica maliciosa. Verifica siempre la fuente de los modelos e inspecciónalos antes del despliegue, no solo su precisión.*

**MITRE ATT&CK:** T1195.001 (Supply Chain Compromise: Compromise Software Dependencies and Development Tools), T1195.002 (Supply Chain Compromise: Compromise Software Supply Chain), T1059 (Command and Scripting Interpreter), T1105 (Ingress Tool Transfer), T1071.001 (Application Layer Protocol: Web Protocols)

**Fuente:**
* [Answers for the TryHackMe Payload Room — Simon Taplin](https://simontaplin.net/2026/06/21/answers-for-the-tryhackme-payload-room/)
* [Payload - TryHackMe — monasx0](https://monasx0.github.io/write-ups/posts/payload-tryhackme/)

**Fuente:** [TryHackMe - Payload](https://tryhackme.com/room/payload)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.