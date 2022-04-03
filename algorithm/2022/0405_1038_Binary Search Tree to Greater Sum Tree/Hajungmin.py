class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class에서 멤버 변수로 total_sum을 만들어주어 트리를 순회하며 더해줄 변수를 만든다.
# global로 total_sum을 선언시에는 테스트 케이스만 통과라 나오고 이후 첫 번째 케이스에서 wrong answer가 나오게 되는데 한 테스트 후에 다른 테스트실행시 global로 실행된 변수에 대해서 초기화가 안되는 듯하다...

class Solution:
    def __init__(self):
        self.total_sum = 0 
        
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 만약 root가 None이 아닐 시 트리의 오른쪽부터 후위순회를 시작한다.
        # 이후 만난 root를 total_sum에 더해주고 root의 값을 바꿔준다 이후 전위 순회를 해주며 트리의 오른쪽에서 왼쪽으로 순회하며 값을 바꿔준다.
        if root:
            self.bstToGst(root.right)
            self.total_sum += root.val
            root.val = self.total_sum
            self.bstToGst(root.left)
            
        # 이후에 값을 바꿔준 트리를 반환해준다.
        return root
