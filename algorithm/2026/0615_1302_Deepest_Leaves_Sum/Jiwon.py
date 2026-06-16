# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.maxDepth = 0
        self.ans = 0

        # DFS 재귀풀이
        def dfs(root, depth):
            if not root:
                return
            # leaf node일 경우
            if not root.left and not root.right:
                if self.maxDepth < depth:  # 더 깊은 곳이 남아 있으면 갱신
                    self.maxDepth = depth
                    self.ans = root.val
                elif self.maxDepth == depth:  # 가장 깊은 곳이랑 동일한 깊이면 더해줌
                    self.ans += root.val
                return

            # 양쪽 leave 재귀탐색
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 1)
        return self.ans
    
