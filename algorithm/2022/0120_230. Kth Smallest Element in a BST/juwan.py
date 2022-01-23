
def inorderTraversal(root):
  """
  inorder로 순회하면 정렬된 리스트를 얻을 수 있음.
  
  """
        res = []
        if root:
            res = inorderTraversal(root.left) 
            res.append(root.val)
            res = res + inorderTraversal(root.right)
        return res


      
      
class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        result_list = inorderTraversal(root)
        
        return result_list[k-1]
            
    
