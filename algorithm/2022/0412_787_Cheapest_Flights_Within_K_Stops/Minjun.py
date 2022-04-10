import copy

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        if src == dst:
            return 0;
        
        prev = [float("inf")]*n
        
        prev[src] = 0
        
        
        for i in range(1, k+2):
            
            now = []*n
            
            for j in range(n):
                
                now[j] = prev[j]
                
            
            changed = False
            
            for flight in flights:
                
                x = flight[0]
                y = flight[1]
                z = flight[2]
                
                if prev[x] != float("inf") and prev[x] + z < now[y]:
                    
                    now[y] = prev[x] + z
                    changed = True
                    
            if not changed:
                break
            
            prev = copy.deepcopy(now)
        
        ans = 0
        
        if prev[dst] == float("inf"):
            ans = prev[dst]
            
        else:
            
            ans = prev[dst]
            
        return ans
    
    
    
    
    
