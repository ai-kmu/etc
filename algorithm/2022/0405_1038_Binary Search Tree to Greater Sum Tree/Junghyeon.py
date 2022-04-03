# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy


class Solution:
    '''
    DFS로 오른쪽 자식노드 -> 부모노드 -> 왼쪽 자식노드 순으로 탐색
    '''
    # 값을 누적시킬 변수
    total_val = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 복사본을 만들어서 복사본에 값 업데이트
        root_c = copy.deepcopy(root)
        
        # right -> root -> left로 탐색
        def DFS(root_c):
            # 빈 노드면 그냥 리턴
            if root_c == None:
                return
            
            DFS(root_c.right)
            # total_val에 값 누적
            self.total_val += root_c.val
            # 누적된 값을 업데이트
            root_c.val = self.total_val
            DFS(root_c.left)
        
        DFS(root_c)
        
        return root_c
