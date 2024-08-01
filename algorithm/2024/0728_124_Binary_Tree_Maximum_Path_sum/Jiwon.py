'''
솔루션 참고
https://yuminlee2.medium.com/leetcode-124-binary-tree-maximum-path-sum-664545ce8bcd#830c
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            # 왼쪽/오른쪽 자식 노드 기준 maxPathSum 계산 (음수는 무시)
            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)

            # 현재 노드를 포함한 maxPathSum 계산, max()로 update
            self.max_sum = max(self.max_sum, node.val + leftMax + rightMax)
            
            return node.val + max(leftMax, rightMax)
        
        dfs(root)
        return self.max_sum
