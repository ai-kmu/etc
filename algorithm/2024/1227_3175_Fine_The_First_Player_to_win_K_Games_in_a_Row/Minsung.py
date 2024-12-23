from collections import deque, defaultdict

class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        q = deque()
        for i in range(len(skills)):
            q.append(i)
        win_cnt = defaultdict(int)  # 각 player 별로 연속 승리 횟수 저장
        max_skill = max(skills)  # 다 이기는 player의 skill 저장
        while q:
            a = q.popleft()  # player one
            b = q.popleft()  # player two

            # 현재 player가 다 이길 경우, 반복문을 도는 것은 무의미함
            if skills[a] == max_skill: return a
            if skills[b] == max_skill: return b

            if skills[a] > skills[b]:
                win_cnt[a] += 1
                win_cnt[b] = 0
                if win_cnt[a] == k:
                    return a
                q.appendleft(a)
                q.append(b)
            else:
                win_cnt[a] = 0
                win_cnt[b] += 1
                if win_cnt[b] == k:
                    return b
                q.append(a)
                q.appendleft(b)
