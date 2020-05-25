# 题目描述
# 输入一棵二叉树，判断该二叉树是否是平衡二叉树。
#
# 在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树

# -*- coding:utf-8 -*-
class BinaryTreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced_solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return abs(self.TreeDepth(pRoot.left) - self.TreeDepth(pRoot.right)) <= 1 and \
               self.isBalanced_solution(
            pRoot.left) and self.isBalanced_solution(pRoot.right)

    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        left_depth = self.TreeDepth(pRoot.left)
        right_depth = self.TreeDepth(pRoot.right)
        return max(left_depth, right_depth) + 1


def connect_tree_node(pRoot:BinaryTreeNode,
                      pLeft:BinaryTreeNode=None,pRight:BinaryTreeNode=None):
    pRoot.left=pLeft
    pRoot.right=pRight
    return pRoot


if __name__ == "__main__":
    # 创建节点
    pNode1 = BinaryTreeNode(1)
    pNode2 = BinaryTreeNode(2)
    pNode3 = BinaryTreeNode(3)
    pNode4 = BinaryTreeNode(4)
    pNode5 = BinaryTreeNode(5)
    pNode6 = BinaryTreeNode(6)
    pNode7 = BinaryTreeNode(7)

    # 连接树节点
    connect_tree_node(pNode5, pNode7, None)
    connect_tree_node(pNode2, pNode4, pNode5)
    connect_tree_node(pNode3, None, pNode6)
    pRoot = connect_tree_node(pNode1, pNode2, pNode3)
    # print(pRoot.val)

    s =Solution()
    isBalanced_solution = s.isBalanced_solution(pRoot)
    print(isBalanced_solution)
