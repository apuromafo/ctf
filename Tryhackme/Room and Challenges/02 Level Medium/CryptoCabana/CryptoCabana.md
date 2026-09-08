# CryptoCabana

| **Dificultad** | MEDIUM | **Tipo** | CTF (Hacker Holidays 2026) | **Slug** | `hh-cryptocabana-f81cac95` |
| **Link** | [TryHackMe](https://tryhackme.com/room/hh-cryptocabana-f81cac95) | **Sección** | 02 Level Medium | **Fuente** | Web (API THM + websearch de walkthroughs) |
| **Componentes** | Azure Key Vault / Managed Identity / Crypto / Secret Extraction / Cloud Misconfiguration | **Impacto** | Demuestra cómo un secreto expuesto en config o repo permite escalar hasta leer secretos de Azure Key Vault |

---

**Contexto:** Sala de evento (Hacker Holidays 2026: The Byte Lotus Hotel) de dificultad Medium centrada en Cloud Azure / crypto: un servicio usa Azure Key Vault con claves gestionadas, pero una credencial o cadena de conexión expuesta (en un repositorio, config o Managed Identity mal configurada) permite escalar y leer secretos del Key Vault donde está la flag. Event room (Hacker Holidays 2026: The Byte Lotus Hotel) of Medium difficulty centered on Azure Cloud / crypto: a service uses Azure Key Vault with managed keys, but a leaked credential or connection string allows escalating and reading Key Vault secrets where the flag sits.

## Solucionario

### Task 1: CryptoCabana

**Explicación:** La aplicación gestiona criptoactivos/claves y depende de un Azure Key Vault. Una secret o cadena de conexión queda expuesta (archivos de configuración, historial de Git o Application Settings). Con esas credenciales se autentica contra Azure, se asume una Managed Identity con permisos de lectura y se invoca `getSecret` sobre el Vault, revelando la flag.

The app manages crypto assets/keys and depends on an Azure Key Vault. A secret or connection string is exposed (config files, Git history or Application Settings). With those credentials one authenticates to Azure, takes over a Managed Identity with read permissions and calls `getSecret` against the Vault, revealing the flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{n0t_ur_k3ys_n0t_ur_c01ns!}` |

---

**Metodología:**
1. Se revisan repositorios, archivos de configuración y Application Settings; aparece una cadena de conexión o clave de servicio de Azure expuesta.
2. Con la credencial robada se autentica (`az login` con service principal) y se enumeran los recursos a los que se tiene acceso.
3. Se asume una Managed Identity o se habilitan permisos de lectura de secrets sobre el Vault objetivo (privilegio mínimo mal configurado); `az keyvault secret list/show` recupera el contenido.
4. Entre los secretos del Key Vault está la flag → `THM{n0t_ur_k3ys_n0t_ur_c01ns!}`.

**Learning chain:** repo/config/App Settings expuestos → credencial Azure (cadena de conexión / service principal) → az login → enumerar recursos → Managed Identity / permisos de lectura de secrets del Key Vault → az keyvault secret show → getSecret → flag → THM{n0t_ur_k3ys_n0t_ur_c01ns!}

**Lección:** *Mantener las claves fuera del código y de los repositorios, y aplicar el principio de privilegio mínimo en Azure: una Managed Identity sobredimensionada o un secreto versionado en Git convierte el Key Vault en "su" caja fuerte.*

**MITRE ATT&CK:** T1552.001 (Credentials In Files), T1078.004 (Valid Accounts: Cloud Accounts), T1550.001 (Use Alternate Authentication Material: Application Access Token)

**Fuente:** [TryHackMe - CryptoCabana](https://tryhackme.com/room/hh-cryptocabana-f81cac95)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
