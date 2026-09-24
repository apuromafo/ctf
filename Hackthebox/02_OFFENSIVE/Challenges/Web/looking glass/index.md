# looking glass

> **ES:** Web · EASY — command injection en el ping.
> **EN:** Web · EASY — command injection in ping.
:::note CHALLENGE DESCRIPTION

Difficulty: EASY

We've built the most secure networking tool in the market, come and check it out!

我们已经打造了市场上最安全的网络工具，快来体验一下吧！

:::

尝试直接访问，得到

![img](img/image_20250339-213933.png)

根据经验，执行`ping`的功能点，有可能是直接执行命令拼接来实现的，尝试进行命令注入

![img](img/image_20250340-214046.png)

然后尝试直接探测主机情况

![img](img/image_20250341-214152.png)

即可得到flag

![img](img/image_20250342-214220.png)

```flag
HTB{I_f1n4lly_l00k3d_thr0ugh_th3_rc3}
```

---

## Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de contenido activo.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish active content flags.

_Fecha de edición: 2026-09-24_
