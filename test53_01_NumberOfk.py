# 题目描述
# 统计一个数字在排序数组中出现的次数。

# -*- coding:utf-8 -*-


class Solution:
    def get_number_of_k(self, data, k):
        # write code here
        return data.count(k)

    # 找到数组中第一次出现的k

    def get_first_k(self, data, k, start, end):
        if start > end:
            return -1
        # middle_index = int((start + end)/2)
        middle_index = (start + end)>>1
        middle_data = data[middle_index]
        # 如果中间值等于k
        if (middle_data == k):
            # 判断是不是第一出现的k,即判断前面的data[middle_index-1]是否==k,如果不是，则是第一个k,返回
            if (middle_index > 0 and data[middle_index - 1] != k) or (middle_index == 0):
                return middle_index
            else:
                end = middle_index - 1
        elif middle_data > k:
            end = middle_index - 1
        else:
            start = middle_index + 1
        return self.get_first_k(data, k, start, end)

    # //找到数组中最后一次出现k
    def get_last_k(self, data, k, start, end):
        if start > end:
            return -1
        # middle_index = int((start + end)/2)
        middle_index = (start + end) >> 1
        middle_data = data[middle_index]
        # 如果中间值等于k
        if (middle_data == k):
            # 判断是不是第一出现的k,即判断前面的data[middle_index-1]是否==k,如果不是，则是第一个k,返回
            if (middle_index < len(data) - 1 and data[middle_index + 1] != k) \
                    or (middle_index == len(data) - 1):
                return middle_index
            else:
                start = middle_index + 1
        elif middle_data < k:
            start = middle_index + 1
        else:
            end = middle_index - 1
        return self.get_last_k(data, k, start, end)

    # //得到k的次数
    def get_number_of_k1(self, data, k):
        count = 0
        if len(data) > 0:
            first_k = self.get_first_k(data, k, 0, len(data) - 1)
            last_k = self.get_last_k(data, k, 0, len(data) - 1)
            if first_k > -1 and last_k > -1:
                count = last_k - first_k + 1
        return count


if __name__ == "__main__":
    s = Solution()
    data = [1, 2, 3, 3, 3, 3, 4, 5]
    # res = s.get_number_of_k(data, 3)
    res = s.get_number_of_k1(data, 3)
    print(res)
