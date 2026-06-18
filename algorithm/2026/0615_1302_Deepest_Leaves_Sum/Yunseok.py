# 풀이 안해주셔도 됩니다

from collections import defaultdict

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        nodeLevel = defaultdict(list)

        def dfs(currentNode : TreeNode, level: int):

            if not nodeLevel[level]:
                nodeLevel[level] = []

            nodeLevel[level].append(currentNode.val)

            if currentNode.left:
                dfs(currentNode.left, level + 1)

            if currentNode.right:
                dfs(currentNode.right, level + 1)

        dfs(root, 0)

        maxLevel = max(nodeLevel.keys())

        result = sum(nodeLevel[maxLevel])

        return result
