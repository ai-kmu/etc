
def solution(triangle):

    # cache를 입력된 리스트의 크기만큼 -1로 초기화
    cache = [[-1]*len(triangle[i]) for i in range(len(triangle))]
    
    # dp라는 함수를 호출해서 cache 리스트에 최대 값 경로를 차곡차곡 쌓아서 넣기
    dp(triangle, cache, 0 ,0)
    return cache[0][0]

def dp(triangle, cache, row, col):
    
    # 삼각형의 맨 아래에 도달하면 해당 값을 반환한다
    if row == len(triangle)-1:
        cache[row][col] = triangle[row][col]
    
    # cache에 이미 저장된 값이 있다면 바로 반환한다
    if cache[row][col] != -1:
        return cache[row][col]
   
    # 오른쪽 아래와 왼쪽 아래에서 반환된 값 중 큰것을 골라 현재 위치와 더한다
    cache[row][col] =+ (triangle[row][col] + max(dp(triangle, cache, row+1, col), dp(triangle, cache, row+1, col+1)))
    return cache[row][col]


# 프로그래머스 다른 풀이

solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])
