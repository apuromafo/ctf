# Identification & Scoping

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Blue Team / Incident Response (DFIR) | identificationscoping | https://tryhackme.com/room/identificationscoping | 02 Level Medium | TryHackMe | Outlook, Asset Inventory, Spreadsheet of Doom (SoD), SPF/DKIM/DMARC | Identificación y alcance de un incidente |

---

**Contexto:** **Identification & Scoping** es la fase de *Incident Response* (ruta SOC Level 2) ambientada en la organización ficticia **SwiftSpend Financial (SSF)**. Como analista *on-call* se revisan varios **tickets de soporte en Outlook** de la mano del colega **John Sterling**, se cruzan con un **Asset Inventory** (dispositivo, propietario y rol) y se registran los indicadores de compromiso (IoC) en la **Spreadsheet of Doom (SoD)**. El objetivo es responder a dos preguntas clave: *¿es real el incidente?* (**Identification**) y *¿hasta dónde llega?* (**Scoping**). Ambas actividades forman un **bucle de retroalimentación**: confirmar un correo de *phishing* conduce a una segunda víctima, cuyo ticket revela un dominio falsificado que se añade al SoD, y así se amplía el alcance. El caso acaba siendo un **credential phishing** con dominio de remitente falsificado (`emkei.cz`) y controles de correo ausentes (**SPF, DKIM y DMARC**).

## Solucionario

### Task 1: Introducción
**Explicación:**

1. La sala presenta el escenario de SwiftSpend Financial (SSF) y el flujo de trabajo basado en tickets de soporte.
2. Se explica la diferencia entre **Identification** (confirmar que el incidente es real) y **Scoping** (determinar su extensión), y el uso del **Asset Inventory** y de la **SoD** como herramientas centrales.

No answer needed

### Task 2: Ticket#2023012398704232 — el "error extraño" en Outlook
**Explicación:**

1. Se abre el hilo de tickets en **Outlook**; el asunto del `Ticket#2023012398704232` es un «error extraño» reportado por el usuario, que en apariencia es algo mundano.
2. **John** evalúa que el problema podría estar relacionado con la **configuración de seguridad del correo**, concretamente con los registros **SPF, DKIM y DMARC** (su ausencia facilita la suplantación del remitente).
3. Para analizar el equipo `WKSTN-02` se solicitan los **logs del proxy web**, que permiten reconstruir la navegación del usuario y confirmar el contacto con infraestructura maliciosa.

Respuestas:
- Asunto del ticket → `Weird Error in Outlook`
- Con qué podría estar relacionado según John → `SPF, DKIM & DMARC records`
- Datos solicitados para analizar WKSTN-02 → `Web Proxy logs`

### Task 3: Cruzando tickets con el Asset Inventory
**Explicación:**

1. `Ticket#2023012398704231` indica que un equipo necesita actualizar sus definiciones de **Endpoint Protection**. Al buscar el hostname en el **Asset Inventory** se obtiene su propietario: **Derick Marshall**.
2. `Ticket#2023012398704232` aporta el dominio de *phishing* donde la víctima envió sus credenciales, ya presente en el SoD: `b24b-158-62-19-6.ngrok-free.app`.
3. `Ticket#2023012398704233` introduce un segundo dominio de *phishing* que **aún no está en el SoD** y debe añadirse: `kennaroads.buzz`.

Respuestas:
- Propietario del equipo que necesita actualizar Endpoint Protection → `Derick Marshall`
- Dominio de phishing donde se enviaron las credenciales comprometidas → `b24b-158-62-19-6.ngrok-free.app`
- Dominio de phishing a añadir al SoD → `kennaroads.buzz`

### Task 4: Artefactos, SoD y pivoting
**Explicación:**

1. Según el análisis de **John** sobre `Ticket#2023012398704232`, el dominio `emkei.cz` se utilizó para **falsificar el correo** (*email spoofing*) y debe añadirse al SoD.
2. Revisando los artefactos disponibles del ticket se descubre otro usuario que recibió un correo de *phishing* similar pero **no abrió ticket ni lo reportó**: `alexander.swift@swiftspend.finance`.
3. El correo de *phishing* se originó desde una cuenta externa; esa dirección se convierte en un **IoC/punto de pivote** adicional para el SoD: `sales.tal0nix@gmail.com`.
4. Los intercambios de correo exponen en claro la contraseña del usuario comprometido, que fue introducida en el dominio de *phishing*: `Passw0rd!`.

Respuestas:
- Dominio usado para *email spoofing* → `emkei.cz`
- Usuario que recibió el phishing y no lo reportó → `alexander.swift@swiftspend.finance`
- IoC adicional usado como punto de pivote → `sales.tal0nix@gmail.com`
- Contraseña del usuario comprometido → `Passw0rd!`

### Task 5: Conclusión
**Explicación:**

1. La sala cierra repasando cómo el bucle **Identification ↔ Scoping** refina progresivamente el alcance real del compromiso.
2. El caso se entrega a la siguiente fase (*Threat Intel & Containment*) con un SoD enriquecido y una imagen clara del *phishing* de credenciales.

No answer needed

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Introducción | `No answer needed` |
| 2 | Asunto del Ticket#2023012398704232 | `Weird Error in Outlook` |
| 3 | Con qué podría estar relacionado (según John) | `SPF, DKIM & DMARC records` |
| 4 | Datos solicitados para analizar WKSTN-02 | `Web Proxy logs` |
| 5 | Propietario del equipo que necesita actualizar Endpoint Protection | `Derick Marshall` |
| 6 | Dominio de phishing donde se enviaron las credenciales | `b24b-158-62-19-6.ngrok-free.app` |
| 7 | Dominio de phishing a añadir al SoD | `kennaroads.buzz` |
| 8 | Dominio usado para email spoofing | `emkei.cz` |
| 9 | Usuario que recibió el phishing y no lo reportó | `alexander.swift@swiftspend.finance` |
| 10 | IoC adicional usado como punto de pivote | `sales.tal0nix@gmail.com` |
| 11 | Contraseña del usuario comprometido | `Passw0rd!` |
| 12 | Conclusión | `No answer needed` |

---

**Metodología:** Revisión cronológica de los hilos de tickets en **Outlook**, correlación de hostnames y usuarios con el **Asset Inventory**, recolección de artefactos (correos, cabeceras, logs del proxy web) y registro estructurado de IoC en la **Spreadsheet of Doom (SoD)**, aplicando el bucle de retroalimentación **Identification ↔ Scoping** para acotar el verdadero alcance del incidente.

**Learning chain:** Ticket en Outlook → asunto "Weird Error in Outlook" → causa raíz (SPF/DKIM/DMARC) → logs del proxy web → Asset Inventory → propietario (Derick Marshall) → dominio de phishing (ngrok-free.app) → segundo dominio (kennaroads.buzz) → spoofing (emkei.cz) → víctima no reportada (alexander.swift@swiftspend.finance) → IoC de pivote (sales.tal0nix@gmail.com) → contraseña expuesta (Passw0rd!) → SoD actualizado.

**Lección:** *Identification y Scoping no son pasos secuenciales, sino un bucle: cada indicador confirmado reabre la pregunta de quién más se vio afectado. Tratar un SoD y un Asset Inventory como documentos vivos —y leer los tickets en orden cronológico— es lo que permite descubrir víctimas que no reportaron el incidente y evitar cerrar el caso con una visión incompleta. La ausencia de SPF, DKIM y DMARC convierte un correo falsificado en una amenaza creíble.*

**MITRE ATT&CK:** T1566.002 Phishing: Spearphishing Link · T1598.003 Phishing for Information: Spearphishing Link · T1585.002 Establish Accounts: Email Accounts · T1078 Valid Accounts · T1114 Email Collection.

**Fuente:** [TryHackMe - Identification & Scoping](https://tryhackme.com/room/identificationscoping)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
