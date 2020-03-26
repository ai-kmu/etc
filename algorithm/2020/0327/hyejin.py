def solution(arrangement):
    answer = 0
    # 레이저를 쐈을 때, 자를 수 있는 파이프의 수
    pipe_stack = 0
    # 레이저가 나온 경우
    laser = False
    
    for i in range(len(arrangement)):
        # 레이저의 뒷부분(")")이 나왔을 때, 다음으로 넘어간다.
        if laser:
            laser =False
            continue
        # 레이저가 나왔을 때, 자른 파이프를 더해주고, laser를 True로 한다.
        if arrangement[i] == '(' and arrangement[i+1] == ')':
            answer += pipe_stack
            laser = True
        # 쇠막대기가 끝났을 때, 자를 수 있는 파이프 하나를 뺀다.
        elif arrangement[i] == ')':
            pipe_stack -= 1
            answer += 1
        # '('일 경우에 자를 수 있는 파이프를 하나 추가해준다.
        else:
            pipe_stack += 1
    
    return answer
