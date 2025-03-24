class Solution:
    def sumBase(self, n: int, k: int) -> int:
        answer = 0
        while n:
            n, r = divmod(n, k)
            answer += r
        return answer
