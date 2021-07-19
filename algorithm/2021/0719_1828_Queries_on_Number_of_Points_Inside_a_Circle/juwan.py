class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        count = 0
        output = []
        for circle in queries:
            x, y, r = circle
            for point in points:
                a, b = point
                if (a-x)**2 + (b-y)**2<= r**2:
                    count = count + 1
            output.append(count)
            count = 0
            
        return output
                
            
