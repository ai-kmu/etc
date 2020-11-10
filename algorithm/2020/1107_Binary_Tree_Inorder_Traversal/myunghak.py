# inorder travere 재귀
class Solution:
    def inorderTraversal(self, root):
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

    
    
    
    
    
    
# inorder travere 반복문
    
# class Solution:
#     def inorderTraversal(self, root):
#         stack = [root] if root else []
#         ans = []
#         while(len(stack) > 0):
#             T_node = stack.pop()

#             while(T_node):
#                 stack.append(T_node)
#                 T_node = T_node.left
#                 stack[-1].left = None
#             T_node = stack.pop()
            
#             if T_node:
#                 ans.append(T_node.val)
#                 stack.append(T_node.right) if T_node.right else None
#                 T_node = None
#         return ans
