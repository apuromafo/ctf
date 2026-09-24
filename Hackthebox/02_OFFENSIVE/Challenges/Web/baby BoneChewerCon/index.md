# baby BoneChewerCon

> **ES:** Web · EASY — debugger expuesto en producción hacia la secret key.
> **EN:** Web · EASY — debugger exposed in production to the secret key.
:::note CHALLENGE DESCRIPTION

Difficulty: EASY

Due to heavy workload for the upcoming baby BoneChewerCon event, the website is under maintenance and it errors out, but the debugger is still enabled in production!! I think the devil is enticing us to go and check out the secret key.

由于即将到来的Baby BoneChewerCon活动工作量过大，网站正处于维护状态并出现报错，但生产环境的调试器居然仍处于开启状态！！我觉得这简直是魔鬼在引诱我们去查看那个密钥。

:::

直接访问网站

![img](img/image_20250332-183220.png)

页面上面除了一个输入框，没有其他的交互点。

尝试发送一个123

![img](img/image_20250338-183832.png)

在环境信息中，就能得到flag

![img](img/image_20250339-183910.png)

```flag
HTB{wh3n_th3_d3bugg3r_turns_4g41nst_th3_d3bugg33}
```

---

## Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de contenido activo.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish active content flags.

_Fecha de edición: 2026-09-24_
