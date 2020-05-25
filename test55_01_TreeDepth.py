# -*- coding:utf-8 -*-

# 题目描述
# 输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的
# 结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度


class BinaryTreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def connect_tree_node(pRoot:BinaryTreeNode, pLeft:BinaryTreeNode=None,
                      pRight:BinaryTreeNode=None):

    pRoot.left=pLeft
    pRoot.right=pRight
    return pRoot


class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        res2 = self.TreeDepth(pRoot.left)
        res1 = self.TreeDepth(pRoot.right)
        return max(res1, res2) + 1


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
    depth = s.TreeDepth(pRoot)
    print(depth)
