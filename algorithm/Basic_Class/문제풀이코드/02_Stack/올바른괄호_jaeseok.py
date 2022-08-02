from collections import deque

def solution(s):
    q = deque()
    for i in s:
        if i == ')' and q:
            q.pop()
        else:
            q.append(i)
    if q:
        return False
    return True
