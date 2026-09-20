# Lookup

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | challenge | `lookup` | [TryHackMe](https://tryhackme.com/room/lookup) | 01 Level Easy | TryHackMe | web enumeration / subdomain discovery / credential discovery / DNS leads | Enumeración web y de subdominios para descubrir credenciales ocultas y acceder al sistema |

---

**Contexto:** Sala de tipo challenge centrada en la fase de enumeración web de una máquina Linux. Se realiza descubrimiento de subdominios, revisión de recursos y aprovechamiento de pistas de DNS para obtener credenciales válidas.

## Solucionario

### Task 1

**Explicación:** Se enumeran los subdominios y servicios web del objetivo hasta dar con credenciales que permiten el acceso al sistema, obteniendo los dos hashes solicitados como respuesta.

1. 38375fb4dd8baa2b2039ac03d92b820e
2. 5a285a9f257e45c68bb6c9f9f57d18e8

---

| # | Task | Respuesta |
|---|------|-----------|
| 1 | Task 1 | `38375fb4dd8baa2b2039ac03d92b820e` |
| 2 | Task 1 | `5a285a9f257e45c68bb6c9f9f57d18e8` |

---

**Metodología:** Se inicia con un escaneo de puertos y servicios de la máquina objetivo. Posteriormente se realiza enumeración de subdominios mediante fuzzing de DNS o wordlists, se revisan los recursos publicados en cada servicio descubierto y se extraen credenciales válidas para completar el acceso. Las dos respuestas corresponden a los hashes de las credenciales objetivo.

### Cadena de ataque / Attack Chain

```text
nmap -> enumeración web -> subdomain fuzzing -> revisión de recursos -> extracción de credenciales -> hash final
```

**Learning chain:** port scanning → web enumeration → subdomain discovery → credential extraction → hash capture

**Lección:** *Los subdominios olvidados y los recursos web desatendidos suelen contener credenciales o pistas que permiten ingresar a un sistema; la enumeración exhaustiva es la clave.*

**MITRE ATT&CK:** T1083 (File and Directory Discovery), T1595.001 (Active Scanning: Scanning IP Blocks), T1589.002 (Gather Victim Identity Information: Email Addresses)

**Fuente:** [TryHackMe - Lookup](https://tryhackme.com/room/lookup)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.