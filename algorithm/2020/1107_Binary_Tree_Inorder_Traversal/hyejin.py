class Solution:
    # 재귀를 이용한 inorder 탐색
    def visit(self, node): # node가 존재하지 않을 경우, return
        if node == None:
            return []
        
        # 존재할 경우, 재귀적으로 visit함.
        return self.visit(node.left) + [node.val] + self.visit(node.right)
    
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.visit(root)
    
        
