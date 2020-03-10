def solution(progresses, speeds):
    answer = []
    publish = [0 for i in range(len(progresses))]
    day = 1
    while(1):
        if(sum(progresses) == 100 * len(progresses)):
            break
        for i in range (len(progresses)):
            if progresses[i] < 100 and 100 <= progresses[i]+speeds[i]:
                publish[i] = day
            progresses[i]+=speeds[i]
            
            if progresses[i] > 100:
                progresses[i] = 100
        day+=1
    num_public = 0
    print(publish)
    for i in range(len(publish)):
        publish[i] = max(publish[:i+1])
    print(publish)
    publish.append(-1)
    SUM = 1
    for i in range(len(publish)-1):
        if publish[i] != publish[i+1]:
            answer.append(SUM)
            SUM = 1
        else:
            SUM+=1
    return answer
