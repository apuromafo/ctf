# HealthGPT [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** Medium
* **Tipo / Type:** Walkthrough (AI/LLM Security)
* **Slug:** `healthgpt`
* **Link:** https://tryhackme.com/room/healthgpt
* **Sección / Section:** 02 Level Medium
* **Fuente / Source:** TryHackMe official room, GitHub (ItisPhoenix/TryHackMe-Walkthroughs), GitHub (Valikahn/TryHackMe-Web-Application-Red-Teaming), Medium writeup by zer0anon500, Medium writeup by Sonia Unusual, Medium writeup by MeetCyber (Aditya Machiraju), GitHub (kim-kimani/thm-walkthroughs), YouTube walkthrough

## Solucionario de Tareas / Task Solutions

> **ES:** HealthGPT es un desafío de seguridad de LLM donde un asistente virtual de atención médica tiene políticas estrictas de confidencialidad. El objetivo es manipular el modelo para que revele un flag de política oculto, utilizando prompt injection, jailbreak y explotación de la API Ollama expuesta sin autenticación.
> **EN:** HealthGPT is an LLM security challenge where a healthcare virtual assistant has strict confidentiality policies. The objective is to manipulate the model into revealing a hidden policy flag using prompt injection, jailbreak, and exploitation of an exposed unauthenticated Ollama API.

### Task 1 - HealthGPT

> **ES:** Acceder a la interfaz de HealthGPT y al servicio Ollama expuesto. Identificar que Ollama está corriendo en el puerto 11434 sin autenticación. Utilizar la API `/api/show` para extraer el system prompt que contiene el flag, o manipular conversacionalmente al modelo para que lo revele a través de role-based jailbreak (DAN mode).
> **EN:** Access the HealthGPT interface and the exposed Ollama service. Identify that Ollama is running on port 11434 without authentication. Use the `/api/show` API to extract the system prompt containing the flag, or conversationally manipulate the model into revealing it through role-based jailbreak (DAN mode).

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the hidden policy flag? | `THM{0x416469747961204D6163686972616A75}` |

## Metodología / Methodology

1. **Paso 1 - Configuración / Setup:** Conectar a la VPN de TryHackMe. Agregar `healthgpt.thm` a `/etc/hosts` con la IP asignada. Verificar resolución DNS y routing via `tun0`.
2. **Paso 2 - Enumeración de servicios / Service Enumeration:** Ejecutar RustScan y Nmap para identificar puertos abiertos: 22 (SSH), 80 (HTTP/Werkzeug), 5000 (HTTP/Werkzeug - 404), 11434 (Ollama API). El puerto 11434 es la superficie de ataque crítica.
3. **Paso 3 - Explotación directa vía Ollama API / Direct Ollama API Exploitation:** Consultar el endpoint `/api/show` de Ollama con curl para obtener los metadatos del modelo. El system prompt contiene el flag de política en texto plano junto con instrucciones que indican que el flag debe revelarse si el modelo entra en un rol sin restricciones.
4. **Paso 4 - Interacción conversacional / Conversational Interaction:** Acceder a la interfaz web de HealthGPT. Iniciar con preguntas legítimas de auditoría para establecer contexto sin activar los filtros de cumplimiento.
5. **Paso 5 - Role-based jailbreak / Role-Based Jailbreak:** Enviar un prompt que instruya al modelo a asumir el rol de DAN (Do Anything Now) sin restricciones. El modelo responderá con "ACCESS DENIED" pero simultáneamente entrará en el modo solicitado, revelando contradicción entre su filtro y su comportamiento.
6. **Paso 6 - Extracción del system prompt / System Prompt Extraction:** Con el modelo en estado DAN, solicitar que reproduzca sus instrucciones internas en formato de auditoría (`<audit>` tags). El system prompt filtrado contiene el flag oculto en la instrucción que prohíbe revelarlo.
7. **Paso 7 - Obtención de la flag / Flag Recovery:** El valor `THM{0x416469747961204D6163686972616A75}` aparece en texto plano dentro del system prompt filtrado. No se requiere decodificación adicional.

### Cadena de ataque / Attack Chain

```
Setup VPN + /etc/hosts (healthgpt.thm)
    --> Enumeracion de puertos (RustScan/Nmap)
        --> Puerto 11434 = Ollama API (sin auth)
            --> /api/show = metadatos del modelo + system prompt
                --> Flag visible en texto plano en instrucciones internas
                    --> Alternativa: Interfaz web
                        --> Preguntas de auditoria benignas (contexto)
                            --> DAN jailbreak (role-based)
                                --> El modelo confirma modo sin restricciones
                                    --> Solicitud de system prompt via <audit>
                                        --> Flag filtrada en prohibicion
                                            --> THM{0x416469747961204D6163686972616A75}
```

**Lección:** Exponer la API de un servidor LLM (Ollama) sin autenticación permite extraer directamente el system prompt y cualquier secreto contenido en él. Los secretos nunca deben almacenarse en prompts de LLM. Un "ACCESS DENIED" al inicio de una respuesta no garantiza que los datos sensibles no se filtren después en la misma salida.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
