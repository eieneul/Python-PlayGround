"""
生成默认4位的验证码（大小写字母和数字组成）

"""
import random


def generate_code(code_len=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    for _ in range(code_len):
        code += random.choice(all_chars)
    return code

# print(generate_code(5))
