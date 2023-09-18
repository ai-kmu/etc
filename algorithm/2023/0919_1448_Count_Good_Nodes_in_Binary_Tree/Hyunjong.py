# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# dfs로 풀기
class Solution(object):
    def goodNodes(self, root):

        def dfs(node, max_val):
            # 종료 조건
            if not node:
                return 0

            # 다음 조건일 때 count = 1
            if node.val >= max_val:
                max_val = node.val
                count = 1
            # 아니면 count = 0
            else:
                count = 0
            
            # dfs 순환
            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)

            return count
        return dfs(root, float('-inf'))
