#LeetCode 226. Invert Binary Tree
#1 : 10 ~ 1 : 0

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):

        if root is None or (root.left is None and root.right is None):
            return root

        if root.left is not None:
            self.invertTree(root.left)

        if root.right is not None:
            self.invertTree(root.right)

        tmp = root.left
        root.left = root.right
        root.right = tmp

        return root


# if __name__ == '__main__':
#
#     node1=TreeNode(1)
#     node3 = TreeNode(3)
#     node2=TreeNode(2,node1,node3)
#
#     node6=TreeNode(6)
#     node9=TreeNode(9)
#     node7=TreeNode(7,node6,node9)
#
#     root=TreeNode(4,node2,node7)
#
#     solution=Solution()
#
#     solution.invertTree(root)
#
#     # print(root.left.val)
#     # # print(root.right.val)
#     #
#     # print(root.left.left.val)
#     # print(root.left.right.val)
#
#     solution.searchTree(root)





