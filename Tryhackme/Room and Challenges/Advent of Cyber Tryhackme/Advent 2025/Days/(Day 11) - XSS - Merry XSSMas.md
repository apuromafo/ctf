# Advent 2025\Days [N/A]

- **XSS** is a web application vulnerability that lets attackers inject malicious code (usually JavaScript) into input fields that reflect content viewed by other users
     1. Reflected XSS: when the injection is immediately projected in a response; exploited via phishing; targets individual victims 
     2. Stored XSS: malicious script is saved on the server and then loaded for every user who views the affected page

- Protection against XSS
     1. Use textContent instead of inner HTML
     2. Make cookies inaccessible to JS
     3. Sanitise input/output and encode

  
  

## Respuestas / Answers
- Which type of XSS attack requires payloads to be persisted on the backend? : `stored`
- What's the reflected XSS flag? : `THM{Evil_Bunny}`
- What's the stored XSS flag? : `THM{Evil_Stored_Egg}`

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
