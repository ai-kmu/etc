def split_u_v(p):
    l, r = 0, 0
    u, v = '', ''
    for pp in p:
        if l != 0 and l == r:
            v += pp
            continue
            
        if pp == '(': l += 1
        else: r += 1
        
        u += pp
    return u, v
    
def solution(p):
    
    # 1
    if not p:
        return ""
    
    # 2
    u, v = split_u_v(p)
    
    # 3. u가 '올바른 괄호 문자열'인 경우
    if u[0] == '(':
        return u + solution(v)
    
    # 4. u가 '올바른 괄호 문자열'이 아닌 경우
    else:
        # 4-1
        answer = '('
        # 4-2
        answer += solution(v)
        # 4-3
        answer += ')'
        # 4-4
        u = u[1:-1]
        for uu in u:
            if uu == '(': 
                answer += ')'
            else: 
                answer += '('
        
    return answer
