# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        answer = 0
        
        # dfs로 현재 path의 최댓값만 유지해가며 good node의 갯수를 찾는다
        def dfs(node, max_num):
            nonlocal answer
            if node.val >= max_num:
                answer += 1
                max_num = node.val
            
            if node.left is not None:
                dfs(node.left, max_num)
            if node.right is not None:
                dfs(node.right, max_num)
        
        dfs(root, root.val)
        return answer
