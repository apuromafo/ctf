# The Bandit Surfer

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Reto CTF | adv3nt0fdbopsjcap | https://tryhackme.com/room/adv3nt0fdbopsjcap | 03 Level Hard | TryHackMe | SQLi, SSRF, PIN, PATH hijacking | Alto |

---

**Contexto:**
> **ES:** Sala CTF heredera de las sagas "Bandit" y "Surfer/Yeti", que encadena inyección SQL, SSRF y explotación de un PIN, además de abuso de PATH para finalizar con un hijacking de ejecución. La tercera flag es una contraseña en claro.
> **EN:** CTF room in the line of the "Bandit" and "Surfer/Yeti" sagas, chaining SQL injection, SSRF and PIN exploitation, plus PATH abuse ending in execution hijacking. The third flag is a plaintext password.

## Solucionario

### Task 1: Banderas del reto / Challenge flags
**Explicación:**
Contenido original de la tarea:

```text
1. 1. THM{SQli_SsRF_2_WeRkZeuG_PiN_ExPloit}
   2. THM{BaNDiT_YeTi_Lik3s_PATH_HijacKing}
   3. 4-3f$FEBwD6AoqnyLjJ!!Hk4tc*V6w$UuK#evLWkBp
```

### Preguntas y Respuestas / Questions and Answers

| Task | Respuesta / Answer |
|---|---|
| 1.1 | `THM{SQli_SsRF_2_WeRkZeuG_PiN_ExPloit}` |
| 1.2 | `THM{BaNDiT_YeTi_Lik3s_PATH_HijacKing}` |
| 1.3 | `4-3f$FEBwD6AoqnyLjJ!!Hk4tc*V6w$UuK#evLWkBp` |

---

**Metodología:**
1. Obtención de la primera flag explotando inyección SQL y SSRF junto con la manipulación de un PIN: `THM{SQli_SsRF_2_WeRkZeuG_PiN_ExPloit}`.
2. Abuso de la variable PATH para secuestrar la ejecución y obtener la segunda flag: `THM{BaNDiT_YeTi_Lik3s_PATH_HijacKing}`.
3. Recuperación de la contraseña en claro que cierra el reto: `4-3f$FEBwD6AoqnyLjJ!!Hk4tc*V6w$UuK#evLWkBp`.

### Cadena de ataque / Attack Chain
```text
SQLi + SSRF + PIN -> Flag 1 -> PATH hijacking -> Flag 2 -> Credencial en claro -> Flag 3
```

**Learning chain:**
SQLi -> SSRF -> PIN -> Flag 1 -> PATH hijacking -> Flag 2 -> Contraseña en claro -> Flag 3.

**Lección:** *El PATH es un vector silencioso: cuando un binario se invoca sin ruta absoluta, quien controla el path controla la ejecución.*

**MITRE ATT&CK:**
- T1190 Exploit Public-Facing Application
- T1574 Hijack Execution Flow
- T1078 Valid Accounts

**Fuente:** [TryHackMe - The Bandit Surfer](https://tryhackme.com/room/adv3nt0fdbopsjcap)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.