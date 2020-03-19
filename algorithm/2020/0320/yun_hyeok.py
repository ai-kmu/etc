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
        
        # 현재 문서의 우선 순위보다 더 높은 우선 순위를 가진 첫번째 마주치는 문서를 찾는다.
        for idx, val in enumerate(priorities):
            if val > priority:
                until = idx
                break
        
        # 우선 순위가 더 높은 문서가 없다면 문서를 출력한다. (deque에서 제거한고 count를 올린다.)
        if until == 0:
            priorities.popleft()
            m = mark.popleft()
            count += 1
            
            # 인쇄 순서를 알고 싶은 문서였다면 count를 반환한다.
            if m == True:
                return count
        
        # 우선 순위가 더 높은 문서가 있다면
        # 그 앞에 있는 모든 문서를 꺼내서 뒤에 차례대로 넣는다.
        i = 0
        while i < until:
            priority = priorities.popleft()
            priorities.append(priority)
            
            m = mark.popleft()
            mark.append(m)
            
            i += 1
