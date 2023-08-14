class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:

        # 무한 루프를 방지하기 위해 1번부터 시작하도록 0번 index를 채워넣음
        cost.insert(0, -1)
        
        self.answer = 0

        def dfs(node):
            # 트리를 벗어나는 노드 처리
            if node > n:
                return 0
            
            # 왼쪽과 오른쪽을 비교해서 두 경로가 같은 cost를 가지도록 더해야 하는 양을 answer에 추가
            left = dfs((node * 2))
            right = dfs((node * 2) + 1)
            self.answer += abs(left - right)
            # 최대 cost를 유지하면서 위로 거슬러 올라감
            return cost[node] + max(left, right)

        dfs(1)

        return self.answer
