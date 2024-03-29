# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        answer = []

        # root가 아예 비어 있으면 빈 list를 return
        if root is None:
            return answer

        # root 노드부터 시작(TreeNode, node의 값, path)를 deque에 추가
        d = deque()
        d.appendleft((root, root.val, [root.val]))

        # root node부터 leaf node까지 순회
        while d:
            node, sum_value, path = d.popleft()
            # leaf node이면서 targetSum과 일치하는지 체크
            if sum_value == targetSum and node.left is None and node.right is None:
                answer.append(path)
                continue
            # 왼쪽에 갈 노드가 있으면 다음 node로 이동, 값의 합과 path를 동시에 갱신
            if node.left is not None:
                d.appendleft(
                    (node.left, sum_value + node.left.val, path + [node.left.val])
                )
            # 오른쪽에 갈 노드가 있으면 다음 node로 이동, 값의 합과 path를 동시에 갱신
            if node.right is not None:
                d.appendleft(
                    (node.right, sum_value + node.right.val, path + [node.right.val])
                )

        return answer
