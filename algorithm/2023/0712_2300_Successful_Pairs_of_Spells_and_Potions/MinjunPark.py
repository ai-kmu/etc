from bisect import bisect_right

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = []
        n = len(potions)
        potions.sort()

        for i in spells: # 각 spell마다 계산
            pairs.append(n-bisect_right(potions, (success-1)//i)) # 이진탐색으로 success가능한 목표 값보다 1 작은 index를 찾고, n에서 빼서 개수를 셈 

        return pairs
