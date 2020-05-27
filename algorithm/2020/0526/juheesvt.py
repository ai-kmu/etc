
def solution(triangle):

    # cache를 입력된 리스트의 크기만큼 -1로 초기화
    cache = [[-1]*len(triangle[i]) for i in range(len(triangle))]
    dp(triangle, cache, 0 ,0)
    return cache[0][0]

def dp(triangle, cache, row, col):

    if row == len(triangle)-1:
        cache[row][col] = triangle[row][col]

    if cache[row][col] != -1:
        return cache[row][col]

    cache[row][col] =+ (triangle[row][col] + max(dp(triangle, cache, row+1, col), dp(triangle, cache, row+1, col+1)))
    return cache[row][col]
