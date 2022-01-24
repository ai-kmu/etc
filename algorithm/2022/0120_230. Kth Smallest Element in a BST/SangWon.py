# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        stack = []
        
        while True:
            while root:
                stack.append(root) #root를 stack에 넣으면서 왼쪽우선으로 이동 
                root = root.left 
            root = stack.pop() #왼쪽에 아무것도 없을 때 pop()을 수행, k가 카운트인데 카운트를 하나씩 줄임
            k -= 1 
            if not k:                 #k가 0일때 root의 값을 반환 
                return root.val
            root = root.right         #pop을 했는데도 k가 아직 0이 아니면 오른쪽을 보기 
        
