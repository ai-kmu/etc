#BST 중위순회를 이용하되 왼쪽,부모,오른쪽을 보는것이 아니라 오른쪽,부모,왼쪽으로 순회
#순회를 하면서 sum_val에 이전값들과 자신의 값을 더한것을 저장한 후 자신의 node.val을 sum_val 값으로 바꿔줌
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        sum_val = 0
        def traverse(root): 
            nonlocal sum_val
            if root==None:
                return
            traverse(root.right)
            sum_val += root.val
            root.val = sum_val
            traverse(root.left)
        traverse(root)
        return root
