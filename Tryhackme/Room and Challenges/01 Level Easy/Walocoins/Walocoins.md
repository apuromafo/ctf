# Walocoins

| **Dificultad** | Easy |
| **Tipo** | Sala teórica (criptomonedas) |
| **Slug** | `walocoins` |
| **Link** | [TryHackMe](https://tryhackme.com/room/walocoins) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Blockchain / nodos / billeteras / mineros / bitcoin / legacy vs bech32 / scrypt / RPC / CPU mining |
| **Impacto** | Sala creada por clarksoft para repasar conceptos de criptomonedas (WaloCoin/WLC, creado por n3v1l): componentes de la blockchain, despliegue de un nodo en Ubuntu, billeteras y archivos de configuración, operaciones de consola (getaddressinfo, getwalletinfo, importprivkey, sendtoaddress), el minero sobre scrypt y el ecosistema de la moneda. |

---

**Contexto:** WaloCoin (WLC) es una criptomoneda educativa para aprender el ecosistema cripto sin riesgo de dinero real. Para mantenerse viva necesita tres componentes: **nodos, billeteras y mineros**. El nodo se despliega en Ubuntu 18.04 usando el PPA de Bitcoin y el archivo de configuración `~/.walocoin/walocoin.conf`; la billetera (siendo los archivos críticos `walocoin.conf` y `wallet.dat`) soporta direcciones Legacy (empiezan con `W`) y Bech32 (empiezan con `wlc`), gestionadas con `getaddressinfo`/`getwalletinfo`, e importables con `importprivkey`. El minero usa el algoritmo scrypt vía CPU, con puerto RPC por defecto `9772`, usuario `minero` y el parámetro `-t` para indicar los núcleos. La sala se resuelve con el apoyo del video explicativo de n3v1l ([YouTube nAMYHdqDCc0](https://www.youtube.com/watch?v=nAMYHdqDCc0)).

## Solucionario

### Task 1: Introducción

**Explicación:** Se explica qué es WaloCoin: criptomoneda educativa de la comunidad de hacking (L4t1nHTB, HackSpace, etc.) para aprender blockchain sin fines económicos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | He leído lo anterior y me queda claro que por el momento los WLC son sólo una criptomoneda de aprendizaje. | `No answer needed` |

### Task 2: Componentes de la Blockchain

**Explicación:** Todo el ecosistema de una criptomoneda se sustenta en tres pilares que deben coexistir para mantenerse viva.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué tres componentes deben existir para que una criptomoneda se mantenga viva? | `nodos billeteras mineros` |

### Task 3: El Nodo

**Explicación:** Los nodos son réplicas distribuidas de la blockchain. Se instalan en Ubuntu 18.04 usando el PPA de Bitcoin, la configuración va en `~/.walocoin/walocoin.conf` y el servicio se gestiona con `systemctl` (binario `walocoind`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | He seguido las instrucciones para instalar un nodo. | `No answer needed` |

### Task 4: Billetera

**Explicación:** Instalación de la billetera en Windows y archivos críticos: `walocoin.conf` (configuración de conexión) y `wallet.dat` (la billetera personalizada).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama el archivo que contiene la configuración de conexión? | `walocoin.conf` |
| 2 | ¿Cómo se llama el archivo que contiene nuestra billetera personalizada? | `wallet.dat` |

### Task 5: Operaciones dentro de la Billetera

**Explicación:** La consola de la billetera gestiona direcciones Legacy (empiezan con `W`) y Bech32 (empiezan con `wlc`). Comandos clave: `getaddressinfo` (info de una dirección), `getwalletinfo` (info de la billetera), `importprivkey` (importar una llave privada) y `help sendtoaddress` (ver los argumentos para enviar). Se puede enviar WLC desde la consola.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Ya lograste ver tu dirección de billetera walocoin? | `No answer needed` |
| 2 | ¿Con qué letra comienza tu dirección LEGACY? | `W` |
| 3 | ¿De qué tipo es la dirección que puedes compartir con tus contactos? | `bech32` |
| 4 | ¿Con qué comando en la consola puedes ver la información de una dirección? | `getaddressinfo` |
| 5 | ¿Con cuál comando obtengo información de mi wallet? | `getwalletinfo` |
| 6 | ¿Con cuál comando importaría a una billetera dada una llave privada? | `importprivkey` |
| 7 | ¿Es posible enviar WLC desde la consola? | `Si` |
| 8 | ¿Cómo puedo saber el orden de los argumentos para enviar WLC desde la consola? | `help sendtoaddress` |

### Task 6: Minero de Criptomoneda

**Explicación:** Configuración del minado por CPU con el algoritmo Scrypt, puerto RPC por defecto `9772`, usuario por defecto `minero` y parámetro `-t` para los núcleos. El minado vía tarjeta gráfica no está habilitado.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Puerto por omisión de RPC para nodos en nuestro script? | `9772` |
| 2 | ¿Está habilitado el minado de WLC vía tarjeta gráfica? | `No` |
| 3 | ¿Cuál es el usuario para conectarse al nodo principal? | `minero` |
| 4 | ¿Con qué tres primeras letras comienza tu dirección bech32? | `wlc` |
| 5 | ¿Puedes descubrir qué algoritmo se usa en el minado? | `scrypt` |
| 6 | ¿Qué parámetro del minado indicaría la cantidad de núcleos a usar? | `-t` |

### Task 7: Final

**Explicación:** Cierre de la sala: compartir WLC, practicar el minado y revisar el explorador de bloques `https://blockexplorer.walocoin.xyz` para seguir aprendiendo la tecnología subyacente.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | He finalizado. | `No answer needed` |

---

**Metodología:** Lectura de los conceptos de blockchain/Autres → instalación del nodo (PPA Bitcoin) → instalación y configuración de la billetera → operaciones de consola (direcciones Legacy/Bech32) → configuración del minero scrypt → verificación del ecosistema en el block explorer.
**Learning chain:** componentes de la blockchain → nodos → billetera y sus archivos → direcciones y comandos RPC → minería por CPU con scrypt → cierre.
**MITRE ATT&CK:** T1046 (Network Service Discovery), T1059 (Command and Scripting Interpreter), T1204 (User Execution)
**Fuente:** [TryHackMe - Walocoins](https://tryhackme.com/room/walocoins)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
