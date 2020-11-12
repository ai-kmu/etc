class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = list()
        output = list()
        if not root:
            return []
        while True:
            while root:
                # 가장 왼쪽에 있는 값부터 담아야 하기 때문에 root.left가 None이 될 때까지 stack에 담기
                stack.append(root)
                root = root.left
            if stack == []:
                break
            # 담은 stack에서 하나씩 가져와서 val을 담고 root를 node.right로 갱신
            node = stack.pop()
            output.append(node.val)
            root = node.right
        return output
