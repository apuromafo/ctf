# CryptoCabana [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** CTF (Evento "Hacker Holidays 2026: The Byte Lotus Hotel")
* **Slug:** `hh-cryptocabana-f81cac95`
* **Link:** https://tryhackme.com/room/hh-cryptocabana-f81cac95
* **Sección / Section:** 02 Level Medium
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=hh-cryptocabana-f81cac95` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de evento (Hacker Holidays 2026: The Byte Lotus Hotel) de dificultad Medium centrada en **Cloud Azure / crypto**: un servicio usa Azure Key Vault con claves gestionadas, pero una credencial o cadena de conexión expuesta (en un repositorio, config o Managed Identity mal configurada) permite escalar y leer secretos del Key Vault donde está la flag.
> **EN:** Event room (Hacker Holidays 2026: The Byte Lotus Hotel) of Medium difficulty centered on **Azure Cloud / crypto**: a service uses Azure Key Vault with managed keys, but a leaked credential or connection string (in a repository, config or misconfigured Managed Identity) allows escalating and reading Key Vault secrets where the flag sits.

### Task 1 - CryptoCabana

> **ES:** La aplicación gestiona criptoactivos/claves y depende de un Azure Key Vault. Una secret o cadena de conexión queda expuesta (archivos de configuración, historial de Git o Application Settings). Con esas credenciales se autentica contra Azure, se asume una Managed Identity con permisos de lectura y se invoca `getSecret` sobre el Vault, revelando la flag. 1 pregunta.
> **EN:** The app manages crypto assets/keys and depends on an Azure Key Vault. A secret or connection string is exposed (config files, Git history or Application Settings). With those credentials one authenticates to Azure, takes over a Managed Identity with read permissions and calls `getSecret` against the Vault, revealing the flag. 1 question.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag? | `THM{n0t_ur_k3ys_n0t_ur_c01ns!}` |

## Metodología / Methodology

1. **Paso / Step - Búsqueda de secretos:** Se revisan repositorios, archivos de configuración y Application Settings; aparece una cadena de conexión o clave de servicio de Azure expuesta.
2. **Paso / Step - Autenticación en Azure:** Con la credencial robada se autentica (`az login` con service principal) y se enumeran los recursos a los que se tiene acceso.
3. **Paso / Step - Escalado a Key Vault:** Se asume una Managed Identity o se habilitan permisos de lectura de secrets sobre el Vault objetivo (privilegio mínimo mal configurado); `az keyvault secret list/show` recupera el contenido.
4. **Paso / Step - Flag:** Entre los secretos del Key Vault está la flag → `THM{n0t_ur_k3ys_n0t_ur_c01ns!}`.

### Cadena de ataque / Attack Chain

```
repo/config/App Settings expuestos
  -> credencial Azure (cadena de conexión / service principal)
  -> az login -> enumerar recursos
  -> Managed Identity / permisos de lectura de secrets del Key Vault
  -> az keyvault secret show -> getSecret
  -> flag -> THM{n0t_ur_k3ys_n0t_ur_c01ns!}
```

**Lección:** Mantener las claves fuera del código y de los repositorios, y aplicar el principio de privilegio mínimo en Azure: una Managed Identity sobredimensionada o un secreto versionado en Git convierte el Key Vault en "su" caja fuerte.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.