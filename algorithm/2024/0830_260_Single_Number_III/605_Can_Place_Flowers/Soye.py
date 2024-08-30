class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            cnt = cnt + 1
        if flowerbed[len(flowerbed)-2] == 0 and flowerbed[len(flowerbed)-1] == 0:
            flowerbed[len(flowerbed)-1] = 1
            cnt = cnt + 1
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 0:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    cnt = cnt + 1
                    flowerbed[i] = 1

        if n <= cnt:
            return True
        else:
            return False             
