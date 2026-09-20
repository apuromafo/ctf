# Outlook NTLM Leak

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `outlookntlmleak` | [TryHackMe](https://tryhackme.com/room/outlookntlmleak) | `01 Level Easy` | THM | Outlook, NTLM, filtración de hashes | Comprensión de la técnica NTLM leak |

> **Objeto:** Comprender la técnica de filtración de hashes NTLM a través de Outlook, en la que se aprovechan los recursos remotos invocados desde el cliente de correo para capturar el hash NTLM de la víctima.

---

**Contexto:** La sala explica la técnica de filtración de hashes NTLM mediante Outlook: se utilizan superficies de autenticación (recursos remotos / formato de archivo) que fuerzan una solicitud de autenticación hacia un servidor controlado por el atacante, exponiendo el hash NTLM del usuario víctima. Todos los pasos documentados no requieren respuesta.

> **ES:** La sala explica la técnica de filtración de hashes NTLM mediante Outlook: se utilizan superficies de autenticación (recursos remotos / formato de archivo) que fuerzan una solicitud de autenticación hacia un servidor controlado por el atacante, exponiendo el hash NTLM del usuario víctima. Todos los pasos documentados no requieren respuesta.

> **EN:** The room explains the NTLM hash leak technique through Outlook: authentication surfaces (remote resources / file format) are used to force an authentication request toward an attacker-controlled server, exposing the victim user's NTLM hash. All documented steps require no answer.

## Solucionario

### Task 1: Outlook NTLM Leak / Outlook NTLM Leak

**Explicación:** La tarea recorre la técnica del leak de hashes NTLM vía Outlook. El contenido original, conservado íntegramente, es el siguiente:

1. No answer needed
2. No answer needed
3. No answer needed
4. No answer needed
5. No answer needed
6. No answer needed

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | No answer needed (paso 1) | `No answer needed` |
| 2 | No answer needed (paso 2) | `No answer needed` |
| 3 | No answer needed (paso 3) | `No answer needed` |
| 4 | No answer needed (paso 4) | `No answer needed` |
| 5 | No answer needed (paso 5) | `No answer needed` |
| 6 | No answer needed (paso 6) | `No answer needed` |

---

**Metodología:** 1) Revisar y comprender la técnica de filtración de hashes NTLM mediante Outlook. 2) Ejecutar o reproducir los pasos demostrativos del walkthrough. 3) Ninguno de los pasos documentados requiere entregar respuesta (No answer needed).

### Cadena de ataque / Attack Chain

1. Preparación del servidor controlado por el atacante para capturar la autenticación.
2. Envío/entrega a la víctima del recurso que fuerza la solicitud de autenticación vía Outlook.
3. Captura del hash NTLM de la víctima.
4. Uso del hash capturado en ataques offline (cracking/passthrough).

**Learning chain:** autenticación NTLM → Outlook → filtración de hash → captura de credenciales → ataque offline

**Lección:** *Los hashes NTLM no son un secreto a prueba de balas: exponer superficies de autenticación invocables desde Outlook permite su captura y posterior reutilización en ataques offline.*

**MITRE ATT&CK:** T1187 - Forced Authentication, T1557.001 - Adversary-in-the-Middle: LLMNR/NBT-NS Poisoning and SMB Relay, T1110 - Brute Force

**Fuente:** [TryHackMe - Outlook NTLM Leak](https://tryhackme.com/room/outlookntlmleak)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.