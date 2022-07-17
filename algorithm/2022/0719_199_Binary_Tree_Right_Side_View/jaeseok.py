# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def sol(node, depth):
            if node:
                output[depth] = node.val
                if node.right is not None or node.left is not None:
                    sol(node.left, depth + 1)
                    # 왼편의 노드에 의해 덮여진 동일한 depth의 노드는 오른편의 노드로 알아서 갱신됨
                    sol(node.right, depth + 1)
                else:
                    # 말단 노드에 도착하면 해당 depth의 노드 value 추가
                    output[depth] = node.val
        if not root:
            return []
        # 불가능한 값들로 output을 채움
        output = [101 for _ in range(100)]
        sol(root, 0)
        # 불가능한 값들을 제외한 list를 반환
        return list(filter(lambda x: x <= 100, output))
