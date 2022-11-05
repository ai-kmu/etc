def solution(distance, rocks, n):
    
    # rocks 정렬 후 마지막 위치인 distance 추가
    rocks.sort()
    rocks.append(distance)
    
    left = 0
    right = distance
    
    while left <= right:
        # mid는 탐색하려는 거리 범위의 중간으로 지정
        # min_dist는 현재 상황에서 거리의 최솟값을 저장하는 변수
        # curr_point는 거리를 계산하여 돌들을 제거할지 말지 결정하는 포인트
        # remove_num은 제거할 돌의 수
        mid = (right + left) // 2
        min_dist = float('inf')
        curr_point = 0
        remove_num = 0
        
        # rocks를 돌며 현재 curr_point에서부터 돌까지 거리 계산
        for rock in rocks:
            dist = rock - curr_point
            
            # 만약 거리가 mid값보다 작다면 제거 대상
            if dist < mid:
                remove_num += 1
                
            # 만약 거리가 mid와 같거나 크다면 해당 지점으로 curr_point를 옮김
            # 그 후 현재 계산된 최소 거리값과 비교해서 거리 값을 갱신
            else:
                curr_point = rock
                min_dist = min(dist, min_dist)
        
        # 만약 제거한 돌이 n보다 크면 right의 범위를 줄여서 mid값을 줄임
        if remove_num > n:
            right = mid - 1
        
        # 만약 제거한 돌의 수가 n과 같거나 작으면 left의 위치를 옮김
        # 제거된 바위의 수가 적어 바위를 더 없애거나 mid의 값을 늘려서 탐색해보는 것
        else:
            left = mid + 1
            answer = min_dist
    
    return answer
