import sys
import copy
N, M, K = map(int, input().split())

control_1 = list(input().split())
control_2 = list(input().split())


memo = [[0] * M for j in range(N)]

def dfs(i, j):

    if i < 0 or j < 0:
        return 0
    if memo[i][j] != 0:
        return memo[i][j]
    
    if control_1[i] == control_2[j]:

        memo[i][j] = 1 + dfs(i-1, j-1)
        return memo[i][j]

    return memo[i][j]


ans = 0

for i in range(N):
    for j in range(M):
        ans = max(dfs(i,j), ans)

print(ans)
