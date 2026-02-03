class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        return sum([1 for i in range(len(str(num)) - k + 1) if ((int(str(num)[i:i+k]) != 0) and (num % int(str(num)[i:i+k]) == 0))])
