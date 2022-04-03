# 중위순회를 거꾸로 하면서 노드 값을 축적, 축적된 값으로 자신의 노드를 갱신해가는 문제.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 노드 값 담을 변수
        sum = 0
        
        def reverse_inorder(root):
            # 이 함수의 지역변수가 아니기 때문에 nonlocal 달아줘야함
            nonlocal sum
            
            # 값이 있을 때만 더하고 갱신
            if root:
                # 우측 먼저
                reverse_inorder(root.right)
                
                # 현재 값까지 더해서
                sum += root.val
                
                # 값 갱신
                root.val = sum
                
                # 왼쪽 호출
                reverse_inorder(root.left)
        
        reverse_inorder(root)
        return root
