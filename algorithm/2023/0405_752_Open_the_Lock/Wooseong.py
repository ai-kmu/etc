from collections import deque as dq

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 이웃 찾기 함수
        def neighbors(code):
            next_ = []
            # code 한 자리 씩만 뽑아서 돌림
            for i in range(4):
                before = int(code[i])
                for diff in (-1 ,1):
                    # +10은 -1을 방지하기 위함
                    after = (before + diff + 10) % 10
                    next_.append(code[:i] + str(after) + code[i+1:])
            
            return next_            

        # 예외: 시작부터 막혀버릴 때
        if '0000' in deadends:
            return -1

        # 탐색을 O(1)로 하기 위해 deadends를 set으로 변경
        # 후에 visited로도 활용함
        dead_visit = set(deadends)

        # BFS
        q = dq(['0000'])
        answer = 0
        while q:
            # 현재 q에 있는 애들만 탐색
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == target:
                    return answer
                
                # 각 자리를 하나 씩 시계/반시계로 옮겼을 때 가능한 애들 탐색
                for nghb in neighbors(curr):
                    if nghb in dead_visit:
                        continue
                    
                    # 가능하면 추가
                    dead_visit.add(nghb)
                    q.append(nghb)
            
            # 현재 q에 있는 애들 탐색 끝나면 한 번 이동한 거임
            answer += 1
        
        return -1
