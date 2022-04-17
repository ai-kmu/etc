# dp[L][R] = s1 - s2
# => nums[L:R+1]를 갖고 했을 때
# player1의 score(s1)과 player2의 score(s2)의 차이.

# 그러니까 답은
# nums[0:-1]를 갖고 했을 때 s1 >= s2이므로
# dp[0][-1] >= 0이 된다.

class Solution:
    def PredictTheWinner(self, nums):
        n = len(nums)
        # 만약 n = 1이면 player1만 뽑고 끝나니까
        # 무조건 이김
        if n == 1: return True

        # n 행, 그니까 L = n까진 안 만들어도 된다
        dp = [[0] * n for _ in range(n)]
        
        # 왜냐면 nums[L:R+1]을 가지고 볼 거기 때문이고
        # L = R = n인 경우는 n = 1과 동치이기 때문
        for diff in range(n):
            for L in range(n - diff):
                R = L + diff
                # L = R이면 하나 남은 거니까 player1이 그거 뽑고 끝남
                # s1 = nums[L], s2 = 0 => dp[L][R] = nums[L]
                if L == R: dp[L][R] = nums[L]

                # 그 외에 player1의 선택지는 왼쪽을 뽑거나 오른쪽을 뽑거나이다.
                # player1이 한쪽을 택하면 남은 거 중에 player2가 택할 것
                else:
                    # 왼쪽을 택하면 남은 건 [L+1:R+1]이고
                    # 오른쪽을 택하면 남은 건 [L:(R-1)+1]이다.
                    choose_L = nums[L] - dp[L+1][R]
                    choose_R = nums[R] - dp[L][R-1]

                    # 둘 중 더 높은 값을 택해야 player1이 이길 것.
                    dp[L][R] = max(choose_L, choose_R)
        
        # print(dp)
        return dp[0][-1] >= 0
