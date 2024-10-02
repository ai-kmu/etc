# 풀이 실패

class Solution:
    def minFlips(self, s: str) -> int:
        s_odd, s_even = "", ""

        # 홀수, 짝수 인덱스 분리
        for idx, i in enumerate(s):
            if idx % 2 == 0:
                s_even += i
            else:
                s_odd += i
