SOC L1 Alert Reporting
 **Room Link:** https://tryhackme.com/room/socl1alertreporting


Aquí tienes el apunte en formato Markdown diseñado para organizar la información y las respuestas de la sala **SOC L1 Alert Reporting**.

---

# 🛡️ SOC L1: Alert Reporting, Escalation, and Communication

Este módulo se enfoca en la transición de las alertas de Nivel 1 (L1) a Nivel 2 (L2), cubriendo la documentación, la escalación técnica y los protocolos de comunicación en un SOC.

## 📊 Tarea 2: Alert Funnel

Conceptos clave sobre el flujo de trabajo tras el triaje inicial.

* **Alert Reporting:** Proceso de describir formalmente los detalles y hallazgos de una alerta. Es crucial para los *True Positives* que requieren ser escalados.
* **Alert Escalation:** Acción de pasar alertas sospechosas o complejas a un analista L2 para una revisión profunda o remediación.
* **Communication:** Interacción con otros departamentos (IT, RRHH, etc.) para validar actividades o solicitar información adicional.

> **Preguntas de la Tarea:**
> * **¿Proceso de pasar alertas a un analista L2?** `Alert Escalation`
> * **¿Proceso de describir formalmente los detalles?** `Alert Reporting`
> 
> 

---

## 📝 Tarea 3: Reporting Guide

Un buen reporte ahorra tiempo al analista L2 y sirve como registro histórico (los logs crudos expiran, pero las alertas suelen ser permanentes). Se recomienda el enfoque de las **5 Ws**:

1. **Who (Quién):** Usuario o cuenta involucrada.
2. **What (Qué):** Secuencia exacta de eventos o comandos.
3. **When (Cuándo):** Marca de tiempo exacta del inicio y fin.
4. **Where (Dónde):** Dispositivo, IP o URL afectada.
5. **Why (Por qué):** El razonamiento detrás del veredicto final.

> **Preguntas de la Tarea:**
> * **Email que filtró el documento sensible:** `m.boslan@tryhackme.thm`
> * **Remitente del correo de phishing:** `support@microsoft.com`
> * **Flag por escribir un buen reporte (5 Ws):** `THM{nice_attempt_faking_microsoft_support}`
> 
> 

---

## 🚀 Tarea 4: Escalation Guide

Se debe escalar si: la alerta indica un ataque mayor, requiere acciones de remediación (aislar host, resetear password), requiere comunicación externa o si el analista L1 no comprende totalmente la alerta.

* **Pasos en el Dashboard:**
1. Escribir el reporte y dar un veredicto.
2. Cambiar el estado a **In Progress**.
3. Asignar al **L2 de turno**.



> **Preguntas de la Tarea:**
> * **Nombre del analista L2 actual:** `E.Fleming`
> * **Flag tras escalar correctamente a L2:** `THM{good_job_escalating_your_first_alert}`
> * **Flag tras investigar la segunda alerta (Webshell):** `THM{looks_like_webshell_via_old_exchange}`
> 
> 

---

## 📞 Tarea 5: SOC Communication

Casos críticos y mejores prácticas de comunicación:

* **L2 no disponible:** Si una alerta crítica no es atendida en 30 min, llamar por teléfono a L2, luego L3 y finalmente al Manager.
* **Cuenta comprometida:** Si Slack/Teams está comprometido, **no** usar ese chat para contactar al usuario; usar métodos alternativos como llamadas.
* **Error de clasificación:** Si notas días después que clasificaste mal una alerta, informa inmediatamente a L2.

> **Preguntas de la Tarea:**
> * **¿Contactar primero al manager ante una amenaza crítica?** `Nay` (Primero se intenta con L2/L3).
> * **¿Contactar a L2 inmediatamente si crees que omitiste un ataque?** `Yea`
> 
> 

---

## 🏁 Tarea 6: Conclusion

Esta sección resume las competencias clave adquiridas para un analista L1:

* **Alert Reporting**: Esencial para preservar y proporcionar el contexto de la actividad al analista L2.
* **Escalation**: Garantiza que las amenazas sean remediadas a tiempo mediante la intervención de personal con mayor jerarquía o especialización.
* **Communication**: Facilita una coordinación clara y efectiva entre el SOC y otros departamentos de la organización.

> **Pregunta de la Tarea:**
> * **I am ready to move on!**
> * **Respuesta:** `No answer needed`
> 
> 
