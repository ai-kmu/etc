# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        queue = [root]
        # bfs를 수행하면서 각 level마다 최대인 값만 넣으면 됌
        while queue:
            max_of_curr_level = None # 순서대로 집어넣기 때문에 가장 마지막값이 max 값임
            # level마다 queue다시 생성
            new_queue = []
            for node in queue: # 현재 level의 queue를 탐색
                if node is None: # node가 None이면 그냥 패스
                    continue
                new_queue.append(node.left)
                new_queue.append(node.right)
                max_of_curr_level = node.val
            queue = new_queue
            if max_of_curr_level is not None: # 현재 level에서 값이 들어있으면 추가
                answer.append(max_of_curr_level)
            
        return answer
