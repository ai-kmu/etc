from collections import deque


def solution(numbers, target):
    answer = 0
    q = deque()
    # 큐에 숫자와 인덱스를 집어넣어서 진행
    # 초기값은 첫번째 숫자에 + 혹은 -를 붙인 것
    q.append((numbers[0], 0))
    q.append((-1 * numbers[0], 0))
    while q:
        r, i = q.popleft()
        i += 1
        # 연산을 끝까지 수행하지 않았다면
        if i != len(numbers):
            # 큐에 추가 연산을 넣어줌
            q.append((r + numbers[i], i))
            q.append((r - numbers[i], i))
        else:
            # 연산이 끝까지 진행되고 target값과 같다면 정답
            if r == target:
                answer += 1
    return answer
