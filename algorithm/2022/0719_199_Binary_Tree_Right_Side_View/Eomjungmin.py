# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = {} # 입력 root의 깊이별로 right-side 값 저장하는 딕셔너리 선언
        
        def dfs(node, result, level):
        '''
        dfs 방법을 이용하여 right-side 값을 저장하도록 함
         - 입력 node가 none이면 dfs 종료하도록 함
         - result 딕셔너리는 root의 깊이별로 rights-side 값이 저장된 것임
         - dfs할 때 먼저 현재 node의 오른쪽 값을 계속 저장
         - 오른쪽 저장 후 node의 왼쪽 값을 계속 저장.
         - 왼쪽값도 dfs하는 이유는 문제에서 right-side라는 것이 반드시 node의 오른쪽 값만을 보는 게 아니라
         - 입력 root에서 깊이마다 가장 오른쪽에 있는 값 모두 본다.
         - 그래서 node의 왼쪽도 보면서 root의 깊이별로 right-side 값을 저장해야 함
        '''
            if node == None:
                return
            
            if level not in result:
                result[level] = node.val
                
            dfs(node.right, result, level+1)
            dfs(node.left, result, level+1)
            
        dfs(root, result, 1)
        
        return result.values()
