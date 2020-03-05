#올바른 괄호 문자열인지 판단
def check_valid(p):
    cnt = 0
    for char in p:
        if char == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                return False
    return cnt == 0
    
def seperate(p):
    if not p:
        return p
    
    cnt, idx = 0, 0
    
    #균형잡힌 괄호 문자열 찾기
    while idx < len(p):
        if p[idx] == '(':
            cnt += 1
        else:
            cnt -= 1
        idx += 1  
        if cnt == 0:
            break
            
    u = p[:idx]
    v = p[idx:]
    
    if check_valid(u):
        return u + seperate(v)
    t = ''
    for ch in u[1:-1]:
        if ch == '(':
            t += ')'
        else:
            t += '('
    return '(' + seperate(v) + ')' + t

    
def solution(p):
    return seperate(p)
