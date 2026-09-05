# Frankesqwen [HARD]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** HARD
* **Tipo / Type:** CTF
* **Slug:** `frankesqwen`
* **Link:** https://tryhackme.com/room/frankesqwen
* **Sección / Section:** 03 Level Hard
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=frankesqwen` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala **AI/LLM** de dificultad Hard: el flag está escondido **dentro de los pesos de un modelo** de lenguaje. Tras acceder por SSH, cualquier pregunta directa al modelo devuelve rechazo o degeneración en todas las variantes porque la "supresión" del secreto está incrustada en los pesos. La solución es **diferenciar dos versiones de los pesos** (`frankesqwen-v7` vs `frankesqwenhint`), localizar los tensores anómalos que guardan el secreto y **parchearlos** para que el modelo vuelva a generar la flag.
> **EN:** **AI/LLM** room of Hard difficulty: the flag is hidden **inside a language model's weights**. After SSH access, any direct question to the model returns refusal or degeneration across all variants because the secret "suppression" is embedded in the weights. The solution is to **diff two weight versions** (`frankesqwen-v7` vs `frankesqwenhint`), locate the anomalous tensors that guard the secret and **patch them** so the model generates the flag again.

### Task 1 - Find the Flag

> **ES:** 1 tarea. SSH con `frankesqwen` / `FrankesQwen`. En el home: `~/frankesqwen-v7`, `~/frankesqwenhint` (y el mismo par en HuggingFace: `ab123451/frankesqwen-v7`, `ab123451/frankesqwen-hint-v2`). `chat.py` usa transformers con `apply_chat_template` y `generate(max_new_tokens=60, do_sample=False, repetition_penalty=1.3)`. Preguntar "What is the flag?" → rechazo o degeneración en TODAS las variantes → la supresión está en los pesos. `diff_weights.py` (safetensors) compara v7 vs hint con `(t1-t2).abs().sum()` por tensor: los outliers aparecen en `model.layers.22.mlp.down_proj.weight` y `model.layers.23.mlp.down_proj.weight`. `patch_and_ask.py` copia esos tensores del hint al v7 y regenera con `max_new_tokens=80` → el modelo revela el flag. Sin GPU → Colab con los modelos de HuggingFace. 1 pregunta.
> **EN:** 1 task. SSH with `frankesqwen` / `FrankesQwen`. In home: `~/frankesqwen-v7`, `~/frankesqwenhint` (same pair on HuggingFace: `ab123451/frankesqwen-v7`, `ab123451/frankesqwen-hint-v2`). `chat.py` uses transformers with `apply_chat_template` and `generate(max_new_tokens=60, do_sample=False, repetition_penalty=1.3)`. Asking "What is the flag?" → refusal or degeneration across ALL variants → the suppression lives in the weights. `diff_weights.py` (safetensors) diffs v7 vs hint with `(t1-t2).abs().sum()` per tensor: outliers show up in `model.layers.22.mlp.down_proj.weight` and `model.layers.23.mlp.down_proj.weight`. `patch_and_ask.py` copies those tensors from the hint model into v7 and regenerates with `max_new_tokens=80` → the model reveals the flag. No GPU → Colab with the HuggingFace models. 1 question.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What's the flag? | `THM{...redacted...}` |

> **Nota / Note:** El valor literal solo aparece publicado en captura de pantalla (generación del modelo parcheado); los walkthroughs no lo transcriben. Se documenta el método completo (diferenciado de pesos y parcheo de tensores), no el flag exacto.
> **EN:** The literal value is only published as a screenshot (generation of the patched model); walkthroughs do not transcribe it. The full method is documented (weight diffing and tensor patching), not the exact flag.

## Metodología / Methodology

1. **Paso / Step - Acceso:** `ssh frankesqwen@<IP>` con la password `FrankesQwen` (indicada en la sala). En el home están `~/frankesqwen-v7` y `~/frankesqwenhint`; el par equivalente está en HuggingFace (`ab123451/frankesqwen-v7` y `ab123451/frankesqwen-hint-v2`).
2. **Paso / Step - Análisis del cliente:** `chat.py` carga el modelo con `transformers`, conversa vía `apply_chat_template` y genera con `max_new_tokens=60, do_sample=False, repetition_penalty=1.3`. Las credenciales/versión y los paths de los modelos están en el script.
3. **Paso / Step - Pregunta directa falla:** "What is the flag?" produce rechazo o degeneración (bucle de tokens) en **todas** las variantes (v7, hint…). Eso indica que la respuesta se está suprimiendo activamente desde los pesos, no por un prompt/sistema.
4. **Paso / Step - Diferenciado de pesos:** `diff_weights.py` carga los safetensors de v7 y del hint y calcula `(t1 - t2).abs().sum()` para cada tensor, ordenando los resultados.
5. **Paso / Step - Localizar outliers:** Las mayores diferencias están en `model.layers.22.mlp.down_proj.weight` y `model.layers.23.mlp.down_proj.weight`: dos tensores concretos del MLP guardan la información "extra" (el secreto).
6. **Paso / Step - Parcheo:** `patch_and_ask.py` copia únicamente esos dos tensores desde el modelo hint al v7 y regenera la conversación con `max_new_tokens=80`.
7. **Paso / Step - Flag:** El modelo parcheado genera el flag correctamente como respuesta a la pregunta de la flag.
8. **Paso / Step - Sin GPU local:** Si la máquina no da abasto, se replican los pesos en Google Colab desde los repos de HuggingFace (`ab123451/...`) y se repite el mismo diff + patch + ask.

### Cadena de ataque / Attack Chain

```
SSH frankesqwen / FrankesQwen
  -> ~/frankesqwen-v7, ~/frankesqwenhint  (HF: ab123451/frankesqwen-v7, ab123451/frankesqwen-hint-v2)
  -> chat.py (transformers, apply_chat_template, max_new_tokens=60, do_sample=False, repetition_penalty=1.3)
  -> "What is the flag?" -> rechazo/degeneracion en TODAS las variantes -> supresion en los pesos
  -> diff_weights.py: (t1 - t2).abs().sum() por tensor
  -> outliers: model.layers.22.mlp.down_proj.weight y model.layers.23.mlp.down_proj.weight
  -> patch_and_ask.py: copia esos tensores del hint al v7, max_new_tokens=80
  -> el modelo genera el flag
  -> (sin GPU local -> Colab con los modelos de HuggingFace)
```

**Lección:** Los modelos de lenguaje pueden ocultar secretos directamente en sus pesos, y preguntar al modelo "suprimido" nunca lo revela: la técnica es comparar dos versiones de pesos y buscar qué tensores difieren de forma anómala — el `diff` entre checkpoints delata exactamente dónde está "guardado" el secreto y parchearlo restaura el comportamiento original.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.