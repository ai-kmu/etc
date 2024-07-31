'''
Solution
- https://velog.io/@heyggun/1%EC%8A%A44%EC%BD%942%ED%8C%8C-164.-LeetCode
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')  # infinity 정의, int는 선언 불가, float('inf') <-> float('-inf')
        self.dfs(root)
        return self.ans

    def dfs(self, cur_node: Optional[TreeNode]) -> int:
        if cur_node == None:
            return 0
        left_max_value = max(0, self.dfs(cur_node.left))  # 왼쪽 경로를 택하거나 택하지 않거나
        right_max_value = max(0, self.dfs(cur_node.right))  # 오른쪽 경로를 택하거나 택하지 않거나
        self.ans = max(self.ans, cur_node.val + left_max_value + right_max_value)  # 현재 노드를 포함한 경로 중 최대값과 비교
        return cur_node.val + max(left_max_value, right_max_value)  # 위 라인 코드와 다르게 현재 노드를 포함하지 않을 경우 왼쪽, 오른쪽 경로 중 하나만 선택 가능
