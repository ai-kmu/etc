# 동일한 레벨에서 가장 큰 node를 보려면 우측에서 부터 보자.
# 우측이 None이라면 왼쪽으로 옮기면 된다.
# 그러기 위해서는 모든 방향으로 탐색이 필요하다.
# 큰 값을 남기기 위해서는 우선 좌측부터 탐색한 후 만일 우측 node가 None이 아니라면 덮어씌우는 방식을 사용하였다.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = [0] * 100
        
        def rec_func(root, depth): # 우선 최대 길이를 반환함, 그와 동시에 ans에 알맞은 값을 채워 넣음
            if root:
                ans[depth] = root.val # 현재 깊이에 값을 채워 넣음. 이 때는 값의 크기는 상관하지 않음. 만약 작은 값이라면 이후 덮어씌워짐
                depth = max(rec_func(root.left, depth+1), rec_func(root.right, depth+1)) # 나중에 길이를 반환하기 위해서는 왼쪽과 오른쪽 탐색하며 길이도 알아볼 필요가 있다.
                
            return depth
        
        depth = rec_func(root, 0)
        
        return ans[:rec_func(root, 0)]
