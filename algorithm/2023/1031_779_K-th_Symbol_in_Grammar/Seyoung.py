# 여러 솔루션을 참고해서 풀었으므로 리뷰 안해주셔도 괜찮습니다.

import math

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        # n-1번째 행의 길이
        prew_row = 2 ** (n - 1)  

        # n-1번째 행에서 k번째 열 = n번째 행에서 (k+1) // 2 번째 열
        prev_k = self.kthGrammar(n - 1, (k + 1) // 2) 

        if prev_k == 0:
            return 0 if k % 2 == 1 else 1
        else:
            return 1 if k % 2 == 1 else 0


