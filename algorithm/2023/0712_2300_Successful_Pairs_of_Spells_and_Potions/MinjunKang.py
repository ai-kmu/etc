class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
            ans = []
            for s in spells:
                a = [i for i, v in enumerate(potions) if s * v >= success]
                ans.append(len(a))
            return ans
