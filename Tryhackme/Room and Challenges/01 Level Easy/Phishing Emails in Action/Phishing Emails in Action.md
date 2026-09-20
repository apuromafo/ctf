# Phishing Emails in Action

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `phishingemailsinaction` | [TryHackMe](https://tryhackme.com/room/phishingemailsinaction) | 01 Level Easy | THM | Análisis de phishing, Remitente y dominio, BCC, Ingeniería social, Urgencia, Adjuntos maliciosos | Análisis de emails de phishing reales |

---

**Contexto:** Aplica en la práctica el análisis de emails de phishing reales: identificar el remitente y el dominio usado por el atacante, detectar a la empresa suplantada, reconocer técnicas de ingeniería social (BCC y urgencia), recomendar la acción correcta ante el email y analizar el adjunto malicioso.

> **ES:** Analiza emails de phishing reales paso a paso: remitente, dominio del atacante, empresa suplantada, técnicas de ingeniería social y adjunto malicioso.
> **EN:** Analyze real phishing emails step by step: sender, attacker domain, impersonated company, social engineering techniques and the malicious attachment.

## Solucionario

### Task 1: Email Attack in Action / Email Attack in Action

**Explicación:** Presenta el escenario del laboratorio: una organización recibe emails de phishing que deben analizarse para entender la campaña del atacante.

1. No answer needed

### Task 2: El email de phishing / The Phishing Email

**Explicación:** Permite inspeccionar el primer email recibido y observar que el nombre de remitente visible es noreply.

2. noreply

### Task 3: Dominio del atacante / Attacker Domain

**Explicación:** Del análisis del email se extrae el dominio empleado por el atacante, presentado en formato ofuscado (defanged) como devret[.]xyz.

3. devret[.]xyz

### Task 4: Empresa suplantada / Impersonated Company

**Explicación:** Identifica la empresa que el atacante está suplantando. En este caso, el email suplanta a Citrix mediante un sistema de citas falso.

4. Citrix

### Task 5: Acción recomendada / Recommended Action

**Explicación:** Define la respuesta que debe dar un usuario al encontrar este email: reenviarlo a phishing@netflix.com para que el equipo de seguridad lo gestione.

5. forward the message to phishing@netflix.com

### Task 6: Señales de alarma / Red Flags

**Explicación:** Enumera las técnicas de ingeniería social presentes en el email: el uso de Blind Carbon Copy (CCO) para ocultar a los destinatarios reales y la Urgency (urgencia) para provocar una respuesta rápida sin pensar.

6. 1. Blind Carbon Copy
   2. Urgency

### Task 7: Adjunto malicioso / Malicious Attachment

**Explicación:** Analiza el adjunto del email, que entrega un ejecutable malicioso en el sistema: el archivo regasms.exe.

7. regasms.exe

### Task 8: Cierre / Conclusion

**Explicación:** Reúne las conclusiones del análisis y refuerza los pasos a seguir al detectar un email de phishing.

8. No answer needed

| Pregunta | Respuesta |
|---|---|
| T1: Escenario inicial | `No answer needed` |
| ¿Con qué nombre de remitente se envía el email de phishing? | `noreply` |
| ¿Qué dominio usa el atacante para el email? | `devret[.]xyz` |
| ¿Qué empresa es suplantada en el email? | `Citrix` |
| ¿Qué debe hacer el usuario al recibir este email? | `forward the message to phishing@netflix.com` |
| ¿Qué técnica enmascara a los destinatarios reales del email? | `Blind Carbon Copy` |
| ¿Qué técnica de ingeniería social impulsa a responder con rapidez? | `Urgency` |
| ¿Cuál es el nombre del archivo malicioso entregado por el adjunto? | `regasms.exe` |
| T8: Tarea de cierre sin respuesta | `No answer needed` |

---

**Metodología:** Inspección manual de emails de phishing reales: análisis de remitente y dominio (ofuscación defanging), verificación de cabeceras y destinatarios (BCC), identificación de técnicas de ingeniería social y del adjunto malicioso, y aplicación de la política de respuesta (reenvío al equipo de seguridad).

### Cadena de ataque / Attack Chain
Entrega del email de phishing al usuario -> Suplantación de identidad (Citrix) con remitente genérico (noreply) y dominio del atacante (devret[.]xyz) -> Uso de BCC y urgencia para evitar el escrutinio y forzar la acción -> Entrega del adjunto malicioso (regasms.exe) -> Compromiso del sistema si el usuario interactúa.

**Learning chain:** Lectura de emails de phishing, ofuscación de dominios, técnicas de ingeniería social (BCC, urgencia), política de reporting y análisis de adjuntos ejecutables.

**Lección:** *La urgencia y el ocultamiento de destinatarios (BCC) son señales de alarma típicas del phishing, y un usuario formado reenvía el email al equipo de seguridad en lugar de responder.*

**MITRE ATT&CK:** T1566 Phishing, T1566.002 Spearphishing Link, T1204.002 User Execution (Malicious File).

**Fuente:** [TryHackMe - Phishing Emails in Action](https://tryhackme.com/room/phishingemailsinaction)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.