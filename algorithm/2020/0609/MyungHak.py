# 왼쪽과 오른쪽만 바꾸면 된다.
# 단 이 바꾸는 작업을 재귀적으로 수행해야 한다.
# 여기서 재귀가 끝날 조건은 root가 마지막에 도달하였을 겨우이다.

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None

        T = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = T
        return root

