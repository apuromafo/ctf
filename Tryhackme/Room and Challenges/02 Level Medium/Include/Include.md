# Include

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Web / Pentesting | include | https://tryhackme.com/room/include | 02 Level Medium | TryHackMe | Node.js, PHP, Prototype Pollution, SSRF, LFI, Log Poisoning | Compromiso total del servidor / RCE |

---

**Contexto:** La máquina **Include** expone dos aplicaciones web: la **Review App** (Node.js/Express, puerto 4000, credenciales por defecto `guest:guest`) y **SysMon** (Apache/PHP, puerto 50000). La kill-chain combina ataques del módulo *Advanced Server-Side Attacks*: asignación masiva de propiedades (**prototype pollution**) para escalar el rol, **SSRF** vía la URL del banner para consultar una API interna y filtrar credenciales, login en SysMon (flag 1), y **LFI** en `profile.php?img=` con bypass `....//` para leer archivos, que se combina con **log poisoning** del servicio SMTP (puerto 25) para lograr **RCE** y leer el archivo oculto (flag 2).

## Solucionario

### Task 1: Flag tras iniciar sesión en SysMon
**Explicación:**

Tras el escaneo (`nmap`) se identifican los puertos 4000 (Review App) y 50000 (SysMon). En la Review App se inicia sesión con `guest:guest`; al sugerir una actividad (`/recommend-activity/1`) la app hace `obj[activityType] = activityName` sobre tu propio objeto de usuario: **mass assignment / prototype pollution**. Enviando JSON con `isAdmin: true` (booleano, no string) se sobreescribe la propiedad y se abre el menú de admin (`/admin/api` y `/admin/settings`).

En `/admin/api` se descubre la API interna `http://127.0.0.1:5000/getAllAdmins101099991` (solo escucha en localhost). En `/admin/settings` el formulario **update-banner-image** hace fetch de una URL del lado servidor = **SSRF**; apuntándolo a la API interna, la respuesta se guarda como data-URI base64 en el banner:

```
{"ReviewAppUsername":"admin","ReviewAppPassword":"admin@!!!","SysMonAppUsername":"administrator","SysMonAppPassword":"S$9$qk6d#**LQU"}
```

Con las credenciales de SysMon (`administrator:S$9$qk6d#**LQU`) se inicia sesión en `:50000` y el dashboard muestra la primera flag.

Respuesta: `THM{!50_55Rf_1S_d_k3Y??!}`

### Task 2: Contenido del archivo oculto en /var/www/html
**Explicación:**

El dashboard de SysMon carga el avatar mediante `profile.php?img=<nombre>`. El parámetro `img` es un **LFI** con un filtro que elimina `../` una sola vez (no recursivo); el bypass es `....//` (tras el `strip` de `../` queda `../`), repetido para ascender a `/` y luego usar ruta absoluta. Se confirma con `....//....//...//etc/passwd` (usuarios `joshua` y `charles`).

Para obtener **RCE** se envenenan los logs del servicio de correo: con `nc -nv <IP> 25` se realiza una conversación SMTP (HELO/MAIL FROM/RCPT TO/DATA) inyectando `<?php system($_GET['cmd']); ?>` en el destinatario; luego se incluye `/var/log/mail.log` vía LFI añadiendo el parámetro `cmd` para ejecutar comandos (`ls`, `cat`). Así se lista `/var/www/html` y se lee el archivo oculto.

Respuesta: `THM{505eb0fb8a9f32853b4d955e1f9123ea}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag tras iniciar sesión en SysMon | `THM{!50_55Rf_1S_d_k3Y??!}` |
| 2 | Contenido del archivo oculto en /var/www/html | `THM{505eb0fb8a9f32853b4d955e1f9123ea}` |

---

**Metodología:** Penetración web de doble aplicación: enumeración de puertos, login por defecto (`guest:guest`), mass assignment vía prototype pollution (`isAdmin=true`), SSRF con `curl -X POST .../update-banner-image --data-urlencode 'url=http://127.0.0.1:5000/getAllAdmins101099991'`, decode de la data-URI base64 para credenciales, LFI con bypass `....//` en `profile.php?img=`, log poisoning vía SMTP (mail.log) y RCE con `system($_GET['cmd'])`.

**Learning chain:** Enumeración → acceso guest → mass assignment/prototype pollution → admin → SSRF → fuga de credenciales → login SysMon (flag 1) → LFI `....//` → log poisoning (SMTP) → RCE → archivo oculto (flag 2).

**Lección:** *Una cadena de defectos "soft" (asignación abierta, SSRF sin restricción de destino, filtro de LFI no recursivo, credenciales en claro) se encadena hasta convertir tres apps internas en una RCE por log poisoning.*

**MITRE ATT&CK:** T1595 Active Scanning · T1190 Exploit Public-Facing Application · T1068 Exploitation for Privilege Escalation · T1005 Data from Local System · T1105 Ingress Tool Transfer · T1059.006 Command and Scripting Interpreter: Python · T1071.001 Application Layer Protocol: Web Protocols.

**Fuente:** [TryHackMe - Include](https://tryhackme.com/room/include)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.