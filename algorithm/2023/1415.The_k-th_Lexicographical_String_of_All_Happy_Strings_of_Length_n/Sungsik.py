class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * 2**(n-1)
        if k > total:
            return ""

        chars = set('abc')
        last = ''

        result = ['']*n
        for i in range(n):
            choice = sorted(chars - set(last))
            total //= len(choice)
            last = choice[(k-1)//total]
            result[i] = last
            k %= total

        return ''.join(result)
