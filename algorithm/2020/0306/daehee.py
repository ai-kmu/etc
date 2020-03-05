import collections

def classify(v):
    std = 0
    left = 0
    right = 0
    for idx, letter in enumerate(v):
        if letter == '(':
            left += 1
        else:
            right += 1
        if left == right:
            std = idx
            break
    return std


def isRight(u):
    deq = collections.deque()
    for _ in u:
        if _ == '(':
            deq.append(_)
        else:
            if deq:
                if deq[-1] == '(':
                    deq.pop()
                else:
                    deq.append(_)
            else:
                deq.append(_)
    if len(deq) == 0:
        return True
    return False
    
def reverse(u):
    _u = u[1:len(u)-1]
    rev = ''
    for _ in _u:
        if _ == '(':
            rev += ')'
        else:
            rev += '('
    return rev
    
def notBalanceCase(u):
    if len(u) == 0:
        return ''
    
    
    idx = classify(u)
    v = u[idx+1:]
    u = u[:idx+1]
    print(u,v)

    if isRight(u):
        return u + notBalanceCase(v)
    
    blank = '('
    blank += notBalanceCase(v) + ')' + reverse(u)
    
    return blank

def solution(p):
    answer = notBalanceCase(p)
    
    return answer
