# u와 v를 분리하는 함수
def detech_u_v(p):
    left = 0
    right = 0
    for i, char in enumerate(p):
        if char == "(":
            left += 1
        else:
            right += 1
        if left == right:
            return p[0:i + 1], p[i + 1:]
    return p, ""


# 올바른 괄호 문자열인지 확인하는 함수
def check_string(u):
    stack = []
    for char in u:
        if char == ')' and len(stack) == 0:
            return False
        elif char == '(':
            stack.append(char)
        else:
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False


# u의 char들을 반대로 뒤집는 함수
def reverse_u(u):
    answer = ''
    if u == '':
        return answer
    for char in u:
        if char == '(':
            answer += ')'
        else:
            answer += '('
    return answer


# 올바른 괄호 문자열을 만드는 함수
def correct_blacket(p):
    if p == '':
        return p
    else:
        u, v = detech_u_v(p)
        if check_string(u):
            return u + correct_blacket(v)
        else:
            answer = '('
            if v == '':
                return answer + ')' + reverse_u(u[1:-1])
            else:
                answer += correct_blacket(v) + ')'
            return answer + reverse_u(u[1:-1])


def solution(p):
    answer = ''
    if p == '' or check_string(p):
        return p
    else:
        answer = correct_blacket(p)

    return answer