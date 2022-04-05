# 늦게 제출해서 죄송합니다..ㅠㅠ

'''
- 트리를 중위순회(왼쪽 subtree -> root -> 오른쪽 subtree) 하면 오름차순 정렬
- 그래서 트리를 오른쪽 subtree -> root -> 왼쪽 subtree 로 순회하면서 방문하면 내림차순 정렬대로 노드를 방문하게 됨
'''
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
        
        
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        global sum1
        sum1 = 0
        
        def traverse(node):
            global sum1
            if not node: return
            else:
                traverse(node.right) # 오른쪽 subtree 부터 탐색
                sum1 += node.val # val 값을 누적
                node.val = sum1 # node 값을 update
                traverse(node.left) # 왼쪽 subtree 탐색
                
        traverse(root)
        return root
