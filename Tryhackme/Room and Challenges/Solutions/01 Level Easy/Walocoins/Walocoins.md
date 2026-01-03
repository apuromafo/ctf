#   WaloCoins

> Sala para el repaso de conceptos de criptomonedas enseñados por **n3v1l** 🇨🇱.

---

**Room Link:** [https://tryhackme.com/jr/walocoins](https://tryhackme.com/jr/walocoins)

<div align="center">
  <img src="https://tryhackme-images.s3.amazonaws.com/room-icons/f457b38f7aebf742a58e88e821e8ace3.png" width="250" alt="walocoins">
</div>

### 📊 Información de la Sala
* **Creador:** clarksoft
* **Fecha de creación:** Hace ~5 años (2020)
* **Estado:** Sala privada y gratuita.
* **Recurso de apoyo:** [Video explicativo en YouTube](https://www.youtube.com/watch?v=nAMYHdqDCc0)

---

> **Nota de Pwn:** Al ser una sala de 2020 sobre cripto-conceptos, asegúrate de revisar bien los scripts o servicios locales que manejen carteras (wallets) o transacciones. Los vectores suelen estar en la lógica de procesamiento de la "moneda".

# 🪙 Solucionario: WaloCoin (TryHackMe)

Guía completa de instalación, configuración y respuestas para la sala de WaloCoin.

---

## Tarea 1: Introducción

**Descripción:** WaloCoin es una criptomoneda educativa creada por **n3v1l** para comunidades de ciberseguridad (L4t1nHTB, HackSpace, etc.), diseñada para aprender sobre el ecosistema cripto sin riesgo real de dinero.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | He leído lo anterior y me queda claro que por el momento los WLC son sólo una criptomoneda de aprendizaje | `No answer needed` |

---

## Tarea 2: Componentes de la Blockchain

**Descripción:** Para que el ecosistema se mantenga vivo, requiere de tres pilares fundamentales.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | ¿Qué tres componentes deben existir para que una criptomoneda se mantenga viva? | `nodos billeteras mineros` |

---

## Tarea 3: El Nodo

**Descripción:** Instrucciones para desplegar un nodo en Ubuntu 18.04. Los nodos son réplicas distribuidas de la blockchain.

**Puntos clave de instalación:**

* **Repositorio:** Se utiliza el PPA de Bitcoin.
* **Configuración:** El archivo se ubica en `~/.walocoin/walocoin.conf`.
* **Servicio:** Se gestiona mediante `systemctl` con el binario `walocoind`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | He seguido las instrucciones para instalar un nodo | `No answer needed` |

---

## Tarea 4: Billetera

**Descripción:** Instalación de la billetera en Windows y archivos críticos de configuración.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | ¿Cómo se llama el archivo que contiene la configuración de conexión? | `walocoin.conf` |
| 2 | ¿Cómo se llama el archivo que contiene nuestra billetera personalizada? | `wallet.dat` |

---

## Tarea 5: Operaciones dentro de la Billetera

**Descripción:** Gestión de direcciones y comandos de consola. Se distinguen dos tipos de direcciones: **Legacy** (empiezan con `W`) y **Bech32** (empiezan con `wlc`).

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | ¿Ya lograste ver tu dirección de billetera walocoin? | `No answer needed` |
| 2 | ¿Con qué letra comienza tu dirección LEGACY? | `W` |
| 3 | ¿De qué tipo es la dirección que puedes compartir con tus contactos? | `bech32` |
| 4 | ¿Con qué comando en la consola puedes ver la información de una dirección? | `getaddressinfo` |
| 5 | ¿Con cuál comando obtengo información de mi wallet? | `getwalletinfo` |
| 6 | ¿Con cuál comando importaría a una billetera dada una llave privada? | `importprivkey` |
| 7 | ¿Es posible enviar WLC desde la consola? | `Si` |
| 8 | ¿Cómo puedo saber el orden de los argumentos para enviar WLC desde la consola? | `help sendtoaddress` |

---

## Tarea 6: Minero de Criptomoneda

**Descripción:** Configuración del minado por CPU utilizando el algoritmo Scrypt.

**Parámetros necesarios para el minero:**

* **Algoritmo:** `scrypt`
* **Puerto RPC por defecto:** `9772`
* **Usuario:** `minero` (por defecto en el script)

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Puerto por omisión de RPC para nodos en nuestro script? | `9772` |
| 2 | El minado de WLC vía tarjeta gráfica está habilitado? | `No` |
| 3 | ¿Cuál es el usuario para conectarse al nodo principal? | `minero` |
| 4 | ¿Con qué tres primeras letras comienza tu dirección bech32? | `wlc` |
| 5 | ¿Puedes descubrir qué algoritmo se usa en el minado? | `scrypt` |
| 6 | ¿Qué parámetro del minado indicaría la cantidad de núcleos a usar? | `-t` |

-- 

Aquí tienes la transformación del **Task 7**, que sirve como cierre de la sala:

---

## Tarea 7: Final

**Descripción:** ¡Felicitaciones! Has terminado la introducción a Walocoin. El objetivo es que ahora compartas tus WLC, practiques el minado y te familiarices con los conceptos de blockchain sin riesgo financiero.

**Recursos adicionales:**

* **Explorador de bloques:** Puedes auditar todas las transacciones de la red en tiempo real, similar a cómo se hace con Bitcoin, en: [https://blockexplorer.walocoin.xyz](https://blockexplorer.walocoin.xyz)
* **Profundización:** La sala recomienda revisar videos adicionales para entender mejor la tecnología subyacente.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | He finalizado | `No answer needed` |

---
 