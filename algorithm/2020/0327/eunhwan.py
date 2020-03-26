def solution(arrangement: str) -> int:
    answer, bar = 0, 0
    arrangement = arrangement.replace('()', '#')    # () -> #
    for data in arrangement:
        if data == '(': # 새로운 막대기 길이
            bar += 1
        elif data == '#':   # 액션 빔~ 레이저빔 쏘고 이전까지의 바 길이 더함
            answer += bar
        elif data == ')':   # 막대기의 끝, -1과 +1 해줌.
            bar -= 1
            answer += 1
    
    return answer
