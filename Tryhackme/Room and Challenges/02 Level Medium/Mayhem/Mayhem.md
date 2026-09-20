# Mayhem

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / C2 crypto | mayhem | https://tryhackme.com/room/mayhem | 02 Level Medium | TryHackMe | Havoc C2, descifrado de tráfico, Windows, credenciales | Compromiso total (descifrado C2 + robo de archivos del usuario) |

---

**Contexto:** La sala **Mayhem** es un CTF centrado en el framework de C2 **Havoc**. El jugador inspecciona el tráfico cifrado del C2, recupera identidades de la víctima (SID y dirección IPv6), descifra los paquetes intercambiados, extrae credenciales filtradas y localiza el archivo robado por el atacante en la máquina, capturando las flags a lo largo del proceso.

## Solucionario

### Task 1: Capturar las flags
**Explicación:**

Se examina el entorno comprometido: se identifican el **SID** de la víctima `S-1-5-21-679395392-3966376528-1349639417-1103` y su **dirección IPv6** de enlace local `fe80::e134:1b0c:c8d5:3020%6`. Analizando el tráfico cifrado de **Havoc C2** se consigue descifrarlo y se obtiene la primera flag `THM{HavOc_C2_DeCRypTing_is_Fun_Fun_FUN}`. Entre los datos recuperados aparecen las **credenciales** `administrato:WfD3hz3AXZ4n` y el archivo de interés `C:\Users\paco\Desktop\Files\clients.csv`; al verificar el archivo robado se consigue la segunda flag `THM{I_Can_SEE_ThE_fiL3_YoU_ToOk}`.

1. `S-1-5-21-679395392-3966376528-1349639417-1103`
2. `fe80::e134:1b0c:c8d5:3020%6`
3. `THM{HavOc_C2_DeCRypTing_is_Fun_Fun_FUN}`
4. `administrato:WfD3hz3AXZ4n`
5. `C:\Users\paco\Desktop\Files\clients.csv`
6. `THM{I_Can_SEE_ThE_fiL3_YoU_ToOk}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | SID de la víctima | `S-1-5-21-679395392-3966376528-1349639417-1103` |
| 2 | Dirección IPv6 de enlace local | `fe80::e134:1b0c:c8d5:3020%6` |
| 3 | Flag del descifrado del C2 | `THM{HavOc_C2_DeCRypTing_is_Fun_Fun_FUN}` |
| 4 | Credenciales recuperadas del tráfico | `administrato:WfD3hz3AXZ4n` |
| 5 | Archivo de la víctima comprometido | `C:\Users\paco\Desktop\Files\clients.csv` |
| 6 | Flag del archivo robado | `THM{I_Can_SEE_ThE_fiL3_YoU_ToOk}` |

---

**Metodología:** Recolección de pcap de C2 → identificación de SID/NDR e IPv6 → descifrado del protocolo de Havoc → extracción de credenciales y archivos → verificación del exfiltrado.

**Learning chain:** Captura de tráfico C2 → identidades (SID, IPv6) → crypto del C2 → credenciales → localización del archivo robado → flags.

**Lección:** *El tráfico de un C2 bien cifrado sigue siendo analizable cuando conoces el formato de los paquetes; las credenciales y los archivos exfiltrados dejan huellas que recuperan la cadena completa.*

**MITRE ATT&CK:** T1041 Exfiltration Over C2 Channel · T1552 Unsecured Credentials.

**Fuente:** [TryHackMe - Mayhem](https://tryhackme.com/room/mayhem)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.