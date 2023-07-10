class Solution(object):
# 풀다가 못풀었어요 

    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        pairs = [0] * len(spells) 
        
        for i in range(len(spells)):
            for j in range(len(potions)):
                if spells[i] * potions[j] >= success:
                    pairs[i] += 1
        
        return pairs
