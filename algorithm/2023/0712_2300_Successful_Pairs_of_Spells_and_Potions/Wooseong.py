from bisect import bisect_right

class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        n = len(potions)
        potions.sort()  # 이분 탐색을 위한 정렬
        answer = []
        for s in spells:
            # spell × potion >= success를 만족하는 potion을 tgt으로 지정
            tgt = (success - 1) // s
            ind = bisect_right(potions, tgt)
            # 최솟값 index 뒤로는 모두 만족 -> 개수 == (n - ind)
            answer.append(n - ind)
        
        return answer
