# 솔루션 참고했습니다....
class Solution(object):
    def findWinningPlayer(self, skills, k):
        n = len(skills)
        if k >= n - 1:
            return skills.index(max(skills))
        
        current_winner = skills[0]
        consecutive_wins = 0
        
        for i in range(1, n):
            if current_winner > skills[i]:
                consecutive_wins += 1
            else:
                current_winner = skills[i]
                consecutive_wins = 1
            
            if consecutive_wins == k:
                return skills.index(current_winner)
        return skills.index(max(skills))
