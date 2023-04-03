# deadend가 set이면 통과이고 list이면 time limit exceeded 

class Solution(object):
    # deque 사용해서 bfs 풀이 방식
    from collections import deque
    def openLock(self, deadends, target):

        # 중복 탐색을 막기 위한 set
        # 방문 혹은 dead 값을 저장한다.
        deadends = set(deadends)

        # 아래 풀이는 시작값 다음것 부터 검증하므로 0000이 deadends면 제거해야 한다.
        if '0000' in deadends:
            return -1

        # 초기값 설정
        tmp = deque([('0000', 0)])

        # tmp가 빌때까지 반복
        while tmp:
            # 현재 값과, 움직인 횟수 확인
            state, aws = tmp.popleft()

            # 현재 결과가 목표값이 되면 return
            if state == target:
                return aws

            # 아니면 4가지 위치를 하나씩 변경
            for i in range(4):
                # 앞 뒤로 하나씩 변경
                for j in (1, -1):
                    # 0~9까지이므로 % 10으로 나머지 처리
                    # 다음 값 설정
                    next_state = state[:i] + str((int(state[i]) + j) % 10) + state[i+1:]
                    # 만약 결과가 dead값이 아니면 tmp에 저장
                    # 또한 순환한 값인지 확인하기 위해 dead에 값 저장
                    if next_state not in deadends:
                        deadends.add(next_state)
                        tmp.append((next_state, aws+1))
        # 모든 경우가 아니면 return -1 
        return -1
