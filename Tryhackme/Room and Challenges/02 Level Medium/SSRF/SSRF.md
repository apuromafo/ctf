# SSRF

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Ofensivo / Web | ssrf | https://tryhackme.com/room/ssrf | 02 Level Medium | TryHackMe | SSRF, Servidor interno 192.168.2.10, HRMS, cURL, Cloud Metadata API | Acceso a recursos internos no expuestos y robo de credenciales |

---

**Contexto:** La sala **SSRF** enseña la vulnerabilidad *Server-Side Request Forgery*: cómo un servidor puede ser engañado para realizar peticiones en nombre del atacante contra hosts internos (192.168.2.10), explotando una API de gestión de personal (HRMS) para tomar el control de un panel admin, acceder a la metadata de cloud (revelando `API20190902,NTS`), provocar un crash de la propia página y validar peticiones ciegas que confirman comunicación. Cada fase va firmada con una flag `THM_`.

## Solucionario

### Task 1: Bienvenida
**Explicación:**

Se presenta el entorno y se confirma el acceso a la máquina vulnerable, sin respuesta requerida.

Respuesta: `No answer needed`

### Task 2: Puntuación del escenario
**Explicación:**

Se anota la valoración inicial del escenario SSRF planteado en la sala.

Respuesta: `6.72`

### Task 3: Explotación del panel HRMS
**Explicación:**

Se explota el SSRF para alcanzar el servicio interno de gestión, autenticándose con las credenciales del usuario admin y accediendo al panel de administración a través del host interno.

1. `hrmsadmin`
2. `hrmsadmin@123`
3. `http://192.168.2.10/admin.php`
4. `THM_{1NiT_S$rF}`

### Task 4: SSRF básico validado
**Explicación:**

Se confirma que el ataque básico de SSRF responde afirmativamente y se recoge la flag correspondiente.

1. `yea`
2. `THM_{B@$ic_s$rF}`

### Task 5: SSRF contra la nube
**Explicación:**

El intento de acceder a la metadata del proveedor de cloud no prospera, la protección aparece deshabilitada, se obtienen los tokens de la API (`API20190902,NTS`) y se determina que el tipo de ataque es ciego (*blind*).

1. `nay`
2. `disabled`
3. `API20190902,NTS`
4. `Blind`

### Task 6: Flag de crash
**Explicación:**

La explotación final hace fallar el servicio web, obteniendo la flag que acredita el compromiso.

Respuesta: `THM_{$$rF_Cr@$h3D}`

### Task 7: Comprobaciones finales
**Explicación:**

Se responden las comprobaciones de cierre del vector SSRF: la opción correcta del listado y la negativa a la última hipótesis planteada.

1. `b`
2. `nay`

### Task 8: Cierre
**Explicación:**

Se concluye la práctica de SSRF sin requerir respuesta final.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Bienvenida | `No answer needed` |
| 2 | Puntuación del escenario | `6.72` |
| 3.1 | Usuario del panel HRMS | `hrmsadmin` |
| 3.2 | Contraseña del panel HRMS | `hrmsadmin@123` |
| 3.3 | URL interna del administrador | `http://192.168.2.10/admin.php` |
| 3.4 | Flag de la fase inicial | `THM_{1NiT_S$rF}` |
| 4.1 | ¿Confirmado el SSRF básico? | `yea` |
| 4.2 | Flag del SSRF básico | `THM_{B@$ic_s$rF}` |
| 5.1 | ¿Accesible la metadata? | `nay` |
| 5.2 | Estado de la protección | `disabled` |
| 5.3 | Tokens de la API | `API20190902,NTS` |
| 5.4 | Tipo de ataque | `Blind` |
| 6 | Flag del crash | `THM_{$$rF_Cr@$h3D}` |
| 7.1 | Opción correcta | `b` |
| 7.2 | Última hipótesis | `nay` |
| 8 | Tarea de cierre | `No answer needed` |

---

**Metodología:** Detección de SSRF, redirección de peticiones del servidor contra la red interna, autenticación a un panel HRMS oculto, abuso del endpoint de metadata cloud y validación de SSRF ciego mediante la respuesta del servicio.

**Learning chain:** Reconocimiento → identificación del SSRF → pivote al host interno → acceso admin → metadata cloud → crash/DoS → flags.

**Lección:** *El SSRF convierte al propio servidor en un proxy del atacante hacia la red interna; cualquier URL filtrada por el cliente es superficie de ataque.*

**MITRE ATT&CK:** T1091 Replication Through Removable Media (no aplica) · T1213 Data from Information Repositories · T1498 Network Denial of Service · T1005 Data from Local System.

**Fuente:** [TryHackMe - SSRF](https://tryhackme.com/room/ssrf)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.