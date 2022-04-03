# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.val = 0
        
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 이진 트리에서 오른쪽에서 시작하는 중위순회로 값을 더하는 방식을 사용
        # 그래서 이 함수(bstToGst)를 재호출 하는 방법을 사용해야 함
        if root == None:
            return 0
        self.bstToGst(root.right) # 오른쪽 트리로 이동
        self.val += root.val # 맨 오른쪽 트리에서 중위순회로 값을 더해 나감
        root.val = self.val # Greater Tree로 바꿔야 하므로 각 요소에 누적해서 더한 값을 새로 대체
        self.bstToGst(root.left) # 왼쪽 트리가 있으면 왼쪽 트리로도 이동 계속 값을 더해 나감
        
        # root와 self.val 출력 결과
        # 출력 결과에서도 볼 수 있듯이 맨 아래 트리값인 8부터 중위 순회 순서로 값을 누적해서 더하면서
        # 각 요소에 값을 대체하는 것을 확인할 수 있다.
        
        # print(root, ", self.val: ", self.val)
        # TreeNode{val: 8, left: None, right: None} , self.val:  8
        # TreeNode{val: 15, left: None, right: TreeNode{val: 8, left: None, right: None}} , self.val:  15
        # TreeNode{val: 26, left: None, right: None} , self.val:  26
        # TreeNode{val: 21, left: TreeNode{val: 26, left: None, right: None}, right: TreeNode{val: 15, left: None, right: TreeNode{val: 8, left: None, right: None}}} , self.val:  26
        # TreeNode{val: 33, left: None, right: None} , self.val:  33
        # TreeNode{val: 35, left: None, right: TreeNode{val: 33, left: None, right: None}} , self.val:  35
        # TreeNode{val: 36, left: None, right: None} , self.val:  36
        # TreeNode{val: 36, left: TreeNode{val: 36, left: None, right: None}, right: TreeNode{val: 35, left: None, right: TreeNode{val: 33, left: None, right: None}}} , self.val:  36
        # TreeNode{val: 30, left: TreeNode{val: 36, left: TreeNode{val: 36, left: None, right: None}, right: TreeNode{val: 35, left: None, right: TreeNode{val: 33, left: None, right: None}}}, right: TreeNode{val: 21, left: TreeNode{val: 26, left: None, right: None}, right: TreeNode{val: 15, left: None, right: TreeNode{val: 8, left: None, right: None}}}} , self.val:  36
        
        return root # Greater Tree로 바꾼 결과를 출력
