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
