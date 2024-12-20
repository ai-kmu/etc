from collections import deque

class Solution:
    def tribonacci(self, n: int) -> int:
        # 초기 값 세 개 -> 원활한 세 개 유지를 위해 deque 사용
        init = deque([0, 1, 1])
        
        while n > 2:
            n -= 1                  # n을 하나 씩 줄여가면서
            init.append(sum(init))  # 다 더한 거 붙이고
            init.popleft()          # 처음 거 떼기
        return init[n]
