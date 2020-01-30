def solution(distance, rocks, n):
    rocks.append(distance)
    rocks = sorted(rocks)
    #시작과 끝을 정의함
    start, end = 0, distance
    answer = list()
    
    #시작이 끝보다 커지면 반복을 종료해야 함
    while start <= end: 
        prev = 0
        cnt = 0 
        mid = (start + end) // 2
        
        for rock in rocks:
            #중간 값과 prev의 차이를 비교했을 때 중간 값이 크다면 cnt를 늘려주고
            #그러지 않다면 prev의 값을 rock으로 바꿈
            #즉, mid값을 기준으로 최소 거리를 정해서 최소 거리보다 작다면 제거하는 방식
            if rock - prev < mid:
                cnt += 1
            else:
                prev = rock
        
        #이분 탐색은 중간 값을 기준으로 크거나 작을 때 변경이 있음
        #cnt가 n보다 크면 중간지점에서 한개를 줄어야 하고 
        #--> 더 작은 폭으로 만들기위해서
        #그렇지 않다면 중간지점에서 한개를 늘려야한다
        if cnt > n:
            end = mid - 1
        else:
            start = mid + 1
            answer.append(mid)
    #cnt와 n이 같은 경우 중, 가장 큰 값을 골라야 함
    print(answer)
    return max(answer)
