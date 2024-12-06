# 이렇게 풀면 안되는데...
from collections import deque
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        # 모든 노드 다 저장
        vals = set([root.val])
        nodes = deque([root])
        while nodes:
            node = nodes.popleft()
            if node.left is None:
                continue
            vals.add(node.left.val)
            vals.add(node.right.val)
            nodes.append(node.left)
            nodes.append(node.right)

        # sort 해서
        vals = sorted(vals)
        # 하나면 -1
        if len(vals) == 1:
            return -1
        # 더 있으면 두 번째로 작은 거 반환
        else:
            return vals[1]
