class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        cnt = 0

        for i in range(len(num_str) - k + 1):
            cur_divisor = num_str[i: i+k]

            if int(cur_divisor) == 0:
                continue

            if num % int(cur_divisor) == 0:
                cnt += 1

        return cnt

