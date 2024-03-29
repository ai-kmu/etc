# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# targetSum을 만족하는 path -> DFS로 해결

class Solution:

    def DFS(self, root, path, ans, sum_val):
        if not root:
            return
        
        # 경로 저장
        path.append(root.val)
        
        if not root.left and not root.right and sum_val == root.val:
            ans.append(list(path))
        
        # DFS 탐색 진행
        self.DFS(root.left, path, ans, sum_val - root.val)
        self.DFS(root.right, path, ans, sum_val - root.val)
        path.pop()
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        self.DFS(root, [], ans, targetSum)
        return ans
