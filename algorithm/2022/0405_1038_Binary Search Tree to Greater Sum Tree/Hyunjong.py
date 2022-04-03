# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 중위 순회 역순(left -> root -> right)으로 조회하면서 조회하는 노드의 값을 acc에 누적시킴
# input : root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# acc 값 누적 예시 : 8 -> 15 -> 26 -> 26 -> 33 -> 35 ->36 ->36 ->36 
# 
class Solution(object):
    acc = 0 # val 값 누적용 변수
    def bstToGst(self, root): 
        if root: # root가 None이 아닌 경우
            self.bstToGst(root.right) # 오른쪽 탐색
            self.acc += root.val # 값 누적
            root.val = self.acc # 값 적용
            self.bstToGst(root.left) # 왼쪽 탐색
        return root
