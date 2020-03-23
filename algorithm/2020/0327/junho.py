def solution(arrangement):
    answer = 0
    stack = []      #arrange의 "(" , ")"를 쌓을 stack
    backnum = 0     #")"가 위치한 장소
    frontnum = 0    #backnum에 대응하는 "("가 위치한 장소
    
    for i in range(len(arrangement)):
        stack.append(i)                     # arrangement 앞부터 stack에 쌓기
        if arrangement[i] == ")":           # ")"일 경우 레이저 또는 막대기 표현
            backnum = stack.pop()           
            frontnum = stack.pop()
            if backnum - frontnum == 1:     # "(" , ")" 가 연속으로 나올 경우 레이저
                answer += len(stack)        # stack에 쌓여있는 "("수 만큼 레이저 아래 막대기 존재
            else :
                answer += 1                 # 레이저에 잘리고 남은 막대기 조각 
    return answer
