from collections import deque

def solution(progresses, speeds):
    
    stack = []
    days = []
    index = 0
    
    # 배포 날짜만 구하기 위해서 계산해서 days에 추가
    # porgresse 갯수 만큼 하면서 100에 progresses[i]를 빼고 
    # speeds[i]를 나눈 몫을 넣어줌 나머지가 0이 아닐때는 몫 + 1 해서 넣음
    for i in range(len(progresses)):
        day = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i] != 0:
            days.append(day + 1)
        else:
            days.append(day)

    # days 수만큼 하고
    # days의 index 가 뒤의 days[i] 보다 작으면 i에 index를 빼고 
    # index를 i로 업데이트
    for i in range(len(days)):
        if days[index] < days[i]:
            stack.append(i - index)
            index = i
    
    # 마지막 친구는 총길이에서 index 만 빼주면됨
    stack.append(len(days) - index)

    return stack
