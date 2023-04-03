from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 만약 0000이 deadends에 있을 경우 종료
        if "0000" in deadends:
           return -1
        
        # BFS를 위한 데크 선언
        q = deque()
        # 현재 숫자와 트리의 레벨 숫자(몇 번 다이얼을 움직였는지)를 넣어줌
        q.append(["0000", 0])
        # deadends를 처음에 visited에 넣어주어 탐색하지 않도록 함
        visited = set(deadends)
        
        while q:
            # 현재 숫자와 몇 번 움직였는지 뽑기
            curr_num, cnt = q.popleft()

            # 만약 현재 숫자가 target과 같을 때 cnt 반환
            if curr_num == target:
                return cnt
            
            # 위에서 뽑은 현재 숫자를 바탕으로 트리의 다음 
            # 레벨에 더해줄 숫자들을 계산
            # 총 자릿수가 4개이기 때문에 4번 루프를 돌며
            # 각 자릿수에 +1, -1을 하는 방식으로 다음 레벨에 추가
            for i in range(len(curr_num)):
                # +1하는 경우 현재 숫자의 i번째 자릿수에서 1을 더해주고
                # mod 10을 하면 9애서 10으로 넘어가는 경우를 계산할 수 있음
                digit = str((int(curr_num[i]) + 1) % 10)
                # 만들어진 숫자를 tmp_str로 저장한 후 visited에 있는지 검사
                tmp_str = curr_num[:i] + digit + curr_num[i+1:]
                # 만약 방문하지 않은 숫자라면 큐에 넣고 visited에 더해줌
                if tmp_str not in visited:
                    q.append([tmp_str, cnt + 1])
                    visited.add(tmp_str)

                # -1을 하는 경우 + 9를 하고 mod 10을 하면 0에서 9로 
                # 넘어갈 수 있음
                digit = str((int(curr_num[i]) + 9) % 10)
                tmp_str = curr_num[:i] + digit + curr_num[i+1:]
                if tmp_str not in visited:
                    q.append([tmp_str, cnt + 1])
                    visited.add(tmp_str)
        # while 문이 다 돌았다는 것은 target을 만들 수 없는 경우이기 때문에 -1 반환
        return -1
