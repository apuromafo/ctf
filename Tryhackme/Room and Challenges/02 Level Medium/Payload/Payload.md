# Payload [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad:** MEDIUM.
* **Tipo:** Premium (requiere suscripción).
* **Slug:** `payload`
* **Link:** https://tryhackme.com/room/payload
* **Objeto:** Habilidades prácticas de la cadena de suministro de IA: analizar logs de despliegue, descompilar modelos, rastrear beacons.
* **Objective:** Practical skills from the AI Supply Chain path: analyse deployment logs, decompile models, trace beacons.

---

## Solucionario de Tareas / Task Solutions

### Escenario / Scenario

Una alerta SOC se disparó a las 03:14 sin despliegues programados ni cambios registrados. El servidor de inferencia ML estaba haciendo conexiones HTTPS salientes a una dirección no reconocida. Te han llamado para investigar.

Todos los materiales del incidente están en `/opt/supply-chain/incident/`. Ese es tu directorio de trabajo para toda la investigación. Contiene:

* `logs/` — logs de despliegue y red
* `models/` — el modelo de producción actualmente en ejecución y un candidato de reemplazo en staging
* Un modelo baseline limpio para comparación

La investigación sigue un orden natural: empieza con los logs para construir una línea de tiempo, luego examina el modelo de producción, y después evalúa el candidato de reemplazo antes de que se despliegue.

### Leyendo el Log de Despliegue / Reading the Deployment Log

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

### Descompilando el Modelo de Producción / Decompiling the Production Model

Navega al directorio de modelos y ejecuta `fickling` contra el modelo de producción:

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

### Comprobando el Log de Captura de Beacon / Checking the Beacon Capture Log

**Q5 — El log de captura de beacon muestra el método HTTP usado en la petición saliente. ¿Cuál es? / The beacon capture log shows the HTTP method used in the outbound request. What is it?**

```
cat /opt/supply-chain/incident/logs/beacon_capture.log
```

Este log capturó la petición saliente que disparó la alerta SOC. Leyéndolo se revela el método HTTP usado en la petición.

> **POST**

Toma nota de la primera parte de la flag visible en este log — la necesitarás para la pregunta final.

### Q6 — Inspeccionando el Modelo Candidato de Reemplazo / Inspecting the Candidate Replacement Model

El equipo de ingeniería preparó un modelo `.h5` como reemplazo pero aún no lo ha desplegado. Ejecuta el script de inspección proporcionado contra él:

```
python3 /opt/supply-chain/tools/inspect_h5_model.py candidate_model.h5
```

La salida marca una capa que requiere revisión:

```
lambda (manipulate_output)
```

Esta es una capa Lambda — una capa personalizada en un modelo Keras/TensorFlow que puede ejecutar código Python arbitrario. El nombre por sí solo es una bandera roja. Este modelo candidato también está comprometido y no debería desplegarse.

> **manipulate_output**

La salida también contiene la segunda parte de la flag. Anótala.

### Q7 — Recuperando la Flag Completa de la Campaña / Recovering the Full Campaign Flag

El atacante dividió el campaign ID en dos artefactos para evitar la exposición completa en una sola captura. Ya tienes ambas piezas:

* **Parte 1** — encontrada en `beacon_capture.log`
* **Parte 2** — encontrada en la salida de `inspect_h5_model.py`

Combínalas en orden y envía la flag completa.

> **THM{b4ckd00r_1n_pl41n_s1ght}**

---

### Qué Enseña Esta Room / What This Room Teaches You

Los ataques a la cadena de suministro de ML son una amenaza real y creciente. Los atacantes no necesitan irrumpir directamente en tu infraestructura — pueden comprometer el modelo mismo antes de que llegue a ti. Esta room demuestra dos técnicas comunes: envenenar un archivo pickle con código arbitrario que se ejecuta al cargar, y ocultar lógica maliciosa dentro de una capa Lambda personalizada en una red neuronal. Ambas son lo bastante sutiles como para pasar revisiones que solo comprueban la precisión del modelo y no su integridad. Siempre verifica la fuente de tus modelos e inspecciónalos antes del despliegue.

---

* **Fuente / Source:**
  * [Answers for the TryHackMe Payload Room — Simon Taplin](https://simontaplin.net/2026/06/21/answers-for-the-tryhackme-payload-room/)
  * [Payload - TryHackMe — monasx0](https://monasx0.github.io/write-ups/posts/payload-tryhackme/)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
