class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthSmallest(self, root, k):
        stack = []
        rank = 0
        node = root
        while stack or node:  #stack 사용,처음에 stack 이 비어있으므로 node 조건에 포함.
            while node:  #현재 node에서 가장 왼쪽으로 이동.
                stack.append(node)  #가는 동안 stack 에 node append. 
                node = node.left
            
            node = stack.pop()  #위 과정에서 가장 왼쪽으로 간 후 -> 끝의 노드를 꺼냄.
            rank += 1  #1증가.
            if rank == k:  #증가 후 k 가 맞으면, 
                return node.val  #반환.
            node = node.right  #k가 아니면 right child, child 가 없는 경우 stack 에서 하나꺼내 위로 올라감.
