# -*- coding:utf-8 -*-


# / 面试题62：圆圈中最后剩下的数字
# // 题目：0, 1, …, n-1这n个数字排成一个圆圈，从数字0开始每次从这个圆圈里
# // 删除第m个数字。求出这个圆圈里剩下的最后一个数字。

def last_remaining(n,m):
    if n<1 or m<1:
        return None

    last=0
    for i in range(2,n+1):
        last=(last+m)%i

    return last


if __name__=="__main__":
    res = last_remaining(5,3)
    print(res)
