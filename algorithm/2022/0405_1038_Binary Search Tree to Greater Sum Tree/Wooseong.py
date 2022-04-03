# 가장 큰 값인 오른쪽 맨 아래에서 시작해서
# 한 단계 씩 올라왔다 내려왔다가 하면서 누적해서 더해나감

# 오른쪽 맨 아래로 가는 법 = DFS

class Solution:
    def dfs(self, node):
        # print(f"input: {node}, accumulation = {self.accum}")
        if not node: return 
        
        # 오른쪽에서 먼저 시작
        self.dfs(node.right)
        
        self.accum += node.val
        node.val = self.accum
        
        # 그 다음 왼쪽 더함
        self.dfs(node.left)
            
    def bstToGst(self, root):
        self.accum = 0 # 누적해서 더하기 위한 self.accum
        self.dfs(root) # recursive DFS

        return root
