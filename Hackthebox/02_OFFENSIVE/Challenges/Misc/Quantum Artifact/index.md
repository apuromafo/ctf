# Quantum Artifact

> **ES:** Misc · EASY — circuito qiskit tipo Bernstein-Vazirani: medir los bits del flag.
> **EN:** Misc · EASY — Bernstein-Vazirani-like qiskit circuit: measure the flag bits.
:::note CHALLENGE DESCRIPTION

Difficulty: EASY

The quantum data came back and analyzed. DISASTER! Our best scientists all agree: Unfortunately our species and our whole culture are about to be eliminated. Due to abnormal behavior of the black hole's singularity our planet is about to get swallowed. Project ""ONESHOT"" is our last hope...

量子数据已经返回并进行了分析。灾难降临了！我们最优秀的科学家一致认为：不幸的是，我们的物种和整个文化即将被毁灭。由于黑洞奇点的异常行为，我们的星球即将被吞噬。项目 “**ONESHOT**” 是我们最后的希望……

:::

题目提供了一个 Python 脚本

```python title="circuit.py"
from qiskit import *
import qiskit.qasm2

flag = open('flag.txt', 'rb').read()
secret = ''.join("{0:08b}".format(c) for c in flag)
circuit = QuantumCircuit(len(secret)+1, len(secret))

circuit.h(range(len(secret)))
circuit.x(len(secret))
circuit.h(len(secret))

circuit.barrier()

for ii, yesno in enumerate(reversed(secret)): 
    if yesno == '1':
        circuit.cx(ii, len(secret))

circuit.barrier()

circuit.h(range(len(secret)))
circuit.barrier()
circuit.measure(range(len(secret)), range(len(secret)))

qasm_code = qiskit.qasm2.dumps(circuit)

# Write the OpenQASM code to a file
with open('challenge_circuit.qasm', 'w') as file:
    file.write(qasm_code)
```

并提供了 `challenge_circuit.qasm` 文件

---

## Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de contenido activo.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish active content flags.

_Fecha de edición: 2026-09-24_
