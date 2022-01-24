#  출제자 comment

#  stack 이용. 

#  자식노드를 진행하다가 더이상 자식노드가 없을 때 pop을 하고 count를 +1하는 기본적인 접근방식은 같았는데  
#  pop을 한 원소를 inorder_arr에 넣는 일까지 추가하였다.

#  리스트를 따로 안만들고 k와 count가 일치할때, pop을 한 value를 return하는 방식으로도 생각해보면 좋을 것 같습니다. 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 왼쪽 탐색부터 그다음 오른쪽 반복 in-order
        stack = deque([])
        inorder_arr = []
        curr = root
        cnt = 0
        while curr is not None or stack:
            # 왼쪽 계속 넣어주고
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            # curr를 맨 left에서부터 시작
            curr = stack.pop()
            cnt += 1
            # 값 넣어주기
            inorder_arr.append(curr.val)
            if k == cnt: # k번째 되면 끝내기
                break
            # 본인의 right subtree 탐색
            curr = curr.right
        
        return inorder_arr[-1]
        
        
