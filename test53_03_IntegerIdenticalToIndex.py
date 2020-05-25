# // 题目：假设一个单调递增的数组里的每个元素都是整数并且是唯一的。请编程实
# // 现一个函数找出数组中任意一个数值等于其下标的元素。例如，在数组{-3, -1,
# // 1, 3, 5}中，数字3和它的下标相等。

def get_number_same_as_index(data):
    if len(data) < 0:
        return None

    left = 0
    right = len(data) - 1
    while left <= right:
        middle = left + ((right - left) >> 1)
        if data[middle] == middle:
            return middle
        if data[middle] > middle:
            right = middle - 1
        else:
            left = middle + 1


if __name__ == "__main__":
    data = [-3, -1, 1, 3, 5]
    res = get_number_same_as_index(data)
    print(res)
