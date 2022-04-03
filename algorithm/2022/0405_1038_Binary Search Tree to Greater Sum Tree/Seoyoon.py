# 가장 큰 숫자부터 내림차순으로 값을 누적하여 기존 노드 값을 변경해가는 문제
# 중위 순회를 거꾸로 하여 노드값 누적
# 오른쪽 노드-> 부모노드 -> 왼쪽 노드 순으로 순회

class Solution:
    ssum = 0 # 누적할 변수
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        if not root: # 노드가 없는 경우
            return root
        
        else: # 노드가 있는 경우
            self.bstToGst(root.right) # 현재 노드의 오른쪽 서브트리 순회
            self.ssum += root.val  # 맨 마지막 오른쪽 트리에 도달하면 현재 노드 누적
            root.val = self.ssum # 현재 노드를 업데이트
            self.bstToGst(root.left) # 다음으로 중위순위 역순으로 left 순회
            
        return root
