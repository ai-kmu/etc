# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # 좋은 노드의 개수를 count하는 것
        
        cnt = 0
        temp = []
        def recur(node, cur_path):
            nonlocal cnt

            if node.val == None: # 만약 null 값이라면 리턴
                return

            cur_path.append(node.val) # 현재까지의 path 저장

            if node.val >= max(cur_path): # 현재 노드 값이 path의 최대값보다 크거나 같으면 증가
                cnt += 1

            cur_path1 = cur_path.copy() # left와 right에 path를 넣어주기 위한 copy
            cur_path2 = cur_path.copy() # 만약 copy 안하면 call by reference라 path가 제대로 저장 안됨
            
            if node.left:                
                recur(node.left, cur_path1)
            if node.right:
                recur(node.right, cur_path2)

        recur(root, temp)

        return cnt
