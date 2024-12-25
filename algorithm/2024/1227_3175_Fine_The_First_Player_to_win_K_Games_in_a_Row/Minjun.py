from collections import deque
class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        # 이긴 플레이어
        wp = 0
        # 이긴 횟수
        w = 0
        # popleft 해야돼서 deque 사용
        player = deque([i+1 for i in range(len(skills)-1)])
        
        # k가 전체 길이보다 길면 정렬돼서 젤 큰놈이 k번 이기게 되어있음.
        m = max(skills)
        if k >= len(skills):
            return skills.index(max(skills))
        # 작으면 함 세봐야함.
        while True:
            p2 = player.popleft()
            if skills[wp] > skills[p2]:
                player.append(p2)
                w += 1
            else:
                player.append(wp)
                wp = p2
                w = 1
            if w == k:
                return wp
