# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.answer = list()  # 정답 경로 
        
        if root == None:  # None input 예외 처리
            return self.answer
        
        self.dfs(root, [root.val], root.val, targetSum)  # root node부터 탐색 시작 
        return self.answer


    def dfs(self, node : TreeNode, current_path : list, currentSum : int, targetSum : int):
        '''
        node : 현재 node 
        current_path : 현재 node를 오는데까지의 경로 
        currentSum : 현재 node 까지의 합
        targetSum : 문제에 주어짐
        
        [0] + [1] -> [0, 1]
        '''
        if node.left == None and node.right == None:  # 현재 node가 leaf node라면 
            if currentSum == targetSum:
                self.answer.append(current_path)  # left node 임과 동시에 조건 만족시 정답 추가
            return
        
        if node.left != None:
            self.dfs(node.left, current_path + [node.left.val], currentSum + node.left.val, targetSum)
        if node.right != None:
            self.dfs(node.right, current_path + [node.right.val], currentSum + node.right.val, targetSum)
        
        
        
        

        
        
        

        




