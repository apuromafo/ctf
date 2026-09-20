# Brute It

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `bruteit` | [TryHackMe](https://tryhackme.com/room/bruteit) | 01 Level Easy | TryHackMe | nmap, ffuf, hydra, fuerza bruta SSH, cracking de clave RSA | Compromiso total del host mediante fuerza bruta web/SSH y escalada a root |

---

**Contexto:** Sala de práctica en la que se compromete un host Linux a través de fuerza bruta sobre un panel de administración web y sobre SSH, seguida de una escalada de privilegios que conduce a root. El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

## Solucionario

### Task 1: Reconocimiento / Reconnaissance

**Explicación:** Pregunta de arranque de la sala, sin respuesta que introducir.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |

### Task 2: Enumeración / Enumeration

**Explicación:** Se escanea el host con nmap para identificar los puertos abiertos, las versiones de los servicios (SSH y Apache) y el sistema operativo, y se descubre con fuzzing el directorio oculto `/admin`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `2`<br>`OpenSSH 7.6p1`<br>`2.4.29`<br>`Ubuntu`<br>`/admin` |

### Task 3: Fuerza bruta web y SSH / Web & SSH Brute Force

**Explicación:** Se fuerza la autenticación del panel web con hydra, se obtienen credenciales válidas y se captura la flag de usuario; el acceso por SSH y el uso de credenciales débiles permiten avanzar por el sistema.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `admin:xavier` |
| 2 | *(Pregunta 2 no especificada en el original)* | `rockinroll` |
| 3 | *(Pregunta 3 no especificada en el original)* | `THM{a_password_is_not_a_barrier}` |
| 4 | *(Pregunta 4 no especificada en el original)* | `THM{brut3_f0rce_is_e4sy}` |

### Task 4: Escalada de privilegios / Privilege Escalation

**Explicación:** Se localiza una clave privada protegida con contraseña, se extrae su hash y se crackea con john (recuperando `football`), lo que permite escalar a root y capturar la flag final.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `football` |
| 2 | *(Pregunta 2 no especificada en el original)* | `THM{pr1v1l3g3_3sc4l4t10n}` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Task 1, Pregunta 1 no especificada en el original)* | `No answer needed` |
| 2 | *(Task 2, Pregunta 1 no especificada en el original)* | `2`<br>`OpenSSH 7.6p1`<br>`2.4.29`<br>`Ubuntu`<br>`/admin` |
| 3 | *(Task 3, Pregunta 1 no especificada en el original)* | `admin:xavier` |
| 4 | *(Task 3, Pregunta 2 no especificada en el original)* | `rockinroll` |
| 5 | *(Task 3, Pregunta 3 no especificada en el original)* | `THM{a_password_is_not_a_barrier}` |
| 6 | *(Task 3, Pregunta 4 no especificada en el original)* | `THM{brut3_f0rce_is_e4sy}` |
| 7 | *(Task 4, Pregunta 1 no especificada en el original)* | `football` |
| 8 | *(Task 4, Pregunta 2 no especificada en el original)* | `THM{pr1v1l3g3_3sc4l4t10n}` |

---

**Metodología:** Enumeración con nmap (puertos 22/80) → fuzzing para descubrir `/admin` → fuerza bruta del login web con hydra → obtención de credenciales y flag de usuario → acceso y explotación vía SSH → extracción de la clave RSA protegida → cracking de su hash con john (passphrase `football`) → escalada a root → flag final.

### Cadena de ataque / Attack Chain

```text
nmap → servicios (SSH 7.6p1 / Apache 2.4.29) → ffuf → /admin → hydra (login web) → credenciales → flag usuario → SSH → clave RSA cifrada → john (passphrase football) → root → flag root
```

**Learning chain:** Enumeración de servicios → descubrimiento de `/admin` → fuerza bruta (hydra) → bandera usuario → crackeo de clave RSA (john) → escalada a root → bandera final

**Lección:** *Las contraseñas débiles y las claves privadas con passphrases crackeables convierten un simple acceso por fuerza bruta en el compromiso total del sistema.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1110 (Brute Force), T1078 (Valid Accounts), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Brute It](https://tryhackme.com/room/bruteit)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.