def solution(arrangement):
    answer = 0
    laser = '()'
    
    # () 이 모양은 레이저이기 때문에 () 모양은 모두 l로 변경해줌
    if laser in arrangement:
        arrangement = arrangement.replace('()', 'l')

    stick = 0
    
    for i in range(len(arrangement)):
        if arrangement[i] == "(": #만약 (로 시작한다면 새로운 막대기가 등장한 것을 의미
            stick += 1
        elif arrangement[i] == "l": #l이 나타난 것은 레이저가 있다는 뜻이므로 이전까지 있었던 막대기 숫자만큼 더해줌
            answer += stick
        else: #)가 나오면 막대기의 끝이라는 것을 의미하기 때문에 막대기의 숫자를 하나 줄여주고 끝난 막대기의 마지막을 더해줌
            stick -= 1
            answer += 1
