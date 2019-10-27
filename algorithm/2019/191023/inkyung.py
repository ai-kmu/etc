def solution(triangle):
    tri_len = len(triangle)
    while tri_len > 1:
        for i in range(tri_len - 1):
            triangle[tri_len - 2][i] += max(triangle[tri_len - 1][i], triangle[tri_len - 1][i+1])
        tri_len -= 1
