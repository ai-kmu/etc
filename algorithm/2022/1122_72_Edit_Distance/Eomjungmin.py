class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 2차원 dp 배열 선언
        # 행의 크기는 word1 길이+1, 열의 크기는 word2 길이+1
        # +1은 null string 포함
        # dp의 의미: 두 word의 각 철자 사이의 거리
        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        m = len(dp)
        n = len(dp[0])

        for i in range(m):
            for j in range(n):
                # null -> null은 0이므로 바로 continue
                if i == j == 0: 
                    continue

                # null -> word2로 가는 경우는 word2의 j번째까지 그 길이만큼 operation
                # 그래서 dp[i][j-1] 값에서 +1
                elif i == 0 and j > 0: 
                    dp[i][j] = dp[i][j-1] + 1
                    continue

                # word1 -> null로 가는 operation도 위 elif와 같은 원리
                elif i > 0 and j == 0:
                    dp[i][j] = dp[i-1][j] + 1
                    continue

                # 현재 word1의 철자와 word2의 철자가 같으면 둘이 없는것과 마찬가지이므로
                # 그래서 이전 대각 요소의 값 그대로 가져옴
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                
                # 현재 word1의 철자와 word2의 철자가 다르면 3가지 dp값 중에서 최소값을 불러온 후
                # 1을 더한 값을 dp에 저장
                # 왼쪽에서 +1: 추가
                # 위에서 +1: 삭제
                # 왼쪽 위 대각에서 +1: 대체
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        return dp[-1][-1]
