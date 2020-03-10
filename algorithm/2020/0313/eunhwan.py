import math

def solution(progresses, speeds):
    answer = []
    
    left_jobs = [100 - i for i in progresses]
    days = [math.ceil(left_jobs[k] / v) for k, v in enumerate(speeds)]
    
    front = 0
    
    for idx in range(len(days)):
        if days[front] < days[idx]:
            answer.append(idx - front)
            front = idx
            
    answer.append(len(days) - front)
            
    return answer
    
    
progresses, speeds = [93,30,55], [1,30,5]
print(solution(progresses, speeds))
