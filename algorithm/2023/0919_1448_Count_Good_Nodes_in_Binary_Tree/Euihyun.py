# tree 다루는게 서툴러서 답 봤습니다.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def goodNodes(self, root):
        """
        이진 트리에서 "좋은 노드"의 개수를 세는 함수입니다.

        :param root: 이진 트리의 루트 노드
        :type root: TreeNode
        :return: "좋은 노드"의 개수
        :rtype: int
        """
        if not root:
            return 0
        
        def dfs(node, curMax):
            """
            깊이 우선 탐색 (DFS)을 사용하여 이진 트리를 순회하고 "좋은 노드"를 찾습니다.

            :param node: 현재 노드
            :type node: TreeNode
            :param curMax: 현재 경로에서의 최대값
            :type curMax: int
            """
            if not node:
                return
            if node.val >= curMax:
                count[0] += 1
                curMax = node.val
            dfs(node.left, curMax)
            dfs(node.right, curMax)
        
        count = [0]
        dfs(root, root.val)
        
        return count[0]
