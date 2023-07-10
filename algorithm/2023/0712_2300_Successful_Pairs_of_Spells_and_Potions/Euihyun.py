# 타임 리밋 해결못하고 봤어요
# 리뷰 안해주셔도 됩니다.
from bisect import bisect_left

class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        sorted_potions = sorted(potions)
        result = []
        for a in spells:
            # a와 곱했을 때 success 이상이 되는 최소 물약의 강도를 계산
            threshold = (success + a - 1) // a
            # 정렬된 물약 배열에서 threshold를 초과하는 첫 번째 인덱스 찾기
            count = len(sorted_potions) - bisect_left(sorted_potions, threshold)

            # 성공적인 쌍의 개수를 결과 리스트에 추가
            result.append(count)
        return result
