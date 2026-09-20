# Sneaky Patch

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | Análisis de Parche / Patch Analysis | sneakypatch | https://tryhackme.com/room/sneakypatch | 01 Level Easy | TryHackMe | Análisis de parches, Backdoor, Ingeniería inversa | Alto |

---

**Contexto:**
> **ES:** Laboratorio de análisis de un parche de software que esconde una puerta trasera. El reto consiste en localizar la modificación maliciosa y confirmar el hallazgo con la flag.
> **EN:** A lab analysing a software patch that hides a backdoor. The challenge is to locate the malicious modification and confirm the finding with the flag.

## Solucionario

### Task 1: Detección de la puerta trasera / Backdoor Detection
**Explicación:**
La única tarea del laboratorio consiste en inspeccionar el parche, detectar la puerta trasera oculta y responder con la flag.

```
1. THM{sup3r_sn34ky_d00r}
```

### Tabla unificada de preguntas/respuestas

| # | Respuesta |
|---|---|
| 1 | `THM{sup3r_sn34ky_d00r}` |

---

**Metodología:**
1. Descarga y descompresión del parche.
2. Comparación de los artefactos parcheados frente a la versión original.
3. Localización del código malicioso inyectado (backdoor).
4. Validación del hallazgo con la flag.

### Cadena de ataque / Attack Chain
Parche malicioso → Revisión del diff → Detección del backdoor → Flag.

**Learning chain:**
Inspección de parches → análisis de diferencias → detección de código no autorizado.

**Lección:** *Un parche legítimo puede ocultar modificaciones no autorizadas; la revisión del contenido real es imprescindible antes de aplicarlo.*

**MITRE ATT&CK:**
| Técnica | ID |
|---|---|
| Supply Chain Compromise | T1195 |
| Compromise Software Dependencies and Development Tools | T1195.001 |
| Hidden Files and Directories | T1564.001 |

**Fuente:** [TryHackMe - Sneaky Patch](https://tryhackme.com/room/sneakypatch)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.