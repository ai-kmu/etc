class Solution:
    def minFlips(self, target: str) -> int:
        flippedNum = 0
        value = 0
        for t in target:  # t이후의 자리는 모두 value값(0 or 1)
            if int(t) != value:
                flippedNum += 1
                value = 0 if value == 1 else 1
        return flippedNum
