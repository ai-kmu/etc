class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ret = []
        
        def find_conditioned_leaf(node, target, route):
            nonlocal ret
            if node is None:
                return

            elif node.left is None and node.right is None and target == node.val:
                ret.append(route + [target])

            else:
                route.append(node.val)
                find_conditioned_leaf(node.left, target - node.val, route)
                find_conditioned_leaf(node.right, target - node.val, route)
                route.pop()
        
        find_conditioned_leaf(root, targetSum, [])
        return ret

        
        
