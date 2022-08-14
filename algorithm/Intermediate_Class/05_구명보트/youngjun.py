from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people_deque = deque(people)

    while len(people_deque) >= 2:
        if people_deque[0] + people_deque[-1] <= limit:
            people_deque.popleft()
            people_deque.pop()
        else:
            people_deque.pop()
        answer += 1
        
    if people_deque:
        answer += 1
        
    return answer
