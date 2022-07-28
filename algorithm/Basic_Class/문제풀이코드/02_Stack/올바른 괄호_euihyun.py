def solution(s):
    # 스택생성
    stack = []
    
    # i 가 '(' 이면 추가 스택에 추가하고 ')'이 들어오면 pop
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            # ')' 를 제거하기 전에 stack 이 비어있으면 
            # '(' 이 들어오기전에 ')'이 들어온 거라 false
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    
    # 최종 적으로 스택이 비었으면 True 아니면 False
    if len(stack) == 0:
        return True
    else:
        return False
    
