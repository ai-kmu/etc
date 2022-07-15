# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        answer = []
        search_depth = 0    

        def search(node, height):
            
            nonlocal search_depth
            if node == None:
                
                return
            
            if height == search_depth:
                search_depth += 1
                answer.append(node.val)
            search(node.right, height + 1)
            search(node.left, height + 1)
            
        search(root, 0)
        
        return answer
                
            
