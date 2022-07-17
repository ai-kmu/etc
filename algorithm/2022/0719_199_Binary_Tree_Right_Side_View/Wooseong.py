# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''예외처리: 빈 root에 대해선 [] 반환'''
        if not root:
            return []
            
        '''
        변수 설정
            윗층  = parent들 - 처음은 root
            아래층 = child들
            답의 0번째 요소는 root.val
        '''
        parents = deque([root])
        children = deque()
        answer = [root.val]
        
        '''BFS'''
        while parents:
            '''
            한 단계 씩 처리
                1. parents 안의 각 parent의 left right(=child)를 나눠서 children에 넣어둔다
                2. 맨 마지막으로 넣은 거(= righside)를 answer에 더한다
            '''
            while parents:
                parent = parents.popleft()
                if parent.left:
                    children.append(parent.left)
                if parent.right:
                    children.append(parent.right)
            if children:
                answer.append(children[-1].val)

            '''
            해당 층에 대한 업데이트 끝남
                -> 이제 children이 새로운 parents가 되고 children은 비운다
            '''
            parents = children
            children = deque()

        return answer
