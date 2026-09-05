# Complimentary [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** CTF (Evento "Hacker Holidays 2026: The Byte Lotus Hotel")
* **Slug:** `hh-complimentary-05e0b604`
* **Link:** https://tryhackme.com/room/hh-complimentary-05e0b604
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=hh-complimentary-05e0b604` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de Cloud AWS (target en vivo, sin descarga) del evento Hacker Holidays. Una aplicación web ofrece una cuenta "complementaria" gratuita con autenticación vía AWS Cognito. La app expone un *identity pool* que otorga credenciales temporales con permisos `GetItem` sobre una tabla DynamoDB, sin restringirlas por rol; al realizar `GetItem` directamente sobre la tabla se lee el dato protegido que contiene la flag. El fallo es un exceso de permisos/política IAM abierta más que un fallo de la app en sí.
> **EN:** AWS Cloud room (live target, no download) from the Hacker Holidays event. A web app offers a free "complimentary" account with authentication via AWS Cognito. The app exposes an *identity pool* that grants temporary credentials with `GetItem` permissions over a DynamoDB table, without restricting them by role; performing `GetItem` directly on the table reads the protected data containing the flag. The flaw is a permission excess / open IAM policy more than a failure of the app itself.

### Task 1 - Complimentary

> **ES:** El registro/identidad en Cognito no valida los atributos custom del usuario, y el *identity pool* entrega credenciales temporales que, por una política IAM mal configurada, permiten `GetItem` sobre la tabla DynamoDB sin restricción de rol. Con las credenciales obtenidas se consulta la tabla (herramienta `aws` CLI o la app) y la flag está guardada en un atributo del ítem.
> **EN:** The Cognito registration/identity does not validate custom user attributes, and the *identity pool* hands out temporary credentials that, due to a misconfigured IAM policy, allow `GetItem` over the DynamoDB table without any role restriction. With the obtained credentials the table is queried (`aws` CLI tool or the app) and the flag is stored in one attribute of the item.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag? | `THM{fr33_app_fr33_d4t4!}` |

## Metodología / Methodology

1. **Paso / Step - Registro público en Cognito:** Se accede a la app web y se crea una cuenta gratuita; el registro/identidad no valida los atributos custom del usuario.
2. **Paso / Step - Obtención de credenciales temporales:** El *identity pool* de AWS entrega credenciales temporales; por una política IAM mal configurada, estas permiten `GetItem` sobre la tabla DynamoDB sin restricción de rol.
3. **Paso / Step - Lectura de la tabla:** Con las credenciales se ejecuta `GetItem` sobre la tabla expuesta; la flag está almacenada en un atributo del ítem.

### Cadena de ataque / Attack Chain

```
registro público en Cognito -> atributos custom sin validar
  -> identity pool -> credenciales temporales (permisos DynamoDB GetItem sin restricción de rol)
  -> DynamoDB GetItem sobre la tabla expuesta
  -> atributo del ítem -> THM{fr33_app_fr33_d4t4!}
```

**Lección:** Los identity pools de AWS con permisos abiertos en DynamoDB exponen datos; aplica privilegio mínimo de IAM.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
