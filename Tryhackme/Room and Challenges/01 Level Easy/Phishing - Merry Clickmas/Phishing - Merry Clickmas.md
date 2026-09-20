# Phishing - Merry Clickmas

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `phishing-aoc2025-h2tkye9fzU` | https://tryhackme.com/room/phishing-aoc2025-h2tkye9fzU | Advent of Cyber 2025 | TryHackMe | SET phishing, credential harvesting, Roundcube | Medio — obtención de credenciales de usuario para acceso al portal TBFC mediante campaña de phishing automatizada |

---

**Contexto:** En el día 2 de Advent of Cyber 2025, se ejecuta una campaña de phishing contra factory@wareville.thm utilizando el Social Engineering Toolkit (SET) para robar credenciales. Se configura un vector de ataque de credential harvesting que captura las credenciales del usuario objetivo y se permite acceder al portal Roundcube del TBFC para confirmar la explotación.

> **ES:** Configura una campaña de phishing con el Social Engineering Toolkit (SET) contra la fábrica de Wareville, captura las credenciales de la víctima con un servidor de credential harvesting y accede al portal Roundcube del TBFC para confirmar la explotación.
> **EN:** Set up a phishing campaign with the Social Engineering Toolkit (SET) against the Wareville factory, harvest the victim's credentials with a credential harvesting server and log in to the TBFC Roundcube portal to confirm the exploitation.

## Solucionario

### Task 1: Configuración del Phishing

**Explicación:** Se arranca SET y se elige la opción de website attack vectors → credential harvesting. Se clona el portal web del TBFC (siguiendo el setup wizard del room: dirección de retorno del AttackBox, plantilla del sitio del TBFC) y se envía el correo de phishing a factory@wareville.thm. Cuando la víctima introduce sus credenciales en la página clonada, SET las captura. La contraseña robada es `unranked-wisdom-anthem`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the password used to access the TBFC portal? | `unranked-wisdom-anthem` |

### Task 2: Confirmación y Resultados

**Explicación:** Con las credenciales capturadas se accede al portal Roundcube del TBFC como el usuario de la fábrica de Wareville. Dentro del buzón (o del portal de pedidos) se consulta la cantidad total de juguetes esperados para entrega, cuyo valor es `1984000`, confirmando así el acceso a los datos internos del TBFC.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the total number of toys expected for delivery? | `1984000` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the password used to access the TBFC portal? | `unranked-wisdom-anthem` |
| 2 | What is the total number of toys expected for delivery? | `1984000` |

---

**Metodología:** Se utilizó el Social Engineering Toolkit (SET) para configurar un servidor de credential harvesting, creando un vector de phishing dirigido a factory@wareville.thm. Se capturaron las credenciales enviadas por la víctima y se utilizó la contraseña obtenida para autenticarse en el portal Roundcube del TBFC, confirmando así la explotación exitosa de la campaña de phishing.

### Cadena de ataque / Attack Chain

```text
SET (credential harvesting) -> página clonada del TBFC -> correo a factory@wareville.thm -> víctima envía credenciales -> captura (unranked-wisdom-anthem) -> login Roundcube -> total de juguetes (1984000)
```

**Learning chain:** SET configuration → credential harvesting server → phishing email delivery → credential capture → Roundcube login → portal data exfiltration

**Lección:** *Una campaña de phishing con tools como SET puede robar credenciales en minutos: clonar un portal legítimo y capturar lo que escribe la víctima basta para comprometer cuentas, por eso el factor humano sigue siendo el eslabón más débil de la seguridad.*

**MITRE ATT&CK:** T1566.002 (Phishing: Spearphishing Link), T1557 (Adversary-in-the-Middle), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - Phishing - Merry Clickmas](https://tryhackme.com/r/room/phishing-aoc2025-h2tkye9fzU)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.