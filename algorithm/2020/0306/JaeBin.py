# 10. 괄호변환

# 균형잡힌 괄호 문자열 만들어지는 index 반환하는 함수
def balanced(p):
    cost = 0
    for idx, bracket in enumerate(p):
        if bracket == '(':
            cost += 1
        elif bracket == ')':
            cost -= 1
        if cost == 0:
            return idx

# 올바른 괄호 문자열인지 확인하는 함수
def correct(string):
    tmp = []
    for i in string:
        if i == '(':
            tmp.append(i)
        else:
            if len(tmp) == 0:
                break
            tmp.pop()
    if len(tmp) == 0:
        return True
    else:
        return False

def solution(p):
    answer = ''
    # 입력이 빈 문자열인 경우, 빈 문자열 반환
    if p == '' or correct(p):
        answer = p
        return answer
    else:
        # 문자열 p를 균형잡힌 괄호 문자열 u, v로 분리
        u, v = p[:balanced(p)+1], p[balanced(p)+1:]
        # 문자열 u가 올바른 괄호 문자열일 경우
        if correct(u):
            string = solution(v)
            answer = u + string
            return answer
        # 문자열 u가 올바른 괄호 문자열이 아닐 경우
        else:
            answer += '('
            answer += solution(v)
            answer += ')'
            u = list(u[1:-1])
            for i in range(len(u)):
                if u[i] == '(':
                    u[i] = ')'
                elif u[i] == ')':
                    u[i] = '('
            answer += ''.join(u)
            return answer

