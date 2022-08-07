def balanced_bracket(s):
    
    if s.count('(') == s.count(')'):
        return True
    else:
        return False

def correct_bracket(s):
    
    stack = []

    if s[0] == ')' or s[-1] == '(':
        return False
    
    for ch in s:
        if ch == '(':
            stack.append('(')
        elif ch == ')':
            if stack:
                stack.pop()
            else:
                return False
            
    return True

def u_v_seperate(s):
    
    for i in range(len(s)):
        if balanced_bracket(s[0:i+1]):
            break
        
    u = s[0:i+1]
    v = s[i+1:]
    
    return u, v

def solution(p):
    
    def rec(s):
        answer = ""
        if len(s) == 0:
            return ""
        u, v = u_v_seperate(s)
        if correct_bracket(u):
            answer = u + rec(v)
        else:
            answer += '('
            answer += rec(v)
            answer += ')'
            u = u[1:-1]
            for i in u:
                if i == '(':
                    answer += ')'
                else:
                    answer += '('
        return answer
    
    return rec(p)
