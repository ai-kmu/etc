from collections import deque

# 각 줄마다 더하면서 겹치는 위치는 더 큰 값으로 채워 마지막 줄에 모든 결과가 나오게 만드는 방법

def solution(triangle):
    num_deque = deque()
    for i in triangle:
        num_deque = cal(num_deque, i)    # 한 줄 씩 계산 
    answer = 0
    while num_deque:                     # 가장 큰 값 찾기
        temp = num_deque.popleft()         
        if temp > answer:                
            answer = temp 
    return answer


def cal(num_deque, i):
    if len(num_deque) >= 2:                      # 세 번째 줄 이상인 경우  
        num = 0                                  # 이 줄의 몇번째를 보고 있는지 나타내는 변수
        front = 0                                # 앞 숫자를 나타내는 변수
        back = 0                                 # 뒷 숫자를 나타내는 변수
        for j in i:                              # 줄에서 하나씩 빼서
            if num == 0:                         # 첫번째인 경우
                front = num_deque.popleft()      # queue에서 숫자를 꺼내 
                num_deque.append(j + front)      # 더하고 queue에 추가
            elif num == len(i)-1:                # 마지막 숫자인 경우
                num_deque.append(j + back)       # back에 더해 queue에 추가
            else:                                # 중간 숫자들은 겹치는 경우가 발생할 수 있음
                back = num_deque.popleft()       # 뒤에 숫자를 꺼내
                if j + front > j + back:         # 더 큰 값을 저장
                    num_deque.append(j + front)
                else:
                    num_deque.append(j + back)
                front = back                     # back을 front로 바꿔줌
            num += 1                             # num을 1 증가
    elif len(num_deque) == 1:              # 두 번째 줄인 경우
        temp = num_deque.popleft()         # 첫 번째 값에
        for j in i:                        # 각 값을 더해
            j += temp
            num_deque.append(j)            # deque에 추가
    else:                                  # 첫 번째 줄인 경우, 그냥 deque에 넣어줌
        num_deque = deque(i)
    return num_deque
