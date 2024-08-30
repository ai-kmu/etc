class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        for i, val in enumerate(flowerbed):
            if val == 0 and self.is_in_rule(flowerbed, i):
                cnt += 1
                flowerbed[i] = 1
        return cnt >= n


    def is_in_rule(self, arr, index):
        # 넣을 수 있다면 True, not False
        try: 
            if index == 0:
                return arr[index+1] != 1
            elif index == len(arr)-1:
                return arr[-2] != 1
            else:
                return arr[index-1] != 1 and arr[index+1] != 1
        except IndexError:
            print(arr)
            print(index)
            return False
