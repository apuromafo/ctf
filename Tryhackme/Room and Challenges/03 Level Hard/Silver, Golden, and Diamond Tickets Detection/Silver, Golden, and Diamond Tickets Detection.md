# Silver, Golden, and Diamond Tickets Detection

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | walkthrough | `krbticketattacks` | [TryHackMe](https://tryhackme.com/room/krbticketattacks) | 03 Level Hard | TryHackMe | krbtgt, PAC, Silver/Golden/Diamond tickets, Kerberoasting, DCSync, Rubeus, Mimikatz, Event IDs 4768/4769/4662/4672/4624/4728/4732/4756, klist, Amcache, PSReadLine, Sysmon | Detección de tickets Kerberos forjados (Silver, Golden y Diamond) correlacionando Security logs y eventos Kerberos del DC y del host objetivo |

---

**Contexto:** La sala investiga tres ataques construidos sobre una misma debilidad de Kerberos: el servicio confía en cualquier ticket que se descifre con una clave que ya posee, sin volver a preguntar al KDC. En el dominio ficticio `lunarbank.thm` (LunarBank) se comparan los tres tickets desde la perspectiva del adversario y del analista: el Silver ticket (TGS forjado con el hash de la cuenta de servicio, T1558.002), el Golden ticket (TGT forjado con el hash de krbtgt, T1558.001) y el Diamond ticket (TGT real cuyo PAC se reescribe con la clave AES de krbtgt). La detección se apoya en el host objetivo (4624 Logon Type 3 y 4672), en el Domain Controller (4769 sin 4768 previo, 4662 por DCSync, 4728/4732/4756 de membresía) y en artefactos DFIR de la workstation LB-WS09 (klist, Amcache.hve, historial PSReadLine). Las máquinas de laboratorio ofrecen credenciales `DFIRUser`/`Secure!` y `Administrator`/`Secure!` (MACHINE_IP), y en la Task 6 se entra por RDP al DC vivo con `LUNARBANK\Administrator`/`Secure!`.

## Solucionario

### Task 1: Introduction / Introducción

**Explicación:** Presenta la familia de ataques de tickets Kerberos (Silver, Golden y Diamond), su marco MITRE ATT&CK T1558 (Steal or Forge Kerberos Tickets) y los objetivos: explicar qué clave hay que robar para forjarlos y cómo detectarlos correlacionando los logs de Windows Security y Kerberos del host y del Domain Controller. Tarea informativa.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Read the above and click Check. | `No answer needed` |

### Task 2: Silver, Golden and Diamond Tickets from an Adversary Perspective / Silver, Golden y Diamond desde la Perspectiva del Adversario

**Explicación:** Explica qué necesita robar el atacante para forjar cada ticket y qué alcanza con ello: el hash de la cuenta de servicio (Silver, por Kerberoasting, T1558.002), el hash de krbtgt (Golden, por DCSync, T1558.001) o la clave AES de krbtgt más credenciales válidas (Diamond). Cada técnica elimina la evidencia que expone a la anterior: Silver nunca contacta al DC, Golden presenta un TGT forjado y Diamond pide un TGT real y lo reescribe.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Which account's password hash must an attacker steal to forge a Golden ticket? | `krbtgt` |
| 2 | Which tool did the operators of the 2025 Poland Wiper Attacks use to forge a Diamond ticket? | `Rubeus` |

### Task 3: Silver Ticket Detection / Detección del Silver Ticket

**Explicación:** Un Silver ticket se presenta directamente al servicio sin pasar por el Domain Controller, así que la investigación arranca en el host objetivo con el 4624 Logon Type 3 (y 4672 si reclamó membresía administrativa) y la confirmación llega por la ausencia del 4769 en el DC. El downgrade a RC4 (0x17) y un Logon GUID a cero son corroboración, y el robo de la clave queda en Amcache.hve, PSReadLine history y Prefetch de la workstation LB-WS09.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Which event ID would the Domain Controller have logged had it issued this service ticket? | `4769` |
| 2 | Which ticket encryption type value indicates an RC4 downgrade? | `0x17` |

### Task 4: Golden Ticket Detection / Detección del Golden Ticket

**Explicación:** Un Golden ticket sí tiene que hablar con el Domain Controller para obtener service tickets, pero rompe el par 4768/4769: hay 4769s sin un 4768 previo que los autentique. El 4662 con los GUID de replicación delata el DCSync que robó el hash de krbtgt, y el ticket recuperado con klist muestra anomalías (vida de diez años, RC4 en un dominio AES). (respuesta sin confirmar: requiere resolver el laboratorio)

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Which event ID on the Domain Controller reveals the DCSync that stole the KRBTGT hash? | `4662` |
| 2 | Which account did the forged ticket impersonate? | `a.khan` |
| 3 | What is the full mimikatz command the attacker used to forge the Golden ticket, as seen in the recovered PowerShell console history? | `-` |
| 4 | What is the End Time of the forged ticket? | `3/15/2036 09:12:04` |

### Task 5: Diamond Ticket Detection / Detección del Diamond Ticket

**Explicación:** Un Diamond ticket empieza siendo un TGT genuino emitido por el DC (por eso existe el 4768, la vida es normal y el cifrado es AES) y el atacante reescribe el PAC para añadir membresía privilegiada. La detección sale de la contradicción: el host registra 4672 otorgando privilegios especiales, pero no existe ningún 4728/4732/4756 que justifique la membresía y el export del directorio no lista a la cuenta como miembro del grupo.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Which event ID records special privileges being assigned to a new logon? | `4672` |
| 2 | Which part of a genuine TGT does a Diamond ticket modify? | `PAC` |

### Task 6: Hands-On Investigation / Investigación Práctica

**Explicación:** Tarea práctica sobre el Domain Controller vivo y aislado (LB-DC01): con las pistas del SOC de LunarBank (actividad administrativa de una cuenta sin privilegios y acceso a un recurso compartido restringido) hay que determinar cuál de los tres ataques ocurrió y probarlo. Se examinan los logs del DC, la evidencia de LB-WS09 en `C:\IR-Evidence\` y el estado del directorio. (respuesta sin confirmar: requiere resolver el laboratorio)

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Which restricted share did the attacker reach using the forged ticket? | `-` |
| 2 | What encryption type does the forged TGT use? (Answer Format: the encryption type name exactly as printed by klist) | `-` |
| 3 | Which account is the only genuine member of the Domain Admins group? | `-` |
| 4 | What is the password for j.reeves, as seen in the PowerShell console history recovered from LB-WS09? | `-` |
| 5 | Which of the three ticket attacks does the evidence identify? | `-` |

### Task 7: Containment, Prevention and Mitigation / Contención, Prevención y Mitigación

**Explicación:** Contención: un Silver ticket se invalida rotando la contraseña de la cuenta de servicio (svc_sql) y reiniciando el servicio; Golden y Diamond exigen el doble reset de krbtgt (New-KrbtgtKeys.ps1) porque AD mantiene la clave anterior y la actual. Prevención: gMSA contra Kerberoasting, restringir los derechos de replicación a los DCs, forzar AES, administración por niveles/PAWs, LAPS y un honey SPN.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Now I know how to defend against ticket attacks! | `No answer needed` |

### Task 8: Conclusion / Conclusión

**Explicación:** Cierre que resume la cadena de evidencia por ticket: Silver se detecta por el acceso sin 4769 en el DC, Golden por el 4769 sin 4768 previo y Diamond por privilegios que nunca fueron otorgados realmente. La lección final es tratar el directorio como ground truth y no confiar en el token que hay delante. Tarea informativa.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Ready for the next Windows Incident Response room. | `No answer needed` |

---

**Metodología:** La sala enlaza tres detecciones Kerberos: (1) Silver — buscar 4624 con Logon Type 3 y 4672 en el host objetivo y probar la ausencia de 4769 en el DC; (2) Golden — agrupar los 4769 por cuenta, verificar que no existe el 4768 previo, pivotar a 4662 (DCSync) y revisar la anomalía del ticket (lifetime y cifrado RC4 vs AES); (3) Diamond — confirmar que el 4768 es genuino y que la membresía privilegiada sin 4728/4732/4756 contradice el export del directorio. La contención rota la clave firmante y la prevención se apoya en gMSA, control de replicación y cifrado AES únicamente.

### Cadena de ataque / Attack Chain

```text
Kerberos confía en el ticket que se descifra con una clave que ya posee
  │
  ├─ Silver Ticket (T1558.002) — un servicio, un host
  │     Kerberoasting: 4769 por svc_sql → hash RC4 crackeado en LB-WS09
  │     Forja local: Rubeus silver / Mimikatz kerberos::golden (target LB-SQL01)
  │     Presentación directa al servicio (sin DC): 4624 Type 3 + 4672 en el host
  │     Detección: 4769 AUSENTE en el DC; 0x17 (RC4); Amcache/PSReadLine en LB-WS09
  │
  ├─ Golden Ticket (T1558.001) — todo el dominio
  │     DCSync (4662 con GUID de replicación) → hash krbtgt → forja (Rubeus/Mimikatz/ticketer)
  │     Presentación al DC: 4769s sin 4768 previo
  │     klist: vida de 10 años (3/15/2036), RC4 en dominio AES, cuenta inexistente o RID inconsistente
  │
  └─ Diamond Ticket — todo el dominio, sin anomalías en el ticket
        Autenticación real (j.reeves) → TGT genuino (4768) → PAC reescrito (añade RID 512)
        Rubeus diamond /ticketuser:Administrator /groups:512 (/krbkey AES)
        4768 existe, AES, vida normal → detección por 4672 sin 4728/4732/4756 y sin membresía en AD
```

**Learning chain:** Kerberos y estructura de tickets → qué clave se roba para forjar cada ticket → Silver/Golden/Diamond desde el adversario → correlación host/DC (4624, 4672, 4768, 4769, 4662) → artefactos DFIR (klist, Amcache, PSReadLine, export de AD) → contención (rotación + doble reset de krbtgt) → prevención (gMSA, replicación restringida, AES, honey SPN).

**Lección:** *Los tickets forjados no se detectan tanto por lo que contienen como por lo que falta o contradicen: el 4769 sin 4768, la ausencia de 4769 en el DC, o una membresía privilegiada que ningún 4728/4732/4756 ni el directorio confirman.*

**MITRE ATT&CK:** T1558 (Steal or Forge Kerberos Tickets), T1558.001 (Golden Ticket), T1558.002 (Silver Ticket), T1558.003 (Kerberoasting), T1003.006 (OS Credential Dumping: DCSync).

**Fuente:** [TryHackMe - Silver, Golden, and Diamond Tickets Detection](https://tryhackme.com/room/krbticketattacks)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.