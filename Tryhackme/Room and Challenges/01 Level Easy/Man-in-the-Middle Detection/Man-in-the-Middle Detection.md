# Man-in-the-Middle Detection

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `maninthemiddledetection` | [TryHackMe](https://tryhackme.com/room/maninthemiddledetection) | 01 Level Easy | THM | Wireshark, ARP spoofing, MAC, análisis de red | Detección de ataques Man-in-the-Middle mediante análisis de tráfico de red |

> **Objeto:** Detectar y analizar ataques Man-in-the-Middle (ARP spoofing) mediante la inspección del tráfico de red de un laboratorio.

---

**Contexto:** Sala práctica de detección de ataques Man-in-the-Middle: se examina el tráfico de red para identificar suplantación ARP, direcciones MAC sospechosas, hosts conectados y credenciales transmitidas en claro por un atacante.

> **ES:** Sala práctica sobre detección de MITM: análisis de tráfico ARP, MAC duplicadas y credenciales en claro.
> **EN:** Hands-on room about MITM detection: ARP traffic analysis, duplicated MAC addresses and cleartext credentials.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación de la sala y de los conceptos de detección de ataques Man-in-the-Middle.

No answer needed

### Task 2: Análisis de tráfico ARP / ARP traffic analysis
**Explicación:** Se inspecciona el tráfico ARP del laboratorio para localizar la suplantación de direcciones y extraer los datos solicitados.

1. 10
2. 02:fe:fe:fe:55:55
3. 2
4. 2
5. 14

### Task 3: Enumeración de la red / Network enumeration
**Explicación:** Se enumeran los hosts y puertos de la red para comprender la topología afectada por el ataque.

1. 211
2. 2
3. 192.168.10.55

### Task 4: Detección MITM / MITM detection
**Explicación:** Se confirma la intercepción del tráfico y se recupera la credencial capturada durante el ataque.

1. 1
2. Secret123!

### Task 5: Verificación / Verification
**Explicación:** Paso intermedio de comprobación en el laboratorio.

No answer needed

### Task 6: Captura de credenciales / Credential capture
**Explicación:** Se repite el análisis para verificar la credencial enviada en claro por la víctima.

1. 1
2. Secret123!

### Task 7: Conclusión / Conclusion
**Explicación:** Cierre de la sala y repaso de los indicadores de compromiso detectados.

No answer needed

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | — | `No answer needed` |
| 2.1 | Resultado 1 del análisis ARP | `10` |
| 2.2 | MAC detectada / Resultado 2 | `02:fe:fe:fe:55:55` |
| 2.3 | Resultado 3 | `2` |
| 2.4 | Resultado 4 | `2` |
| 2.5 | Resultado 5 | `14` |
| 3.1 | Resultado 1 de la enumeración | `211` |
| 3.2 | Resultado 2 | `2` |
| 3.3 | Host identificado | `192.168.10.55` |
| 4.1 | Resultado 1 | `1` |
| 4.2 | Credencial capturada | `Secret123!` |
| 5 | — | `No answer needed` |
| 6.1 | Resultado 1 | `1` |
| 6.2 | Credencial capturada | `Secret123!` |
| 7 | — | `No answer needed` |

---

**Metodología:** Captura y análisis del tráfico de red con Wireshark, inspección de las tramas ARP para detectar suplantación, enumeración de hosts y puertos de la red, y extracción de credenciales que viajan en claro como prueba de la intercepción MITM.

### Cadena de ataque / Attack Chain

Tráfico de red → captura ARP → detección de MAC duplicadas/suplantadas → enumeración de hosts → captura de credenciales en claro.

**Learning chain:** MITM → ARP spoofing → detección → análisis de tráfico → credenciales

*Lección:* Un ataque Man-in-the-Middle por ARP spoofing se detecta revisando tramas ARP, MAC duplicadas y credenciales no cifradas en la red.

**MITRE ATT&CK:** T1557 - Adversary-in-the-Middle, T1557.002 - ARP Cache Poisoning.

**Fuente:** [TryHackMe - Man-in-the-Middle Detection](https://tryhackme.com/room/maninthemiddledetection)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.