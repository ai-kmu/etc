# prefix 알고리즘 사용
# BST의 경우 prefix알고리즘을 사용하면 정렬되어 출력되는 것을 이용
# *주의* : ans와 rank는 모든 재귀함수 내에서 동기화 되어야 함


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def prefix(Tree, ans, rank, k):
            if rank >= k or Tree == None:
                return ans, rank
            
            ans, rank = prefix(Tree.left, ans, rank, k)
            if rank+1 == k:
                ans = Tree.val
                return ans, rank + 1
            return prefix(Tree.right, ans, rank+1, k)
        
        return prefix(root, -1, 0, k)[0]
