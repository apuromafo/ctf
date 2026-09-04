 
# Operation Slither [EASY]

**Enlace de la sala:** [Operation Slither](https://tryhackme.com/room/operationslitherIU)

---

## 🐍 Tarea 1: El Líder / Task 1: The Leader

<p align="center">
<img src="[https://tryhackme-images.s3.amazonaws.com/user-uploads/5ed5961c6276df568891c3ea/room-content/5ed5961c6276df568891c3ea-1769787523829.png](https://tryhackme-images.s3.amazonaws.com/user-uploads/5ed5961c6276df568891c3ea/room-content/5ed5961c6276df568891c3ea-1769787523829.png)" width="200px" />
</p>

*Hemos obtenido acceso a un foro de hackers y encontramos información de nuestra empresa en venta. Todo lo que tenemos es este post. Encuentra cualquier información relacionada con el líder del grupo **Sneaky Viper**.*

### Inteligencia / Intel

```shell
Full user database TryTelecomMe on sale!!!

As part of Operation Slither, we've been hiding for weeks in their network and have now started to exfiltrate information. 
This is just the beginning. We'll be releasing more data soon. Stay tuned!

@v3n0mbyt3_

```

### Preguntas / Questions

1. **Aside from Twitter / X, what other platform is used by v3n0mbyt3_?** (Answer in lowercase)
* *Format:* `*******`
> Answer: `threads`

2. **What is the value of the flag?**
* *Format:* `***{********_******_***_*****_********}`
> Answer: ``THM{sl1th3ry_tw33tz_4nd_l34kr_r3pl13s!}`

> nota: se debe convertir de base64 para abordarlo fuente
>  `https://www.threads.com/@_myst1cv1x3n_/post/C6G32WIvcJW?xmt=AQF0d8N-GTgDST9Wb7IfOI8X2pNON2QwItLja80ZJNTxOg `

---

## 🐍 Tarea 2: El Asistente / Task 2: The Sidekick

<p align="center">
<img src="[https://tryhackme-images.s3.amazonaws.com/user-uploads/5ed5961c6276df568891c3ea/room-content/5ed5961c6276df568891c3ea-1769787567454.png](https://tryhackme-images.s3.amazonaws.com/user-uploads/5ed5961c6276df568891c3ea/room-content/5ed5961c6276df568891c3ea-1769787567454.png)" width="200px" />
</p>

*¡Un segundo mensaje se ha hecho público! Nuestra cuenta en el foro fue eliminada, así que no pudimos obtener el handle del operador esta vez. Sigue el rastro de la primera tarea y caza cualquier información relacionada con el segundo operador del grupo.*

### Inteligencia / Intel

```shell
60GB of data owned by TryTelecomMe is now up for bidding!

Number of users: 64500000 Accepting all types of crypto
For takers, send your bid on Threads via this handle:

HIDDEN CONTENT 
----------------------------------------------------------------------------------------------------- 
You must register or log in to view this content

```

### Preguntas / Questions

1. **What is the username of the second operator talking to v3n0mbyt3 from the previous platform?**
* *Format:* `_***********_`
> Answer: `_myst1cv1x3n_`

2. **What is the value of the flag?**
* *Format:* `***{*******_******_******_********}`
> Answer: `THM{s0cm1nt_00ps3c_f1ng3r_m1scl1ck}`

> nota: se debe convertir de base64 para abordarlo fuente
>  ` instagram , luego souncloud indica prototipe al revisar en https://soundcloud.com/v1x3n-195859753/prototype2  sale la flag `

---

## 🐍 Tarea 3: El Último Operador / Task 3: The Last Operator

<p align="center">
<img src="[https://tryhackme-images.s3.amazonaws.com/user-uploads/5ed5961c6276df568891c3ea/room-content/5ed5961c6276df568891c3ea-1769787593281.png](https://tryhackme-images.s3.amazonaws.com/user-uploads/5ed5961c6276df568891c3ea/room-content/5ed5961c6276df568891c3ea-1769787593281.png)" width="200px" />
</p>

*Hay un nuevo post. Caza al tercer operador usando los descubrimientos pasados y encuentra detalles relacionados con la infraestructura utilizada para el ataque.*

### Inteligencia / Intel

```shell
FOR SALE

Advanced automation scripts for phishing and initial access!

Inclusions:
- Terraform scripts for a resilient phishing infrastructure 
- Updated Google Phishlet (evilginx v3.0)
- GoPhish automation scripts
- Google MFA bypass script
- Google account enumerator
- Automated Google brute-forcing script
- Cobalt Strike aggressor scripts
- SentinelOne, CrowdStrike, Cortex XDR bypass payloads

PRICE: $1500
Accepting all types of crypto
Contact me on REDACTED@protonmail.com 

```

### Preguntas / Questions
> Nota:  para este reto hay que cruzar mucha informacion previa, hasta llegar a 
> `https://github.com/sh4d0wF4NG/red-team-infra/commit/78de1f17c45b994e97b8629aa7e5f42c31a0e7f7#diff-f0543f47d07eca9df28e768583fd7ec54a1cc943195502f06a2bd23e182ff4a5`

1. **What is the handle of the third operator?**
* *Format:* `**********`
> Answer: `sh4d0wF4NG`

2. **What other platform does the third operator use?** (Answer in lowercase)
* *Format:* `******`
> Answer: `github`

3. **What is the value of the flag?**
* *Format:* `***{*****_*****_******_******_**}`
> Answer `THM{sh4rp_f4ngz_l34k3d_bl00dy_pw}`

 
---
### Resumen / Summary

| Task | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | 1 | `threads` |
| 1 | 2 | `THM{sl1th3ry_tw33tz_4nd_l34kr_r3pl13s!}` |
| 2 | 1 | `_myst1cv1x3n_` |
| 2 | 2 | `THM{s0cm1nt_00ps3c_f1ng3r_m1scl1ck}` |
| 3 | 1 | `sh4d0wF4NG` |
| 3 | 2 | `github` |
| 3 | 3 | `THM{sh4rp_f4ngz_l34k3d_bl00dy_pw}` |

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
