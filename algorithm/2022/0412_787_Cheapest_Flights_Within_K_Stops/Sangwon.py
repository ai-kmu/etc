
#BFS를 활용하였다. 기존 경로에서 하나하나 경로를 탐색하여 방문한적 없는 새로운 곳이거나, cost가 더 적은 경우 새로 갱신하는 방식이다. 
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if src == dst: #시작점이 도착점과 같은 경우 0출력 
            return 0
        if not flights: #flights에 아무것도 없으면 -1 처리
            return -1
        
        graph = defaultdict(list)
        for start, destination, price in flights: #flights에서 시작점, 도착점, 가격을 가져온다음 딕셔너리로 지정한 graph에 넣었다. 
            graph[start].append((price, destination))
        
        res = {src:0} #result는 {시작지점:0}으로 설정
        self.BFS(graph, src, K, res)  #재귀적으로 탐색하여 경로를 저장하였다. 
        
        if dst in res:
            return res[dst] #res에 도착 지점이 있다면 누적된 price를 출력
        return -1 #없으면 도착 못한 것이므로 -1
    
    def BFS(self, graph, src, K, res):
        frontier = [src] #frontier에서 값을 하나씩 꺼내서 경로를 탐색.
        while frontier and K >= 0: #frontier에 원소가 있고 K(남은 횟수)가 0보다 크면 반복문을 실행한다. 
            nxt = [] #frontier에 원소를 하나씩 누적해야하기 때문에 다음 행선지를 담을 리스트를 설정
            nxt_cost = [] #cost에 관한 리스트를 설정
            for cur in frontier:   
                cur_cost = res[cur] #frontier에서 현재까지 탐색한 원소를 이용하여 res에 저장되어있는 price를 꺼낸다음, 경로를 하나씩 탐색하여 nxt_cost에 저장한다. 
                for price, destination in graph[cur]: 
                    nxt_cost.append((price+cur_cost, destination)) 
            for price, destination in nxt_cost: #nxtcost에서 하나씩 꺼내서 방문한적이 없는 새로운 경로거나 기존 도착지점까지의 값 보다 더 작은 경우 res안에 있는 값을 갱신
                if destination not in res or price < res[destination]: 
                    res[destination] = price 
                    nxt.append(destination)
            frontier = nxt #nxt에 누적한 원소들을 frontier에 넣는다. 
            K -= 1 #정해진 k횟수이내로 도착해야 하므로 k에서 -1을 한다. 
        return
      
#res = {0:0}  frontier = [0]
#res = {0:0, 1:100} frontier = [0, 1]
#res = {0:0, 1:100, 2:200, 3:600} frontier = [0, 1, 2, 3]
#res에 3이 있으므로 600을 출력
