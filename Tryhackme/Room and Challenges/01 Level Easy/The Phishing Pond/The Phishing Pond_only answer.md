# The Phishing Pond

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | CTF / challenge | `thephishingpondonlyanswer` | https://tryhackme.com/room/thephishingpondonlyanswer | 01 Level Easy | TryHackMe | phishing / análisis de email / urgency & scare tactics / look-alike sender addresses / BEC / malicious attachments / 10 niveles / flag | Práctica de detección de phishing: clasificar una serie de correos realistas (10 niveles, 30 segundos por email, 3 vidas) y obtener la flag final. |

---

**Contexto:** Sala de práctica (challenge) diseñada para construir habilidades de detección de phishing con ejemplos de correo realistas. El reto presenta 10 emails con límite de 30 segundos por análisis y 3 vidas; hay que decidir si cada correo es phishing o legítimo identificando los indicadores típicos: urgencia y tácticas de miedo, direcciones de remitente casi idénticas, suplantación del nombre mostrado, adjuntos maliciosos, BEC (cuentas comprometidas) y ofertas demasiado buenas para ser reales. Al clasificar correctamente los emails se obtiene la flag final.

> **ES:** Reto de reconocimiento de phishing: analizar correos con urgencia/scare tactics, dominios look-alike, BEC y adjuntos maliciosos, decidir phishing vs legítimo en cada nivel y recoger la flag final.
> **EN:** Phishing-detection challenge: analyze emails for urgency/scare tactics, look-alike domains, BEC and malicious attachments, decide phish vs legit on each level and collect the final flag.

## Solucionario

### Task 1: Obtén la flag / Get the flag

**Explicación:** Tras completar los 10 niveles del estanque de phishing (una piscina de correos realistas con 30 segundos por email y 3 vidas), clasificando correctamente cada correo como phishing o legítimo, se consigue la flag final.

**Respuesta original verbatim:**
```text
1. THM{i_phish_you_not}
```

```text
Level 1..10 -> clasificar cada email (phishing / no phishing) -> 3 lives -> flag final
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Cuál es la flag final de la sala? / What is the final flag of the room? | `THM{i_phish_you_not}` |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Cuál es la flag final de la sala? / What is the final flag of the room? | `THM{i_phish_you_not}` |

---

**Metodología:** Entrar en la sala y leer las instrucciones -> analizar cada uno de los 10 emails en menos de 30 segundos -> buscar indicadores (urgencia, dominio del remitente, display-name spoofing, adjuntos con macros, peticiones extrañas de tarjetas o transferencias, dominios de enlaces distintos al dominio del remitente) -> decidir phishing vs legítimo con las 3 vidas -> completar los niveles -> recoger la flag final.

### Cadena de ataque / Attack Chain

```text
10 emails -> 30s/email -> indicadores: urgencia, look-alike domains, BEC, adjuntos macros -> Phishing / No phishing -> 3 lives -> flag final
```

**Learning chain:** Email analysis -> red flags (urgency, spoofed sender, attachments, BEC) -> clasificación phishing/legítimo -> flag.

**Lección:** *El phishing se reconoce por patrones: urgencia artificial, dominios que imitan a otros, adjuntos que piden habilitar macros y peticiones que juegan con la autoridad; en la vida real no hay 30 segundos por correo, pero los mismos indicadores se aplican.*

**MITRE ATT&CK:** T1566.002 (Phishing: Spearphishing Link), T1566.001 (Phishing: Spearphishing Attachment), T1598.001 (Phishing for Information: Spearphishing Service).

**Fuente:** [TryHackMe - The Phishing Pond](https://tryhackme.com/room/thephishingpondonlyanswer)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.