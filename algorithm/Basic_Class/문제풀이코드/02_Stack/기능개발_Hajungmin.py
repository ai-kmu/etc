import math
from collections import deque

def solution(progresses, speeds):
    if not progresses: return []
    
    # 프로세스를 deque로 선언
    # day에 처음 할 일을 끝내는 일수를 구함
    # 처음 일은 한 것이기 때문에 complete에 1을 더함
    progress = deque(progresses)
    first = progress.popleft()
    day = math.ceil((100 - first) / speeds[0])
    complete = 1
    answer = []
    
    # 인덱스가 1부터 시작해야하기 때문에 1부터 루프 돔
    for i in range(1, len(progress)+1):
        # progress에서 popleft해서 현재 progress가져옴
        # 현재 완료 일수 구함
        curr = progress.popleft()
        curr_day = math.ceil((100 - curr) / speeds[i])
        
        # 만약 현재 일수가 이전 일의 일수보다 작거나 같으면 complete 1더함
        if curr_day <= day:
            complete += 1

        # 그외에는 complete을 answer에 더해줌
        # 현재 일을 완료한 것이기 때문에 complete을 1로 초기화
        # day를 curr_day로 갱신
        else:
            answer.append(complete)
            complete = 1
            day = curr_day
    # 마지막에 계산한 complete을 answer에 더해줌
    answer.append(complete)
    return answer
