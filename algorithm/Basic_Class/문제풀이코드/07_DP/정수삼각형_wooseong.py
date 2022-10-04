def solution(tri):
    '''
    tri[r][c] += max(tri[r-1][c-1], tri[r-1][c])
    * c-1이나 c 중에 없는 게 있을 수 있음
    '''
    # 두 번째 줄부터
    for r in range(1, len(tri)):
        # 각 원소들에 접근할 건데
        for c in range(r + 1):
            # 맨 왼쪽에선 윗 줄 맨 왼쪽만 접근 가능
            if c == 0:
                tri[r][c] += tri[r - 1][c]
            # 맨 오른쪽에선 윗 줄 맨 오른쪽만 접근 가능
            elif c == r:
                tri[r][c] += tri[r - 1][c - 1]
            # 다른 곳에선 윗 줄 두 개 중 큰 걸 갖고 와서 더하면 됨
            else:
                tri[r][c] += max(tri[r - 1][c - 1], tri[r - 1][c])
    
    # 마지막 줄에서 최댓값 반환
    return max(tri[-1])
            
