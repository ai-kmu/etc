arrangement = list(input())
total = 0
iron_stick_tracking = 0  # 현재 위치에서 레이저를 쐈을 때 관통되는 쇠막대기 개수를 트래킹한다.

previous = ')'
for parenthesis in arrangement:
    if previous == '(':
        if parenthesis == '(':
            # 쇠막대기 트래킹 추가
            iron_stick_tracking += 1
            total += 1
        elif parenthesis == ')':
            # 레이저 발사
            total += iron_stick_tracking
    elif previous == ')':
        if parenthesis == ')' and not iron_stick_tracking == 0:
            # 쇠막대기 트래킹 제거
            iron_stick_tracking -= 1
    previous = parenthesis

print(total)
