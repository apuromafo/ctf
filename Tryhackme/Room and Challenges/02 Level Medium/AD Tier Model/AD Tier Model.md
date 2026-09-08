# AD Tier Model
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `adtiermodel` |
| **Link** | [TryHackMe](https://tryhackme.com/room/adtiermodel) |
| **Sección** | Active Directory / Hardening / Least Privilege |
| **Fuente** | Writeup de thmrevenant (GitHub) y sehgalrudra07 (Medium) |
| **Componentes** | Active Directory, modelo de tiers (Tier 0/1/2), menor privilegio, RDP, grupos de administradores por niveles |
| **Impacto** | Aprende a implementar los fundamentos del modelo de menor privilegio en un dominio Windows (Tier 0/1/2 de Microsoft) para limitar el impacto del movimiento lateral y la escalada de privilegios. |
---
**Contexto:** Aprende a implementar los fundamentos del modelo de menor privilegio en un dominio de Windows para establecer una línea base común que debería aplicarse a la mayoría de las redes. La room cubre el modelo de acceso por niveles (Tier 0/1/2) de Microsoft y su implementación práctica.
*EN: Learn how to implement the basics of the least privilege model in a Windows domain to establish a common baseline that should apply to most networks. The room covers Microsoft's tiered access model (Tier 0/1/2) and its practical implementation.*
## Solucionario
### Task 1 — Introduction
**Explicación:** Introducción al modelo de niveles y al reto de implementar menor privilegio en un dominio Windows.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Introducción a la sala (sin preguntas). | `No answer needed` |
### Task 2 — Tiered Access Models
**Explicación:** Microsoft propone separar los activos de AD en tres niveles: **Tier 0** (controladores de dominio y todo lo que controle el dominio), **Tier 1** (servidores de aplicaciones y bases de datos) y **Tier 2** (estaciones de trabajo y dispositivos de usuario final). Un admin de Tier 2 NO debe poder iniciar sesión en una máquina de Tier 0.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | A database server should go in which tier? | `Tier 1` |
| 2 | Should a tier 2 admin be able to log into a tier 0 machine? (yea/nay) | `nay` |
| 3 | Domain controllers should be contained in which tier? | `Tier 0` |
### Task 3 — Practical: Tier 0 (Flags 1-4)
**Explicación:** Parte práctica de Tier 0. Al separar las máquinas en niveles se crean credenciales administrativas con acceso solo a su nivel correspondiente. Se recogen las flags 1-4 de los escritorios y archivos correspondientes del entorno Tier 0.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the value of Flag 1? | `THM{1cbe1745bb323359f0505ec3d89a6a73}` |
| 2 | What is the value of Flag 2? | `THM{8f88da49cf77bffa2174e81d568e19a0}` |
| 3 | What is the value of Flag 3? | `THM{17449a8edcc47635a459416209e8a84b}` |
| 4 | What is the value of Flag 4? | `THM{ce6f77b2a7f0f1d32828be502e2442bd}` |
### Task 4 — Practical: Tier 2 (THMWRK2)
**Explicación:** RDP a THMWRK2 con el usuario `THM\t2_bob` (miembro del grupo de administradores de Tier 2), que tiene privilegios administrativos sobre la máquina. El usuario `THM\Administrator` NO puede RDP a THMWRK2 (está restringido por el modelo de niveles).
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which of the following users can be used to RDP into THMWRK2 at this point? | `THM\t2_bob` |
| 2 | When logging into THMWRK2 with the user from the previous question, do you have administrative privileges over the machine? (yea/nay) | `yea` |
| 3 | Is it possible to RDP into the THMWRK2 machine with the THM\Administrator user? (yea/nay) | `nay` |
### Task 5 — Practical: Flags 5-9
**Explicación:** Continuación de la parte práctica en Tier 2: se recogen las flags 5-9 según las indicaciones de la room.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the value of Flag 5? | `THM{48d9885bdfdf308982467f39459d8bcb}` |
| 2 | What is the value of Flag 6? | `THM{c42c75ccd141e36c8ee0610de31e8e12}` |
| 3 | What is the value of Flag 7? | `THM{cef897d4ca15a66441eb96f4fd315bb8}` |
| 4 | What is the value of Flag 8? | `THM{f92c14396e0a01ba220aaea6a32ca5fa}` |
| 5 | What is the value of Flag 9? | `THM{4eb7d17ba6e8b455231269a49fa50cf7}` |
---
**Metodología:** Modelo de acceso por niveles (Tier 0/1/2) → cuentas de administrador por niveles (cada admin solo accede a su nivel) → parte práctica: RDP a THMWRK2 con `THM\t2_bob` y recogida de flags 1-9.
**Learning chain:** menor privilegio → separación de activos en tiers → cuentas administrativas segmentadas → verificación práctica de los límites de acceso entre niveles.
**MITRE ATT&CK:** M1018 (Account Use Policies) / mitigación de movimiento lateral, T1078 (Valid Accounts), T1098 (Account Manipulation) como riesgo mitigado por el tiering.
**Fuente:** [TryHackMe - AD Tier Model](https://tryhackme.com/room/adtiermodel)