class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ans = 0
        str_num = str(num)

        for i in range(len(str_num)-k+1):
            if set(str_num[i:i+k]) == {'0'}:
                pass
            elif num % int(str_num[i:i+k]) == 0:
                ans += 1
        return ans
