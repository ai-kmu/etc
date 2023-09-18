# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs로 체크
        def check(node, val):
            # None 값 들어오면 0
            if node is None:
                return 0
            
            # 현재 노드에 대한 결괏값
            temp = int(node.val >= val)
            
            # 비교값 업데이트
            val = max(node.val, val)

            # 현재 노드 + 왼쪽 노드 dfs + 오른쪽 노드 dfs
            return temp + check(node.left, val) + check(node.right, val)

        return check(root, root.val)
