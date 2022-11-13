'''
이분탐색
- 정답값 자체를 탐색함
- 암튼 최소는 0이고 최대는 distance니까 그 사이 어딘가 있음
'''

def solution(distance, rocks, n):
    answer = 0
    left = 0
    right = distance
    
    rocks.sort()
    
    # 이분 탐색
    while left <= right:
        # 답 예측
        mid = (left + right) // 2
        
        # 지운 돌의 개수
        del_rock = 0
        
        # 거리를 계산할 이전 돌 (처음엔 출발지점))
        prev = 0
        for rock in rocks:
            # 예측한 답보다 현재 거리가 작으면 -> 없애서 답보다 작은 게 없게 만듦
            if rock - prev <  mid:
                del_rock += 1 
            # 크면: 괜찮음
            else:
                prev = rock
            
            # 너무 많이 지우면 이번 타임은 글렀음
            if del_rock > n:
            	break
        
        # 만약 너무 많이 지웠을 경우: 답을 줄여야 됨
        if del_rock > n:
            right = mid - 1
        
        # 아니면: 되나? 올려보자
        else:
            answer = mid
            left = mid + 1
            
    return answer
