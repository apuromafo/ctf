# Anonymous

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF | anonymous | https://tryhackme.com/room/anonymous | 02 Level Medium | TryHackMe | FTP, SMB, MD5, ssh | Compromiso total de la máquina |

---

**Contexto:** La sala **Anonymous** es un CTF sencillo sobre una máquina Linux con varios servicios expuestos. El flujo de resolución parte de enumerar puertos y servicios, descubrir un demonio FTP y un recurso SMB accesible, localizar el share expuesto (`pics`), extraer los archivos que contiene y tratar los hashes MD5 para derivar credenciales que permiten acceder por SSH y comprometer la máquina. Las respuestas documentan el número de puertos, los servicios relevantes y los dos hashes extraídos.

## Solucionario

### Task 1: Explotación de la máquina
**Explicación:**

Se enumera la máquina con `nmap` descubriendo los puertos abiertos y los servicios. Se identifica el servicio FTP y el servicio SMB con un share accesible denominado `pics`. De dicho share se extraen dos archivos cuyo contenido, tras el correspondiente crackeo de hashes MD5, provee las credenciales para el acceso final al sistema.

```bash
nmap -sV -sC <IP>
smbclient -L //<IP>/
smbclient //<IP>/pics
md5sum <ficheros_extraidos>
```

Respuestas de la tarea:

1. `4` (puertos abiertos)
2. `ftp`
3. `smb`
4. `pics`
5. `90d6f992585815ff991e68748c414740`
6. `4d930091c31a622a7ed10f27999af363`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | ¿Cuántos puertos hay abiertos? | `4` |
| 1.2 | Servicio expuesto (enumeración 1) | `ftp` |
| 1.3 | Servicio expuesto (enumeración 2) | `smb` |
| 1.4 | Nombre del share accesible | `pics` |
| 1.5 | Hash MD5 extraído 1 | `90d6f992585815ff991e68748c414740` |
| 1.6 | Hash MD5 extraído 2 | `4d930091c31a622a7ed10f27999af363` |

---

**Metodología:** Enumeración de servicios (nmap), acceso a FTP/SMB, extracción de archivos de un share, crackeo de hashes MD5 y uso de credenciales para acceso remoto (PTES fases de recon, exploitation y post).

**Learning chain:** Reconocimiento → fingerprint de servicios → share SMB → descarga de artefactos → crackeo de hashes → autenticación final.

**Lección:** *Los shares SMB y FTP sin proteger suelen esconder las piezas exactas — hashes, credenciales — que faltan para cerrar el compromiso.*

**MITRE ATT&CK:** T1046 Network Service Discovery · T1083 File and Directory Discovery · T1110 Brute Force · T1552.001 Unsecured Credentials (Files).

**Fuente:** [TryHackMe - Anonymous](https://tryhackme.com/room/anonymous)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.