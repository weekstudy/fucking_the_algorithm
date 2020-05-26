# -*- coding:-utf-8 -*-


# 扑克牌的顺子
# 题目：从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
# 2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王可以看成任意数字。

# 思路，排序，统计零的个数，统计相邻数字之间的空缺
# 如果空缺个数小于等于零的个数，连续，反之不连续


def is_continus(numbers: list):
    if len(numbers) < 1:
        return False
    numbers.sort()
    length = len(numbers)
    # 统计0的个数
    count_zero = numbers.count(0)

    # 统计空缺的个数
    count_blank = 0
    for i in range(count_zero, length - 1):
        if numbers[i + 1] == numbers[i]:
            return False
        elif numbers[i + 1] - numbers[i] > 1:
            count_blank += numbers[i + 1] - numbers[i] - 1

    if count_zero >= count_blank:
        return True
    else:
        return False


if __name__ == "__main__":
    data = [0, 1, 3, 3, 4]
    data = [1, 3, 0, 7, 0]
    data = [0,3,1,6,4]
    res = is_continus(data)
    print(res)
