# 1번 풀이 : 있는 그대로 구현
from collections import deque
class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        # 처음 index를 유지하기 위한 dictionary
        players = {s: i for i, s in enumerate(skills)}
        # k 조정 : 전체 리스트를 다 보고 나면 이길 애는 skill level 제일 높은 애임
        k = min(k, len(skills) - 1)
        
        # 왼쪽부터 보면서 오른쪽에 붙이는 게 필요하기 때문에 deque 사용
        queue = deque(skills)
        # 첫 번째 애의 스킬 레벨 (a)을 기준으로 계산
        win = 0
        a = queue.popleft()
        while win != k:
            b = queue.popleft()
            # 이기면
            if a > b:
                win += 1         # win 늘리기
                queue.append(b)  # 진 애는 맨 뒤로
            # 지면
            elif b > a:
                a, b = b, a      # 서로 바꾸고
                win = 1          # 바뀐 첫 번째 애는 이전 첫 번째를 이긴 거니까 1로 초기화
                queue.append(b)  # 진 애는 맨 뒤로
        
        # 조건 만족하면 정답은 첫 번째 애
        return players[a]


# 2번 풀이 : "뒤로 보내기" 안 하기
class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        # k 조정 : 전체 리스트를 다 보고 나면 이길 애는 skill level 제일 높은 애임
        k = min(k, n - 1)
        
        # 첫 번째 있는 애 (i)를 기준으로 계산
        win = 0
        i = 0
        for j in range(1, n):
            # 지면 i를 바꿔치고, 이전 i를 이겼으니까 win = 1
            if skills[i] < skills[j]:
                i = j
                win = 1
            # 이기면 win만 올리기
            else:
                win += 1
            # 정해진 횟수를 채웠다면 거기서 종료, 첫 번째 애가 정답
            if win == k:
                break
        
        # 아까 조정했던 거처럼, 전체 리스트 다 보고 나면 (for 문 끝나면)
        # 첫 번째에는 skill level이 제일 높은 애가 있고, 걔가 정답
        return i
