import random

class Solution:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        new_sum = (mean * (len(rolls) + n) - sum(rolls))
        ret = []

        if 1 <= new_sum / n <= 6: # 평균 n개 + 남은수만큼 앞에서부터 채우기
            ret = [new_sum // n + (1 if i < new_sum % n else 0) for i in range(n)]
            return ret

        return ret
