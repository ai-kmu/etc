class Solution(object):
    def minIncrements(self, n, cost):
        ans = 0  # 정답 초기화
        
        # 뒤에서부터 노드를 처리
        for i in range(n // 2 - 1, -1, -1):
            left, right = i * 2 + 1, i * 2 + 2
            
            # 현재 노드의 왼쪽 자식과 오른쪽 자식의 비용 차이를 더해줌
            ans += abs(cost[left] - cost[right])

            # 현재 노드의 비용을 자식 노드 중 더 큰 비용으로 조정
            cost[i] += max(cost[left], cost[right])

        return ans
