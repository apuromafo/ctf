# SideQuest 4 - Tutorial (djalilayed files_egg)

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| N/A | Tutorial SideQuest | `advent2025` | N/A | Advent of Cyber Tryhackme | https://github.com/djalilayed/tryhackme/ | receta cyberchef del decodificado del script y clave de acceso al zip | proporciona la clave de la sidequest 4 (breachblocker unlocker) y enlace al walkthrough oficial |

**Contexto:** Archivo auxiliar de la SideQuest 4 (BreachBlocker Unlocker) del Advent of Cyber 2025. Incluye la receta CyberChef para decodificar el script y la clave del ZIP, basado en el repositorio fuente de djalilayed.

#ource https://github.com/djalilayed/tryhackme/

### BreachBlocker Unlocker Side Quest Access key - Full Walkthrough 2025 : 

[BreachBlocker Unlocker Side Quest Access key - Full Walkthrough 2025  - Full Walkthrough 2025]()

Zip file password: CanYouREM3?

## Cyberchef recipe to decode the script

```
Regular_expression('User defined','[A-Za-z0-9+/]{30,}',true,true,false,false,false,false,'List matches')
From_Base64('A-Za-z0-9+/=',true,false)
Regular_expression('User defined','\\$d\\s*=\\s*\'([^\']+)\'',true,true,false,false,false,false,'List capture groups')
From_Base64('A-Za-z0-9+/=',true,false)
XOR({'option':'Decimal','string':'23'},'Standard',false)
Render_Image('Raw')
```

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
