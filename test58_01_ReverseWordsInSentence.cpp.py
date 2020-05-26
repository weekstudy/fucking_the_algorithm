# 题目：输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
# 为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，
#  则输出"student. a am I"

#
# 算法思想：先翻转整个句子，然后，依次翻转每个单词。
# 依据空格来确定单词的起始和终止位置

def reverse(str):
    if len(str)<0:
        return 0
    str_copy = []
    for i in range(len(str)-1,-1,-1):
        str_copy.append(str[i])
    str_copy.append(" ")

    str_copy2 =[]
    str_copy3= []
    str_copy4= []
    for i in range(len(str_copy)):
        if str_copy[i]!=" ":
            str_copy3.append(str_copy[i])
        else:
            str_copy4.extend(str_copy3)
            str_copy4.reverse()
            str_copy4.append(" ")
            str_copy2.extend(str_copy4)
            str_copy4=[]
            str_copy3=[]

    str_copy2 = str_copy2[:-1]
    str_copy2="".join(str_copy2)

    return str_copy2


if __name__=="__main__":
    str="I am a student."
    res =reverse(str)
    print(res)