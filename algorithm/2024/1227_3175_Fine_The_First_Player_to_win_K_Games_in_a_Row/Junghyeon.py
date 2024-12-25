# deque로 풀이
from collections import deque


class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        queue = deque(range(n))
        win_streak = [0] * n

        max_skill = max(skills)
        max_skill_index = skills.index(max_skill)

        while True:
            player1 = queue.popleft()
            player2 = queue.popleft()

            if skills[player1] > skills[player2]:
                winner, loser = player1, player2
            else:
                winner, loser = player2, player1

            # 승자의 연승 기록 증가, 패자의 기록 초기화
            win_streak[winner] += 1
            win_streak[loser] = 0

            # 승자가 최대 실력 선수이거나 연승 조건을 만족하면 승자를 반환
            if winner == max_skill_index or win_streak[winner] == k:
                return winner

            # 승자와 패자를 재배치
            queue.appendleft(winner)
            queue.append(loser)
