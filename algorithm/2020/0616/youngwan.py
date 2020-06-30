from collections import deque

def solution(number, k):
    num_deq = deque()
    num = 0

    for i in number:
        num_deq.append(int(i))                    # number를 하나씩 잘라서 deque에 넣기
    
    num_deq, num = remove_num(num_deq, num, k)    # 작은 숫자 줄이는 함수 실행
    while num != k:                               # 아직 k개를 지우지 않은 경우, remove_num에서 내림차순으로 정렬되기 때문에 뒤에서부터 남은 개수만큼 삭제
        num_deq.pop()
        num += 1

    answer = ''
    while num_deq:
        answer += str(num_deq.popleft())          # 남은 수 이어붙이기

    return answer


def remove_num(num_deq, num, k):
    num_deq2 = deque()
    while num_deq and num != k:                   # number가 다 지나가거나 k개 만큼 지워질 때까지
        number = num_deq.popleft()
        while num_deq2:                           # num_deq의 다음 숫자와 num_deq2의 나중에 들어온 숫자들과 차례대로 비교
            number2 = num_deq2.pop()
            if number <= number2:                 # num_deq2의 숫자가 큰 경우에 종료
                num_deq2.append(number2)
                break
            num += 1                              # num_deq의 숫자가 큰 경우, num_deq2의 숫자가 삭제되므로 num을 1 증가
            if num == k:                          # num이 k와 같아졌다면 종료
                break                   
        num_deq2.append(number)                   # num_deq의 숫자를 num_deq2에 삽입
    while num_deq:                                # num_deq의 남은 숫자들을 num_deq2에 이어붙이기
        num_deq2.append(num_deq.popleft())
    return num_deq2, num
