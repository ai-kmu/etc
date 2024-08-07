# 풀이실패 리뷰 안해주셔도 됩니다

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')
        
        def max_gain(node):
            if not node:
                return 0
            
            # 노드의 왼쪽 및 오른쪽 서브트리에서의 최대 경로 합
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # `node`가 경로의 가장 높은 노드일 때 새로운 경로의 가격
            price_newpath = node.val + left_gain + right_gain
            
            # 새로운 경로를 시작하는 것이 더 좋으면 max_sum 업데이트
            self.max_sum = max(self.max_sum, price_newpath)
            
            # 재귀를 위해:
            # 같은 경로를 계속하는 경우 최대 이익 반환
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)
        return self.max_sum
