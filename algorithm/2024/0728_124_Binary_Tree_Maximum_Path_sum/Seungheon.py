class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        answer = -float(inf)

        def explore(node = root):
            nonlocal answer

            if node == None:
                return 0

            node_val, left_val, right_val = node.val, explore(node.left), explore(node.right)

            case_1 = node_val
            case_2 = node_val + left_val
            case_3 = node_val + right_val
            case_4 = node_val + left_val + right_val

            answer = max(answer, case_1, case_2, case_3, case_4)

            return max( case_1, case_2, case_3)

        explore()

        return answer
