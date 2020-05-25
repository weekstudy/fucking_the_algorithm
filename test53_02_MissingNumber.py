# 0到n-1中缺失的数字
# // 题目：一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字
# // 都在范围0到n-1之内。在范围0到n-1的n个数字中有且只有一个数字不在该数组
# // 中，请找出这个数字。


def get_missing_number(data):
    if len(data) < 0:
        return 0

    left = 0
    right = len(data) - 1
    while (left <= right):
        middle = (left + right) >> 1
        if data[middle] != middle:
            if middle == 0 or data[middle - 1] == middle - 1:
                return middle
            right = middle - 1
        else:
            left = middle + 1
        if (left == len(data)):
            return len(data)

if __name__=="__main__":
    data=[0,1,2,3,4,6]
    res=get_missing_number(data)
    print(res)
