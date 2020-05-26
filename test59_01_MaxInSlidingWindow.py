# -*- coding:utf-8 -*-


# / 题目：给定一个数组和滑动窗口的大小，请找出所有滑动窗口里的最大值。例如，
# // 如果输入数组{2, 3, 4, 2, 6, 2, 5, 1}及滑动窗口的大小3，那么一共存在6个
# // 滑动窗口，它们的最大值分别为{4, 4, 6, 6, 6, 5}，

def maxInWindows(num, size):
    # write code here
    if not num or size == 0:
        return []
    num_list = []
    for i in range(len(num)-size+1):
        max_num = max(num[i:size+i])
        num_list.append(max_num)
    return num_list


if __name__=="__main__":
    num = [2,3,4,2,6,2,5,1]
    res=maxInWindows(num,3)
    print(res)