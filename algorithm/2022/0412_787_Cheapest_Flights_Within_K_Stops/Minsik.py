'''
풀이과정

1. 각 도시별 이동시 비행 비용을 저장할 list를 생성
2. DP를 활용해 각 city 방문마다 드는 비용을 저장(행: 횟수) 

예
1단계: 첫번재 행의 출발점 도시의 0의 값을 할당
=> [[0, inf, inf, inf], [inf, inf, inf, inf], [inf, inf, inf, inf]]

2단계: 다음 행부터는 (2번째행은 출발점 기준) 이전 city에서 이동할 수 있는 구간들에 대해서 비용 값을 할당
# 1. 출발점의 해당하는 city는 0으로 할당
# 2. 이후 이동 그래프 내에서 이전 city가 존재할 경우 다음 city의 해당 비용을 가산
=> [[0, inf, inf, inf], [0, 100, inf, inf], [inf, inf, inf, inf]]

3단계: 2단계를 반복하면 마지막 행에서의 최종 목적지 city 우리가 찾고자 하는 최소 비용이 됨
=> [[0, inf, inf, inf], [0, 100, inf, inf], [0, 100, 200, 700]]
'''

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):

        # 비행 비용을 저장할 list 저장 =>  열: 도시, 행: 이동 city 개수
        cost = []
        for _ in range(K + 2):           # K + 2 => (출발지, 도착지 포함)
            city = []
            for _ in range(n):
                city.append(float('inf')) # 최초 초기화 시 inf로 초기화(최소값 탐색)
            cost.append(city)   

        # 출발점의 값 할당: 0 / 해당 출발 도시 이외에는 다른 도시는 갈 수 없기에 inf로 저장
        cost[0][src] = 0      

        # 출발지를 제외한 나머지 city 탐색 진행
        for i in range(1, K+2):
            cost[i][src] = 0                # 다음 city에서 비용 중 이미 방문한 곳은 0 입력

            # i번째 때 각 도시의 이동 비용 => 이동 graph 값들을 확인하면서, 이전 city에서 현재 city로의 값을 갱신해 나감
            for fly in flights:
                cost[i][fly[1]] = min(cost[i][fly[1]], cost[i - 1][fly[0]] + fly[2])

        # 해당 경로가 없으면 -1 반환(조건)
        if cost[K + 1][dst] == float('inf'):
            return -1

        return cost[K + 1][dst]
