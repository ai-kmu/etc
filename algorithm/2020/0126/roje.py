def solution(distance, rocks, n):
    # 바위와 바위사이의 거리가 이분탐색 기준보다 작을 경우 뒤쪽 돌을 삭제
    # 삭제한 돌의 대수가 n보다 클 경우에는 바위와 바위의 사이를 줄이고, n보다 작거나 같으면
    # 거리를 늘리는 방식으로 이분탐색!!
    
    # 이분 탐색을 위해 rocks 정렬하기
    rocks.sort()
    
    answer = 0
    start = 0
    dest = distance
    
    while start <= dest:
        prev = 0
        cnt = 0
        mins = 1000000000
        
        # 바위 사이 최소 거리
        mid = (start + dest) // 2
        
        for i in range(len(rocks)):
            if rocks[i] - prev < mid:
                cnt += 1
            else:
                mins = min(mins, rocks[i] - prev)
                prev = rocks[i]
        
        if cnt > n:
            dest = mid - 1
        else:
            answer = mins
            start = mid + 1
    
    return answer
