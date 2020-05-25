# -*- coding:utf-8 -*-


# 题目：输入一个正数s，打印出所有和为s的连续正数序列（至少含有两个数）。
#  例如输入15，由于1+2+3+4+5=4+5+6=7+8=15，所以结果打印出3个连续序列1～5、
#  4～6和7～8。

def find_continuous_sequence(sum):

    if sum < 3:
        return None

    small = 1 
    big = 2
    middle = (1 + sum) / 2
    curSum = small + big

    while small < middle:
        if curSum == sum:
            print_continuous_sequence(small, big)

        while curSum > sum and small < middle:
            curSum -= small
            small +=1
            if curSum == sum:
                print_continuous_sequence(small, big)

        big +=1
        curSum += big


def print_continuous_sequence(small:int, big:int):

    for i in range(small,big+1):
        print("%d" % i,end="")

    print("\n")


if __name__=="__main__":
    find_continuous_sequence(9)