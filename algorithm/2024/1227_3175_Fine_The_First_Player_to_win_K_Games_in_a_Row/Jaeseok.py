from collections import deque

class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        # 1. k가 n보다 클 경우 가장 skill이 좋은 사람이 무조건 충족하므로 max인 값의 index를 리턴
        if k >= n:
            return skills.index(max(skills))
        # 그렇지 않다면 deque를 사용해서 실제 요구사항대로 k만큼 연승하는 사람을 구해줌
        # 이긴 사람은 왼쪽으로 다시 넣어주고, 진 사람은 오른쪽 마지막에 넣어주는 방식으로 구현
        else:
            row = 0
            q = deque()
            for i, v in enumerate(skills):
                q.append((i, v))
            while True:
                if row == k:
                    break
                player_a, skill_a = q.popleft()
                player_b, skill_b = q.popleft()
                if skill_a > skill_b:
                    row += 1
                    q.appendleft((player_a, skill_a))
                    q.append((player_b, skill_b))
                else:
                    row = 1
                    q.appendleft((player_b, skill_b))
                    q.append((player_a, skill_a))
        # 최대 연승을 달성하였을 때 가장 왼쪽에 있는 사람을 리턴
        return q.popleft()[0]
        
