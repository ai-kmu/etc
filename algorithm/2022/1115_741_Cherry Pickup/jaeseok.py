# dp로 내려가는 경우와 올라가는 경우 두 가지로 구분해서 풀이하려 시도
# 어떠한 체리를 pick했는지 확인하려고 하였으나 실패
# dfs 등의 방법을 써야 할 듯함(수정중)

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        answer = 0

        # 내려가는 경우
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for row in range(n):
            if grid[row][0] == 1:
                dp[row][0] = dp[row-1][0] + 1
                grid[row][0] = 0
            elif grid[row][0] == -1:
                break
        for col in range(n):
            if grid[0][col] == 1:
                dp[0][col] = dp[0][col-1] + 1
                grid[0][col] = 0
            elif grid[0][col] == -1:
                break

        for row in range(1, n):
            for col in range(1, n):
                if grid[row][col] == -1:
                    dp[row][col] = -1
                else:
                    dp[row][col] = max(dp[row][col-1], dp[row-1][col])
                    if grid[row][col] >= 1:
                        if dp[row][col-1] > dp[row-1][col]:
                            grid[row][col-1] = 0
                        else:
                            grid[row-1][col] = 0
                        dp[row][col] += 1
        print(max(dp[-1]))

        # 올라가는 경우
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for row in range(n-1, 0, -1):
            if grid[row][0] == 1:
                dp[row][0] = dp[row+1][0] + 1
                grid[row][0] = 0
            elif grid[row][0] == -1:
                break
        for col in range(n-1, 0, -1):
            if grid[0][col] == 1:
                dp[0][col] = dp[0][col+1] + 1
                grid[0][col] = 0
            elif grid[0][col] == -1:
                break

        for row in range(n-2, 0, -1):
            for col in range(n-2, 0, -1):
                if grid[row][col] == -1:
                    dp[row][col] = -1
                else:
                    dp[row][col] = max(dp[row][col+1], dp[row+1][col])
                    if grid[row][col] >= 1:
                        if dp[row][col+1] > dp[row+1][col]:
                            grid[row][col+1] = 0
                        else:
                            grid[row+1][col] = 0
                        dp[row][col] += 1
        print(max(dp[0]))

        return answer
