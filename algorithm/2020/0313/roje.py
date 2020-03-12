def solution(progresses, speeds):
    iters = len(progresses)
    answer = {}
    days = []
    
    for idx in range(iters):
        total = progresses[idx]
        day = 0
        while True:
            day += 1
            if (total + speeds[idx] * day) >= 100:
                days.append(day)
                break
                
    for idx in range(iters-1):
        if days[idx] >= days[idx+1]:
            days[idx+1] = days[idx]
    
    for d in days:
        try: answer[d] += 1
        except: answer[d] = 1        
    
            
    return list(answer.values())
