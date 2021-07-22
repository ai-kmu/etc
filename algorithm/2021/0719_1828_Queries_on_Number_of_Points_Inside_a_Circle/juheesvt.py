class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []
        for i, j, r in queries:
            result.append(0)
            for x, y in points:
                
                if (x-i)**2+(y-j)**2 <= r**2:
                    result[-1] += 1
        return result
        
