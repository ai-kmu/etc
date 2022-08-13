from collections import deque
def solution(people, limit):
    
    # 정렬 
    people.sort()
    people = deque(people)
    answer = 0
    
    # 최대 2명임으로 가장 무거운사람과 가장 가벼운 사람을 태운다
    while people: 
        p = people.pop()
        if people and people[0] + p <= limit:
            people.popleft() 
            
        answer += 1
    
    return answer
