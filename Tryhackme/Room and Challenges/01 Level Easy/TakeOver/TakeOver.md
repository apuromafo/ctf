# TakeOver

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | CTF / Web challenge | `takeover` | https://tryhackme.com/room/takeover | 01 Level Easy | TryHackMe | subdomain takeover / /etc/hosts / ffuf / virtual hosts / certificados SAN / S3 bucket / DNS | Captura de la flag mediante la enumeración de subdominios vía virtual hosts y certificados (SAN), accediendo a un dominio mal configurado que apunta a un bucket S3 inexistente y leyendo la flag de la respuesta. |

---

**Contexto:** Reto web fácil sobre subdomain takeover. La empresa "FutureVera" está reconstruyendo su soporte, lo que da una pista sobre el subdominio `support.futurevera.thm`. La máquina se añade a `/etc/hosts` y, tras fuzzing de Host headers con ffuf, se descubren los subdominios `blog.futurevera.thm` y `support.futurevera.thm`. El certificado SSL de `support` tiene un error que solo deja entrar con Firefox; al inspeccionar el certificado se revela un dominio oculto en el campo Subject Alternative Name (SAN). Al añadir ese dominio secreto a `/etc/hosts` y acceder, el servidor redirige a un bucket S3 no encontrado donde la flag aparece en la URL.

> **ES:** Reto de subdomain takeover: se enumeran subdominios con ffuf (vhost), se inspecciona el certificado de `support.futurevera.thm` con Firefox para descubrir un dominio SAN secreto, se añade a `/etc/hosts`, se accede y la redirección a S3 devuelve la flag en la URL.
> **EN:** Subdomain takeover challenge: enumerate subdomains with ffuf (vhost), inspect the `support.futurevera.thm` certificate in Firefox to discover a hidden SAN domain, add it to `/etc/hosts`, access it, and the S3 redirect reveals the flag in the URL.

## Solucionario

### Task 1: Obtén la bandera / Get the flag

**Explicación:** La ruta hacia la flag combina reconocimiento de subdominios, análisis de certificados y explotación de un bucket S3 mal configurado. Se descubren `blog.futurevera.thm` y `support.futurevera.thm` con ffuf; el certificado de `support` expone un dominio oculto en el campo SAN que al añadirse a `/etc/hosts` redirige a S3, donde `flag{...}` aparece como parte del nombre del bucket en la URL de redirección.

```text
1. flag{beea0d6edfcee06a59b83fb50ae81b2f}
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Cuál es la flag? / What is the flag? | `flag{beea0d6edfcee06a59b83fb50ae81b2f}` |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Cuál es la flag? / What is the flag? | `flag{beea0d6edfcee06a59b83fb50ae81b2f}` |

---

**Metodología:** Añadir `futurevera.thm` a /etc/hosts -> ffuf con Host header fuzzing para descubrir `blog` y `support` -> acceder a `support.futurevera.thm` con Firefox (error SSL que solo Firefox acepta) -> inspeccionar el certificado -> campo SAN revela un dominio oculto -> añadir ese dominio a /etc/hosts -> acceder a él -> bucket S3 configurado pero inexistente -> redirección S3 con la flag en la URL -> flag.

### Cadena de ataque / Attack Chain

```text
ffuf / Host header fuzzing -> blog.futurevera.thm + support.futurevera.thm -> Firefox (bypass SSL) -> SAN field en certificado -> dominio secreto -> /etc/hosts -> S3 redirect -> flag{...}.s3-website-us-west-3.amazonaws.com
```

**Learning chain:** Virtual host enumeration -> certificado/SAN -> subdomain takeover -> bucket S3 mal configurado -> flag.

**Lección:** *Los campos SAN de los certificados SSL revelan subdominios ocultos, y un bucket S3 apuntado por un subdominio no reservado es una puerta abierta a subdomain takeover: la flag queda expuesta en la propia URL de redirección.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1584.001 (Compromise Infrastructure: Domains).

**Fuente:** [TryHackMe - TakeOver](https://tryhackme.com/room/takeover)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.