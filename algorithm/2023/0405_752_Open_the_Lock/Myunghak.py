# 4차원상에서의 길찾기 문제
# 최단거리를 찾아야 하므로 BFS로 탐색
# 0과 9가 붙어있음을 나타내기 위해 StrList 사용

from collections import deque

class Solution:
    def openLock(self, deadends, target) -> int:
        StrList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9","0", "9"] # 0에서 한칸 뒤로가면 0고 9에서 한칸 앞으로 가면 0이라는걸 표현하기 위해 사용

        deadends = set(deadends)
        Q = deque([("0000", 0)])
        visit = set("0000")

        while(Q):
            cur, ans = Q.popleft()
            if cur in deadends:
                continue
            if cur == target:
                return ans
            for i in range(4):
                # 현재 state로부터 갈수 있는거 탐색
                check1 = cur[:i] + StrList[int(cur[i]) + 1] + cur[i+1:]
                check2 = cur[:i] + StrList[int(cur[i]) - 1] + cur[i+1:]
                if check1 not in visit:
                    Q.append((check1, ans+1))
                    visit.add(check1)
                if check2 not in visit:
                    Q.append((check2, ans+1))
                    visit.add(check2)
        return -1
    
