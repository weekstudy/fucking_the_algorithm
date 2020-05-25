# 题目描述
# 一个整型数组里除了两个数字之外，其他的数字都出现了两次。
# 请写程序找出这两个只出现一次的数字。

# -*- coding:utf-8 -*-
import sys


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        new_array = []
        for i in array:
            if array.count(i) == 1:
                new_array.append(i)
        return new_array

    def find_nums_appear_once(self, data, num1=0, num2=0):
        if len(data) < 2:
            return None
        resultOR = 0
        for i in range(len(data)):
            resultOR ^= data[i]

        index_of1 = self.find_first_bits1(resultOR)
        num1 = num2 = 0;
        for j in range(len(data)):
            if (self.is_bit1(data[j], index_of1)):
                num1 ^= data[j]
            else:
                num2 ^=data[j]
        return num1,num2

    def find_first_bits1(self, num):
        index_bit = 0
        # while num & 1==0 and index_bit<8*sys.getsizeof(int):
        while ((num & 1) == 0) and (index_bit < 8 * 4):
            num = num >> 1
            index_bit += 1

        return index_bit

    def is_bit1(self, num, index_bit):
        num = num >> index_bit
        return num & 1


if __name__ == "__main__":
    # print(1^1)
    # a=100
    # print(sys.getsizeof(a))
    data = [2, 4, 3, 6, 3, 2, 5, 5]
    s=Solution()
    res=s.find_nums_appear_once(data)
    print(res)