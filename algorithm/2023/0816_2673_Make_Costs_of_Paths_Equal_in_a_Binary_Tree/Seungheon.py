class Solution(object):
    def minIncrements(self, n, cost):

        # n = 6 -> 5 6 / 3 4 / 1 2 / 0

        # 바텀업 방식으로 두개씩 탐색
        # 차이만큼을 answer에 더해줌
        # 두 값중 큰값을 부모 노드에 더해준다

        answer = 0
        for i in range(n//2, 0 , -1):
            idx = i * 2 - 1
            answer += abs(cost[idx] - cost[idx+1])
            cost[idx//2] += max(cost[idx], cost[idx+1])
   
        return answer
