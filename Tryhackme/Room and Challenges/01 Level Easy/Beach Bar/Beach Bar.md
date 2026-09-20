# Beach Bar

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | challenge | `hh-beachbar-d849f7f7` | [TryHackMe](https://tryhackme.com/r/room/hh-beachbar-d849f7f7) | Hunt & Hack House | THM | nmap/enumeration/credential reuse/yml playlist | Captura de credenciales reutilizadas y escalada a root mediante un playlist YAML expuesto |

---

**Contexto:** Una playa tropical esconde más que arena y sol: el servidor del Beach Bar aloja archivos de configuración en formato YAML que contienen credenciales reutilizadas. La enumeración inicial revela servicios ocultos y un playlist que sirve como vector de acceso inicial al sistema.

> **ES:** En un servidor del Beach Bar se descubren servicios ocultos durante la enumeración. Un archivo de playlist en YAML expone credenciales reutilizadas que permiten la conexión SSH; las mismas credenciales reutilizadas otorgan acceso root y permiten capturar ambas flags.
> **EN:** Enumerating the Beach Bar server reveals hidden services. An exposed YAML playlist contains reused credentials that grant SSH access; the same reused credentials provide root access and allow both flags to be captured.

## Solucionario

### Task 1: User Flag
**Explicación:** Tras la enumeración inicial con Nmap y la búsqueda de archivos, se localiza un playlist YAML con credenciales reutilizadas. Con ellas se establece una sesión SSH como usuario regular y se captura el user flag.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| What is the user flag? | `THM{y4ml_pl4yl1st_pwns_th3_b34ch}` |

### Task 2: Root Flag
**Explicación:** Al reutilizar las mismas credenciales encontradas en el archivo YAML, se obtiene acceso root al sistema y se captura el root flag.

| Pregunta / Question | Respuesta / Answer |
|--------------------|--------------------|
| What is the root flag? | `THM{cr3d3nt14l_r3us3_4t_th3_b34ch_b4r}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | User flag | `THM{y4ml_pl4yl1st_pwns_th3_b34ch}` |
| 2 | Root flag | `THM{cr3d3nt14l_r3us3_4t_th3_b34ch_b4r}` |

---

**Metodología:** Se inicia con un escaneo nmap completo de la máquina target para identificar servicios abiertos. Posteriormente se procede a la enumeración exhaustiva de directorios y archivos, localizando un archivo YAML con credenciales reutilizadas. Con las credenciales obtenidas se establece conexión SSH como usuario regular y se completa la captura del user flag. La escalada de privilegios se logra explotando credenciales reutilizadas que otorgan acceso root al sistema, permitiendo capturar el root flag.

### Cadena de ataque / Attack Chain

```text
nmap -> enumeración de puertos -> discovery de directorios -> análisis del playlist YAML -> extracción de credenciales -> SSH -> captura del user flag -> reutilización de credenciales -> root -> captura del root flag
```

**Learning chain:** nmap scanning → port enumeration → directory discovery → YAML playlist analysis → credential extraction → SSH access → user flag capture → credential reuse escalation → root access → root flag capture

**Lección:** *Los archivos de configuración expuestos (como playlists YAML) suelen contener credenciales en claro; la reutilización de esas credenciales en otros servicios permite escalar fácilmente a root.*

**MITRE ATT&CK:** T1078 (Valid Accounts), T1110 (Brute Force), T1021 (Remote Services), T1552 (Credentials In Files)

**Fuente:** [TryHackMe - Beach Bar](https://tryhackme.com/r/room/hh-beachbar-d849f7f7)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.