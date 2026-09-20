# Source

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `source` | [TryHackMe](https://tryhackme.com/room/source) | 01 Level Easy | TryHackMe | Supply Chain, Webmin, Installer Backdoor | Technical — Supply chain compromise analysis |

---

**Contexto:** Este room explora un escenario de compromiso de cadena de suministro (supply chain), donde un paquete de instalación malicioso fue distribuido. Se Analiza el impacto de la contaminación de fuentes de software y la importancia de verificar la integridad de las instalaciones.

## Solucionario

### Task 1: Supply Chain Analysis

**Explicación:** Se Analiza el escenario de compromiso de cadena de suministro y se Identifican las flags correspondientes a la comprometación y la necesidad de actualizar la instalación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag for the compromised version? | `THM{SUPPLY_CHAIN_COMPROMISE}` |
| 2 | What is the flag for the updated installation? | `THM{UPDATE_YOUR_INSTALL}` |

---

**Metodología:** Se Analiza el escenario de compromiso de cadena de suministro, identificando el vector de ataque y la solución recomendada para mitigar el riesgo.

### Cadena de ataque / Attack Chain

**Learning chain:** Supply Chain Analysis → Installer Identification → Compromise Detection → Patch Remediation → Risk Mitigation

**Lección:** *La cadena de suministro de software es un vector de ataque crítico: verificar la integridad de las instalaciones y mantener el software actualizado son medidas esenciales para mitigar este tipo de compromisos.*

**MITRE ATT&CK:** T1195.002 — Compromise Software Supply Chain; T1195 — Supply Chain Compromise

**Fuente:** [TryHackMe - Source](https://tryhackme.com/room/source)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.