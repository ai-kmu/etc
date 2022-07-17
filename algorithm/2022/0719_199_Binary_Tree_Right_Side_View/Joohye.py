# 오른쪽 노드를 타고 내려가면 된다.
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 딕셔너리에 값 저장
        self.level = {}
        
        def dfs(root,i):
            if not root: 
                return 
            # 방문하지 않은 level의 노드라면
            if i not in self.level:
                self.level[i] = root.val
            # 재귀로 오른쪽 왼쪽 체크
            dfs(root.right, i+1)
            dfs(root.left, i+1)
         
        dfs(root,0)
        return self.level.values()
