# -*- coding:utf-8 -*-

# 题目描述
# 把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数
# 但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。
# 求按从小到大的顺序的第N个丑数。


class Solution:
    def get_ugly_number_solution(self, index):
        # write code here
        if index < 1:
            return 0
        time2 = []
        time3 = []
        time5 = []
        ugly_number_list = [1, ]
        temp = 1
        for i in range(index):
            time2.append(temp * 2)
            time3.append(temp * 3)
            time5.append(temp * 5)

            temp = min(min(time2), min(time3), min(time5))
            ugly_number_list.append(temp)
            if temp in time2:
                del time2[0]
            if temp in time3:
                del time3[0]
            if temp in time5:
                del time5[0]
        return ugly_number_list[index - 1]


if __name__ == "__main__":
    s = Solution()
    res = s.get_ugly_number_solution(3)
    print(res)
