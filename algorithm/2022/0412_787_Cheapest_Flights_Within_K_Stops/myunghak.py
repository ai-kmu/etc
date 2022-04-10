# 다익스트라로 품
# 우선 시작 위치 부터 시작 위치까지의 거리는 0으로 초기화
# 그 후 아래 알고리즘을 반복
#         dst까지의 거리 = min(지금까지 구한 dst까지의 거리, 지금 까지 구한 src까지의 거리 + src에서 dst까지의 거리)

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        dist = [1000000] * n # 1000000은 수치상 나올수 있는 최대값
        dist[src] = 0
        
        for _ in range(k+1):
            tmp_dist = [d for d in dist]  # 이게 없으면 중간에 업데이트 된 dst와 그렇지 않은 dst가 혼존하여 문제가 발생

            for s, d, c in flights: # source, dst, src
                dist[d] = min(tmp_dist[s] + c, dist[d])
        
        return dist[dst] if dist[dst] != 1000000 else -1
