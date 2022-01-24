#  출제자 comment

#  중위 순회 구현

#  하나씩 방문하여 append를 하는 방식으로 취했다. 
#  원소를 다 추가한 뒤, return answer[k-1]을 이용하여 다 탐색한 뒤에 k번째 작은 수를 호출하였다. -- 1

#  1) 중간에 count를 따로 생성해서 노드를 방문해서 원소를 append를 할 때마다 count를 +1을 하게 만든다. 
#  -> count를 이용하여 정답을 출력하는 방식도 생각해보면 좋을 것 같습니다.

class Solution(object):
    def kthSmallest(self, root, k):
        # 값을 저장시키기 위해 생성
        result = []
        # 제일 왼쪽아래(가장 작은값)부터 차례대로 result에 추가
        def Traversal( root, result):
            # 이동 했을때 node가 null이면 아무 행동을 안하도록
            if root:
                # 왼쪽 아래 노드 부터 탐색
                Traversal(root.left, result)
                # 마지막으로 탐색한 노드의 val 값을 result에 추가
                result.append(root.val)
                # 왼쪽 노드 탐색 후 오른쪽 노드 탐색
                Traversal(root.right, result)
        
        Traversal(root, result)
        # 작은값부터 추가된 result에서 node에서 k 번째로 작은 값 반환
        return result[k- 1]
