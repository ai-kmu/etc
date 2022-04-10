import copy

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        cheapest = [float("inf")] * n
        
        cheapest[src] = 0
        
        
        
        
        for i in range(k):
            
            
            costs = copy.deepcopy(cheapest)
            
            for j in flights:
                
                u, v, w = j[0], j[1], j[2]
                
                
                if cheapest[u] == float("inf"):
                    continue
                    
                if cheapest[u] + w < costs[v]:
                    
                    costs[v] = cheapest[u] + w
            
            cheapest = costs
            
        if cheapest[dst] == float("inf"):
            return -1
        
        else:
            return cheapest[dst]
        
        
