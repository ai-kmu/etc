class Solution: # 코드 너무 지저분함
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
            
        idx = 0
        cnt = 0
        while idx < len(flowerbed):
            current_elem = flowerbed[idx]
            if current_elem == 1:
                idx += 2
            else:
                next_idx = idx + 1
                if next_idx < len(flowerbed) and flowerbed[next_idx] == 0:
                    cnt += 1
                    idx += 2
                elif next_idx == len(flowerbed):
                    cnt += 1
                    idx += 1
                else:
                    idx += 1

            if cnt == n:
                return True

        return False
