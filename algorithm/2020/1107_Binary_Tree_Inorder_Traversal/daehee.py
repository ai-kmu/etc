class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        def recurr(root):                         # 각각 노드가 있는지 확인하고 inorder 순서로 변경해주기
            if root==None:
                return
            output=[]
            if recurr(root.left)!=None:
                output += recurr(root.left)
            output.append(root.val)
            if recurr(root.right)!=None:
                output += recurr(root.right)
            return output
            
        
        answer = recurr(root)
        
        return answer
