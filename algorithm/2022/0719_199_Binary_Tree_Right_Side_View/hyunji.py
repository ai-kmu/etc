class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        
        def DFS(now, depth):  
            
            if now == None:
                return
            
            # 제일 오른쪽부터 탐색하기 때문에 
            # answer의 길이와 depth가 동일한 경우만 append하면 된다
            if depth == len(answer):
                answer.append(now.val)
            
            # 트리의 오른쪽부터 탐색
            DFS(now.right, depth+1)
            DFS(now.left, depth+1)
            
        DFS(root, 0)
        return answer
