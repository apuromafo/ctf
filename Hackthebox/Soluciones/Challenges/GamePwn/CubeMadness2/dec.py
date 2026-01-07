'''
https://www.kn0sky.com/?p=6d09d68d-54b7-4d59-804f-24a5b6aa39b8

Modify encrypted memroy.

HTB{08FU5C473D_4ND_UNKN0WN}
'''

def decode(val: int) -> int:
    """
    模拟 C++ 中的 decode 函数：
    1. val 左移 9 位，截断为 32bit；
    2. 转为 64bit 后再左移 32 位；
    3. 除以 key，返回结果。
    """
    tmp = (val << 9) & 0xFFFFFFFF  # _shlx_u32 返回 32 位结果
    key = 0x6208CECB
    tmp = tmp << 32               # 升为 64 位再左移 32 位
    tmp //= key                   # 整除
    return tmp


# -------- main --------
if __name__ == "__main__":
    val = 0x248F
    key = 0x6208CECB

    # 计算 32bit 乘法的高低部分
    full_prod = (val & 0xFFFFFFFF) * (key & 0xFFFFFFFF)  # 保持在 64 位范围内
    result_lo = full_prod & 0xFFFFFFFF                  # 低 32 位
    result_hi = (full_prod >> 32) & 0xFFFFFFFF          # 高 32 位

    # 打印高低两部分（十六进制）
    print(f"{result_hi:X} {result_lo:X}")

    # 模拟 _sarx_i32，算术右移 9 位，需要先按 32 位有符号数处理
    # 将高 32 位视作有符号数
    signed_hi = result_hi if result_hi < 0x80000000 else result_hi - 0x100000000
    res = signed_hi >> 9
    # 打印右移后的结果（十六进制）
    print(f"{res & 0xFFFFFFFF:X}")

    # 调用 decode(19)
    inp = decode(19)
    print(f"inp: {inp:X}")

