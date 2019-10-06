def solution(operations):
    answer = []
    queue = []
    for oper in operations:
        if "I" == oper[0]:
            queue.append(int(oper[2:]))
        elif "D 1" == oper and len(queue) !=0:
            queue.remove(max(queue))
        elif "D -1" == oper and len(queue) !=0:
            queue.remove(min(queue))
            

    if len(queue)==0:
        answer = [0,0]
    else:    
        min_num = min(queue)
        max_num = max(queue)
        answer.append(max_num)
        answer.append(min_num)
                
               
    return answer
