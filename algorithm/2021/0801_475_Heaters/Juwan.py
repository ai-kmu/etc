import sys

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        
        houses.sort()
        heaters.append(-sys.maxsize)
        heaters.append(sys.maxsize)
        heaters.sort()
        
                
        radius, j = 0, 0
        for i in range(1, len(heaters)):
            while j < len(houses) and houses[j] <= heaters[i]:
                radius = max(radius, min(heaters[i]-houses[j], abs(heaters[i-1]-houses[j])))
                j += 1
        return radius
