def solution(priorities, location):
    length = len(priorities)
    for i in range(len(priorities)):
        priorities[i] = [priorities[i], i] 
    rank = 1
    while True:
        if (max(priorities)[0] <= priorities[0][0]):
            if(priorities[0][1] == location):
                return rank
            rank+=1
        else:
            priorities.append(priorities[0])
        priorities.pop(0)
