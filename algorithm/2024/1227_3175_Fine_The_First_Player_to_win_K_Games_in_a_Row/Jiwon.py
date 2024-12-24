## 이렇게 푸는 게 아닌 거 같은디......

class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:

        # [player, skill, winning cnt]
        players = deque([[i, skills[i], 0] for i in range(len(skills))])

        tmp = sorted(players, key=lambda x: x[1], reverse=True)
        if k > len(skills) - 1:
            return tmp[0][0]

        for _ in range(len(skills)):
            p1 = players.popleft()
            p2 = players.popleft()

            if p1[1] > p2[1]:
                p1[2] += 1
                if p1[2] == k:
                    return p1[0]
                players.appendleft(p1)  # 이긴 애는 제일 앞으로
                players.append(p2)  # 진 애는 제일 뒤로
            else:
                p2[2] += 1
                if p2[2] == k:
                    return p2[0]
                players.appendleft(p2)  # 이긴 애는 제일 앞으로
                players.append(p1)  # 진 애는 제일 뒤로
                
        return players[0][0]
        
