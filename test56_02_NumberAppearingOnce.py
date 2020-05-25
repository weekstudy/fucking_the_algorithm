# // 面试题56（二）：数组中唯一只出现一次的数字
# // 题目：在一个数组中除了一个数字只出现一次之外，其他数字都出现了三次。请
# // 找出那个吃出现一次的数字。


def find_number_appearace_once(data):

    if len(data) <= 0:
        return None

    sum_list=[i-i for i in range(32)]

    for i in range(len(data)):
        bit_mask = 1
        for j in range(31,-1,-1):
            bit = data[i] & bit_mask
            if bit != 0:
                sum_list[j] += 1
            bit_mask=bit_mask << 1
    result = 0
    for i in range(32):

        result = result << 1
        result += sum_list[i] % 3
    return result

if __name__=="__main__":
    data=[4, 4, 1, 1, 1, 7, 4]
    res=find_number_appearace_once(data)
    print(res)