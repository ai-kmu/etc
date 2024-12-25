class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        
        winner_skill = skills[0]
        winner = 0
        
        for i in range(1, n):
            if winner_skill < skills[i]:
                winner_skill = skills[i]
                winner = i
            
            # k번 이상 경기를 진행하고, winner가 k번 이상 경기한 사람이면
            # 바로 winner를 return
            if i >= k and winner <= i - k + 1:
                return winner
        return winner
