# VulnNet Active

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | Reto / Challenge (Active Directory) | vulnnetactive | https://tryhackme.com/room/vulnnetactive | 02 Level Medium | TryHackMe | Active Directory, SMB, Kerberos, PrivEsc | Alta - compromiso de dominio |

> **Objeto:** Comprometer el entorno de Active Directory de la red VulnNet y leer las flags de usuario y de dominio/administrador.

---

**Contexto:** "VulnNet Active" es un reto centrado en explotación de infraestructuras Active Directory. El usuario deberá abusar de servicios autenticados (SMB, Kerberos), moverse lateralmente y escalar privilegios hasta obtener el acceso de administrador de dominio.

> **ES:** Reto que practica el compromiso de un dominio Active Directory completo.
> **EN:** Challenge that practices compromising a full Active Directory domain.

## Solucionario

### Task 1: Flag de usuario / User flag

**Explicación:** Enumerar el dominio y abusar de los servicios autenticados para obtener credenciales y leer la flag de usuario.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es la flag de usuario? / What is the user flag? | THM{3eb176aee96432d5b100bc93580b291e} |

### Task 2: Flag de administrador / Administrator flag

**Explicación:** Escalar privilegios dentro del dominio mediante ataques a Active Directory para leer la flag de administrador.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es la flag de administrador? / What is the admin flag? | THM{d540c0645975900e5bb9167aa431fc9b} |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Cuál es la flag de usuario? / What is the user flag? | `THM{3eb176aee96432d5b100bc93580b291e}` |
| 1 | ¿Cuál es la flag de administrador? / What is the admin flag? | `THM{d540c0645975900e5bb9167aa431fc9b}` |

---

**Metodología:**

1. Enumeración de servicios del controlador de dominio.
2. Abuso de servicios autenticados (SMB/Kerberos).
3. Obtención de credenciales y acceso a la máquina.
4. Escalada de privilegios hasta administrador de dominio.
5. Captura de flags de usuario y administrador.

### Cadena de ataque / Attack Chain

```text
Enumeración AD -> Abuso de servicios -> Credenciales -> Acceso -> Privesc -> Domain Admin -> Flags
```

**Learning chain:**

- Los servicios autenticados de Windows exponen funcionalidad aprovechable.
- La escalada en entornos AD pasa por obtener tickets/credenciales válidas.
- El compromiso final se valida con la flag de administrador de dominio.

**Lección:** *Un dominio se compromete encadenando enumeración, abuso de credenciales y movimento lateral.*

**MITRE ATT&CK:**
- T1003 - OS Credential Dumping
- T1558 - Steal or Forge Kerberos Tickets
- T1482 - Domain Trust Discovery
- T1068 - Exploitation for Privilege Escalation

**Fuente:** [TryHackMe - VulnNet Active](https://tryhackme.com/room/vulnnetactive)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.