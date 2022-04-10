class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # cost를 저장하는 리스트와 시작지점에서 cost를 선언해줌
        # cost를 처음 초기화할 때는 inf값으로 초기화
        costs = [float('inf')] * n
        costs[src] = 0
        
        # k라는 제한이 있고 현재 노드 다음부터 고려해야하기 때문에 k+1번 만큼 루프를 돈다
        for i in range(k+1):
            # temp에 cost리스트를 복사한 후에 사용
            tempcosts =  costs.copy()
            
            # flights에서 차례로 start, destination, cost를 불러옴
            for s, d, c in flights:
                #만약 cost가 inf라면 업데이트를하지 않음
                if costs[s] == float('inf'):
                    continue
                # 만약 현재 cost에 노드까지 더해진 cost를 더한 것이 도착노드의 cost보다 작으면 temp에 있는 cost를 업데이트 한다
                if costs[s] + c < tempcosts[d]:
                    tempcosts[d] = costs[s] + c
            # 이후 temp에 있는 값들로 cost리스트를 업데이트한다.
            costs = tempcosts 
            
        # 만약 cost가 inf값이라면 -1을 반환하고 아니라면 현재 cost를 반환
        if costs[dst] == float('inf'): return -1
        else: return costs[dst]
