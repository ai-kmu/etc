# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    
    
    def recursion(self, node: TreeNode) -> TreeNode:
        """
        재귀 함수 이용
        
        Binary Tree에서 child node의 오른쪽이 우선 순위임. 따라서 오른쪽을 먼저 탐색.
        그런데, 자세히 보면 child node의 값을 parent node에 더해주는 것이 아니라,
        단순히 오른쪽 -> 왼쪽으로가며 그 값을 더해주는 것임.
        문제는 반환해야하는 값이 처음에 주어진 Tree와 동일한 구조를 가져야함.
        
        단순히 List를 이용하여 오른쪽으로 Inorder priorty로 값을 더해서 저장해주었다가 나중에
        트리 구조와 동일하게 값을 넣어 할 순 있지만 그건 매우 귀찮음.
        
        오른쪽으로 Inorder 탐색과 동시에 그 노드의 값을 바꿔줄거임 ㅇㅇ.
        
        그렇게하면 트리를 다시 만들 필요도 없음. 
        
        
        """

        if node:
            self.recursion(node.right)
            self.accumulate_value = self.accumulate_value + node.val
            node.val = self.accumulate_value
            self.recursion(node.left)
            
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        self.accumulate_value = 0 # 누적 합계를 Recursion을 활용하여 node value를 바꿔주는 방식으로 진행할 것임.
        self.recursion(root)
        
        return root
        
        
