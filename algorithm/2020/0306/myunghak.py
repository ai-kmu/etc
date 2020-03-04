def is_correct(p):
    open_num = 0
    for i in p:
        if(i == '('):
            open_num +=1
        else:
            open_num -=1    
        
        if open_num < 0:
            return False
        
    if open_num == 0:
        return True
    else:
        return False
    
def is_balanced(p):
    open_num, close_num = 0, 0

    
    for i in p:
        if(i == '('):
            open_num +=1
        else:
            close_num +=1
    if(open_num == close_num):
        return True
    else:
        return False
    
def stage2(p, answer):
    if len(p) == 0:
        return p
    u = ""
    v = ""
    for i in range(1, len(p)):
        if is_balanced(p[0:i + 1]):
            u = p[0:i + 1]                
            v = p[i+1:len(p)]
            break
    
    empty_str = ""
    
    if is_correct(u):
        
        u += stage2(v, answer)
        return u
    else:
        empty_str += "("
        empty_str += stage2(v, answer)
        empty_str += ")"
        u = u[1:-1]
        temp_str = ""
        for j in range(len(u)):
            if u[j] =='(':
                temp_str += ')'
            else:
                temp_str += '('
        empty_str += temp_str
        return empty_str
    return u
    
def solution(p):
    answer = ''
    answer = stage2(p, "")
                
    return answer

