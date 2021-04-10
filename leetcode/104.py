# 104. 二叉树的最大深度
# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最大深度 3 。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        # root: TreeNode
        # int:
        # if root.left != None:
        #     return self.maxDepth(root.left) + 1
        # if root.right != None:
        #     return self.maxDepth(root.right) + 1
        # if root.left or root.right == None:
        #     return 1


        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1


if __name__ == '__main__':
    # [3, 9, 20, null, null, 15, 7]
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)

    n1.left = n2
    n1.right = n3
    n3.left = n4
    n3.right = n5
    print(n1.left.val)
    s = Solution()
    print(s.maxDepth(n1))
