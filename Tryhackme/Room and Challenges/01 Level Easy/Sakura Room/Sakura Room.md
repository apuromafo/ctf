# Sakura Room

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `sakuraroom` | [TryHackMe](https://tryhackme.com/room/sakuraroom) | `01 Level Easy` | THM | OSINT, redes sociales, correo, Ethereum, Wi-Fi, geolocalización | Resolución completa del reto OSINT |

---

**Contexto:** Reto de OSINT centrado en reconstruir la identidad digital de Aiko (SakuraSnowAngelAiko) a partir de pistas públicas: se rastrean sus perfiles en redes sociales, su correo electrónico, su nombre real, su actividad con criptomonedas (Ethereum, Ethermine, Tether), el SSID y la MAC de su red Wi-Fi, y sus viajes mediante códigos de aeropuerto y destinos.

> **ES:** Reto de OSINT en el que, a partir de las pistas públicas de la usuaria SakuraSnowAngelAiko, se reconstruye su identidad digital: perfiles, correo (SakuraSnowAngel83@protonmail.com), nombre real (Aiko Abe), monedero de Ethereum, datos Wi-Fi y desplazamientos.
> **EN:** OSINT challenge in which, from public clues of user SakuraSnowAngelAiko, her digital identity is reconstructed: profiles, email (SakuraSnowAngel83@protonmail.com), real name (Aiko Abe), Ethereum wallet, Wi-Fi data and travels.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Tarea inicial de la room: únicamente requiere arrancar la sala y confirmar que está lista; no hay conocimiento técnico que aplicar todavía.

1. Let's Go!

### Task 2: Identidad en redes / Social media identity

**Explicación:** La primera pista lleva hasta el perfil de la usuaria en redes sociales, cuyo nombre de usuario es SakuraSnowAngelAiko.

2. SakuraSnowAngelAiko

### Task 3: Correo y nombre real / Email and real name

**Explicación:** Del perfil se extraen el correo electrónico (SakuraSnowAngel83@protonmail.com) y el nombre real de la persona (Aiko Abe).

1. SakuraSnowAngel83@protonmail.com
2. Aiko Abe

### Task 4: Criptomonedas / Cryptocurrency

**Explicación:** Se identifica la actividad de Aiko con criptomonedas: la red Ethereum, su monedero 0xa102397dbeeBeFD8cD2F73A89122fCdB53abB6ef, la plataforma de minería Ethermine y el stablecoin Tether.

1. Ethereum
2. 0xa102397dbeeBeFD8cD2F73A89122fCdB53abB6ef
3. Ethermine
4. Tether

### Task 5: Wi-Fi y MAC / Wi-Fi and MAC

**Explicación:** Se recupera el SSID de su punto de acceso (SakuraLoverAiko) junto con la dirección MAC 84:af:ec:34:fc:f8 asociada al dispositivo.

1. SakuraLoverAiko
2. 84:af:ec:34:fc:f8

### Task 6: Viajes / Travel

**Explicación:** Los códigos de aeropuerto (DCA, HND) y los destinos (Lake Inawashiro, Hirosaki) revelan los desplazamientos y puntos de interés de Aiko.

1. DCA
2. HND
3. Lake Inawashiro
4. Hirosaki

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|---|---|---|
| 1.1 | Expresión de confirmación de la room | `Let's Go!` |
| 2.1 | Nombre de usuario en redes sociales | `SakuraSnowAngelAiko` |
| 3.1 | Correo electrónico de la usuaria | `SakuraSnowAngel83@protonmail.com` |
| 3.2 | Nombre real de la usuaria | `Aiko Abe` |
| 4.1 | Red de criptomonedas utilizada | `Ethereum` |
| 4.2 | Dirección del monedero | `0xa102397dbeeBeFD8cD2F73A89122fCdB53abB6ef` |
| 4.3 | Plataforma de minería | `Ethermine` |
| 4.4 | Stablecoin relacionada | `Tether` |
| 5.1 | SSID del punto de acceso | `SakuraLoverAiko` |
| 5.2 | Dirección MAC del dispositivo | `84:af:ec:34:fc:f8` |
| 6.1 | Código de aeropuerto de origen | `DCA` |
| 6.2 | Código de aeropuerto de destino | `HND` |
| 6.3 | Lago visitado | `Lake Inawashiro` |
| 6.4 | Destino final del viaje | `Hirosaki` |

---

**Metodología:** 1) Localizar el perfil de SakuraSnowAngelAiko y confirmar la entrada a la sala. 2) Revisar sus redes sociales para obtener correo y nombre real. 3) Rastrear su actividad con criptomonedas (monedero, minería y tether). 4) Buscar el SSID y la dirección MAC asociados a su red Wi-Fi. 5) Correlacionar códigos de aeropuerto y lugares para reconstruir sus viajes.

### Cadena de ataque / Attack Chain

```text
Confirmación de la room -> perfil SakuraSnowAngelAiko -> correo + nombre real -> actividad Ethereum/Ethermine/Tether -> SSID SakuraLoverAiko + MAC -> viajes (DCA, HND, Lake Inawashiro, Hirosaki)
```

**Learning chain:** OSINT en redes sociales -> extracción de correo y nombre real -> rastreo de actividad en criptomonedas -> identificación de datos Wi-Fi (SSID/MAC) -> reconstrucción de viajes por geolocalización

**Lección:** *El OSINT consiste en encadenar pistas públicas aparentemente aisladas (un perfil, un correo, una wallet, un SSID, una MAC) hasta reconstruir la identidad digital y física de una persona.*

**MITRE ATT&CK:** T1593 (Search Open Websites/Domains), T1592.001 (Gather Victim Host Information: Hardware)

**Fuente:** [TryHackMe - Sakura Room](https://tryhackme.com/room/sakuraroom)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.