# 구현 실패. https://www.youtube.com/watch?v=b6AGUjqIPsA 보고 구현하고 공부함
# Minimum Edit Distance 알고리즘

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M = len(word1)
        N = len(word2)
        # dp 테이블의 행 : word1 + Null, 열 : word2 + Null
        dp = [[0] * (N+1) for _ in range(M+1)]
        # 행은 delete, 즉 열이 증가하면 증가한 부분에 해당하는 word1의 행을 삭제하겠다는 의미
        for i in range(1, M+1):
            dp[i][0] = i
        # 열은 insert, 즉 행이 증가하면 증가한 부분에 해당하는 word2의 열을 추가하겠다는 의미
        for j in range(1, N+1):
            dp[0][j] = j
        # 대각선으로 증가하는 경우는 replace 연산을 의미함. 해당 행을 해당하는 열로 바꾸겠다는 의미
            
        # dp 테이블 순회
        for i in range(1, M+1):
            for j in range(1, N+1):
                # 두 부분 문자열이 동일하다면 대각선 부분을 그대로 가져옴(replace긴 한데 바꿔줄 이유가 없음)
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                # 아니라면 insert, delete, replace 연산 중에 가장 적은 연산을 가져와서 1번 더 연산해줌
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        # 제일 마지막 부분이 정답
        return dp[-1][-1]
