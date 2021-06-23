class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        max_reach = 6001                    # 뒤로 2번 갈 수 없기 때문에 6000을 넘을 수 없음
        visited = set()
        for pos in forbidden:
            visited.add((pos, True))        # 앞으로 가는 경우 True
            visited.add((pos, False))       # 뒤로 가는 경우 False -> 뒤로 두번 못 가기 때문에 
        can_reach = [(0, True)]             # 시작
        jump = 0
        while can_reach:
            now_reach = []
            for pos, can_back in can_reach: 
                if pos == x:
                    return jump
                if pos + a < max_reach and (pos + a, True) not in visited:               # 앞으로 가는 경우, 이전에 방문한 적이 없으면 진행
                    now_reach.append((pos + a, True))
                    visited.add((pos + a, True))
                if can_back == True and pos - b > 0 and (pos - b, False) not in visited: # 뒤로 가는 경우, 이전에 방문한 적이 없고 그 전에 뒤로 간게 아니라면 진행
                    now_reach.append((pos - b,False))
                    visited.add((pos - b, False))
            can_reach = now_reach
            jump += 1
            
        return -1
