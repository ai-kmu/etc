import bisect

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # spells 요소 * potions 요소 >= succes 찾는 문제
        # 이진분류로 idx 찾아서 개수 구하는 방법으로 접근

        # 전체 개수: success 보다 작은 마지막 idx 구해서 빼기 위함
        n = len(potions)
        # 이진분류를 위해 정렬
        potions.sort()
        return [n - bisect_right(potions, (success-1)//i) for i in spells]
