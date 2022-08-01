def solution(s):
    answer = True
    s_list = []
    
    # 닫는 괄호가 있다면 여는 괄호가 있어야함
    # 여는 괄호는 스택안에 넣어주고 
    for ch in s:
        
        # 닫는 괄호라면 앞에 여는 괄호가 있어야 함
        if ch == ')':
            if not s_list:
                return False
            s_list.pop()
        else:
            s_list.append(ch)
    
    # 다 끝났는데도 리스트에 남아있다면 닫히지 않았기 때문에 False
    if s_list:
        return False
    
    return True
