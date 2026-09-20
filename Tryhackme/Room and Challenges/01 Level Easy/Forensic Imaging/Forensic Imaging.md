# Forensic Imaging

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | forensics / walkthrough | `forensicimaging` | https://tryhackme.com/room/forensicimaging | 01 Level Easy | TryHackMe | dd / dc3dd / md5sum / lsblk / history / mount / adquisición forense | Defensivo: crear una imagen forense de una unidad USB, verificar su integridad con hashes y montarla para extraer la evidencia. |

---

> **Objeto:** Realizar una adquisición forense de un dispositivo USB siguiendo el procedimiento documentado: identificar la unidad (`lsblk`), revisar qué comandos usó el investigador anteriormente (`history`), crear la imagen con `dd`/`dc3dd`, comprobar su integridad con `md5sum` y montarla en `/mnt` para recuperar las flags enterradas en la evidencia.

**Contexto:** Sala introductoria de forense digital (by NES). Un investigador interrumpió su análisis de una memoria USB de un caso: el sistema ya tiene el dispositivo conectado y el flujo de trabajo previsto en los apuntes. La tarea es reproducir cada paso usando las herramientas de línea de comandos de Linux: ver los dispositivos dispones con `lsblk`, consultar `~/.bash_history` para conocer los comandos ya utilizados (tar/dc3dd), verificar el hash del firmware/imagen (`md5sum`), montar la imagen creada y leer los archivos de flag. Se repite el proceso con una segunda imagen usando `dc3dd`.

> **ES:** "Forensic Imaging" — adquisición forense de un USB con `dd`/`dc3dd`, verificación con `md5sum` y montaje para extraer evidencia.
> **EN:** An intro forensic room that walks through imaging a USB with `dd`/`dc3dd`, integrity verification via `md5sum`, and mounting the image to recover the flags.

## Solucionario

### Task 1: Despliegue / Deployment

**Explicación:** Se pone en marcha la máquina virtual del laboratorio. No hay pregunta que responder.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Deploy and start the machine. / Despliega la máquina. | `No answer needed` |

### Task 2: Identificación de la unidad / Identifying the Device

**Explicación:** Para saber qué dispositivo físico es la memoria USB se enumeran los discos y particiones con `lsblk`. Para conocer qué ha hecho el investigador anterior se lee el historial de comandos de su sesión con `history` (o `cat ~/.bash_history`), donde está documentado el procedimiento de creación de la imagen.

```bash
lsblk                     # listar los dispositivos y sus particiones
history                   # comandos previos de la sesión del investigador
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2.1 | ¿Qué comando usarías para localizar el dispositivo? / What command would you use to locate the device? | `lsblk` |
| 2.2 | ¿Qué comando usarías para revisar los comandos usados previamente? / What command would you use to review previously used commands? | `history` |

### Task 3: Preparación del entorno / Environment Preparation

**Explicación:** Paso intermedio del flujo para montar/desmontar la evidencia y preparar el directorio de trabajo conforme al procedure del caso. No requiere texto de respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 3 | Follow the procedure. / Sigue el procedimiento. | `No answer needed` |

### Task 4: Registro del hash de la imagen / Image Hash Verification

**Explicación:** Tras crear la imagen del dispositivo (p. ej. con `dd if=/dev/sdb of=/tmp/disk.dd bs=...` según los apuntes), se comprueba la integridad calculando su hash con `md5sum`. El valor obtenido debe coincidir con el hash documentado en el caso, confirmando que la adquisición es íntegra.

```bash
md5sum /tmp/diskusb.img | tee hash.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 4 | ¿Qué hash has obtenido al verificar la imagen? / What is the hash you verified? | `1f1da616156f73083521478c334841bb` |

### Task 5: Montaje de la imagen / Mounting the Image

**Explicación:** La imagen es una partición ext4; se monta en `/mnt` con `mount` y se lista su contenido. Al inspeccionar la evidencia aparece el primer archivo de flag.

```bash
sudo mount -o loop /tmp/diskusb.img /mnt && ls /mnt
cat /mnt/flag.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 5 | ¿Cuál es la primera flag? / What is the first flag? | `THM{mounttt-mounttt-me}` |

### Task 6: Segunda imagen con dc3dd / Second Image with dc3dd

**Explicación:** Para la segunda unidad se repite el procedimiento con `dc3dd`, la herramienta de adquisición forense (que además de copiar verifica los hashes). Se obtiene el hash `1fab86e499934dda789c9c4aaf27101d` y, tras montar la nueva imagen, se recupera la flag final.

```bash
dc3dd if=/dev/sdc of=/tmp/second.dd hash=md5 log=evidence.log
sudo mount -o loop /tmp/second.dd /mnt && cat /mnt/flag.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 6.1 | ¿Qué hash obtienes al crear la imagen con dc3dd? | `1fab86e499934dda789c9c4aaf27101d` |
| 6.2 | ¿Cuál es la segunda flag? / What is the second flag? | `THM{well-done-imaginggggggg}` |

### Task 7: Conclusión / Conclusion

**Explicación:** Se cierra la investigación con la adquisición y verificación íntegra de ambas imágenes forenses. No hay respuesta que escribir.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 7 | Complete the room. / Completa la sala. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Deploy and start the machine. | `No answer needed` |
| 2.1 | What command would you use to locate the device? | `lsblk` |
| 2.2 | What command would you use to review previously used commands? | `history` |
| 3 | Follow the procedure. | `No answer needed` |
| 4 | What is the hash you verified? | `1f1da616156f73083521478c334841bb` |
| 5 | What is the first flag? | `THM{mounttt-mounttt-me}` |
| 6.1 | What hash do you get creating the image with dc3dd? | `1fab86e499934dda789c9c4aaf27101d` |
| 6.2 | What is the second flag? | `THM{well-done-imaginggggggg}` |
| 7 | Complete the room. | `No answer needed` |

---

**Metodología:** Enumerar el dispositivo y repasar el historial del caso. Crear la imagen con `dd`/`dc3dd` usando el dispositivo detectado con `lsblk`. Verificar la integridad con `md5sum` (coincide con el hash documentado). Montar la imagen con `mount -o loop` en `/mnt` y extraer la flag. Repetir el ciclo completo para la segunda imagen con `dc3dd` (hash + verificación de log).

### Cadena de ataque / Attack Chain

```text
lsblk -> history -> dd/dc3dd (imagen del USB) -> md5sum (hash íntegro) -> mount -o loop -> leer flag -> segunda imagen con dc3dd -> flag final
```

**Learning chain:** forensic imaging -> dd/dc3dd -> lsblk/history -> md5sum -> mount -o loop -> evidence extraction.

**Lección:** *En forense digital, la integridad es lo primero: se documenta el dispositivo con `lsblk`, se adquiere con `dd`/`dc3dd` y se verifica con hashes (`md5sum`) antes de montar la imagen para el análisis.*

**MITRE ATT&CK:** N/A (metodología forense / adquisición de evidencia)

**Fuente:** [TryHackMe - Forensic Imaging](https://tryhackme.com/room/forensicimaging)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.