def solution(numbers):
    answer = ''
    # 숫자들을 이어붙여야 하므로 우선 numbers를 list 형태로 만듬
    numbers = list(map(str, numbers))
    # 같은 숫자로 연속했을 때 앞에 오도록 정렬 ex) 90보다 9가 앞에 있는 것이 더 큰 수를 만들 수 있기 때문
    numbers.sort(key = lambda x: x * 5, reverse = True)
    # 정렬된 숫자들로 이어붙임
    for i in numbers:
        answer += i
    # 000.. 같은 테스트 케이스가 있기 때문에 answer를 int형으로 만들었다가 다시 str형태로 
    return str(int(answer))
