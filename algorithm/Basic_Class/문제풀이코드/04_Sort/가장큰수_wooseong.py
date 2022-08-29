def solution(numbers):
    # 반복과 join을 위해 str 배열로 변경
    numbers = list(map(str, numbers))
    # 세 번 반복해서 큰 순으로 정렬
    # -> 문자열은 자리수에 관계 없이 앞부터 각각 비교한다.
    numbers.sort(key=lambda x: x * 3, reverse=True)
    
    # join으로 정답 문자열 생성
    answer = ''.join(numbers)
    # 맨 앞이 0이다 == 애초에 0만 들어왔다
    # -> 답은 '0'
    if answer[0] == '0':
        answer = '0'
    
    return answer
