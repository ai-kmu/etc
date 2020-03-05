def solution(p):
    def divide_uv(s):
        count_l = 0
        count_r = 0
        for i in range(len(s)):
            if s[i] == '(':
                count_l += 1
            elif s[i] == ')':
                count_r += 1
            if count_l == count_r:
                break
        return s[:i+1], s[i+1:]
    
    def right(s):
        result = True
        count = 0
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                count -= 1
            if count < 0:
                result = False
                break
        return result
        

    if p is '':
        return ''
    
    u, v = divide_uv(p)
    
    if right(u) == True:
        return u + solution(v)
        
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        
        del_u = u[1:-1]
        for i in range(len(del_u)):
            if del_u[i] == '(':
                answer += ')'
            else:
                answer += '('
        return answer
