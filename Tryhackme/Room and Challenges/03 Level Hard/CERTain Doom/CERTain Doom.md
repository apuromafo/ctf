# CERTain Doom

| **Dificultad** | Hard |
| **Tipo** | CTF |
| **Slug** | `certaindoom` |
| **Link** | [TryHackMe](https://tryhackme.com/room/certaindoom) |
| **Sección** | 03 Level Hard |
| **Fuente** | thmrevenant (GitHub) |
| **Componentes** | Apache Tomcat / CVE-2020-9484 / ysoserial / deserialización / ligolo-ng / Docker / JWT / CVE-2022-21449 |
| **Impacto** | RCE por deserialización en Apache Tomcat (CVE-2020-9484) y forja de un JWT ES256 con Psychic Signatures (CVE-2022-21449) tras pivotar por contenedores Docker con ligolo-ng. |

---

**Contexto:** En CERTain Doom se explota un Apache Tomcat 9 vulnerable a `CVE-2020-9484` (deserialización RCE) para obtener la flag web. Tras pivotar por Docker con ligolo-ng, se accede a una app de biblioteca cuyo backend `library-back` contiene la flag del usuario en un `chat.log`, y la flag secreta se obtiene saltándose un JWT con `CVE-2022-21449` (Psychic Signatures).

## Solucionario

### Task 1: Flag web

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the web flag? | `THM{c4T_g07_73H_d353r14L1z4710N_8lu3z}` |

### Task 2: Flag del usuario

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user's flag? | `THM{1n73Rn4L_53rV1C35_n07_45_H1dD3N_4S_7H3Y_533|\/|}` |

### Task 3: Flag súper secreta

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the super secret flag? | `THM{H1dD3|\|_1n_Pl41N_516h7}` |

---

**Metodología:**
1. Escaneo de puertos: `80` y `8080` abiertos; el 8080 corresponde a Apache Tomcat 9.
2. En `/reports` hay un formulario de subida de informes (acepta cualquier tipo de archivo) que guarda en `/usr/local/tomcat/temp/uploads`.
3. `CVE-2020-9484`: la cookie `JSESSIONID` puede apuntar a una ruta local relativa; se usa `ysoserial` (con Java 11, la pista "hoy es el número de la suerte 11") para generar payloads de deserialización `CommonsCollections2`.
4. Tres fases: `downloadPayload.session` (descarga `payload.sh` vía curl), `chmodPayload.session` (`chmod 777`) y `executePayload.session` (`bash payload.sh`); cada una se sube retocando la cookie `JSESSIONID` con `../../../../../temp/uploads/<nombre>`.
5. Se recibe la reverse shell en el listener; flag web en el directorio actual.
6. Estamos en un contenedor (`/etc/hosts` muestra `172.18.0.2` y `172.20.0.4`); se monta túnel con ligolo-ng para alcanzar `172.18.0.0/16` y `172.20.0.0/16`.
7. Reconocimiento interno: `172.20.0.2` (app biblioteca, puerto 80) y `172.20.0.3` (backend `library-back`, puerto 8080).
8. Análisis del backend (`/documents`): la cookie `credz` da acceso; con `/documents?author` se listan archivos (`hello.txt`, lista de TODOs y `chat.log`), y con `/documents/download/<archivo>` se descargan.
9. El `chat.log` contiene la flag del usuario y una pista: el backend usa JWT con un algoritmo vulnerable en Java desactualizado.
10. `/documents/count` indica 5 documentos pero solo se ven 4; fuzzeando los IDs con `/documents/<ID>` se encuentra `specs.pdf` (oculto), que solo `hydra` puede descargar.
11. `CVE-2022-21449` (Psychic Signatures): se forja un JWT ES256 con firma `r=s=0` en DER (`MAYCAQACAQA`) y los claims `{upn: hydra, groups: [user]}` → acceso a los archivos ocultos de `hydra` y descarga de `specs.pdf`.
12. En `specs.pdf` se salta la última página (troll) y en la página 8 aparece la flag súper secreta.

**Learning chain:** `nmap → Tomcat 9 en :8080 → CVE-2020-9484 (ysoserial + JSESSIONID path traversal) → reverse shell → web flag → Docker (/etc/hosts) → ligolo-ng → library-back (172.20.0.3:8080) → credz cookie → /documents exfiltration → chat.log → user flag → CVE-2022-21449 (JWT ES256 r=s=0) → specs.pdf (página 8) → super secret flag`

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1105 (Ingress Tool Transfer), T1059 (Command and Scripting Interpreter), T1078 (Valid Accounts), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - CERTain Doom](https://tryhackme.com/room/certaindoom)