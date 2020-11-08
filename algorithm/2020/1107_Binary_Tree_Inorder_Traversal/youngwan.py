class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorderTra(root):                            # inorder 탐색 함수
            inorder = []
            if root.left:                                # 왼쪽 노드 탐색
                inorder += inorderTra(root.left)
            inorder.append(root.val)                     # 가운데 노드 탐색
            if root.right:
                inorder += inorderTra(root.right)        # 오른쪽 노드 탐색
            return inorder
            
        inorder_list = [] 
        if root:
            inorder_list = inorderTra(root)
        return inorder_list
