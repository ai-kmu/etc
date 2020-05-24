def solution(triangle):
    #밑에서 부터 올라오면서 최대값을 구하기
    tri_len = len(triangle)
    while tri_len > 1:
        for i in range(tri_len - 1):
            triangle[tri_len - 2][i] += max(triangle[tri_len - 1][i], triangle[tri_len - 1][i+1])
        tri_len -= 1
    return triangle[0][0]
