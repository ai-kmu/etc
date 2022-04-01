 # dfs를 이용해 오른쪽 끝노드(가장큰수)를 탐색 후 백트래킹하면서 값들을 더해줬습니다.
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        sum=0
        visited=[]
        def dfs(node:TreeNode):
            nonlocal sum
            
            if node.val in visited:
                return
            
            
            visited.append(node.val)
            
            if node.right is not None:
                dfs(node.right) # 오른쪽 노드로 dfs 재귀
                
            sum+=node.val # 거쳐온 노드들의 합
            node.val=sum # 현재 노드 업데이트
            
            if node.left is not None:
                dfs(node.left) # 왼쪽 노드로 dfs 재귀
            
        
        dfs(root)
        return root
