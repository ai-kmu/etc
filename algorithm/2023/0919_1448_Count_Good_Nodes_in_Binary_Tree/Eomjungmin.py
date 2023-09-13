class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root.left == None and root.right==None:
            return 1

        res = 0
        def dfs(root, path):
            nonlocal res
            if max(path) == root.val:
                res += 1
            if root.left != None:
                path.append(root.left.val)
                dfs(root.left, path)
                del path[-1]
            if root.right != None:
                path.append(root.right.val)
                dfs(root.right, path)
                del path[-1]
            if root.left == None and root.right == None:
                return

        dfs(root, [root.val])
        return res
