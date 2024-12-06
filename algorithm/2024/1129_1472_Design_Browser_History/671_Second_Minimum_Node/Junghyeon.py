# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        result = []
        # root.right.right

        if root.right == None:
            return -1

        def function(root):
            while root.right != None:
                result.append(root.right.val)
                result.append(root.left.val)
                
                root_right = root.right
                root_left = root.left
                function(root_right)
                function(root_left)

                break

        function(root)

        result.sort()

        min_num = result[0]

        for i in result:
            if i == min_num:
                continue
            else:
                return i

        return -1
