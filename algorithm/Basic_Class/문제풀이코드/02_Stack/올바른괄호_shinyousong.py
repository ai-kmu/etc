def solution(s):
    stk = []
    for i in range(len(s)):
        if s[i] == ")" and stk == []:
            return False
        if s[i] == "(":
            stk.append(1)
        else:
            del stk[-1]
    if stk == []:
        return True
    return False
