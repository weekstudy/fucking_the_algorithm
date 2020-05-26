# 对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
# 例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。
# -*- coding:utf-8 -*-


def left_rotate_String(s, n):
    # write code here
    return s[n:]+s[:n]


def left_rotate_String1(s,n):
    str1=[]
    str2=[]
    for i in range(len(s)):
        if i<n:
            str1.append(s[i])
        else:
            str2.append(s[i])
    str3="".join(str2+str1)
    return str3


if __name__=="__main__":
    str = "abcdefg"
    # res =left_rotate_String(str,2)
    res =left_rotate_String1(str,2)
    print(res)