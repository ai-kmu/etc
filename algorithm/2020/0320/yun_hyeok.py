def solution(priorities, location):
    from collections import deque
    priorities = deque(priorities)
    mark = [False] * len(priorities)
    mark = deque(mark)
    mark[location] = True
    count = 0
    
    while True:
        priority = priorities[0]
            
        until = 0
        for idx, val in enumerate(priorities):
            if val > priority:
                until = idx
                break
        if until == 0:
            priorities.popleft()
            m = mark.popleft()
            count += 1
            if m == True:
                return count
            continue
        i = 0
        while i < until:
            priority = priorities.popleft()
            priorities.append(priority)
            
            m = mark.popleft()
            mark.append(m)
            
            i += 1
