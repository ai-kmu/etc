class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0, 1]
        count = 0
        answer = 0
        
        for f in flowerbed:
            if f:
                answer += max((count - 1) // 2, 0)
                count = 0
            else:
                count += 1
        return answer >= n
