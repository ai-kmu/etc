# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node_list = deque([root])
        node_val_list = []

        # 레벨 단위로 노드 순회
        while node_list:
            node = node_list.popleft()

            if node is not None:
                node_val_list.append(node.val)
                node_list.append(node.left)
                node_list.append(node.right)

        print(node_val_list)
        num_nodes = len(node_val_list)
        i = 0

        # 홀수 레벨의 노드들 reverse
        while 2**i < num_nodes:
            if i % 2:
                node_val_list[2**i - 1:2*(2**i - 1) + 1] = node_val_list[2**i - 1:2*(2**i - 1) + 1][::-1]
            i += 1

        node_val_list = deque(node_val_list)
        node_list.append(root)

        # 노드 값 반영
        while node_list:
            node = node_list.popleft()

            if node is not None:
                node.val = node_val_list.popleft()
                node_list.append(node.left)
                node_list.append(node.right)

        return root


        
