# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        aws = []
        def dfs(root, layer):
            if not root:
                # 종료 조건 빈 노드
                return None
            if layer == len(aws):
                # layer와 aws의 개수가 같으면 append
                aws.append(root.val)
            # 오른쪽 => 왼쪽 순으로 탐색
            dfs(root.right, layer+1)
            # 오른쪽 탐색
            dfs(root.left, layer+1)
            # 왼쪽 탐색
            return aws
        return dfs(root, 0)
