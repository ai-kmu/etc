from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # spells는 다 봐야 하지만, potions는 다 볼 필요 없음
        # -> 정렬 후 적절한 위치를 binary search로 찾음
        potions = sorted(potions)
        n = len(potions)
        return [n - bisect_left(potions, success / s) for s in spells]
