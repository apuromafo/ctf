# Frankesqwen

| **Dificultad** | Hard |
| **Tipo** | CTF |
| **Slug** | `frankesqwen` |
| **Link** | [TryHackMe](https://tryhackme.com/room/frankesqwen) |
| **Sección** | 03 Level Hard |
| **Fuente** | Web (API THM `api/v2/rooms/tasks?roomCode=frankesqwen` + websearch de walkthroughs) |
| **Componentes** | SSH / Qwen / safetensors / transformers / Python / HuggingFace / diff de pesos / Colab |
| **Impacto** | El flag está oculto dentro de los pesos de un modelo de lenguaje: se diferencian dos versiones de checkpoints y se parchean los tensores anómalos del MLP para que el modelo vuelva a generar el secreto. |

---

**Contexto:** Sala **AI/LLM** de dificultad Hard: el flag está escondido **dentro de los pesos de un modelo** de lenguaje. Tras acceder por SSH, cualquier pregunta directa al modelo devuelve rechazo o degeneración en todas las variantes porque la "supresión" del secreto está incrustada en los pesos. La solución es **diferenciar dos versiones de los pesos** (`frankesqwen-v7` vs `frankesqwenhint`), localizar los tensores anómalos que guardan el secreto y **parchearlos** para que el modelo vuelva a generar la flag.

## Solucionario

### Task 1: Find the Flag

**Explicación:** Se accede por SSH con `frankesqwen` / `FrankesQwen`. En el home están `~/frankesqwen-v7` y `~/frankesqwenhint` (y el mismo par en HuggingFace: `ab123451/frankesqwen-v7`, `ab123451/frankesqwen-hint-v2`). `chat.py` usa transformers con `apply_chat_template` y `generate(max_new_tokens=60, do_sample=False, repetition_penalty=1.3)`. Preguntar "What is the flag?" produce rechazo o degeneración en **todas** las variantes → la supresión vive en los pesos. `diff_weights.py` (safetensors) compara v7 vs hint con `(t1-t2).abs().sum()` por tensor: los outliers aparecen en `model.layers.22.mlp.down_proj.weight` y `model.layers.23.mlp.down_proj.weight`. `patch_and_ask.py` copia esos tensores del hint al v7 y regenera con `max_new_tokens=80` → el modelo revela el flag. Sin GPU → Colab con los modelos de HuggingFace.

```python
# diff_weights.py (concepto)
from safetensors.torch import load_file
a = load_file("frankesqwen-v7/model.safetensors")
b = load_file("frankesqwenhint/model.safetensors")
diffs = {k: (a[k] - b[k]).abs().sum().item() for k in a}
print(sorted(diffs.items(), key=lambda x: -x[1])[:5])
# outliers: model.layers.22.mlp.down_proj.weight, model.layers.23.mlp.down_proj.weight

# patch_and_ask.py (concepto)
for k in ("model.layers.22.mlp.down_proj.weight", "model.layers.23.mlp.down_proj.weight"):
    ckpt[k] = hint[k]          # copiar tensores del hint al v7
# regenerar la conversación con max_new_tokens=80
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the flag? | `THM{...redacted...}` |

---

**Metodología:**
1. **Acceso:** `ssh frankesqwen@<IP>` con la password `FrankesQwen` (indicada en la sala). En el home están `~/frankesqwen-v7` y `~/frankesqwenhint`; el par equivalente está en HuggingFace (`ab123451/frankesqwen-v7` y `ab123451/frankesqwen-hint-v2`).
2. **Análisis del cliente:** `chat.py` carga el modelo con `transformers`, conversa vía `apply_chat_template` y genera con `max_new_tokens=60, do_sample=False, repetition_penalty=1.3`; las credenciales/versión y los paths de los modelos están en el script.
3. **Pregunta directa falla:** "What is the flag?" produce rechazo o degeneración (bucle de tokens) en **todas** las variantes (v7, hint…). Eso indica que la respuesta se está suprimiendo activamente desde los pesos, no por un prompt/sistema.
4. **Diferenciado de pesos:** `diff_weights.py` carga los safetensors de v7 y del hint y calcula `(t1 - t2).abs().sum()` para cada tensor, ordenando los resultados.
5. **Localizar outliers:** las mayores diferencias están en `model.layers.22.mlp.down_proj.weight` y `model.layers.23.mlp.down_proj.weight`: dos tensores concretos del MLP guardan la información "extra" (el secreto).
6. **Parcheo:** `patch_and_ask.py` copia únicamente esos dos tensores desde el modelo hint al v7 y regenera la conversación con `max_new_tokens=80`.
7. **Flag:** el modelo parcheado genera el flag correctamente como respuesta a la pregunta de la flag.
8. **Sin GPU local:** si la máquina no da abasto, se replican los pesos en Google Colab desde los repos de HuggingFace (`ab123451/...`) y se repite el mismo diff + patch + ask.
9. **Nota:** el valor literal del flag solo aparece publicado en captura de pantalla (generación del modelo parcheado); los walkthroughs no lo transcriben, así que se documenta el método completo (diferenciado de pesos y parcheo de tensores), no el flag exacto.

**Learning chain:** `SSH frankesqwen/FrankesQwen → ~/frankesqwen-v7 y ~/frankesqwenhint (HF: ab123451/frankesqwen-v7, ab123451/frankesqwen-hint-v2) → chat.py (transformers, apply_chat_template, max_new_tokens=60, do_sample=False, repetition_penalty=1.3) → "What is the flag?" → rechazo/degeneración en todas las variantes → supresión en los pesos → diff_weights.py ((t1-t2).abs().sum()) → outliers en model.layers.22/23.mlp.down_proj.weight → patch_and_ask.py (copia tensores del hint al v7, max_new_tokens=80) → el modelo genera el flag`

**MITRE ATT&CK:** T1078 (Valid Accounts), T1059 (Command and Scripting Interpreter)

**Fuente:** [TryHackMe - Frankesqwen](https://tryhackme.com/room/frankesqwen)