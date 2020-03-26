def solution(arrangement):
    answer = 0
    pole = 0
    before = ''
    # 괄호의 개수만큼
    for i in range(len(arrangement)):
        now = arrangement[i]
        # 첫번째는 이전이 없기 때문에 첫번째 아닌 괄호에 대해서 이전 괄호를 체크
        if(i != 0):
            before = arrangement[i-1]
        # '('가 연속으로 나온 경우는 막대가 하나 추가
        if now == '(' and before == '(':
            pole += 1
        # ')'뒤에 '('가 나온 경우는 막대기가 될 수도 절단기가 될 수도 있기 때문에 그냥 진행 
        elif now == '(' and before == ')':
            continue
        # '(' 뒤에 ')' 나온 경우는 절단기
        elif now == ')' and before == '(':
            # 절단기가 나오면 막대기의 수만큼 조각이 나오기 때문에 막대기의 수를 더해준다
            answer += pole
        # ')' 뒤에 ')' 나온 경우는 막대기가 하나 줄어드는 경우
        elif now == ')' and before == ')':
            # 막대기를 하나 줄이고 막대기의 마지막 부분 한 개가 더해진다
            pole -= 1
            answer += 1
    return answer
