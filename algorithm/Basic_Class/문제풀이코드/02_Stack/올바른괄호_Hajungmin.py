def solution(s):
    # stack 선언
    stack = []
    
    # 문자열을 돌며 여는 괄호면 무조건 stack에 append
    for i in s:
        if i == '(':
            stack.append(i)
        # 닫는 괄호인데 stack에 아무것도 없다면 False return
        # 그 외에는 stack에서 pop
        else:
            if not stack : return False
            stack.pop()
    # 다 돌았을 때 stack에 뭐라도 있으면 False 아니면 True
    return False if len(stack) > 0 else True
