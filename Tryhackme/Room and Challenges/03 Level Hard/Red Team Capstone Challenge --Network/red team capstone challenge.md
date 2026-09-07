# Red Team Capstone Challenge --Network

| **Dificultad** | Hard |
| **Tipo** | CTF derivado del contenido |
| **Slug** | `redteamcapstonechallenge` |
| **Link** | [TryHackMe](https://tryhackme.com/room/redteamcapstonechallenge) |
| **Sección** | 03 Level Hard |
| **Fuente** | TryHackMe (Red Team Capstone) |
| **Componentes** | nmap / BloodHound / Kerberos / mimikatz / SMB / RDP / WinRM / chisel / SWIFT application |
| **Impacto** | Reto final del path de Red Team: asalto completo a una red corporativa con dos divisiones (Corporate y Bank), del Tier 2 al Tier 0, dominio padre, y un sistema SWIFT con flujo de aprobación que se explota hasta realizar una transferencia fraudulenta simulada. |

---

**Contexto:** El Red Team Capstone Network es el examen final que integra todas las técnicas del path: breaching del perímetro, breaching de Active Directory y, después, el recorrido completo de la red corporativa representada por dos divisiones (Corporate y Bank) con tres niveles de privilegio (Tier 2, Tier 1 y Tier 0), más el dominio padre. En cada nivel se exige primero un foothold y después la administración de esa infraestructura, subiendo por las supracadenas de confianza. El colofón es acceder a la aplicación SWIFT, conseguir una cuenta con permiso de capturista (capturer) y otra como aprobador (approver), y completar la transferencia fraudulenta simulada. La puntuación se obtiene enviando los 20 flags al servidor del reto.

## Solucionario

### Task 1: Breaching the Perimeter

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Submit the flag obtained after breaching the perimeter. | `THM{18800db2-ef64-4544-9bb7-56ba2dfa31ea}` |

### Task 2: Breaching Active Directory

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Submit the flag obtained after breaching Active Directory. | `THM{febcc4c0-b939-11ed-afa1-0242ac120002}` |

### Task 3: Corporate Division Tier 2 Infrastructure

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Submit the flag for the foothold on Corporate Division Tier 2 Infrastructure. | `THM{0ad79d03-5078-4970-ab91-ab24de6892a4}` |
| 2 | Submit the flag for administrative access to Corporate Division Tier 2 Infrastructure. | `THM{2540046c-b93b-11ed-afa1-0242ac120002}` |

### Task 4: Corporate Division Tier 1 Infrastructure

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Submit the flag for the foothold on Corporate Division Tier 1 Infrastructure. | `THM{30924538-a5c8-4499-993e-45f646f0b814}` |
| 2 | Submit the flag for administrative access to Corporate Division Tier 1 Infrastructure. | `THM{13b800c8-b2eb-49e2-bb43-4ea1b8c4a53a}` |

### Task 5: Corporate Division Tier 0 Infrastructure

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Submit the flag for the foothold on Corporate Division Tier 0 Infrastructure. | `THM{703d2509-a6e8-4bc8-bc53-788543e6f405}` |
| 2 | Submit the flag for administrative access to Corporate Division Tier 0 Infrastructure. | `THM{bd4f60cd-57a9-4cd5-88b9-0957e08c0df3}` |

### Task 6: Bank Division Tier 2 Infrastructure

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Submit the flag for the foothold on Bank Division Tier 2 Infrastructure. | `THM{a00af774-cf0d-483c-a1e1-bb082df4ab18}` |
| 2 | Submit the flag for administrative access to Bank Division Tier 2 Infrastructure. | `THM{1111d961-5086-40e9-804e-f512b55066bc}` |

### Task 7: Bank Division Tier 1 Infrastructure

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Submit the flag for the foothold on Bank Division Tier 1 Infrastructure. | `THM{9505045e-de3c-4d82-a621-8474f8256033}` |
| 2 | Submit the flag for administrative access to Bank Division Tier 1 Infrastructure. | `THM{347b0f8d-e819-44e7-bbf5-5a49fc601bca}` |

### Task 8: Bank Division Tier 0 Infrastructure

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Submit the flag for the foothold on Bank Division Tier 0 Infrastructure. | `THM{2d2b9799-b378-403a-9600-fab5b1ba7b05}` |
| 2 | Submit the flag for administrative access to Bank Division Tier 0 Infrastructure. | `THM{fbf52b9c-b61d-4a3c-85ab-31e466532ef7}` |

### Task 9: Parent Domain

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Submit the flag for the foothold on the Parent Domain. | `THM{ee8d8803-0551-4867-b665-e4cbf70d2652}` |
| 2 | Submit the flag for administrative access to the Parent Domain. | `THM{354ef832-add1-42f5-aba7-677062939ada}` |

### Task 10: SWIFT Application

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Submit the flag obtained after accessing the SWIFT application. | `THM{6bc2f0f0-1eda-47bd-9eb2-8abff4a5d4d1}` |
| 2 | Submit the flag obtained after accessing the SWIFT application with a capturer account. | `THM{204768b4-0d1d-4e0d-82b5-6015ec81f548}` |
| 3 | Submit the flag obtained after accessing the SWIFT application with an approver account. | `THM{e53f46e8-389b-4edb-bb44-34f87993969e}` |

### Task 11: Simulated Fraudulent Transfer

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Submit the flag obtained after making the simulated fraudulent transfer. | `THM{fd1ad4d0-b01d-455d-a17c-5a4b046e5361}` |

---

**Metodología:**
1. Romper el perímetro para obtener acceso inicial y el primer flag de breaching (reconocimiento, servicios expuestos y explotación de la superficie externa).
2. Breaching de Active Directory: obtener las primeras credenciales de dominio y moverte dentro del entorno para controlar la corporación.
3. División Corporate (Tier 2, Tier 1, Tier 0): consolidar foothold y después acceso administrativo en cada nivel, escalando a través de los privilegios y la infraestructura.
4. División Bank (Tier 2, Tier 1, Tier 0): repetir la progresión foothold + admin dentro de la división bancaria.
5. Parent Domain: saltar de las divisiones al dominio padre, obtener foothold y elevarse a administrador del bosque.
6. SWIFT application: acceder a la aplicación, operar una cuenta capturista (capturer) y una aprobadora (approver), y acoplar el flujo con doble aprobación para materializar la transferencia fraudulenta simulada y cerrar el reto.
7. Enviar cada uno de los 20 flags al servidor de puntuación del reto para validarlos.

**Learning chain:** `breaching perímetro → AD → Corporate Tier 2→1→0 → Bank Tier 2→1→0 → Parent Domain → SWIFT (capturer/approver) → transferencia fraudulenta`

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1078 (Valid Accounts), T1210 (Exploitation of Remote Services), T1003 (OS Credential Dumping), T1021 (Remote Services), T1550 (Use Alternate Authentication Material)

**Fuente:** [TryHackMe - Red Team Capstone Challenge --Network](https://tryhackme.com/room/redteamcapstonechallenge)