def solution(priorities, location):
    answer = 0
    lst = []
    
    for i,j in enumerate(priorities):
        lst.append([j,i])

    while len(lst) != 0:
        
        if lst[0][0] == max(lst)[0]:
            a = lst.pop(0)
            answer += 1
            if a[1] == location:
                break
        else:
            lst.append(lst.pop(0))
            
    return answer
    
    
