#  출제자 comment

#  중위 순회 구현

#  하나씩 방문하여 append를 하는 방식으로 취했다. 
#  원소를 다 추가한 뒤, return answer[k-1]을 이용하여 다 탐색한 뒤에 k번째 작은 수를 호출하였다. -- 1

#  1) 중간에 count를 따로 생성해서 노드를 방문해서 원소를 append를 할 때마다 count를 +1을 하게 만든다. 
#  -> count를 이용하여 정답을 출력하는 방식도 생각해보면 좋을 것 같습니다.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = None # 정답을 저장하기 위한 변수 self.ans를 None으로 초기화
        self.k = k # k를 밑에 find_ans 함수에서 사용하기 위해 self를 붙여서 선언
        
        # node가 주어질 때 node의 왼쪽을 보면서 동시에 self.k를 1 감소시킴
        # self.k가 0이면 이때 찾고자 하는 k번째 node이므로 이 node의 값을 return
        # 만약 찾고자 하는 k번째 수가 아니면 node의 오른쪽도 탐색
        # BFS랑 유사하게 코드 구동하는 식으로 구성함
        def find_ans(node):
            if self.ans == None and node:
                find_ans(node.left)
                self.k-=1
                if self.k == 0:
                    self.ans = node.val
                    return
                find_ans(node.right)
                
        find_ans(root)        
        return self.ans
