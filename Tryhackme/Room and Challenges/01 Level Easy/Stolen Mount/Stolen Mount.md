# Stolen Mount

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | challenge | `stolenmount` | [TryHackMe](https://tryhackme.com/room/stolenmount) | 01 Level Easy | TryHackMe | NFS, mounts, privilegios sin root squash | Escalada de privilegios a root mediante montaje NFS con el servicio sin root squash habilitado |

---

**Contexto:** Sala que explota una mala configuración del servicio NFS (Network File System) con la opción `no_root_squash` habilitada, lo que permite a un atacante montar un recurso compartido y modificar archivos con privilegios de root. El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

> **ES:** Servidor NFS configurado con `no_root_squash`. Se monta el recurso compartido y se explota la configuración para obtener shell como root y capturar la flag `THM{n0t_s3cur3_f1l3_sh4r1ng}`.
> **EN:** NFS server configured with `no_root_squash`. The shared resource is mounted and the misconfiguration is exploited to obtain a root shell and capture the flag `THM{n0t_s3cur3_f1l3_sh4r1ng}`.

## Solucionario

### Task 1: Explotación NFS / NFS Exploitation

**Explicación:** Se explota la configuración del NFS con `no_root_squash` para obtener privilegios de root en el servidor y capturar la flag de la sala. Todo el contenido original se conserva verbatim:

1. THM{n0t_s3cur3_f1l3_sh4r1ng}

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de la sala / Machine flag | `THM{n0t_s3cur3_f1l3_sh4r1ng}` |

---

**Metodología:** Se identifica el servicio NFS activo → se enumera el recurso compartido con `showmount -e` → se detecta la opción `no_root_squash` → se monta el recurso compartido localmente → se crea un binario con shell inversa o se modifica `/etc/passwd` para obtener root → se captura la flag.

### Cadena de ataque / Attack Chain

```text
nmap -> NFS activo -> showmount -e -> no_root_squash -> mount -> creación de binario con SUID -> ejecución como root -> flag THM{n0t_s3cur3_f1l3_sh4r1ng}
```

**Learning chain:** NFS enumeration --> showmount --> no_root_squash detected --> shared resource mount --> SUID binary creation --> root shell --> machine flag

**Lección:** *La opción `no_root_squash` en NFS permite que un usuario local ejecute código con privilegios de root en el servidor, convirtiendo un recurso compartido mal configurado en una escalada de privilegios directa.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1133 (External Remote Services – NFS), T1068 (Exploitation for Privilege Escalation), T1543 (Create or Modify System Process – SUID binary)

**Fuente:** [TryHackMe - Stolen Mount](https://tryhackme.com/room/stolenmount)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.