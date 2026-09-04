# AD Tier Model [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Walkthrough (Premium)
* **Slug:** `adtiermodel`
* **Link:** https://tryhackme.com/room/adtiermodel
* **Sección / Section:** Active Directory / Hardening / Least Privilege
* **Fuente / Source:** Writeup de thmrevenant (GitHub) y sehgalrudra07 (Medium)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Aprende a implementar los fundamentos del modelo de menor privilegio en un dominio de Windows para establecer una línea base común que debería aplicarse a la mayoría de las redes. La room cubre el modelo de acceso por niveles (Tier 0/1/2) de Microsoft y su implementación práctica.
> **EN:** Learn how to implement the basics of the least privilege model in a Windows domain to establish a common baseline that should apply to most networks. The room covers Microsoft's tiered access model (Tier 0/1/2) and its practical implementation.

---

### Task 1 — Introduction

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| *(No hay preguntas / No questions)* | — |

---

### Task 2 — Tiered Access Models

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| A database server should go in which tier? | `Tier 1` |
| Should a tier 2 admin be able to log into a tier 0 machine? (yea/nay) | `nay` |
| Domain controllers should be contained in which tier? | `Tier 0` |

---

### Task 3 — Practical: Tier 0 (Flags 1-4)

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the value of Flag 1? | `THM{1cbe1745bb323359f0505ec3d89a6a73}` |
| What is the value of Flag 2? | `THM{8f88da49cf77bffa2174e81d568e19a0}` |
| What is the value of Flag 3? | `THM{17449a8edcc47635a459416209e8a84b}` |
| What is the value of Flag 4? | `THM{ce6f77b2a7f0f1d32828be502e2442bd}` |

---

### Task 4 — Practical: Tier 2 (THMWRK2)

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Which of the following users can be used to RDP into THMWRK2 at this point? | `THM\t2_bob` |
| When logging into THMWRK2 with the user from the previous question, do you have administrative privileges over the machine? (yea/nay) | `yea` |
| Is it possible to RDP into the THMWRK2 machine with the THM\Administrator user? (yea/nay) | `nay` |

---

### Task 5 — Practical: Flags 5-9

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the value of Flag 5? | `THM{48d9885bdfdf308982467f39459d8bcb}` |
| What is the value of Flag 6? | `THM{c42c75ccd141e36c8ee0610de31e8e12}` |
| What is the value of Flag 7? | `THM{cef897d4ca15a66441eb96f4fd315bb8}` |
| What is the value of Flag 8? | `THM{f92c14396e0a01ba220aaea6a32ca5fa}` |
| What is the value of Flag 9? | `THM{4eb7d17ba6e8b455231269a49fa50cf7}` |

---

## Metodología / Methodology

1. **Modelo de acceso por niveles / Tiered access model:** Microsoft propone separar los activos de AD en tres niveles para limitar el impacto del movimiento lateral y la escalada de privilegios:
   - **Tier 0:** Controladores de dominio (Domain Controllers), administradores de dominio, y todo lo que controle el dominio (identidad, autenticación).
   - **Tier 1:** Servidores de aplicaciones y de base de datos (database servers), y las cuentas que los administran.
   - **Tier 2:** Estaciones de trabajo de usuarios regulares y otros dispositivos de usuario final.
2. **Cuentas de administrador por niveles / Tiered administrator accounts:** al separar las máquinas en niveles, se crean credenciales administrativas con acceso solo a su nivel correspondiente. Un admin de Tier 2 NO debe poder iniciar sesión en una máquina de Tier 0.
3. **Parte práctica / Practical part:** RDP a THMWRK2 con el usuario `THM\t2_bob` (miembro del grupo de administradores de Tier 2), que tiene privilegios administrativos sobre la máquina. El usuario `THM\Administrator` NO puede RDP a THMWRK2 (está restringido por el modelo de niveles). Recoger las flags 1-9 de los escritorios y archivos correspondientes.

**Lección:** el modelo de niveles (tiering) de AD es una implementación práctica del principio de menor privilegio. Limita el impacto de un compromiso: si un atacante compromete una cuenta de Tier 2, no puede moverse lateralmente a los controladores de dominio (Tier 0).

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
