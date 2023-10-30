import math


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        self.answer = 0

        def dfs(k, flag):
            if k == 1:
                self.answer = 1 if flag is True else 0
                return

            if k % 2 == 0:
                flag = not flag

            return dfs(math.ceil(k / 2), flag)

        if k <= 2:
            return [0, 1][k - 1]

        dfs(k, False)

        return self.answer
