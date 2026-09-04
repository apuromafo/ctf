 
## AI/ML Security Threats  

 <img src="https://tryhackme-images.s3.amazonaws.com/room-icons/6228f0d4ca8e57005149c3e3-1744795088730" width="250" alt=" AI/ML Security Threats">

> **Información de la sala**
> * **Tipo:** Walkthrough (Guía paso a paso)
> * **Acceso:** Sala gratuita. ¡Cualquiera puede desplegar las máquinas! 
> * **Creado por:** tryhackme,Maxablancas,h4sh3m00
> * **Enlace oficial:** [https://tryhackme.com/room/aimlsecuritythreats](https://tryhackme.com/room/aimlsecuritythreats)
 

# aimlsecuritythreats [EASY]

## Los Pilares de la IA / The Pillars of AI

La inteligencia artificial se refiere a una máquina o sistema informático capaz de llevar a cabo tareas que, de otro modo, requerirían razonamiento, comprensión, resolución de problemas o creatividad humana.

### Aprendizaje Automático (Machine Learning) / Machine Learning

El ML sigue un ciclo de vida estructurado para garantizar el desarrollo y despliegue confiable de los modelos.

Este proceso comienza con la definición del problema, como determinar si un correo electrónico es spam. A continuación, se recopilan, limpian y preparan los datos mediante la ingeniería de características, asegurando que se extraigan patrones significativos evitando el sobreajuste (**overfitting**: cuando la familiaridad de un modelo con los datos de entrenamiento provoca que no logre realizar generalizaciones sobre datos no vistos o puros).

El modelo es entonces entrenado utilizando un algoritmo seleccionado, seguido de una evaluación y ajuste para optimizar el rendimiento. Una vez perfeccionado, el modelo se despliega en un entorno de producción para su uso en el mundo real.

### Algoritmos de Aprendizaje Automático / Machine Learning Algorithms

Los algoritmos de ML son los métodos matemáticos utilizados para aprender patrones de los datos, mientras que los modelos de ML son los resultados entrenados derivados de estos algoritmos.

Estos algoritmos constan de tres componentes clave:

* Un **proceso de decisión**.
* Una **función de error**.
* Un **proceso de optimización del modelo**.

Los algoritmos de ML se dividen en cuatro categorías principales: supervisado, no supervisado, semi-supervisado y por refuerzo.

### Redes Neuronales y Aprendizaje Profundo (Deep Learning) / Neural Networks and Deep Learning

El objetivo principal de la IA es permitir que las computadoras se comporten como humanos a través del uso de redes neuronales. El cerebro humano procesa información utilizando neuronas interconectadas que se comunican entre sí mediante sinapsis.

Al igual que el cerebro procesa estímulos sensoriales, la **capa de entrada** recibe datos puros. Las **capas ocultas** procesan y refinan la entrada, donde cada conexión tiene un **peso** (weight) que determina su importancia. Finalmente, la **capa de salida** produce la predicción. Cuando una red tiene más de tres capas, se clasifica como un algoritmo de DL (Deep Learning).

---

### Responde las siguientes preguntas / Answer the following questions

1. What category of machine learning combines both labelled and unlabelled data?

`Semi-supervised Learning`

2. What is the first layer in a neural network that handles incoming raw data?

`Input layer`

3. Which learning method does not require human-labeled data and can extract features from raw, unstructured input?

`Deep Learning`

4. What are the weighted connections between nodes in a neural network meant to simulate in the human brain?

`Synapses`

---

## LLMs

Los Modelos de Lenguaje Extensos (LLMs) son modelos de IA basados en aprendizaje profundo que pueden procesar y generar texto prediciendo la siguiente palabra en una secuencia.

Se entrenan en una fase de "pre-entrenamiento" procesando cantidades masivas de datos. En lugar de depender de datos etiquetados, utilizan miles de millones de parámetros. Utilizan un algoritmo llamado **backpropagation** (retropropagación) para ajustar estos parámetros y mejorar las predicciones.

Las redes neuronales **transformer**, introducidas por Google en 2017, revolucionaron los LLMs al permitir el procesamiento de texto en paralelo y asignar "atención" a palabras clave para mejorar la comprensión contextual. Después del pre-entrenamiento, se realiza el **RLHF** (Aprendizaje por Refuerzo a partir de Retroalimentación Humana).

---

### Responde las siguientes preguntas / Answer the following questions

1. What type of AI model enabled major advancements in ChatGPT and similar tools?

`Large Language Models`

2. What is the first training stage where an LLM processes massive amounts of data?

`Pre-training`

3. What type of neural network introduced by Google in 2017 powers modern LLMs?

`Transformer`

---

## Amenazas de Seguridad en IA / AI Security Threats

### Vulnerabilidades en Modelos de IA / AI Model Vulnerabilities

1. **Prompt Injection**: Sobrescribir las instrucciones originales para fines maliciosos.
2. **Data Poisoning**: Manipular los datos de entrenamiento para sesgar el resultado.
3. **Model Theft**: Clonar un modelo interactuando con su API.
4. **Privacy Leakage**: Revelar inadvertidamente información sensible de los datos de entrenamiento.
5. **Model Drift**: Deterioro del rendimiento del modelo con el tiempo.

### Ataques Mejorados / Enhanced Attacks

1. **Malware**: Generación instantánea de código malicioso.
2. **DeepFakes**: Replicar la voz o imagen de una persona para vulnerar la autenticación.
3. **Phishing**: Creación de correos electrónicos fluidos y convincentes.

---

### Responde las siguientes preguntas / Answer the following questions

1. What framework was developed by MITRE to guide the understanding of AI-specific cyber threats?

`ATLAS`

2. What type of attack involves cloning an AI model by interacting with its API?

`Model Theft`

3. What generative AI technique can replicate a person’s voice or appearance with high realism?

`DeepFake`

4. What common social engineering attack has become harder to detect due to AI-generated fluent and convincing messages?

`Phishing`

---

## IA Defensiva e IA Segura / Defensive AI and Safe AI

La IA mejora nuestra capacidad de **analizar**, **predecir**, **resumir** e **investigar**. Para asegurar la IA, debemos implementar:

* Controles de acceso (RBAC y MFA).
* Cifrado de datos de entrenamiento.
* Estándares de seguridad.
* Monitoreo del modelo con herramientas de explicabilidad como **SHAP** y **LIME**.

---

### Responde las siguientes preguntas / Answer the following questions

1. According to IBM, how many days faster does AI help identify and contain breaches?

`108`

2. What cybersecurity task benefits from AI helping to imagine attacker behavior we might not consider?

`Threat Hunting`

3. Explainability tools such as SHAP and LIME help with what?

`Model Monitoring`

---

## Práctica y Conclusión / Practice and Conclusion

### Responde las siguientes preguntas / Answer the following questions

What's the flag?

`THM{443/60/16384}`

---
 
## Conclusión / Conclusion

Al comienzo de esta sala, se señaló que "el conocimiento es poder" y esto es especialmente cierto en la lucha contra las ciberamenazas de la IA. El ritmo al que esta tecnología ha irrumpido en escena ha dejado a muchos sintiéndose rezagados. Ahora, con una mejor comprensión de la IA y la tecnología subyacente que le permite ser la fuerza que es actualmente en nuestra industria (y en todas), comprendes qué está representando una amenaza para nuestros sistemas y qué debe ser asegurado como resultado. Aquí tienes un resumen de lo que se ha cubierto:

* **Artificial Intelligence** (AI) es el campo general que se ocupa de permitir que las máquinas/sistemas imiten el comportamiento humano.
* **Machine learning** (ML) es un subcampo de la IA en el que un modelo puede ser alimentado y entrenado con entradas y utilizado para realizar predicciones.
* **Deep learning** (DL) es, a su vez, un subcampo del ML. Ya no necesita interacción humana y puede auto-enseñarse y procesar cantidades masivas de datos, lo cual es posible mediante el uso de **Redes Neuronales**.
* El DL ha permitido el surgimiento de tecnologías como los **LLMs** (y otra **IA generativa**), que, mediante el uso de redes neuronales transformer y atención, pueden ser consultados en lenguaje natural, entenderlo y responder de manera conversacional y similar a la humana.
* La IA es un arma peligrosa en manos de un atacante. Tiene el potencial de **mejorar los ciberataques existentes**, como el phishing, y aumentar la superficie de ataque al **introducir vulnerabilidades de IA**.
* Aunque es peligrosa en manos de atacantes, la IA **puede ser invaluable en la lucha contra las ciberamenazas de IA** y debe ser adoptada, pero **haciéndolo de forma segura** para que no se introduzcan vulnerabilidades.

---

### Glosario / Glossary:

* **Phishing**: Cuando se envían correos electrónicos a uno o varios objetivos fingiendo provenir de una entidad de confianza para engañar a las personas y que proporcionen información sensible.
* **AI (IA)**: La Inteligencia Artificial es la tecnología que permite a las computadoras y máquinas simular el comportamiento humano, como el aprendizaje y el razonamiento.
* **ML**: El Aprendizaje Automático (Machine Learning) es el término utilizado para describir los algoritmos y funciones que se utilizan para lograr que las computadoras piensen y actúen de la misma manera que lo hacen los humanos y la naturaleza.
 