# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
## BST는 왼쪽 트리값 < root값 < 오른쪽 트리값 으로 구성되어 있다
## 중위 탐색(left -> root -> right)을 하면 정렬된 순서로 만들 수 있다
## recursive한 방법

        ans = []
        self.inorder(root, ans)
        return ans[k-1]
    
    def inorder(self, root, ans):
        ## root를 전부 탐색했으면 return ans
        if not root:
            return ans

        ## 탐색할 root가 남은 경우
        ## 왼쪽 탐색
        if root.left:
            self.inorder(root.left, ans)
        
        ## root 저장
        ans.append(root.val)
        
        ## 오른쪽 탐색
        if root.right:
            self.inorder(root.right, ans)
