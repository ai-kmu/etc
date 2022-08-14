'''
인원 제한 둘:
    제일 가벼운 애 넣고, 무거운 애부터 순차적으로 데려옴
    제일 가벼운 애와도 같이 못 간다면 걘 혼자 갈 운명
sort하고 왼쪽 오른쪽 같이 빼기 위해 deque
'''

from collections import deque

def solution(people, limit):
    if len(people) == 1:
        return 1

    people.sort()
    people = deque(people)

    ans = 0
    while len(people) >= 2:
        # 가벼운 애와 무거운 애 받고 시작
        light = people.popleft()
        heavy = people.pop()
        
        # 둘이 같이 탈 수 있다면 태워보냄
        if light + heavy <= limit:
            ans += 1

        # 같이 못 탄다면
        else:
            # 무거운 애 보내고
            ans += 1
            # 가벼운 애 다시 넣기
            people.appendleft(light)
    
    # 끝나면 사람이 1명 또는 0명 남은 상태
    return ans + len(people)
