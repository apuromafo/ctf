# Ancient Encodings

> **ES:** Crypto · VERY EASY — reversión del encoding (hex de bytes_to_long + base64) para recuperar el flag.
> **EN:** Crypto · VERY EASY — encoding reversal (bytes_to_long hex + base64) to recover the flag.
:::note CHALLENGE DESCRIPTION

Difficulty: VERY EASY

Your initialization sequence requires loading various programs to gain the necessary knowledge and skills for your journey. Your first task is to learn the ancient encodings used by the aliens in their communication.

你的初始化序列需要加载各种程序，以获取旅程中所需的知识和技能。你的第一个任务是学习外星人在通信中使用的古老编码方式。

:::

在附件中得到加密脚本

```python
from Crypto.Util.number import bytes_to_long
from base64 import b64encode
from secret import FLAG


def encode(message):
    return hex(bytes_to_long(b64encode(message)))


def main():
    encoded_flag = encode(FLAG)
    with open("output.txt", "w") as f:
        f.write(encoded_flag)


if __name__ == "__main__":
    main()
```

编写解密脚本

```python
from Crypto.Util.number import long_to_bytes
from base64 import b64encode, b64decode

with open("output.txt", "r") as f:
    data = f.read()

data = b64decode(long_to_bytes(int(data, 16)).decode()).decode()

print(data)
```

```plaintext title="Flag"
HTB{411_7h3_3nc0d1n9_423_h323_70_574y}
```

---

## Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de contenido activo.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish active content flags.

_Fecha de edición: 2026-09-24_
