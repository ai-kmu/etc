class Solution:
    def tribonacci(self, n: int) -> int:
        ans_list = [0, 1, 1]
        answer = 0

        for i in range(n-2):
            answer += ans_list[i] + ans_list[i+1] + ans_list[i+2]
            ans_list.append(answer)
            answer = 0

        return ans_list[n]
