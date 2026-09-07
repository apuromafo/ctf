# Phishing Basics

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `phishingbasics` |
| **Link** | [TryHackMe](https://tryhackme.com/room/phishingbasics) |
| **Sección** | 01 Level Easy |
| **Fuente** | Redacción oficial de TryHackMe + laboratorio SET (Social Engineering Toolkit) con máquina de atacante |
| **Componentes** | Fases del phishing / psicología (6 principios) / typosquatting / SPF / DKIM / DMARC / métricas de campaña (benchmarks) / SET credential harvester / Rainloop (email spoofing) |
| **Impacto** | Fundamentos de phishing como vía de acceso inicial en pentest: ciclo completo y demo práctica de SET con harvester de credenciales |

---

**Contexto:** El phishing explota el elemento humano: **smishing** va por SMS, **spear phishing** se personaliza para un objetivo y **whaling** apunta a ejecutivos (CEO). La psicología usa 6 principios (Scarcity, Urgency, Authority, Fear, Curiosity, Trust). Técnicamente existe el **typosquatting** (dominios con erratas) y el **spoofing** de correo, que se mitiga con **SPF + DKIM + DMARC**. Toda campaña mide métricas con benchmarks (click rate 8–14% aceptable; credential entry >5% es **High risk**). En el lab usarás **SET** para montar un *credential harvester* en `/home/attacker/setoolkit/index.html`, mandar el correo con la alias `support@tryaccounting.thm` desde Rainloop y cazar las credenciales de Bob: la contraseña con el flag final es la prueba de éxito.

## Solucionario

### Task 1: Introducción / Introduction

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Are you ready? | `No answer needed` |

### Task 2: Phishing 101

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the primary channel used during a **smishing** attack? | `SMS` |
| 2 | You are a CEO and have just received a phishing email **sent only to you**. What type of phishing is this? | `Whaling` |

### Task 3: Psicología del Phishing / Psychology of Phishing

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | A special offer for the new iPhone will **expire in 24 hours** if you don't act now. Which principle? | `Urgency` |
| 2 | An executive requests sensitive data **emphasising their position**. Which principle? | `Authority` |
| 3 | A message promising **exclusive access** to a product **no one else knows about**. Which principle? | `Curiosity` |
| 4 | An email claiming your credentials were found in a **recent data breach**. Which principle? | `Fear` |

### Task 4: Técnicas de Phishing / Phishing Techniques

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which technique relies on users making a **typo**? | `Typosquatting` |
| 2 | Which three security measures help defend against email **spoofing**? *(Alphabetical order, separated by commas)* | `DKIM, DMARC, SPF` |

### Task 5: Anatomía de una Campaña / Anatomy of a Phishing Campaign

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Your campaign shows a **credential entry rate of 6%**. What risk level per the benchmarks? | `High risk` |
| 2 | Which metric measures the percentage of users who **open an attachment**? | `Attachment Detonation Rate` |
| 3 | A client has a **click rate of 10%**. Which single recommendation from the table? | `Focused security awareness training` |

### Task 6: El Kit de Ingeniería Social / The Social Engineering Toolkit *(vm)*

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the **password flag**? | `THM{you_just_got_phished!}` |

### Task 7: Conclusión / Conclusion

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Well done on completing this room! | `No answer needed` |

---

**Metodología:**
1. **Phishing 101:** smishing usa SMS/mensajes de texto (SMS + phishing = smishing; vishing = voz); un spear phishing dirigido a un ejecutivo de alto cargo es **whaling**.
2. **Psicología:** los 6 principios son Scarcity, Urgency, Authority, Fear, Curiosity, Trust: countdown → "expira en 24h" = **Urgency**; el rango/cargo ("soy el ejecutivo") = **Authority**; promesa de información exclusiva/secreta ("nadie más lo sabe") = **Curiosity**; alarma sobre un incidente personal ("brecha, credenciales filtradas") = **Fear**.
3. **Técnicas:** **Typosquatting** registra dominios similares por error de tecleo (`tryhacme.com` vs `tryhackme.com`); la defensa contra spoofing en orden alfabético es **DKIM, DMARC, SPF** (DomainKeys Identified Mail; Domain-based Message Authentication, Reporting & Conformance; Sender Policy Framework).
4. **Anatomía de campaña:** benchmarks → Credential Entry Rate `<2% low`, `2–5% moderate`, `>5% high` → 6% = **High risk**; la métrica de adjuntos es **Attachment Detonation Rate** (% de usuarios que abren/ejecutan un adjunto); con click rate 10% (rango "8–14% acceptable") la recomendación única es **Focused security awareness training**.
5. **Lab de SET:** responder antes los conceptos (Task 2–5) leyendo las definiciones del room. SSH `attacker:attacker1234` a la VM `MACHINE_IP`, preparar el sitio en `/home/attacker/setoolkit/` y lanzar **SET** → Website Attack Vectors → Credential Harvester (Custom Import) con el HTML propio (IP POST-back = `MACHINE_IP`, opción `1. Copy just the index.html`, URL `http://tryacounting.thm` — nótese el **typo** intencional).
6. **Verificar el harvester** en `http://MACHINE_IP` ("Time to Get Phishy"). Rainloop en `http://MACHINE_IP:8080` con `attacker@phisher.thm : attacker1234`: elegir la alias **`support@tryaccounting.thm`** en el campo *From* para esquivar el filtro de seguridad y enviar el correo a `bob@tryaccounting.thm` (asunto tipo `Action Required: Password Expiration Notice` con el link `http://tryacounting.thm`).
7. **Recoger credenciales:** en la terminal de SET aparecen las credenciales de Bob → **password flag = `THM{you_just_got_phished!}`**. Cierra el ciclo: psicología + técnica + herramientas + reporting. Siguiente reto sugerido: **You Got Mail**.

**Learning chain:** OSINT → objetivo Bob (bob@tryaccounting.thm) + política de passwords estricta → typosquatting `http://tryacounting.thm` (una 'c' menos) → SET credential harvester (custom import) → email spoofing con alias `support@tryaccounting.thm` desde Rainloop → pretexto "Action Required: Password Expiration Notice" (urgency + authority) → víctima introduce credenciales → SET las captura → THM{you_just_got_phished!}

**MITRE ATT&CK:** T1566.001 (Phishing: Spearphishing Attachment), T1566.002 (Phishing: Spearphishing Link), T1598.002 (Phishing for Information: Spearphishing Attachment), T1585 (Establish Accounts), T1588 (Obtain Capabilities)

**Fuente:** [TryHackMe - Phishing Basics](https://tryhackme.com/room/phishingbasics)