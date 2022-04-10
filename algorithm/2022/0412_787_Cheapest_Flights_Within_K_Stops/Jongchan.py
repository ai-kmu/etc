class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        nodes=[[float('inf')]*n for _ in range(n)] # 인접행렬 inf로 초기화
        
        for f in flights: # 인접행렬에 값 넣어주기
            nodes[f[0]][f[1]]=f[2];
        
        stop = -1
        cost = 0
        min_cost=float('inf')
        cur_visited=[]
        
        def dfs(cur_node):
            nonlocal stop, cost, min_cost
            
            
            if cur_node == dst: # 목적지에 도달하면 현재방향으로 탐색 그만
                if cost < min_cost:
                    min_cost = cost
                return
            
            if stop == k: # 주어진 stop수 k가 되면 현재 방향으로의 탐색 그만
                return
            
            for i in range(n):
                if nodes[cur_node][i] != float('inf') and i not in cur_visited: # 현재 가고있는 경로에서 이미 왔던 경로는 안감
                    cost += nodes[cur_node][i]
                    cur_visited.append(i)
                    stop += 1
                    #print(i)
                    dfs(i) # 재귀
                    cost -= nodes[cur_node][i]
                    cur_visited.pop()
                    stop -= 1

                    
        dfs(src)
        if min_cost == float('inf'): # 예외처리 -> 불가능하면 -1
            min_cost = -1
            
        return min_cost
