def solution(arrangement):
    answer = 0
    pole = 0
    before = ''
    for i in range(len(arrangement)):
        now = arrangement[i]
        if(i != 0):
            before = arrangement[i-1]
        if now == '(' and before == '(':
            pole += 1
        elif now == '(' and before == ')':
            continue
        elif now == ')' and before == '(':
            answer += pole
        elif now == ')' and before == ')':
            pole -= 1
            answer += 1
    return answer
