class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 현재 값이 없으면 false 반환
        if not root:
            return False
        
        # 왼쪽, 오른쪽 둘 다 없으면 현재 값으로 target 만족 해야함
        if not root.left and not root.right:
            return root.val == targetSum
        
        new_target = targetSum - root.val
        
        # 왼쪽, 오른쪽에서 현재 값을 뺀 나머지를 해줄 수 있는지 확인
        # 둘 중 하나라도 성공하면 되기 때문에 `or`
        return (
            self.hasPathSum(root.left, new_target) or
            self.hasPathSum(root.right, new_target)
        )
