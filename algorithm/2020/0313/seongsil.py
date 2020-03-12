import math

def solution(progresses, speeds):
    answer = []
    criteria = 0
    num = 1
    
    work = [math.ceil((100-p)/s) for p,s in zip(progresses, speeds)]
    
    
    for i in range(len(work)):
        if work[criteria] > work[i]:
            work[i] = work[criteria]
        elif work[criteria] < work[i]:
            criteria = i
        
    for i in range(len(work)-1):
        if work[i] == work[i+1]:
            num += 1
        else:
            answer.append(num)
            num = 1
        if i == len(work)-2:
            answer.append(num)
    
    return answer
