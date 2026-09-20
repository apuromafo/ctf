# PassCode

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | challenge | `passcode` | https://tryhackme.com/room/passcode | 01 Level Easy | TryHackMe | Web3, smart contracts, blockchain (DarkInject), RPC, interacción con contratos | Explotación de un contrato inteligente para extraer la flag alojada en su almacenamiento/estado |

---

**Contexto:** PassCode es un reto de ciberseguridad blockchain (formato Hackfinity / web3) publicado en TryHackMe. El desafío plantea un contrato inteligente desplegado sobre la red/framework DarkInject y pide a la persona jugadora extraer la flag interactuando con el contrato, sus funciones y su almacenamiento interno.

> **ES:** Enfréntate al reto web3: interactúa con el contrato inteligente PassCode desplegado en la blockchain del reto a través de un proveedor RPC, analiza las funciones y el storage del contrato y obtén la flag que guarda.
> **EN:** Face the web3 challenge: interact with the PassCode smart contract deployed on the challenge blockchain through an RPC provider, analyze the contract functions and storage, and retrieve the flag it holds.

## Solucionario

### Task 1: Flag

**Explicación:** El reto consiste en recuperar la flag almacenada en el contrato inteligente del desafío. El flujo típico es: conectar al proveedor RPC de DarkInject (la blockchain del reto), cargar el bytecode/ABI del contrato y llamar a sus funciones tal y como se documenta en el enunciado, empleando la clave privada que se entrega como parte del primer split. Según el planteamiento proporcionado, la clave privada aparece en el primer split y el reto se resuelve al inspeccionar el estado del contrato, donde queda la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Explota el contrato para conseguir la flag / Exploit the contract to retrieve the flag | `THM{web3_h4ck1ng_code}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Explota el contrato para conseguir la flag / Exploit the contract to retrieve the flag | `THM{web3_h4ck1ng_code}` |

---

**Metodología:** Análisis de un contrato inteligente desplegado en una blockchain de laboratorio (DarkInject): conexión al nodo mediante RPC, inspección de las funciones públicas del contrato, uso de la clave privada proporcionada para interactuar con él y lectura de la flag almacenada en su estado/storage.

### Cadena de ataque / Attack Chain

```text
RPC -> DarkInject (blockchain del reto) -> contrato PassCode -> funciones/storage -> flag
```

**Learning chain:** web3 basics → smart contract interaction → RPC providers → contract storage → flag extraction

**Lección:** *En el mundo blockchain, "seguridad por oscuridad" no existe: todas las funciones y todo el storage de un contrato son de dominio público, así que cualquier secreto que un contrato almacene es, por definición, recuperable.*

**MITRE ATT&CK:** N/A (web3/smart contract challenge)

**Fuente:** [TryHackMe - PassCode](https://tryhackme.com/room/passcode)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.