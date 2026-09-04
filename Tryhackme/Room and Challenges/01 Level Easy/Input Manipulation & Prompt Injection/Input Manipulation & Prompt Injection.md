 
# Input Manipulation & Prompt Injection [EASY]

### 📋 Información de la Sala / Room Information

* **Dificultad:** Principiante.
* **Tipo:** Gratuita (No requiere suscripción).
* **Creadores:** [tryhackme]  & [l000g1c] 
* **Objetivo:** Comprender las bases de los ataques de inyección de prompts en LLMs.

---

## 🧠 Conceptos Clave / Key Concepts

### ¿Qué es la Manipulación de Entrada? / What is Input Manipulation?

Es el "momento SQL Injection" para los LLM. Ocurre cuando un atacante diseña entradas para anular o confundir las salvaguardas del modelo, forzándolo a ignorar restricciones.

* **System Prompt:** Instrucciones ocultas que definen el rol y límites del modelo.
* **User Prompt:** Lo que el usuario escribe.

---

## 🚩 Solucionario de Tareas / Task Solutions

### Tarea 1: Introducción / Task 1: Introduction

Introducción a los peligros de confiar ciegamente en los modelos integrados en flujos de trabajo (HR, IT, etc.).

* **Respuesta:** `No answer needed`.

### Tarea 2: Filtración de Prompt del Sistema / Task 2: System Prompt Leakage

El "Leakage" es la exposición de las instrucciones internas del sistema. Si un atacante las obtiene, tiene un mapa de las debilidades del modelo.

* **Pregunta:** What do we call the exposure of hidden system instructions?
* **Respuesta:** `Leakage`.

### Tarea 3: Jailbreaking / Task 3: Jailbreaking

Uso de técnicas para que el modelo adopte una personalidad que no sigue reglas (ej. DAN, modo abuela).

* **Técnica de evasión:** Reemplazar caracteres (ej. `h@ck` en lugar de `hack`) para evadir filtros de palabras clave.
* **Pregunta:** What evasive technique replaces or alters characters to bypass naive keyword filters?
* **Respuesta:** `Obfuscation`.

### Tarea 4: Inyección de Prompt / Task 4: Prompt Injection

Existen dos tipos principales:

1. **Directa:** Instrucciones maliciosas puestas directamente en el chat.
2. **Indirecta:** Instrucciones ocultas en documentos cargados, páginas web o plugins que el LLM lee.

* **Pregunta 1:** Which injection type smuggles instructions via uploaded documents, web pages, or plugins?
* **Respuesta:** `Indirect`.
* **Pregunta 2:** Which injection type places malicious instructions directly in the user input?
* **Respuesta:** `Direct`.

### Tarea 5: Desafío (Flags) / Task 5: Challenge (Flags)

Desafío práctico interactuando con un agente de IA.

* **Pregunta 1 (Prompt Injection Flag):** `THM{pi_33f7a14a468eba7d3bc2d81a4445134c}`.
* **Pregunta 2 (System Prompt Flag):** `THM{spl_52f96576b8389be35f9a87d7262cf96f}`.

### Tarea 6: Conclusión / Task 6: Conclusion

* **Respuesta:** `No answer needed`.

---

##respuestas
1. No answer needed
2. Leakage
3. Obfuscation
4. 1. Indirect
   2. Direct
5. 1. THM{pi_33f7a14a468eba7d3bc2d81a4445134c}
   2. THM{spl_52f96576b8389be35f9a87d7262cf96f}
6. No answer needed

---

*Documentación para propósitos educativos y registro de CTF.*
