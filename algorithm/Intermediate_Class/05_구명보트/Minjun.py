# deque를 안쓰면 시간초과가 납니다
# 눈물

from collections import deque

def solution(people, limit):
    cnt = 0
    people.sort()
    people = deque(people)
    while people:
        if people[0] + people[-1] > limit:
            people.pop()
            cnt += 1
        elif len(people) >= 2:
            people.pop()
            people.popleft()
            cnt += 1
        else:
            people.pop()
            cnt += 1
    return cnt
