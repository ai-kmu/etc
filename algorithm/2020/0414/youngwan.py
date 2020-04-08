from collections import deque

def solution(food_times, k):
    answer = 0
    # deque를 음식의 개수만크 생성
    eat_dq = deque(range(len(food_times)))
    # times의 초기값은 0만 아니면 되기 때문에 1로 잡아둠
    times = 1
    # times == 0인 경우는 한 바퀴를 돌지 못하기 때문에 while문 밖에서 처리
    # len(eat_dq)가 0인 경우는 남은 음식이 없다는 것을 의미
    while times != 0 and len(eat_dq) != 0:
        food_times, k, eat_dq, times = eat(food_times, k, eat_dq)
    # eat_dq가 0은 먹을 음식이 없다는 것을 의미
    if len(eat_dq) == 0:
        answer = -1
    # 남은 횟수만큼 음식 섭취
    else:
        for i in range(k):
            num = eat_dq.popleft()
            eat_dq.append(num)
        # 이전까지가 중단되기 전까지 먹은 것이므로 다음에 오는 음식을 먹을 차례
        # index는 0부터 시작이므로 +1
        answer = eat_dq.popleft() + 1
    return answer


def eat(food_times, k, eat_dq):
    # 남은 횟수를 남은 음식의 총 개수로 나누어 준다
    # times는 몇 바퀴 돌 수 있는지를 계산
    times = k // len(eat_dq)
    # after_times는 남은 시간을 계산
    after_times = k % len(eat_dq)
    for i in range(len(eat_dq)):
        eat_num = eat_dq.popleft()
        # times보다 이번에 먹을 음식 섭취 시간이 적다면 그만큼을 after_times(남은 시간)에 더해준다
        if food_times[eat_num] <= times:
            after_times += times - food_times[eat_num]
            food_times[eat_num] = 0
        # times보다 이번에 먹을 음식 섭취 시간이 길다면 times만큼 빼주고 다시 deque에 넣어준다
        else:
            food_times[eat_num] -= times
            eat_dq.append(eat_num)
    return food_times, after_times, eat_dq, times
