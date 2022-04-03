
# in-order traverse를 하면서 전역변수에 숫자를 하나씩 더해주기만 하면된다.
# 단 이 때 순서는 left --> middle --> right이다.
# 그리고 함수를 실행 전 함수 내에서 공유할 summation이라는 변수를 0으로 초기화 해주어야 하낟.

summation = 0

class Solution:
    def rec_func(self, root):
        global summation
        if root:
            self.rec_func(root.right) # 오른쪽부터 탐색
            summation += root.val
            root.val = summation
            self.rec_func(root.left) # 왼쪽 탐색
        return root
    
    def bstToGst(self, root: TreeNode):
        global summation
        summation = 0 # 공유할 변수 초기화

        return self.rec_func(root)
        
