# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rlist = []
        
        if root == None:
            return []
          
        temp = root
        
        while temp is not None:
            rlist.append(temp.val)
            left = temp.left
            if temp.right is not None:
                temp = temp.right
                left = temp.left
            else:
                if left is not None:
                    temp = left.right
                    left = temp.left
                else:
                    break
        
        return rlist

