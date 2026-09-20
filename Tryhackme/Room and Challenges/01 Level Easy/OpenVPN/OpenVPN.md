# OpenVPN

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `openvpn` | [TryHackMe](https://tryhackme.com/room/openvpn) | `01 Level Easy` | THM | OpenVPN, configuración VPN, conexión | Conexión a la red de TryHackMe |

> **Objeto:** Aprender a instalar y utilizar OpenVPN para conectarse a la red de TryHackMe, cargando el fichero de configuración de la sala y verificando el túnel con la bandera de conexión.

---

**Contexto:** Sala de configuración de red: se instala OpenVPN, se descargan los ficheros de configuración del usuario, se establece el túnel hacia la red de TryHackMe y se valida la conexión obteniendo la bandera `flag{connection_verified}`.

> **ES:** Sala de configuración de red: se instala OpenVPN, se descargan los ficheros de configuración del usuario, se establece el túnel hacia la red de TryHackMe y se valida la conexión obteniendo la bandera `flag{connection_verified}`.

> **EN:** Network setup room: OpenVPN is installed, the user's configuration files are downloaded, the tunnel to the TryHackMe network is established and the connection is validated by obtaining the flag `flag{connection_verified}`.

## Solucionario

### Task 1: OpenVPN / OpenVPN

**Explicación:** La tarea guía la conexión VPN completa. El contenido original, conservado íntegramente, es el siguiente:

1. No answer needed
2. No answer needed
3. No answer needed
4. No answer needed
5. No answer needed
6. flag{connection_verified}

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | No answer needed (paso 1) | `No answer needed` |
| 2 | No answer needed (paso 2) | `No answer needed` |
| 3 | No answer needed (paso 3) | `No answer needed` |
| 4 | No answer needed (paso 4) | `No answer needed` |
| 5 | No answer needed (paso 5) | `No answer needed` |
| 6 | ¿Qué flag se obtiene al conectarse a la red de TryHackMe con OpenVPN? | `flag{connection_verified}` |

---

**Metodología:** 1) Instalar OpenVPN con los paquetes necesarios. 2) Descargar el fichero de configuración de la sala y de la VPN del usuario. 3) Establecer la conexión VPN con los privilegios requeridos. 4) Verificar el túnel y obtener la bandera `flag{connection_verified}`.

### Cadena de ataque / Attack Chain

1. Instalación de los paquetes de OpenVPN.
2. Obtención del fichero de configuración de la VPN.
3. Conexión a la red de TryHackMe mediante el túnel.
4. Verificación de la conectividad → `flag{connection_verified}`.

**Learning chain:** instalación de OpenVPN → fichero de configuración → túnel VPN → verificación de conexión → flag

**Lección:** *Establecer el túnel VPN es el primer paso operativo en las plataformas de laboratorio; verificar la conexión mediante una bandera confirma que el tráfico circula correctamente por la red aislada.*

**MITRE ATT&CK:** T1046 - Network Service Discovery, T1071.001 - Application Layer Protocol: Web Protocols

**Fuente:** [TryHackMe - OpenVPN](https://tryhackme.com/room/openvpn)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.