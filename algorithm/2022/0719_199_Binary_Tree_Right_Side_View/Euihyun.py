# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        def search(node, level):
            # node 가 비어 있으면 리턴으로 탈출
            if node == None:
                return
            
            # 층에 값을 넣지 않았으면 ans에 추가(null은 바로 리턴되서 한층에 하나씩만 추가됨)
            if level == len(ans):
                ans.append(node.val)
                
            # 오른쪽만 볼거니까 오른쪽 부터 탐색
            search(node.right, level + 1)
            
            # 오른쪽 없이 왼쪽만 있을 경우를위해 왼쪽 탐색
            search(node.left, level + 1)
            return ans
        
        return search(root, 0)
    
    
