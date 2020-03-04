
# 2. 균형잡힌 괄호 문자열로 구분 : u, v로 나누는 기준 
def balanced(p):
    num = 0
    for i, val in enumerate(p):
        if val == ")":
            num -= 1
        if val == "(":
            num += 1
        if num == 0:
            return p[:i+1], p[i+1:]
        
# 3. 올바른 괄호 문자열 유무 확인
def all_right(p):
    temp = []
    for i in p:
        if i == "(":
            temp.append(i)
        else:
            if len(temp) == 0:
                return False
            temp.pop()
    if len(temp) != 0:
        return False
    return True

def solution(p):
    # 1. 빈 문자열이나 문자열 전체가 옳은 경우
    if p == "" or all_right(p): return p
    
    # 2. 균형잡힌 괄호 문자열로 분리
    u, v = balanced(p)
    
    # 3. 문자열 u가 올바른 괄호 문자열일 경우
    if all_right(u):
        string = solution(v)
        
        return u + string
    
    # 4. 문자열 u가 올바르지 않은 괄호 문자열일 경우
    else:
        # 4.
        temp = "(" + solution(v) + ")"
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            elif u[i] == ")":
                u[i] = "("
            temp += u[i]
        return temp
