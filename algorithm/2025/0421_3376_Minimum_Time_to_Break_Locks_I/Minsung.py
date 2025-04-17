'''
memory limit, time limit, recursionlimit
많은 경우를 마주하고... 타개하려 했지만... 실패했습니다...
'''
from collections import Counter
from math import ceil
import sys
sys.setrecursionlimit(int(1e7))

class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:
        '''
        brute-force
            action 
                1. 부술 수 있는 lock 중 최대 lock을 부순다.
                    - binary search 미사용, n=8이라 굳이?
                2. 아무 block도 부수지 않는다.
                    - time step을 하나씩 증가 X, strength[i] 클 수 있어서 비효율적
                    - 남은 lock 중 최솟값을 부술 수 있을만큼 time warping
        '''
        self.remained = Counter(strength)
        self.time = 0
        self.x = 1
        self.k = k
        self.ans=int(1e5)
        self.backtrack(0)
        return self.ans
    
    def backtrack(self, energy:int):
        flag = True  # 모든 lock을 부쉈는지 check
        
        # action 1
        max_remained = 0
        for k, v in self.remained.items():
            if v!=0: flag = False
            if v!=0 and energy>=k:
                max_remained = max(max_remained, k)
        if max_remained != 0:  # 부술 수 있는 lock이 있을 경우
            self.remained[max_remained] -= 1
            self.x += self.k
            self.time += 1
            self.backtrack(self.x)
            self.remained[max_remained] += 1
            self.x -= self.k
            self.time -= 1
        if flag==False:  # 모든 lock을 부쉈을 경우
            self.ans = min(self.ans, self.time-1)

        # action 2, 지금 부술 수 있는 최대 lock보다 더 큰 lock을 부수는 행동
        next_lock = 0
        for k, v in self.remained.items():
            if v!=0 and k>max_remained:
                next_lock = min(next_lock, k)
        # energy+x*time >= next_lock
        needed_time = ceil((next_lock-energy)/self.x)
        x = self.x
        self.x += self.k*needed_time
        self.time += needed_time
        self.backtrack(energy+x*needed_time)
