class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        tmp_list = []

        for i in range(len(num_str) - k + 1):
            tmp_str = ''
            for j in range(i, i + k):
                tmp_str += num_str[j]
            tmp_list.append(int(tmp_str))

        ans = 0
        for n in tmp_list:
            if n != 0 and num % n == 0:
                ans += 1

        return ans
        
