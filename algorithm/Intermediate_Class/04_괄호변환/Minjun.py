def solution(p):   
    # 올바른 괄호 문자열 체크 함수
    def check(s):
        cnt = 0
        for i, c in enumerate(s):
            if c == "(":
                cnt += 1
            else:
                cnt -= 1
            # 음수가 되는 순간 => 순서가 안 맞음(올바르지않음)
            if cnt < 0:
                return False           
        return True

    # 문자열 분리 함수
    def divide(s):
        # 1. 빈 문자열 반환
        if s == '':
            return ""
        cnt = 0
        for i, c in enumerate(s):
            if c == "(":
                cnt += 1
            else:
                cnt -= 1
            # 2. 균형잡힌 괄호 문자열 분리 => cnt 0이 되는 순간 괄호열 페어가 맞는 것. (올바른 지는 아직 모름)
            if cnt == 0:
                u = s[:i+1]
                v = s[i+1:]
                # 3. 올바른 괄호 문자열 
                if check(u):
                    return u + divide(v)
                # 4. 올바르지 않은 괄호 문자열
                else:
                    return "(" + divide(v) + ")" + reversing(u[1:-1])

    # 4-4 뒤집어주는 함수
    def reversing(s):
        a = ''
        for i in s:
            if i == "(":
                a += ")"
            else:
                a += "("             
        return a

    return divide(p)
