# Just a VPN Login

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | challenge | `justavpnlogin` | [TryHackMe](https://tryhackme.com/room/justavpnlogin) | 01 Level Easy | TryHackMe | SOC, threat intelligence, TryDetectThis, LummaStealer, YARA, análisis de hash, OSINT | Triaje SOC de un login VPN sospechoso con inteligencia de amenazas (TryDetectThis) |

---

**Contexto:** Eres un analista SOC de primera línea. Recibes la alerta interna "Unusual VPN login of susan.martin@probablyfine.thm from 37.19.201.132 (Singapore)" justo cuando Susan se encuentra en Singapur en una conferencia; sin embargo, al contactarla confirma que NO entró en la VPN. En un hotspot público instaló una herramienta de "security check", un binario cuyo hash es b8e02f2bc0ffb42e8cf28e37a26d8d825f639079bf6d948f8debab6440ee5630. A través de la plataforma de inteligencia de amenazas TryDetectThis (cuya URL de acceso hay que abrir en el navegador) se investigan la IP, el dominio y el hash, lo que termina encadenando toda la campaña mediante un reporte de threat intelligence.

## Solucionario

### Task 1: Just a VPN Login / Solo un inicio de sesión de VPN

**Explicación:** La sala simula el triaje de una alerta SOC de principio a fin. Toda la investigación se realiza desde la plataforma TryDetectThis: primero se valida la IP de origen 37.19.201.132 mediante un lookup de ASN y se identifica el servicio que ofrece (VPN). Después se analiza el hash del binario, consultando el nombre de archivo, la firma de detección de Microsoft (Trojan:Win32/LummaStealer.PM!MTB), los dominios contactados, el clúster de infraestructura (151 dominios vinculados por su certificado HTTPS), la regla YARA de kevoreilly que coincide con el binario y el reporte de inteligencia que menciona el hash. Las últimas preguntas se responden leyendo ese reporte, que detalla la campaña y a sus afiliados.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the ASN number related to the IP? | `212238` |
| 2 | Which service is offered from this IP? | `VPN` |
| 3 | What is the filename of the file related to the hash? | `zY9sqWs.exe` |
| 4 | What is the threat signature that Microsoft assigned to the file? | `Trojan:Win32/LummaStealer.PM!MTB` |
| 5 | One of the contacted domains is part of a large malicious infrastructure cluster. Based on its HTTPS certificate, how many domains are linked to the same campaign? | `151` |
| 6 | The file matches one of the YARA rules made by 'kevoreilly'. What line is present in the rule's 'condition' field? | `uint16(0) == 0x5a4d and any of them` |
| 7 | The file is also mentioned in a threat intel report. What is the title of the report mentioning this hash? | `Behind the Curtain: How Lumma Affiliates Operate` |
| 8 | Which team did the author of the malware start collaborating with in early 2024? | `GhostSocks` |
| 9 | A Mexican-based affiliate related to the malware family also uses other infostealers. Which mentioned infostealer targets Android systems? | `CraxsRAT` |
| 10 | The report states that the affiliates behind the malware use the services of AnonRDP. Which Mitre ATT&CK sub-technique does this align with? | `T1583.003` |

---

**Metodología:** Se recibe la alerta de login VPN poco habitual → la usuaria confirma que no entró y que instaló un binario de "security check" en un hotspot público → se busca la IP 37.19.201.132 en TryDetectThis (ASN 212238, servicio VPN) → se analiza el hash b8e02f...5630: nombre de archivo (zY9sqWs.exe), firma de Microsoft (LummaStealer), dominios contactados y clúster de certificado HTTPS (151 dominios) → se valida la regla YARA de kevoreilly → se localiza el reporte de intelligence "Behind the Curtain: How Lumma Affiliates Operate" → se extraen la colaboración con GhostSocks, el infostealer Android CraxsRAT y el uso de AnonRDP (T1583.003) para cerrar el triaje.

### Cadena de ataque / Attack Chain

```text
susan.martin@probablyfine.thm conectada a un hotspot público
    -> Instala un "security check" (zY9sqWs.exe / LummaStealer)
    -> Distribución del binario y cadena de infraestructura maliciosa (VPN, ASN 212238)
    -> Exfiltración de credenciales y tokens de la víctima
    -> Uso indebido de las credenciales en un login VPN no autorizado (37.19.201.132, Singapur)
    -> Generación de la alerta SOC: "Unusual VPN login"
    -> Triaje con TryDetectThis: IP, dominio y hash
    -> Encadenamiento de la campaña (151 dominios, GhostSocks, CraxsRAT, AnonRDP)
```

**Learning chain:** Alerta interna de SOC → verificación con la usuaria (no fue ella) → lookup de IP, ASN y servicio → análisis del hash y firma de antivirus → dominios contactados y clúster por certificado HTTPS → match de regla YARA → lectura del reporte de threat intelligence → correlación de TTPs y afiliados para el triaje final.

**Lección:** *Un "login VPN inusual" puede ser la punta del iceberg: correlacionando IP, hash, infraestructura y threat intelligence se revela toda la campaña.*

**MITRE ATT&CK:** T1583.003 (Acquire Infrastructure: Virtual Private Server) por el uso de AnonRDP por parte de los afiliados del malware, junto a T1566 (Phishing) y T1185 (Browser Session Hijacking) como vectores vinculados a la estafa, todo con foco defensivo en el triaje SOC.

**Fuente:** [TryHackMe - Just a VPN Login](https://tryhackme.com/room/justavpnlogin)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.