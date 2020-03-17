def solution(priorities, location):
    answer = 0
    while(location != -1):
        printing = True
        now = priorities.pop(0)
        for num in priorities:
            if(now < num):
                printing = False
                priorities.append(now)
                if(location == 0):
                    location = len(priorities) -1
                else:
                    location -= 1
                break
        if(printing == True):
            answer += 1
            if(location == 0):
                location = -1
            else:
                location -= 1
    return answer
