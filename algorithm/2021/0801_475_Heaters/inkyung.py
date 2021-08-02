class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        n = len(heaters)
        d = {}
        
        for i in houses:
            d[i] = float(inf)
            
        for i in houses:
            left = 0
            right = n
            
            while(left < right):
                mid = left + (right - left) // 2
                
                if heaters[mid] == i:
                    d[i] = abs(i - heaters[mid])
                    break
                elif heaters[mid] < i:
                    left = mid + 1
                    d[i] = min(d[i], abs(i - heaters[mid]))
                else:
                    right = mid
                    d[i] = min(d[i], abs(i - heaters[mid]))
        answer = 0
        for i in d:
            answer = max(answer, d[i])
        return answer
