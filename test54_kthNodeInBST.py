#
# // 面试题54：二叉搜索树的第k个结点
# // 题目：给定一棵二叉搜索树，请找出其中的第k小的结点。

# 树节点
# 连接节点---为函数添加提示，静态参数，表示只能是这个类型，->表示返回值类型

class BinaryTreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        #第三个节点是4
        #前序遍历5324768,中序遍历2345678,后序遍历2436875
        #所以是中序遍历，左根右
        global result
        result=[]
        self.mid_node(pRoot)
        if  k<=0 or len(result)<k:
            return None
        else:
            return result[k-1]
              
    def mid_node(self,root):
        if not root:
            return None
        self.mid_node(root.left)
        result.append(root)
        self.mid_node(root.right)


def connect_tree_node(pRoot:BinaryTreeNode, pLeft:BinaryTreeNode,
                      pRight:BinaryTreeNode):

    pRoot.left=pLeft
    pRoot.right=pRight
    return pRoot


if __name__ == "__main__":
    # 创建节点
    pNode5 = BinaryTreeNode(5)
    pNode3 = BinaryTreeNode(3)
    pNode7 = BinaryTreeNode(7)
    pNode2 = BinaryTreeNode(2)
    pNode4 = BinaryTreeNode(4)
    pNode6 = BinaryTreeNode(6)
    pNode8 = BinaryTreeNode(8)

    # 连接树节点
    connect_tree_node(pNode3, pNode2, pNode4)
    connect_tree_node(pNode7, pNode6, pNode8)
    res = connect_tree_node(pNode5, pNode3, pNode7)
    print(res.val)

    s=Solution()
    target = s.KthNode(res, 7)

    print(target.val)
