# 题目描述
# 输入两个链表，找出它们的第一个公共结点。
# -*- coding:utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def find_first_commonNode(self, pHead1, pHead2):
        # write code here
        list1 = []
        while pHead1:
            list1.append(pHead1.val)
            pHead1 = pHead1.next
        while pHead2:
            if pHead2.val in list1:
                return pHead2
            else:
                pHead2 = pHead2.next


if __name__ == "__main__":
    list1_node1 = ListNode(1)
    list1_node2 = ListNode(2)
    list1_node1.next = list1_node2
    list1_node3 = ListNode(3)
    list1_node2.next = list1_node3
    list1_node4 = ListNode(6)
    list1_node3.next = list1_node4
    list1_node5 = ListNode(7)
    list1_node4.next = list1_node5

    list2_node1 = ListNode(4)
    list2_node2 = ListNode(5)
    list2_node1.next = list2_node2
    list2_node3 = ListNode(6)
    list2_node2.next = list2_node3
    list2_node4 = ListNode(7)
    list2_node3.next = list2_node4

    s = Solution()
    res = s.find_first_commonNode(list1_node1, list2_node1)
    print(res.val)
