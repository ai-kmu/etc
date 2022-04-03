
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def bstToGst(self, root):
		global sum
		sum = 0
		def next_node(node):      
			global sum
			if not node:
				return
			else:
				next_node(node.right)
				sum += node.val
				node.val = sum
				next_node(node.left)
		next_node(root)
		return root
