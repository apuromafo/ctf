# Profiles

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Investigación | profiles | https://tryhackme.com/room/profiles | 02 Level Medium | TryHackMe | Archivos de perfil, Cron, Linux, Escalada de privilegios | Compromiso de la máquina / escalada a root |

---

**Contexto:** La sala **Profiles** plantea una investigación sobre una máquina Linux en la que los archivos de perfil (`.bashrc`, cron) juegan un papel central. Las respuestas recogen credenciales, marcas temporales, hashes, direcciones y la tarea `cron` que copia `.bashrc` sobre el perfil de root, evidenciando una persistencia/escalada basada en perfiles de usuario.

## Solucionario

### Task 1: Enumeración de perfiles y cron / Profiles and cron enumeration
**Explicación:**

La secuencia de respuestas documenta los artefactos encontrados durante el análisis: una credencial, la marca de tiempo del evento, el hash asociado, la dirección `IP:puerto` del servicio, la ubicación del crontab de root con el número de línea, y la tarea cron periódica que copia el perfil de bash al usuario root.

```
1. Ftrccw45PHyq
2. 2023-11-07 03:49:45
3. 0511ccaad402d6d13ce801e1e9136ba2
4. 10.0.2.72:1337
5. /var/spool/cron/crontabs/root:131127
6. * * * * * cp /opt/.bashrc /root/.bashrc
```

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué credencial se localiza en el análisis? | `Ftrccw45PHyq` |
| 2 | ¿Qué fecha/hora registra el evento? | `2023-11-07 03:49:45` |
| 3 | ¿Qué hash se identifica? | `0511ccaad402d6d13ce801e1e9136ba2` |
| 4 | ¿Qué dirección IP y puerto se asocian al servicio? | `10.0.2.72:1337` |
| 5 | ¿Dónde se ubica la entrada del crontab de root? | `/var/spool/cron/crontabs/root:131127` |
| 6 | ¿Qué tarea cron se encuentra programada? | `* * * * * cp /opt/.bashrc /root/.bashrc` |

---

**Metodología:** Revisión de archivos de perfil y credenciales, correlación temporal de eventos, análisis de hashes, inspección del crontab de root y comprensión de la tarea recurrente sobre `.bashrc`.

### Cadena de ataque / Attack Chain

```
Acceso inicial / recolección de credenciales
        │
        ▼
Análisis de archivos de perfil (bashrc) y cron
        │
        ▼
Identificar tarea: cp /opt/.bashrc /root/.bashrc
        │
        ▼
Abuso del perfil copiado a root → control del entorno root
```

**Learning chain:** Recolección de credenciales → correlación de timestamps → inspección de cron de root → abuso de `.bashrc`.

**Lección:** *Un archivo de perfil manipulable que se copia periódicamente sobre la cuenta de root convierte cualquier edición en persistencia con privilegios máximos; los cron jobs deben auditarse como vectores de escalada.*

**MITRE ATT&CK:** T1053.003 Scheduled Task/Job (Cron) · T1547.001 Boot or Logon Autostart (Profile) · T1068 Exploitation for Privilege Escalation.

**Fuente:** [TryHackMe - Profiles](https://tryhackme.com/room/profiles)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.