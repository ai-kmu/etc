 class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    class Solution:
        def kthSmallest(self, root, k):
            stack = []                 # stack에 저장할 list 정의 
            rank = 0                   # 순서 정의 
            node = root                # node 정의

            while stack or node:      # stack 내부의 값이 없을 때까지 반복 (초기 stack의 경우 내부가 공란 -> 노드도 조건으로 정의)
                while node:           # 현재 노드(첫번째) -> 왼쪽으로 이동
                    stack.append(node) # 이동하면서 stack_list에 node 값을 저장
                    node = node.left   

                node = stack.pop()     # (왼쪽 도달 시) 끝의 node를 꺼냄
                rank += 1              # 기존 순서를 1 올림
                if rank == k:          # 올린 이후 정의한 k와 맞으면 해당 결과값을 반환 
                    return node.val
                node = node.right       # k가 맞지 않는다면 오른쪽으로 이동해 반복
