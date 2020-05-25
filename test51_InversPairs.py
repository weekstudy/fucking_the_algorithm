# -*- coding:utf-8 -*-
# 题目描述
# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
# 输入一个数组,求出这个数组中的逆序对的总数P。
# 并将P对1000000007取模的结果输出。 即输出P%1000000007

import copy


class Solution:
    # 遍历
    def inverse_pairs(self, data):
        # write code here
        if not data:
            return []
        counts = 0
        for i in range(len(data)):
            for j in range(i,len(data)):
                if data[i] > data[j]:
                    counts += 1
        return counts%1000000007

    # 归并
    def inverse_pairs1(self,data):
        if not data:
            return []
        # 深拷贝
        data_copy=copy.deepcopy(data)
        count=self.inverse_pairs_core(data,data_copy,0,len(data)-1)
        return count

    def inverse_pairs_core(self,data, data_copy,start,end):

        if start==end:
            data_copy[start]=data[start]
            return 0
        length=int((end-start)/2)
        left=self.inverse_pairs_core(data_copy,data,start,start+length);
        right=self.inverse_pairs_core(data_copy,data,start+length+1,end);

        i=start+length
        j=end
        index_copy=end
        count=0
        while(i>=start and j>=start+length+1):
            if data[i]>data[j]:

                data_copy[index_copy]=data[i]
                index_copy -= 1
                i -= 1
                count+=j-start-length
            else:
                data_copy[index_copy]=data[j]
                index_copy-=1
                j-=1

        for i in range(i,start,-1):
            data_copy[index_copy]=data[i]
            index_copy -= 1
            # i -= 1
        for j in range(j,end-length-start-1,-1):
            data_copy[index_copy]=data[j]
            index_copy-=1

        return left+right+count


if __name__=="__main__":
    s =Solution()
    data =[7,5,6,4]
    # res =s.inverse_pairs(data)
    res =s.inverse_pairs1(data)
    print(res)