# 실패
def solution(numbers):
    answer = ''
    # 값의 최대 길이 저장
    len2 = len(str(max(numbers)))
    # 인덱스 위치별 크기를 비교하고
    # 인덱스 이전 위치보다 값이 감소했다면 길이가 짧은 것보다 우선순위를 낮게 주어야 함
    # 이후 인덱스가 없으면 최후 값으로 대체하는 식으로 구현 가능
    # 접근을 잘못한 것 같은데...
    numbers.sort(key = lambda x: tuple(str(x)[i] if len(str(x)) > i else str(x)[-1] for i in range(len2)), reverse = True)
    for s in numbers:
        answer += str(s)
    return answer
