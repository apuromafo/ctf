# OWASP Mutillidae II

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `owaspmutillidaeii` | https://tryhackme.com/room/owaspmutillidaeii | 01 Level Easy | TryHackMe | Mutillidae II, web application security, OWASP Top 10, bWAPP (penetration testing practice) | Entrenamiento guiado en una aplicación web deliberadamente vulnerable (penetration testing practice) |

---

**Contexto:** Este room es una guía práctica de la aplicación web deliberadamente vulnerable **Mutillidae II**, utilizada para entrenar técnicas de web application security. El objetivo es completar las tareas dentro del laboratorio, donde se validan automáticamente las respuestas obtenidas.

> **ES:** Despliega la máquina, accede a la aplicación Mutillidae II sobre LAMP y recorre las tareas del laboratorio para completar el tour guiado de práctica de pentesting web.
> **EN:** Deploy the machine, access the deliberately vulnerable Mutillidae II application and complete the guided hands-on training for web application pentesting.

## Solucionario

### Task 1: Tour guiado / Guided Tour

**Explicación:** EL room no requiere respuestas en texto: toda la *verificación* se realiza de forma interactiva dentro de la propia aplicación Mutillidae, que entrega valores de validación/task por tarea completada. Las preguntas de la sección se responden directamente en la página web del laboratorio.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Complete cada tarea de laboratorio dentro de Mutillidae / Complete each in-app task in Mutillidae | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Complete cada tarea de laboratorio dentro de Mutillidae / Complete each in-app task in Mutillidae | `No answer needed` |

---

**Metodología:** Aprendizaje guiado basado en laboratorio: se despliega la máquina acoplada al room, se accede a la aplicación web vulnerable (PHP/MySQL sobre LAMP) y se resuelven las tareas de seguridad web directamente en el entorno interactivo de Mutillidae II, cuya validación es interna a la aplicación.

### Cadena de ataque / Attack Chain

```text
Deploy VM -> acceder a Mutillidae II (LAMP) -> resolver tareas del laboratorio -> validación in-app -> room completado
```

**Learning chain:** web application security → OWASP Top 10 → Mutillidae II hands-on labs → in-app validation → guided pentest practice

**Lección:** *Las plataformas de entrenamiento guiado como Mutillidae II permiten practicar vulnerabilidades web en un entorno controlado donde la validación interna sustituye al Q&A, tan solo se debe desplegar la máquina y seguir el tour del laboratorio.*

**MITRE ATT&CK:** N/A (training environment)

**Fuente:** [TryHackMe - OWASP Mutillidae II](https://tryhackme.com/room/owaspmutillidaeii)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.