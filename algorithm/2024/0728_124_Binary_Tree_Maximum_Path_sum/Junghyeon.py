# 재귀적으로 탐색하며 최대 경로 합을 갱신
class Solution:
    def maxPathSum(self, root):
        # 범위는 -1000 ~ 1000
        self.max_num = -1001
            
        def get_val(node):
            if not node:
                return 0
            
            left = max(get_val(node.left),0)
            right = max(get_val(node.right),0)
            
            sum_tmp = node.val + left + right
            self.max_num = max(self.max_num, sum_tmp)
            
            return node.val + max(left, right)
        
        get_val(root)
        
        return self.max_num
