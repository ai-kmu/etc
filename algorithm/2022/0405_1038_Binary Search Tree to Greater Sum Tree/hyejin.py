# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum_of_node = 0
        
        def calc_node(root):
            if not root:
                return 0
            # 오른쪽은 기준 node보다 매번 큼 - 오른쪽부터 업데이트
            calc_node(root.right)
            # 원래 키보다 모든 키의 합
            self.sum_of_node += root.val
            # 자기 기준 root value update
            root.val = self.sum_of_node
            
            # left로 탐색
            calc_node(root.left)
        
        calc_node(root)
        
        return root
