def solution(s):
    # 개수가 글러 먹은 경우
    if len(s) % 2:
        return False
    # 처음이나 끝이 잘못된 경우
    elif s[0] == ')' or s[-1] == '(':
        return False
    
    # 열리면 +1, 닫히면 -1
    pair = 0
    for bracket in s:
        if bracket == '(':
            pair += 1
        elif bracket == ')':
            pair -= 1
        
        # 음수가 되었다 == 더 닫혔다
        if pair < 0:
            return False
        
    # 정상이라면 pair == 0이어야함
    return pair == 0
