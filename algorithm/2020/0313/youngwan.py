def solution(progresses, speeds):
    remain = remaintime(progresses, speeds)
    big = 0
    num = 0
    answer = []
    for i in range(len(remain)):
        if(i == 0):
            big = remain[i]
            num += 1
        elif(big < remain[i]):
            big = remain[i]
            answer.append(num)
            num = 1
        else:
            num += 1
    answer.append(num)
    return answer

def remaintime(progresses, speeds):
    remain = []
    for i in range(len(progresses)):
        if((100-progresses[i])%speeds[i] == 0):
            remain.append((100-progresses[i])//speeds[i])
        else:
            remain.append((100-progresses[i])//speeds[i] + 1 )
    return remain
