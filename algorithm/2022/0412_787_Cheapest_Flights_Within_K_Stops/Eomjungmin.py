from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 각 노드에 대한 도착지와 cost를 dict형태로 저장
        dist_cost = defaultdict(list)
        for s, d, c in flights:
            dist_cost[s] += [[d, c]]
            
        # 초기 cost, stop, 시작점 src 선언
        # stop의 경우 맨 처음에 처음부터 어딘가로 갈 땐 stop이 0이므로 -1로 초기화
        h = [(0,-1,src)]
        
        
        dest_min_s = defaultdict(lambda: float(inf)) # src에서 해당 노드로 가는 최소 stop 수 저장. inf로 초기화.
        dest_min_s[src] = 0 # 현재 src의 최소 stop 수는 0
        
        while h:
            cost, stop, dest = heapq.heappop(h) # h를 heap로 선언한 후 cost가 가장 작은 cost,stop,dest 출력
            
            if  dest_min_s[dest] < stop: # 현재 dest 노드에 저장된 최소 stop수가 현재 stop보다 작으면 다음 루프로 넘어감
                continue
                
            if dest == dst: # 현재 dest가 dst에 도착하면
                return cost # 최종 cost를 출력
            
            dest_min_s[dest] = stop # 현재 dest 노드의 최소 stop 수 저장
            
            if stop < k: # stop 횟수가 k보다 작으면
                for d, c in dist_cost[dest]: # 현재 dest에서 다음으로 가는 노드에 대한 추가된 cost와 다음 노드 저장
                    heapq.heappush(h, (cost + c, stop + 1, d))
                    
        return -1
