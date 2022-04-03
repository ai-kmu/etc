# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     
    
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        great_node = 0
        
        def sum_of_node(node: TreeNode) -> TreeNode:
            nonlocal great_node
            if node:
                sum_of_node(node.right)  #노드의 오른쪽부터 살펴본다.
                great_node += node.val   #great_node에 숫자를 누적한다.
                node.val = great_node    #값을 덮어 씌운다.
                sum_of_node(node.left)   #왼쪽으로 이동한다. 자기자신을 호출함으로써 재귀적이다.
        
        
        sum_of_node(root)
        
        return root
        
