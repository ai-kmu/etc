# 다듬고 싶은데 시간이 없어...
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # 예외처리 1: n = 0이면 무조건 됨
        if n == 0:
            return True

        length = len(flowerbed)

        # 예외처리 2
        # 길이가 1일 때는 아래 for문 사용 못함
        if length == 1:
            return bool(not flowerbed[0])
        
        # 예외처리 3
        # 어쩌다 보니 해놨는데, 있으면 속도가 빨라져서 냅둠
        # 길이가 2일 때
        elif length == 2:
            # 2개는 못 심음
            if n == 2:
                return False
            # 하나라도 심어져 있으면 1개도 못 심음
            elif n == 1:
                return bool(not sum(flowerbed))

        # 길이가 3일 때
        elif length == 3:
            # 3개는 못 심음
            if n == 3:
                return False
            # 2개를 심으려면
            elif n == 2:
                # 하나도 안 심어져 있어야 함
                if sum(flowerbed):
                    return False
                else:
                    return True
            # 1개를 심으려면
            elif n == 1:
                # 가운데에는 없어야 됨
                if flowerbed[1]:
                    return False
                # 가운데 말고 하나 정돈 심어져도 됨
                else:
                    return sum(flowerbed) != 2

        # index가 홀수인 애들 -> 짝수인 애들 순으로 심어보기
        # 자기 기준으로 좌우에 없을 때 하나 씩 빼서 0이 되면 True
        # 양끝에서는 바로 옆에 하나만 보면 됨
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

        # 홀수 -> 짝수도 안 되고 짝수 -> 홀수도 안 되면 안 되는 거임
        return False
