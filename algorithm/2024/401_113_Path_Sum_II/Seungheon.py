from collections import defaultdict

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        answer_list = []

        # backtracking
        def dfs(node = root, node_list = []):

            node_list.append(node.val)
            if node.left is None and node.right is None and sum(node_list) == targetSum:
                answer_list.append(node_list.copy())

            if node.left:
                dfs(node.left, node_list)
                node_list.pop()

            if node.right:
                dfs(node.right, node_list)
                node_list.pop()
        
      # 예외처리      
        if root:
            dfs()
        
        return answer_list
