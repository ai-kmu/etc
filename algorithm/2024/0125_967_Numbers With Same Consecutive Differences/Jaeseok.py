from collections import deque

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # 중복을 피하기 위해 set 형태로 answer 선언
        answer = set()
        q = deque()
        
        # leading zero를 피하기 위해 첫 자리수는 1부터 시작
        # 자리수 붙임을 쉽게 하기 위해서 str 형태로 관리
        for i in range(1, 10):
            q.append(str(i))
            while q:
                strings = q.popleft()
                # 길이를 다 채우면 answer에 추가
                if len(strings) == n:
                    answer.add(int(strings))
                    continue
                # 마지막 자리수에서 k를 더한 값과 k를 뺀 값이 0~9 사이의 범위면 deque에 추가
                l_int = int(strings[-1])
                plus_cons = l_int + k
                minus_cons = l_int - k
                if plus_cons < 10:
                    q.append(strings + str(plus_cons))
                if minus_cons >= 0:
                    q.append(strings + str(minus_cons))

        # 정답은 list 형태이므로 변환
        return list(answer)
