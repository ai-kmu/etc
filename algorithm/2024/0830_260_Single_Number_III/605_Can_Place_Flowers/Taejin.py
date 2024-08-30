class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        else:
            cnt = 0
            for i in range(len(flowerbed)):
                if flowerbed[i] != 1 and flowerbed[max(0, (i - 1))] == 0 and flowerbed[min((i + 1), len(flowerbed) - 1)] == 0:
                    flowerbed[i] = 1
                    cnt += 1

        print(flowerbed, cnt)
        return cnt >= n

        
