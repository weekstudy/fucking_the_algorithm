# -*- coding:utf-8 -*-

# 不用加减乘除做加法
# 题目：写一个函数，求两个整数之和，要求在函数体内不得使用＋、－、×、÷
#  四则运算符号。

# 思路：用二进制算

def add(num1, num2):

    while num2:
        sum = num1 ^ num2
        p = 0xffffffff & ((num1 & num2) << 1)
        if p > 0x7FFFFFFF:
            p = -(~(p - 1) & 0xFFFFFFFF)
        num1 = sum
        num2 = p
    return num1

if __name__ == "__main__":
    res = add(0, 15)
    print(res)
    # print(bin(-2))
