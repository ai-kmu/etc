# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        
        answer = []
        
        
        def find(node, idx):
            
            if node == None:
                return
            
            if len(answer) == idx:
                answer.append(node.val)
            
            # rigth를 탐색해서 성공하면 answer 길이가 +1 -> left 무시됨.
            find(node.right, idx+1)
            find(node.left, idx+1)
        
        find(root, 0)
        
        return answer
