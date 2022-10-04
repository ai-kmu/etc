def solution(triangle):
    # 두 번째줄부터 계산 시작
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            # 시작 위치 설정
            start1, start2 = triangle[i][j], triangle[i][j]
            # 이전 층 j-1와 계산
            if 0 <= j - 1 < len(triangle[i - 1]):
                start1 += triangle[i - 1][j - 1]
            # 이전 층 j와 계산.
            if 0 <= j < len(triangle[i - 1]):
                start2 += triangle[i - 1][j]
            # 둘 중 큰 값으로 시작 위치에 저장
            triangle[i][j] = max(start1, start2)
    # 큰 값 return
    return max(triangle[-1])
