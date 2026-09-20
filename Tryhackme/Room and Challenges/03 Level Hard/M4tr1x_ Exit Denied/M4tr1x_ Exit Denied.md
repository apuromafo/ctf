# M4tr1x_ Exit Denied

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | CTF | m4tr1xexitdenied | https://tryhackme.com/room/m4tr1xexitdenied | 03 Level Hard | TryHackMe | Web, LFI/RFI, GPG, SSH-TOTP, Docker | Alto |

---

**Contexto:**
> **ES:** Reto de nivel Hard inspirado en la película Matrix: explotación web (panel de reporte `/reportPanel.php`), manipulación de módulos (`modManagerv2`), manejo de archivos GPG (`p.txt.gpg`), autenticación SSH-TOTP y obtención de múltiples banderas a lo largo de la cadena de compromiso.
> **EN:** Hard-level challenge inspired by the movie Matrix: web exploitation (report panel `/reportPanel.php`), module handling (`modManagerv2`), GPG file handling (`p.txt.gpg`), SSH-TOTP authentication and multiple flags along the compromise chain.

## Solucionario

### Task 1: Tarea 1
**Explicación:**
1. 1. No answer needed
   2. /reportPanel.php
   3. No answer needed
   4. modManagerv2
   5. p.txt.gpg
   6. /0100101101100101011110010110110101100001011010110110010101110010
   7. No answer needed
   8. G9KY2siJp9OOymdCiQclQn9UhxL6rSpoA3MXHCDgvHCcrCOOuT
   9. SSH-TOTP
   10. No answer needed
   11. fL4g{Ia]\/[bEGYngn1nGT0bel13v3} 
   12. Flag{R3ALw0r1D4507Ez09WExit}
   13. 718008
   14. fL4g{|amFre3N0w}

### Preguntas y Respuestas / Questions and Answers

| Task | Respuesta / Answer |
|---|---|
| 1.1 | `No answer needed` |
| 1.2 | `/reportPanel.php` |
| 1.3 | `No answer needed` |
| 1.4 | `modManagerv2` |
| 1.5 | `p.txt.gpg` |
| 1.6 | `/0100101101100101011110010110110101100001011010110110010101110010` |
| 1.7 | `No answer needed` |
| 1.8 | `G9KY2siJp9OOymdCiQclQn9UhxL6rSpoA3MXHCDgvHCcrCOOuT` |
| 1.9 | `SSH-TOTP` |
| 1.10 | `No answer needed` |
| 1.11 | `fL4g{Ia]\/[bEGYngn1nGT0bel13v3} ` |
| 1.12 | `Flag{R3ALw0r1D4507Ez09WExit}` |
| 1.13 | `718008` |
| 1.14 | `fL4g{|amFre3N0w}` |

---

**Metodología:**
1. Explotación del panel de reporte (`/reportPanel.php`) y del gestor de módulos (`modManagerv2`).
2. Manejo del archivo GPG (`p.txt.gpg`) y de la clave codificada en binario (`/01001011...`).
3. Autenticación vía SSH-TOTP y posterior escalada dentro del entorno.
4. Extracción de las distintas banderas (`fL4g{...}` y `Flag{...}`).

### Cadena de ataque / Attack Chain
1. Reconocimiento web del panel de reporte.
2. Explotación del gestor de módulos.
3. Descifrado/manipulación del archivo GPG y datos binarios.
4. Autenticación SSH-TOTP.
5. Escalada y extracción de banderas.

**Learning chain:** Web (`/reportPanel.php`) -> `modManagerv2` -> GPG -> SSH-TOTP -> Banderas.

**Lección:** *Encadenar entradas web, cifrado y autenticación multifactor expone superficies que por separado parecen seguras.*

**MITRE ATT&CK:**
- T1190 (Exploit Public-Facing Application)
- T1203 (Exploitation for Client Execution)
- T1021.004 (Remote Services: SSH)
- T1556 (Modify Authentication Process)

**Fuente:** [TryHackMe - M4tr1x_ Exit Denied](https://tryhackme.com/room/m4tr1xexitdenied)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.