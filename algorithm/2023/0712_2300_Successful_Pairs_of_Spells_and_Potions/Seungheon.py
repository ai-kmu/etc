class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # sort 후 이진탐색
        potions.sort()
        return [len(potions) - bisect_right(potions, (success-1)/s) for s in spells] 
