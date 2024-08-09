# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # 만약 노드가 없으면 False 반환
        if root == None:
            return False
        
        # 현재 노드가 리프 노드이고, 그 값이 targetSum과 같다면 True 반환
        if root.left == None and root.right == None:
            return root.val == targetSum
        
        # 재귀적으로 왼쪽과 오른쪽 자식을 탐색하며 targetSum에서 현재 노드의 값을 뺌
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
