# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 정답값 초기화 - self 이용해서 전역변수 활용
        self.max_sum = float('-inf')
        
        def dfs(node: Optional[TreeNode]) -> int:
            # 탈출: null 만나면 0 추가
            if not node:
                return 0
            
            # 재귀적으로 현재 기준 왼쪽, 오른쪽 방향 max path sum 계산
            # 이때 총합이 음수인 것은 제외 -> `node.val`에 음수 더해봤자임
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)
            
            # 현재 포함 전체 path sum 계산
            current_path_sum = node.val + left_max + right_max
            
            # 정답값 업데이트
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # 부모 노드로 현재 포함한 전체 path sum 반환
            return node.val + max(left_max, right_max)
        
        # root에서 dfs 시작
        dfs(root)
        return self.max_sum
