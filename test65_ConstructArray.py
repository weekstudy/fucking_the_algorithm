# -*- coding:utf-8 -*-

#  面试题66：构建乘积数组
# // 题目：给定一个数组A[0, 1, …, n-1]，请构建一个数组B[0, 1, …, n-1]，其
# // 中B中的元素B[i] =A[0]×A[1]×… ×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

def multiply(data):
    new_data=[]
    for i in range(len(data)):
        temp = 1
        temp1,temp2 = data[0:i],data[i+1:]
        for j in range(len(temp1)):
            temp*=temp1[j]
        for k in range(len(temp2)):
            temp*=temp2[k]
        new_data.append(temp)
    return new_data


if __name__=="__main__":
    data =[2,1,2,3]
    res=multiply(data)
    print(res)