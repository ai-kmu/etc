from collections import deque

def solution(people, limit):
    
    people.sort()

    deq = deque(people)
    
    answer = 0
    
    while deq:
        
        if deq[0] + deq[-1] <= limit and len(deq) != 1:
            deq.popleft()
            deq.pop()
            answer += 1
        else:
            deq.pop()
            answer += 1

    return answer
