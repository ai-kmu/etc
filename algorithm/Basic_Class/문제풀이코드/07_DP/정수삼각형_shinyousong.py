def solution(triangle):
    # 다 돌아봐야 할듯
    # 삼각형 모양의 배열을 만들고 dptable로 사용
    dptable = [[0] * (i + 1) for i in range(len(triangle))]
    dptable[0][0] = triangle[0][0]
    # dp
    for i in range(len(triangle)):
        for j in range(i + 1):
            # 맨 끝 둘
            if j == 0:
                dptable[i][j] = dptable[i-1][j] + triangle[i][j]
            elif j == i:
                dptable[i][j] = dptable[i-1][j-1] + triangle[i][j]
            # 나머지는 큰데서
            else:
                dptable[i][j] = max(dptable[i-1][j-1], dptable[i-1][j]) + triangle[i][j]
    return max(dptable[len(triangle) - 1])
