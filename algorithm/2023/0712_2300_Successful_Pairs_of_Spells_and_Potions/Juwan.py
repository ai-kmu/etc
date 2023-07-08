from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        
        # spelsl가 potions이 있음
        # spells[i]는 i번째 spell의 강함 정도
        # potions[j]는 j번째 potion의 강함 정도
        
        # 그 다음 success가 주어짐
        # spell과 potion의 곱 조합으로 최소 success 이상만 되면 된다.

        ans = []

        potions.sort() # 냅다 정렬

        m = len(potions) # potions의 길이

        # 직접 list에 spell 하나씩 곱하니까 time limit이 걸림
        # 따라서 success를 spell 하나씩 나누어서 tmp를 정의하고, potions에서 tmp 인덱스 위치파악
        # 그 다음 그 인덱스 이후로는 어차피 성공이니까 개수만 m에서 빼줘서 카운트하면 됨

        for i in spells:
            tmp = (success - 1)//i  # tmp가 potions에서 최대한 left margin이 되어야함. 그래서 1 뺌
            idx = bisect_left(potions, tmp + 1)  # bisect_left로 인덱스 구함
            ans.append(m - idx)  # 빼고 ans에 넣으면 됨

        return ans       
