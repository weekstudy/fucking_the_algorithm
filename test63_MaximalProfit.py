# -*- coding:utf-8 -*-

# 股票的最大利润
# // 题目：假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖交易该股
# // 票可能获得的利润是多少？例如一只股票在某些时间节点的价格为{9, 11, 8, 5,
# // 7, 12, 16, 14}。如果我们能在价格为5的时候买入并在价格为16时卖出，则能
# // 收获最大的利润11。


# 思路：先记录i-1个数字中的最小值，然后用当前numbers[i]减去最小值，
# 得到当前利润最大值

def max_diff(numbers):
    if numbers==[]:
        return None
    min_val=numbers[0]
    max_val=numbers[1]-min_val

    for i in range(2,len(numbers)):
        if numbers[i-1]<min_val:
            min_val=numbers[i-1]
        current_max=numbers[i]-min_val
        if current_max>max_val:
            max_val=current_max
    return max_val


if __name__=="__main__":
    data=[9,11,8,5,7,12,16,14]
    res=max_diff(data)
    print(res)






