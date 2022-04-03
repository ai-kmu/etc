'''
# 오른쪽검사->값업데이트->왼쪽검사->위쪽노드로 이동
# 위의 과정 반복 후 더 이상 탐색할 노드가 없을 경우 종료

ex)Example 1 으로 설명. 4(root.val)시작.
4(root.right) -> 6(root.right) -> 7(root.right) -> 8(root.right) = null -> score : 8 = 0 + 8
7(root.right) = 8 -> score : 15 = 7 + 8
6(root.right) = 15 -> score : 21 = 6 + 15 
6(root.left) = 5 -> score : 26 = 5 + 21
4(root.right) -> score : 30 = 4 + 26 -> 4(root.left)로 넘어간다.
4(root.left) -> 1(root.right) -> 2(root.right) -> 3(root.right) = null -> score : 33 = 3 + 33
2(root.right) = 33 -> score : 35 = 2 + 33
1(root.right) = 35 -> score : 36 = 1 + 35
1(root.left) = 0 -> score : 36 = 0 + 36
4(root.left) -> 왼쪽 검사 끝났으므로, 종료.
'''

class Solution:
    # score 초기화
    def __init__(self):  
        self.score = 0
    
    def bstToGst(self, root: TreeNode) -> TreeNode:       
        if root is not None:
            # 오른쪽 검사
            self.bstToGst(root.right)  

            # 값 업데이트(반드시 오른쪽과 왼쪽 검사 사이에만 값을 업데이트해줘야함)
            self.score += root.val  
            # 해당 노드에 값 저장(example1, 파란색 숫자) 
            root.val = self.score   

            # 왼쪽 검사
            self.bstToGst(root.left)   

        # 올라간다
        return root  
    
    
   
            
        
