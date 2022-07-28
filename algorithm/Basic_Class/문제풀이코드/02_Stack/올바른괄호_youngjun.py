def solution(s):
    # stack을 만들어 준다.
    stack = []
    
    # 만약 맨 앞이 ) 거나, 맨 뒤가 ( 이면 올바른 괄호가 아니므로 False 반환.
    if s[0] == ')' or s[-1] == '(':
        return False
    # s를 돌면서
    for ch in s:
        # stack에 ( 를 넣어준다.
        if ch == '(':
            stack.append('(')
        # ) 이고, stack에 ( 가 남아 있을 경우 하나씩 지워준다.
        elif ch == ')' and stack:
            stack.pop()
        # ) 이고, stack에 아무것도 남아 있지 않을 경우 False를 반환한다.
        else:
            return False
    
    # stack에 ( 가 남아 있으면 False를 반환한다.
    if stack:
        return False
    # stack이 비어 있으면 True를 반환한다.
    else:
        return True
