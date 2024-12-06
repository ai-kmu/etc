# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        print(root)
        results = set()
        self.dfs(root, results)
        
        results_list = list(results)
        results_list.sort()
 
        if len(results_list) > 1:
            return results_list[1]
        else:
            return -1

    
    def dfs(self, input_node, results_list):
        if input_node == None:
            return None
        
        left_node = None
        right_node = None

        results_list.add(input_node.val)

        left_node = self.dfs(input_node.left, results_list)
        right_node = self.dfs(input_node.right, results_list)
        if left_node == None and right_node == None:
            return input_node.val
