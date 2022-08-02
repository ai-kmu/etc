from collections import deque
def solution(progresses, speeds):
    answer = []
    needdays = deque()
    cnt = 0
    for i in range(len(progresses)):
        remain = 100 - progresses[i] 
        j = 0
        while remain > 0:
            remain -= speeds[i]
            j += 1
        needdays.append(j)
    answer.append(1)
    maxday = needdays.popleft()
    while needdays:
        nextday = needdays.popleft()
        if maxday >= nextday:
            answer[cnt] += 1
        else:
            maxday = nextday
            answer.append(1)
            cnt += 1
    return answer
