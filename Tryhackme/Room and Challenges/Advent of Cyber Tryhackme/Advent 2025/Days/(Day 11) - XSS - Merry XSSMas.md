# XSS - Merry XSSMas

| **Dificultad** | Easy | **Tipo** | walkthrough | **Slug** | `day11xssmerryxssmas` |
| **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber25) |
| **Sección** | Advent of Cyber Tryhackme |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | XSS / Reflected XSS / Stored XSS / textContent / innerHTML / cookies / input sanitisation |
| **Impacto** | Comprender y explotar XSS reflejado y almacenado para obtener flags |

---

**Contexto:** Día 11 del Advent of Cyber 2025. Se introduce el Cross-Site Scripting (XSS), una vulnerabilidad web que permite inyectar código JavaScript en campos de entrada que otros usuarios verán reflejado. Se distinguen el XSS reflejado (la inyección aparece de inmediato en la respuesta y se explota vía phishing contra víctimas individuales) y el XSS almacenado (el script se guarda en el servidor y se carga para todo usuario). También se repasan las protecciones: usar textContent en lugar de innerHTML, hacer las cookies inaccesibles a JavaScript y sanear/codificar entradas y salidas.

## Solucionario

### Día 11: XSS - Merry XSSMas

**Explicación:**

- **XSS** is a web application vulnerability that lets attackers inject malicious code (usually JavaScript) into input fields that reflect content viewed by other users
     1. Reflected XSS: when the injection is immediately projected in a response; exploited via phishing; targets individual victims 
     2. Stored XSS: malicious script is saved on the server and then loaded for every user who views the affected page

- Protection against XSS
     1. Use textContent instead of inner HTML
     2. Make cookies inaccessible to JS
     3. Sanitise input/output and encode

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which type of XSS attack requires payloads to be persisted on the backend? | `stored` |
| 2 | What's the reflected XSS flag? | `THM{Evil_Bunny}` |
| 3 | What's the stored XSS flag? | `THM{Evil_Stored_Egg}` |

---

**Metodología:** Se identificó el tipo de XSS (reflejado vs almacenado) por cómo se proyecta el payload. Para el XSS reflejado se inyectó el payload directamente en el campo vulnerable y se capturó la flag reflejada; para el XSS almacenado el payload quedó persistido en el backend y se obtuvo la flag cuando el contenido se cargó para otros usuarios.
**Learning chain:** XSS reflejado (payload inmediato) -> XSS almacenado (payload persistido en backend) -> textContent vs innerHTML -> cookies HttpOnly -> sanitización de entrada/salida -> Flags

Cadena de ataque / Attack Chain:
```
inyección <script> en input -> respuesta reflejada (Reflected XSS) -> flag THM{Evil_Bunny}
inyección <script> persistida en servidor (Stored XSS) -> carga para todos los usuarios -> flag THM{Evil_Stored_Egg}
```

**Lección:** *La diferencia entre XSS reflejado y almacenado determina el alcance: el reflejado es individual y suele llegar por phishing, mientras que el almacenado impacta a todos los visitantes; la defensa pasa por no usar innerHTML, proteger las cookies de JS y sanear todo input/output.*

**MITRE ATT&CK:** T1059.007 - JavaScript, T1189 - Drive-by Compromise

**Fuente:** [TryHackMe - XSS - Merry XSSMas](https://tryhackme.com/room/adventofcyber25)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.