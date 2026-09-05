# CERTain Doom [HARD]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** HARD
* **Tipo / Type:** CTF (Free)
* **Slug:** `certaindoom`
* **Link:** https://tryhackme.com/room/certaindoom
* **Sección / Section:** 03 Level Hard
* **Fuente / Source:** thmrevenant (GitHub)

## Solucionario de Tareas / Task Solutions

> **ES:** En CERTain Doom se explota un Apache Tomcat 9 vulnerable a `CVE-2020-9484` (deserialización RCE) para obtener la flag web. Tras pivotar por Docker con ligolo-ng, se accede a una app de biblioteca cuyo backend `library-back` contiene la flag del usuario en un `chat.log`, y la flag secreta se obtiene saltándose un JWT con `CVE-2022-21449` (Psychic Signatures).
> **EN:** In CERTain Doom you exploit an Apache Tomcat 9 vulnerable to `CVE-2020-9484` (deserialization RCE) to get the web flag. After pivoting through Docker with ligolo-ng, you reach a library app whose `library-back` backend holds the user flag in a `chat.log`, and the secret flag is obtained by faking a JWT with `CVE-2022-21449` (Psychic Signatures).

### Task 1 — Flag web / Web flag

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the web flag? | `THM{c4T_g07_73H_d353r14L1z4710N_8lu3z}` |

### Task 2 — Flag del usuario / User's flag

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the user's flag? | `THM{1n73Rn4L_53rV1C35_n07_45_H1dD3N_4S_7H3Y_533|\/|}` |

### Task 3 — Flag súper secreta / Super secret flag

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the super secret flag? | `THM{H1dD3|\|_1n_Pl41N_516h7}` |

## Metodología / Methodology

1. **Paso / Step:** Escaneo de puertos: puertos `80` y `8080` abiertos. El puerto 8080 corresponde a Apache Tomcat 9.
2. **Paso / Step:** En `/reports` hay un formulario de subida de informes (acepta cualquier tipo de archivo) que guarda en `/usr/local/tomcat/temp/uploads`.
3. **Paso / Step:** `CVE-2020-9484`: la cookie `JSESSIONID` puede apuntar a una ruta local relativa; se usa `ysoserial` (con Java 11, la pista "hoy es el número de la suerte 11") para generar payloads de deserialización `CommonsCollections2`.
4. **Paso / Step:** Tres fases: `downloadPayload.session` (descarga `payload.sh` vía curl), `chmodPayload.session` (`chmod 777`) y `executePayload.session` (`bash payload.sh`); cada una se sube retocando la cookie `JSESSIONID` con `../../../../../temp/uploads/<nombre>`.
5. **Paso / Step:** Se recibe la reverse shell en el listener; flag web en el directorio actual.
6. **Paso / Step:** Estamos en un contenedor (`/etc/hosts` muestra `172.18.0.2` y `172.20.0.4`); se monta túnel con ligolo-ng para alcanzar `172.18.0.0/16` y `172.20.0.0/16`.
7. **Paso / Step:** Reconocimiento interno: `172.20.0.2` (app biblioteca, puerto 80) y `172.20.0.3` (backend `library-back`, puerto 8080).
8. **Paso / Step:** Análisis del backend (`/documents`): la cookie `credz` da acceso; con `/documents?author` se listan archivos (`hello.txt`, lista de TODOs y `chat.log`), y con `/documents/download/<archivo>` se descargan.
9. **Paso / Step:** El `chat.log` contiene la flag del usuario y una pista: el backend usa JWT con un algoritmo vulnerable en Java desactualizado.
10. **Paso / Step:** `/documents/count` indica 5 documentos pero solo se ven 4; con `/documents/<ID>` se fuzzear los IDs y se encuentra `specs.pdf` (oculto), que solo `hydra` puede descargar.
11. **Paso / Step:** `CVE-2022-21449` (Psychic Signatures): se forja un JWT ES256 con firma `r=s=0` en DER (`MAYCAQACAQA`) y los claims `{upn: hydra, groups: [user]}` → se accede a los archivos ocultos de `hydra` y se descarga `specs.pdf`.
12. **Paso / Step:** En `specs.pdf` se salta la última página (troll) y en la página 8 aparece la flag súper secreta.

### Cadena de ataque / Attack Chain

```
nmap -> Tomcat 9 en :8080 -> CVE-2020-9484 (ysoserial + JSESSIONID path traversal) -> reverse shell -> web flag -> Docker (/etc/hosts 172.18.0.2 / 172.20.0.4) -> ligolo-ng -> library-back (172.20.0.3:8080) -> credz cookie -> /documents exfiltration -> chat.log -> user flag -> CVE-2022-21449 (JWT ES256 r=s=0) -> specs.pdf (página 8) -> super secret flag
```

**Lección:** Dos CVE de deserialización/cadena de firma (2020-9484 y 2022-21449) convierten una página de subida de archivos y un backend de biblioteca en un camino de RCE y robo de documentos de alto nivel.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.