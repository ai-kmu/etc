class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        coords = []  
        res = []  
        
        for i, j ,k in buildings: 
            coords.append([i,-k])
            coords.append([j,k])
        
        coords.sort()

        pq = [0]
        prev_max = 0

        for i in coords:
            if i[1]<0:
                pq.append(i[1]*-1)          
            else:
                pq.remove(i[1])
            
            curr_max = max(pq)
            if prev_max != curr_max:
                res.append([i[0],curr_max])
                prev_max = curr_max
        
        return res
