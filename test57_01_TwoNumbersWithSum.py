# -*- coding: utf-8 -*-


# 题目描述
# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，
# 使得他们的和正好是S，如果有多对数字的和等于s,输出任意一对


def find_numbers_with_sum(data, sum):
    # found = False
    num1 = num2 = None
    if len(data) < 1 or num1 == 0 or num2 == 0:
        return None

    ahead = len(data) - 1
    behind = 0
    while ahead > behind:
        curSum = data[ahead] + data[behind]

        if curSum == sum:

            num1 = data[behind]
            num2 = data[ahead]
            # found = True
            break

        elif curSum > sum:
            ahead -= 1
        else:
            behind += 1

    return num1, num2


if __name__ == "__main__":
    data = [1, 2, 3, 4, 7, 11, 12,15]

    res=find_numbers_with_sum(data,15)
    print(res)