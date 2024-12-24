from collections import deque

class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        # 플레이어 큐, 승 수 선언
        players = deque(range(len(skills)))
        wins = 0

        # 이긴 횟수가 길이 - 1인 경우는 제일 큰 스킬을 가진 플레이어.
        if k >= len(skills) - 1:  
            return skills.index(max(skills))

        # wins가 k를 만족할 때까지 반복
        while wins < k:
            # 두 플레이러르 플레이어 덱에서 팝
            player1 = players.popleft()
            player2 = players.popleft()
            
            # 먼저 팝된 플레이어가 지는 경우, 이긴 횟수 초기화 및 플레이어 스왑 진행
            if skills[player1] < skills[player2]:
                wins = 0
                player1, player2 = player2, player1

            # 플레이어1을 큐의 첫번째, 플레이어2를 큐의 마지막에 추가
            players.appendleft(player1)
            players.append(player2)
            
            # 이긴 횟수 증가
            wins += 1

        # 플레이어 리스트의 첫번째 반환
        return players[0]
