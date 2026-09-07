# Phishing Basics [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough (Free)
* **Slug:** `phishingbasics`
* **Link:** https://tryhackme.com/room/phishingbasics
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Redacción oficial de TryHackMe + laboratorio SET (Social Engineering Toolkit) con máquina de atacante
* **Componentes:** Fases del phishing · psicología (6 principios) · typosquatting · SPF/DKIM/DMARC · métricas de campaña (benchmarks) · SET credential harvester · Rainloop (email spoofing)
* **Impacto rol:** Fundamentos de phishing como vía de acceso inicial en pentest. Cubre el ciclo completo planificar→recon→payload→explotar→reportar y una demo práctica de SET con harvester de credenciales. Requiere en el lab: desplegar VM y usar SET + Rainloop para capturar credenciales.

## Solucionario de Tareas / Task Solutions

> **ES:** El phishing explota el elemento humano: **smishing** va por SMS, **spear phishing** se personaliza para un objetivo y **whaling** apunta a ejecutivos (CEO). La psicología usa 6 principios (Scarcity, Urgency, Authority, Fear, Curiosity, Trust). Técnicamente existe el **typosquatting** (dominios con erratas) y el **spoofing** de correo, que se mitiga con **SPF + DKIM + DMARC**. Toda campaña mide métricas con benchmarks (click rate 8–14% aceptable; credential entry >5% es **High risk**). En el lab usarás **SET** para montar un *credential harvester* en `/home/attacker/setoolkit/index.html`, mandar el correo con la alias `support@tryaccounting.thm` desde Rainloop y cazar las credenciales de Bob: la contraseña con el flag final es la prueba de éxito.
> **EN:** Phishing exploits the human element: **smishing** goes via SMS, **spear phishing** is tailored to one target and **whaling** targets executives (CEOs). The psychology uses 6 principles (Scarcity, Urgency, Authority, Fear, Curiosity, Trust). Technically there's **typosquatting** (mistyped domains) and email **spoofing**, mitigated by **SPF + DKIM + DMARC**. Campaigns are measured against benchmarks (click rate 8–14% acceptable; credential entry >5% = **High risk**). In the lab you'll use **SET** to build a *credential harvester* at `/home/attacker/setoolkit/index.html`, send the email with the `support@tryaccounting.thm` alias from Rainloop and catch Bob's credentials: the flag-as-password is the proof of success.

### Task 1 — Introducción / Introduction

* **Check:** `Are you ready?`
* **ES:** El phishing es el camino de acceso inicial más usado; este room lo cubre desde la perspectiva del pentester.
* **EN:** Phishing is the go-to initial-access vector; this room covers it from a pentester's perspective.

### Task 2 — Phishing 101

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the primary channel used during a **smishing** attack? | `SMS` |
| You are a CEO and have just received a phishing email **sent only to you**. What type of phishing is this? | `Whaling` |

* **Smishing:** SMS / mensajes de texto (SMS + phishing = smishing; vishing = voz).
* **CEO:** spear phishing dirigido a un ejecutivo de alto cargo = **whaling**.

### Task 3 — Psicología del Phishing / Psychology of Phishing

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| A special offer for the new iPhone will **expire in 24 hours** if you don't act now. Which principle? | `Urgency` |
| An executive requests sensitive data **emphasising their position**. Which principle? | `Authority` |
| A message promising **exclusive access** to a product **no one else knows about**. Which principle? | `Curiosity` |
| An email claiming your credentials were found in a **recent data breach**. Which principle? | `Fear` |

* **Urgency:** countdown → "expira en 24h".
* **Authority:** el rango/cargo → "soy el ejecutivo".
* **Curiosity:** promesa de información exclusiva/secreta → "nadie más lo sabe".
* **Fear:** alarma sobre un incidente personal → "brecha, credenciales filtradas".
* Los 6 principios: **Scarcity · Urgency · Authority · Fear · Curiosity · Trust** (memotécnica mental: SUAFCT).

### Task 4 — Técnicas de Phishing / Phishing Techniques

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Which technique relies on users making a **typo**? | `Typosquatting` |
| Which three security measures help defend against email **spoofing**? *(Alphabetical order, separated by commas)* | `DKIM, DMARC, SPF` |

* **Typosquatting:** registrar dominios similares por error de tecleo (`tryhacme.com` vs `tryhackme.com`).
* **Orden alfabético / Alphabetical:** **DKIM, DMARC, SPF** (DomainKeys Identified Mail; Domain-based Message Authentication, Reporting & Conformance; Sender Policy Framework).

### Task 5 — Anatomía de una Campaña / Anatomy of a Phishing Campaign

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Your campaign shows a **credential entry rate of 6%**. What risk level per the benchmarks? | `High risk` |
| Which metric measures the percentage of users who **open an attachment**? | `Attachment Detonation Rate` |
| A client has a **click rate of 10%**. Which single recommendation from the table? | `Focused security awareness training` |

* **Benchmarks:** Credential Entry Rate → `<2% low`, `2–5% moderate`, `>5% high` → **6% = High risk**.
* **Métrica de adjuntos:** Attachment Detonation Rate (% de usuarios que abren/ejecutan un adjunto).
* **Click rate 10%:** está en el rango "8–14% acceptable" → recomendación única = **Focused security awareness training**. (Por encima de 14% sería el mismo tipo de formación pero "focused" cambia a otra acción según tabla; con 10% aplica directamente la del renglón Click Rate.)

### Task 6 — El Kit de Ingeniería Social / The Social Engineering Toolkit *(vm)*

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the **password flag**? | `THM{you_just_got_phished!}` |

* **Contexto del lab:** SSH `attacker:attacker1234` a la VM `MACHINE_IP`. Preparar el sitio (usar `/home/attacker/setoolkit/`).
* **SET — orden de menús / menu order:** `1. Social-Engineering Attacks` → `2. Website Attack Vectors` → `3. Credential Harvester Attack Method` → `3. Custom Import` (usar tu propio HTML; IP POST-back = `MACHINE_IP`; path `/home/attacker/setoolkit/`; opción `1. Copy just the index.html`; URL `http://tryacounting.thm` — nótese el **typo** intencional).
* **Correo / Email:** Rainloop en `http://MACHINE_IP:8080` con `attacker@phisher.thm : attacker1234`. Elegir la alias **`support@tryaccounting.thm`** en el campo *From* para esquivar el filtro de seguridad y enviar el correo a `bob@tryaccounting.thm` (asunto tipo `Action Required: Password Expiration Notice` con el link `http://tryacounting.thm`).
* **Resultado / Result:** en la terminal de SET aparecen las credenciales de Bob → **password flag = `THM{you_just_got_phished!}`**.

### Task 7 — Conclusión / Conclusion

* **Check:** `Well done on completing this room!` (siguiente reto sugerido: **You Got Mail**).
* **ES:** Cierra el ciclo: psicología + técnica + herramientas + reporting.
* **EN:** Closes the cycle: psychology + technique + tools + reporting.

## Metodología / Methodology

1. **Paso / Step:** Responder conceptos (Task 2–5) leyendo las definiciones del room.
2. **Paso / Step:** SSH a la VM y lanzar **SET** → Website Attack Vectors → Credential Harvester (Custom Import) con el HTML en `/home/attacker/setoolkit/`.
3. **Paso / Step:** Verificar el harvester en `http://MACHINE_IP` ("Time to Get Phishy").
4. **Paso / Step:** Rainloop (`MACHINE_IP:8080`) → nuevo mensaje → *From* = alias `support@tryaccounting.thm` → enviar a `bob@tryaccounting.thm`.
5. **Paso / Step:** Recoger las credenciales que muestra SET → flag = `THM{you_just_got_phished!}`.

### Cadena de ataque / Attack Chain

```
OSINT -> objetivo: Bob (bob@tryaccounting.thm) + política de passwords estricta
  -> typosquatting: dominio http://tryacounting.thm (una 'c' menos)
  -> SET: credential harvester en custom import (IP MACHINE_IP, /home/attacker/setoolkit/)
  -> email spoofing: alias support@tryaccounting.thm desde Rainloop (bypass del filtro)
  -> asunto/pretexto: Action Required: Password Expiration Notice (urgency + authority)
  -> la víctima introduce credenciales en el harvester -> SET las captura
  -> flag = THM{you_just_got_phished!}
```

**Mapeo MITRE ATT&CK:** T1566.001 (Phishing: Spearphishing Attachment) y T1566.002 (Spearphishing Link) · T1598.002 (Phishing for Information) · T1588/T1585 (infraestructura) · T1534 (bastante teórico aquí). El uso de SET para credential harvesting es clásico en assessments autorizados.

**Lección:** *Un pretexto con autoridad + urgencia y un dominio con un typo bastan para robar credenciales.* El defender lado rojo: revisar siempre la URL real, validar remitente y activar SPF/DKIM/DMARC.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.