from collections import deque

def solution(progresses, speeds):
    # progresses queue 생성
    progresses_queue = deque(progresses)
    # speeds queue 생성
    speeds_queue = deque(speeds)
    answer = []
    
    # progresses queue가 남아있는 동안
    while progresses_queue:
        
        # progresses number 생성
        progresses_num = 0
        
        # 작업을 하나씩 늘려준다.
        for i in range(len(progresses_queue)):
            progresses_queue[i] += speeds_queue[i]
            
        # progresses queue가 남아있는 동안, 맨 왼쪽 작업의 진도가 100이 넘어가면 100보다 작은 값이 나올때까지 popleft 하며, progresses num을 늘려준다.
        while progresses_queue and progresses_queue[0] >= 100:
            progresses_queue.popleft()
            speeds_queue.popleft()
            progresses_num += 1
        
        # 만약 progresses num이 0이 아닐 경우 answer에 추가해준다.
        if progresses_num != 0:
            answer.append(progresses_num)

    return answer
