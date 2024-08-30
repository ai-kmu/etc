# 다듬고 싶은데 시간이 없어...
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)

        if n == 0:
            return True

        if length == 1:
            return bool(not flowerbed[0])
        
        elif length == 2:
            if n == 2:
                return False
            elif n == 1:
                return bool(not sum(flowerbed))

        elif length == 3:
            if n == 3:
                return False
            elif n == 2:
                if sum(flowerbed):
                    return False
                else:
                    return True
            elif n == 1:
                if flowerbed[1]:
                    return False
                else:
                    return sum(flowerbed) != 2

        # index가 홀수인 애들 -> 짝수인 애들 순으로 심어보기
        odd_first = n
        for i in range(1, length, 2):
            if i == (length - 1):
                left = flowerbed[i - 1]
                curr = flowerbed[i]
                if not curr:
                    odd_first -= int(not left)
            else:
                left = flowerbed[i - 1]
                curr = flowerbed[i]
                right = flowerbed[i + 1]
                if not curr:
                    odd_first -= int((not left) and (not right))
            if odd_first == 0:
                print("1")
                return True

        # index가 짝수인 애들 -> 홀수인 애들 순으로 심어보기
        even_first = n
        for i in range(0, length, 2):
            if i == 0:
                curr = flowerbed[i]
                right = flowerbed[i + 1]
                if not curr:
                    even_first -= int(not right)
            elif i == (length - 1):
                left = flowerbed[i - 1]
                curr = flowerbed[i]
                if not curr:
                    even_first -= int(not left)
            else:
                left = flowerbed[i - 1]
                curr = flowerbed[i]
                right = flowerbed[i + 1]
                if not curr:
                    even_first -= int((not left) and (not right))
            if even_first == 0:
                return True

        return False
                
