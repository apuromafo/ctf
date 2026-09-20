# TShark Challenge I_ Teamwork

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `tsharkchallengeiteamwork` | [TryHackMe](https://tryhackme.com/room/tsharkchallengeiteamwork) | 01 Level Easy | THM | tshark, phishing, correo, pcap, PayPal, análisis forense | Análisis de un correo de phishing y su infraestructura mediante tshark sobre una pcap |

---

**Contexto:**

> **ES:** La sala analiza una pcap con un correo de phishing que suplanta a PayPal. Con tshark se extrae la URL de fraude, la fecha y hora del mensaje, la marca suplantada, la IP maliciosa y el remitente del correo, identificando la infraestructura usada contra la víctima.

> **EN:** This room analyzes a pcap containing a phishing email impersonating PayPal. With tshark you extract the fraudulent URL, the message timestamp, the impersonated brand, the malicious IP, and the sender email, identifying the infrastructure used against the victim.

## Solucionario

### Task 1: Configuración / Setup

**Explicación:**

1. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Guided setup of the room and its files. | `No answer needed` |

### Task 2: Análisis del phishing / Phishing Analysis

**Explicación:**

2. 1. hxxp[://]www[.]paypal[.]com4uswebappsresetaccountrecovery[.]timeseaways[.]com/
   2. 2017-04-17 22:52:53 UTC
   3. PayPal
   4. 184[.]154[.]127[.]226
   5. johnny5alive[at]gmail[.]com
   6. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the phishing URL? | `hxxp[://]www[.]paypal[.]com4uswebappsresetaccountrecovery[.]timeseaways[.]com/` |
| 2 | What is the timestamp of the phishing email? | `2017-04-17 22:52:53 UTC` |
| 3 | Which brand is impersonated? | `PayPal` |
| 4 | What is the malicious IP address? | `184[.]154[.]127[.]226` |
| 5 | What is the sender's email address? | `johnny5alive[at]gmail[.]com` |
| 6 | Additional guided step. | `No answer needed` |

---

**Metodología:** Se examina la captura con tshark y se localizan los paquetes correspondientes al correo de phishing. Se extrae la URL fraudulenta, la fecha y hora exacta del mensaje, la marca suplantada (PayPal), la IP de la infraestructura maliciosa y la dirección de correo del remitente, reconstruyendo el ataque de spear phishing dirigido a recuperar credenciales de la víctima.

### Cadena de ataque / Attack Chain

Email capture → phishing URL extraction → email metadata → malicious IP → sender attribution.

**Learning chain:** pcap parsing → phishing URL → email metadata → IP tracing → brand impersonation

**Lección:** *El correo es la puerta de entrada más usada: analizar su URL, metadatos y remitente decide si un mensaje es una trampa o una simple alerta falsa.*

**MITRE ATT&CK:** T1566.001 (Phishing: Spearphishing Attachment), T1204 (User Execution), T1071.001 (Application Layer Protocol: Web Protocols)

**Fuente:** [TryHackMe - TShark Challenge I_ Teamwork](https://tryhackme.com/room/tsharkchallengeiteamwork)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.