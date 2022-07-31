'''
걸리는 날: (100 - progress) / speed
근데 결과가 소수일 경우
하루가 더 필요함    ex) 2.3 -> 3
이걸 해주는 게 math.ceil()
'''

import math

def solution(progresses, speeds):
    # 걸리는 날 계산하기
    days = [math.ceil((100 - p)/s) for p, s in zip(progresses, speeds)]
    
    # 정답 list
    answer = []
    # 첫 번째 기준은 days[0]임
    curr_day = days[0]
    # 배포되는 수 초기화
    distribute = 0

    # 걸리는 날 탐색
    for day in days:
        # 만약 앞보다 걸리는 날이 적다면 걔까지 배포
        if curr_day >= day:
            distribute += 1
        
        # 아니라면
        else:
            # 그전까지 배포된 거 answer에 넣고
            answer.append(distribute)
            # 1로 초기화: 현재 day 포함해서 배포할 거임
            distribute = 1
            # 걸리는 날 갱신
            curr_day = day
    
    # 마지막 남은 거 붙이기
    answer.append(distribute)
            
    return answer
