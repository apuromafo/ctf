# Phishing - Phishmas Greetings

| **Dificultad** | Easy | **Tipo** | walkthrough | **Slug** | `day12phishingphishmasgreetings` |
| **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber25) |
| **Sección** | Advent of Cyber Tryhackme |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | phishing / impersonation / social engineering / typosquatting / punycode / spoofing / SPF / DKIM / DMARC |
| **Impacto** | Clasificar correos de phishing reales distinguiendo impersonación, spoofing, typosquatting y spam |

---

**Contexto:** Día 12 del Advent of Cyber 2025. Se aprenden las técnicas para detectar correos de phishing: comprobar si el remitente coincide con el dominio interno o la estructura de email de la empresa (impersonation), reconocer el **typosquatting** (dominios con erratas comunes), el **punycode** (Unicode convertido a ASCII que permite dominios falsos) y el **spoofing** (hacerse pasar por un dominio legítimo). También se revisan los mecanismos de autenticación de email: SPF (servidores autorizados), DKIM (firma digital del mensaje) y DMARC (política sobre qué hacer con correos sospechosos).

## Solucionario

### Día 12: Phishing - Phishmas Greetings

**Explicación:**

- You can spot impersonation attempts by looking to see if the sender's email matches the internal domain or the standard email structure of the company
- Social engineering in phishing
- **Typosquatting** is when an attacker registers a common misspelling of an organisation's domain
- **punycode** is a special encoding system that converts Unicode characters (used in writing systems like Chinese, Cyrillic, and Arabic) into ASCII
- **spoofing** is a way attackers can trick users into thinking they are receiving emails from a legitimate domain.

- if an email really comes from who it says it does:
    1. SPF: Says which servers are allowed to send emails for a domain (like a list of approved senders).
    2.  DKIM: Adds a digital signature to prove the message wasn’t changed and really came from that domain.
    3.  DMARC: Uses SPF and DKIM to decide what to do if something looks fake (for example, send it to spam or block it).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Classify the 1st email, what's the flag? | `THM{yougotnumber1-keep-it-going}` |
| 2 | Classify the 2nd email. What's the flag? | `THM{nmumber2-was-not-tha-thard!}` |
| 3 | Classify the 3rd email. What's the flag? | `THM{Impersonation-is-areal-thing-keepIt}` |
| 4 | Classify the 4th email. What's the flag? | `THM{Get-back-SOC-mas!!}` |
| 5 | Classify the 5th email. What's the flag? | `THM{It-was-just-a-sp4m!!}` |
| 6 | Classify the 6th email. What's the flag? | `THM{number6-is-the-last-one!-DX!}` |

---

**Metodología:** Se analizó cada uno de los seis correos aplicando los conceptos del día: comparación del remitente con el dominio interno, búsqueda de typosquatting/punycode/spoofing y comprobación de SPF, DKIM y DMARC. Según la técnica detectada se clasificó cada email y se obtuvo su flag.
**Learning chain:** clasificación de emails -> impersonation (*typosquatting*/punycode/spoofing) -> autenticación SPF/DKIM/DMARC -> 6 flags

Cadena de ataque / Attack Chain:
```
correo sospechoso -> remitente no coincide con dominio interno -> typosquatting/punycode/spoofing -> SPF/DKIM/DMARC fallidos o ausentes -> clasificación (impersonation/spam/etc.) -> flag THM{...}
```

**Lección:** *Un correo que "parece" legítimo se puede desmontar en segundos comparando el dominio del remitente y comprobando SPF/DKIM/DMARC; el typosquatting y el punycode explotan justamente la falta de atención a los detalles del dominio.*

**MITRE ATT&CK:** T1566.002 - Phishing: Spearphishing Link, T1566.001 - Phishing: Spearphishing Attachment

**Fuente:** [TryHackMe - Phishing - Phishmas Greetings](https://tryhackme.com/room/adventofcyber25)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.