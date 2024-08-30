class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i, v in enumerate(flowerbed):
            if v == 0:
                if i == len(flowerbed) - 1 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                elif i == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            if n == 0:
                return True
                
        return False
