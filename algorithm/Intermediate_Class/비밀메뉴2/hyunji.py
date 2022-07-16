# 오답
# 예전 스터디에서 배운 LCS 사용해서 풀었는데 왜 틀렸는지 모르겠어요...

import sys

N, M, K = map(int, sys.stdin.readline().split())

arr_N = list(map(int, sys.stdin.readline().split()))
arr_M = list(map(int, sys.stdin.readline().split()))

L = [[0 for i in range(3001)] for j in range(3001)]

def longestNum(arr_N, arr_M, N, M):
    for i in range(N+1):
        L[i][0] = 0
    
    for i in range(M+1):
        L[0][i] = 0

    for i in range(1, N+1):
        for j in range(1, M+1):
            # 두 나열된 숫자들 중 현재 숫자가 서로 같은 경우
            if arr_N[i-1] == arr_M[j-1]:
                # 문자가 같기 때문에 수열 길이 + 1
                L[i][j] = L[i-1][j-1] + 1

            # 두 나열된 숫자들 중 현재 숫자가 서로 다른 경우
            else:
                L[i][j] = max(L[i][j-1], L[i-1][j])
    
    return L[N][M]

longest_num = longestNum(arr_N, arr_M, N, M)
print(longest_num)
